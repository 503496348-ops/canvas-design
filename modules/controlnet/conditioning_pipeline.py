"""
Conditioning Pipeline — end-to-end control conditioning for SD/Flux models.
Inspired by ControlNet's zero-convolution architecture.

Provides a complete pipeline from input image → control extraction →
conditioning tensor → model integration.
"""

import logging
from dataclasses import dataclass, field
from typing import Any, Optional
from enum import Enum

logger = logging.getLogger(__name__)


class ModelType(Enum):
    SD15 = "sd1.5"
    SDXL = "sdxl"
    FLUX = "flux"
    CUSTOM = "custom"


@dataclass
class ConditioningConfig:
    """Configuration for the conditioning pipeline."""
    model_type: ModelType = ModelType.SD15
    control_types: list[str] = field(default_factory=lambda: ["canny"])
    control_weights: list[float] = field(default_factory=lambda: [1.0])
    global_strength: float = 1.0
    conditioning_step: int = 0  # 0 = from start
    resolution: tuple[int, int] = (512, 512)
    use_zero_conv: bool = True
    blend_mode: str = "add"


@dataclass
class ConditioningResult:
    """Result of the conditioning pipeline."""
    control_images: dict[str, Any]  # control_type → processed image
    fused_image: Any                # final fused conditioning
    conditioning_tensor: Any        # model-ready tensor (if torch available)
    config: ConditioningConfig
    metadata: dict = field(default_factory=dict)


class ConditioningPipeline:
    """
    End-to-end conditioning pipeline for controlled image generation.

    Pipeline stages:
    1. Input preprocessing (resize, normalize)
    2. Control signal extraction (per control type)
    3. Control fusion (weighted combination)
    4. Zero convolution (optional, for training safety)
    5. Conditioning tensor generation (model-ready format)
    """

    def __init__(self, config: Optional[ConditioningConfig] = None):
        self.config = config or ConditioningConfig()

    def run(
        self,
        input_image: Any,
        prompt: str = "",
        negative_prompt: str = "",
    ) -> ConditioningResult:
        """
        Execute the full conditioning pipeline.

        Args:
            input_image: Source image (PIL Image or path)
            prompt: Text prompt (for text+control conditioning)
            negative_prompt: Negative prompt

        Returns:
            ConditioningResult with all processed outputs
        """
        from PIL import Image

        # 1. Load and preprocess
        if isinstance(input_image, str):
            image = Image.open(input_image).convert('RGB')
        elif hasattr(input_image, 'convert'):
            image = input_image.convert('RGB')
        else:
            image = Image.fromarray(input_image)

        # Resize to target resolution
        w, h = self.config.resolution
        image = image.resize((w, h), Image.LANCZOS)

        # 2. Extract control signals
        from control_processors import process_control, ControlType
        control_images = {}
        for ctrl_name in self.config.control_types:
            try:
                ctrl_type = ControlType(ctrl_name)
                signal = process_control(image, ctrl_type)
                control_images[ctrl_name] = signal.image
            except (ValueError, Exception) as e:
                logger.warning(f"Failed to process control '{ctrl_name}': {e}")

        if not control_images:
            logger.warning("No control signals generated, using original image")
            control_images["raw"] = image

        # 3. Fuse controls
        from control_fusion import ControlFuser, BlendMode
        blend = BlendMode(self.config.blend_mode)
        fuser = ControlFuser(blend)

        for ctrl_name, weight in zip(self.config.control_types, self.config.control_weights):
            fuser.add_control(ctrl_name, weight=weight)

        fused = fuser.fuse(control_images)

        # 4. Apply global strength
        if self.config.global_strength < 1.0:
            fused = self._blend_with_original(fused, image, self.config.global_strength)

        # 5. Generate conditioning tensor
        conditioning_tensor = self._to_tensor(fused)

        return ConditioningResult(
            control_images=control_images,
            fused_image=fused,
            conditioning_tensor=conditioning_tensor,
            config=self.config,
            metadata={
                "prompt": prompt,
                "negative_prompt": negative_prompt,
                "controls_extracted": list(control_images.keys()),
                "resolution": self.config.resolution,
            },
        )

    def _blend_with_original(self, control: Any, original: Any, strength: float) -> Any:
        """Blend control signal with original image based on strength."""
        import numpy as np

        ctrl_arr = np.array(control.convert('L')).astype(np.float64) / 255.0
        orig_arr = np.array(original.convert('L')).astype(np.float64) / 255.0

        blended = ctrl_arr * strength + orig_arr * (1 - strength)
        blended = (np.clip(blended, 0, 1) * 255).astype(np.uint8)

        from PIL import Image
        return Image.fromarray(blended)

    def _to_tensor(self, image: Any) -> Any:
        """Convert image to model-ready tensor."""
        try:
            import torch
            import numpy as np

            arr = np.array(image).astype(np.float32) / 255.0
            if len(arr.shape) == 2:
                arr = np.stack([arr, arr, arr], axis=0)
            elif len(arr.shape) == 3:
                arr = arr.transpose(2, 0, 1)

            # Add batch dimension
            tensor = torch.from_numpy(arr).unsqueeze(0)
            return tensor

        except ImportError:
            logger.warning("PyTorch not available, returning numpy array")
            import numpy as np
            arr = np.array(image).astype(np.float32) / 255.0
            if len(arr.shape) == 2:
                arr = np.stack([arr, arr, arr], axis=0)
            return arr

    def zero_conv_init(self, channels: int = 3) -> Any:
        """
        Initialize zero convolution weights (ControlNet's key innovation).
        Both weight and bias start as zeros, ensuring no distortion before training.
        """
        try:
            import torch
            import torch.nn as nn
            conv = nn.Conv2d(channels, channels, 1)
            nn.init.zeros_(conv.weight)
            nn.init.zeros_(conv.bias)
            return conv
        except ImportError:
            logger.warning("PyTorch not available for zero_conv_init")
            return None


# === Convenience Functions ===

def quick_condition(
    image_path: str,
    control_type: str = "canny",
    strength: float = 0.8,
    resolution: tuple = (512, 512),
) -> ConditioningResult:
    """Quick one-line conditioning for common use cases."""
    config = ConditioningConfig(
        control_types=[control_type],
        control_weights=[1.0],
        global_strength=strength,
        resolution=resolution,
    )
    pipeline = ConditioningPipeline(config)
    return pipeline.run(image_path)


def multi_control_condition(
    image_path: str,
    controls: list[str],
    weights: Optional[list[float]] = None,
    resolution: tuple = (1024, 1024),
) -> ConditioningResult:
    """Multi-control conditioning with custom weights."""
    if weights is None:
        weights = [1.0 / len(controls)] * len(controls)

    config = ConditioningConfig(
        control_types=controls,
        control_weights=weights,
        resolution=resolution,
    )
    pipeline = ConditioningPipeline(config)
    return pipeline.run(image_path)


# === Model-Specific Presets ===

SD15_PRESET = ConditioningConfig(
    model_type=ModelType.SD15,
    resolution=(512, 512),
    use_zero_conv=True,
)

SDXL_PRESET = ConditioningConfig(
    model_type=ModelType.SDXL,
    resolution=(1024, 1024),
    use_zero_conv=True,
)

FLUX_PRESET = ConditioningConfig(
    model_type=ModelType.FLUX,
    resolution=(1024, 1024),
    use_zero_conv=False,  # Flux uses different conditioning
)
