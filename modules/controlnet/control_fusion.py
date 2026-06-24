"""
Control Fusion — combine multiple control signals for image generation.
Inspired by ControlNet's multi-control approach with strength scheduling.

Supports weighted combination of multiple control signals,
temporal strength scheduling, and adaptive blending.
"""

import math
import logging
from dataclasses import dataclass, field
from typing import Optional
from enum import Enum

logger = logging.getLogger(__name__)


class BlendMode(Enum):
    ADD = "add"           # Weighted addition
    MAX = "max"           # Element-wise maximum
    OVERLAY = "overlay"   # Overlay blend
    MULTIPLY = "multiply" # Multiply blend


@dataclass
class ControlWeight:
    """Weight configuration for a control signal."""
    control_type: str
    weight: float = 1.0
    start_step: float = 0.0  # When to start applying (0-1)
    end_step: float = 1.0    # When to stop applying (0-1)
    fade_in: float = 0.0     # Fade-in duration (0-1)
    fade_out: float = 0.0    # Fade-out duration (0-1)


class StrengthScheduler:
    """
    Schedules control strength across diffusion steps.

    Supports:
    - Constant strength
    - Linear ramp (fade in/out)
    - Cosine schedule
    - Step function (on/off at specific steps)
    - Custom schedule from function
    """

    def __init__(self, schedule_type: str = "constant", **kwargs):
        self.schedule_type = schedule_type
        self.params = kwargs

    def get_strength(self, step: float, total_steps: int = 1) -> float:
        """
        Get strength value for current step.

        Args:
            step: Current step (0 to total_steps-1)
            total_steps: Total number of steps

        Returns:
            Strength value (0.0 to 1.0)
        """
        progress = step / max(total_steps - 1, 1)  # 0.0 to 1.0

        if self.schedule_type == "constant":
            return self.params.get("strength", 1.0)

        elif self.schedule_type == "linear_ramp":
            start = self.params.get("start", 0.0)
            end = self.params.get("end", 1.0)
            return start + (end - start) * progress

        elif self.schedule_type == "cosine":
            strength = self.params.get("strength", 1.0)
            return strength * (1 + math.cos(math.pi * progress)) / 2

        elif self.schedule_type == "step":
            threshold = self.params.get("threshold", 0.5)
            on_strength = self.params.get("on_strength", 1.0)
            off_strength = self.params.get("off_strength", 0.0)
            return on_strength if progress < threshold else off_strength

        elif self.schedule_type == "fade_in_out":
            peak = self.params.get("peak", 0.5)
            max_strength = self.params.get("strength", 1.0)
            if progress < peak:
                return max_strength * (progress / peak)
            else:
                return max_strength * (1 - (progress - peak) / (1 - peak))

        elif callable(self.schedule_type):
            return self.schedule_type(progress)

        return 1.0


class ControlFuser:
    """
    Combines multiple control signals into a single conditioning tensor.

    Features:
    - Weighted combination with per-control strength schedules
    - Multiple blend modes
    - Conflict resolution (when controls disagree)
    - Adaptive normalization
    """

    def __init__(self, blend_mode: BlendMode = BlendMode.ADD):
        self.blend_mode = blend_mode
        self._weights: list[ControlWeight] = []
        self._schedulers: dict[str, StrengthScheduler] = {}

    def add_control(
        self,
        control_type: str,
        weight: float = 1.0,
        schedule: Optional[StrengthScheduler] = None,
        start_step: float = 0.0,
        end_step: float = 1.0,
    ) -> None:
        """Add a control signal with weight and schedule."""
        cw = ControlWeight(
            control_type=control_type,
            weight=weight,
            start_step=start_step,
            end_step=end_step,
        )
        self._weights.append(cw)
        if schedule:
            self._schedulers[control_type] = schedule

    def fuse(
        self,
        control_images: dict[str, any],
        step: int = 0,
        total_steps: int = 1,
    ) -> any:
        """
        Fuse multiple control images into a single conditioning image.

        Args:
            control_images: Dict mapping control_type to PIL Image/numpy array
            step: Current diffusion step
            total_steps: Total diffusion steps

        Returns:
            Fused control image
        """
        import numpy as np
        from PIL import Image

        if not control_images:
            raise ValueError("No control images provided")

        # Get dimensions from first image
        first_img = next(iter(control_images.values()))
        if hasattr(first_img, 'size'):
            w, h = first_img.size
        else:
            h, w = first_img.shape[:2]

        # Initialize accumulator
        if self.blend_mode == BlendMode.ADD:
            accumulator = np.zeros((h, w), dtype=np.float64)
        elif self.blend_mode == BlendMode.MAX:
            accumulator = np.zeros((h, w), dtype=np.float64)
        elif self.blend_mode == BlendMode.MULTIPLY:
            accumulator = np.ones((h, w), dtype=np.float64)

        total_weight = 0.0

        for cw in self._weights:
            if cw.control_type not in control_images:
                continue

            # Check step range
            progress = step / max(total_steps - 1, 1)
            if progress < cw.start_step or progress > cw.end_step:
                continue

            # Get scheduled strength
            strength = cw.weight
            if cw.control_type in self._schedulers:
                strength *= self._schedulers[cw.control_type].get_strength(step, total_steps)

            if strength <= 0:
                continue

            # Convert image to array
            img = control_images[cw.control_type]
            if hasattr(img, 'convert'):
                img_array = np.array(img.convert('L')).astype(np.float64)
            else:
                img_array = np.array(img).astype(np.float64)

            # Normalize to 0-1
            if img_array.max() > 1:
                img_array = img_array / 255.0

            # Resize if needed
            if img_array.shape != (h, w):
                img_pil = Image.fromarray((img_array * 255).astype(np.uint8))
                img_pil = img_pil.resize((w, h), Image.BILINEAR)
                img_array = np.array(img_pil).astype(np.float64) / 255.0

            # Apply blend
            weighted = img_array * strength

            if self.blend_mode == BlendMode.ADD:
                accumulator += weighted
            elif self.blend_mode == BlendMode.MAX:
                accumulator = np.maximum(accumulator, weighted)
            elif self.blend_mode == BlendMode.MULTIPLY:
                accumulator *= (weighted + 0.001)  # avoid zero

            total_weight += strength

        # Normalize
        if self.blend_mode == BlendMode.ADD and total_weight > 0:
            accumulator /= total_weight

        # Clip and convert back
        accumulator = np.clip(accumulator, 0, 1)
        result = (accumulator * 255).astype(np.uint8)

        return Image.fromarray(result)

    def fuse_batch(
        self,
        control_images: dict[str, any],
        total_steps: int = 20,
    ) -> list[any]:
        """
        Generate fused control images for all steps.

        Returns:
            List of fused images, one per step.
        """
        return [
            self.fuse(control_images, step=s, total_steps=total_steps)
            for s in range(total_steps)
        ]


# === Preset Fusion Configurations ===

def create_balanced_fusion(controls: list[str], weight: float = 0.5) -> ControlFuser:
    """Create a balanced fusion with equal weights."""
    fuser = ControlFuser(BlendMode.ADD)
    for ctrl in controls:
        fuser.add_control(ctrl, weight=weight)
    return fuser


def create_cascaded_fusion(controls: list[str]) -> ControlFuser:
    """Create a cascaded fusion where controls activate sequentially."""
    fuser = ControlFuser(BlendMode.ADD)
    n = len(controls)
    for i, ctrl in enumerate(controls):
        start = i / n
        end = (i + 1) / n
        schedule = StrengthScheduler("fade_in_out", peak=0.5, strength=1.0)
        fuser.add_control(ctrl, weight=1.0, schedule=schedule, start_step=start, end_step=end)
    return fuser


def create_composition_fusion(
    main_control: str,
    detail_control: str,
    main_weight: float = 0.7,
    detail_weight: float = 0.3,
) -> ControlFuser:
    """Create a composition fusion: main control for structure, detail for fine-tuning."""
    fuser = ControlFuser(BlendMode.ADD)
    fuser.add_control(main_control, weight=main_weight)
    fuser.add_control(detail_control, weight=detail_weight)
    return fuser
