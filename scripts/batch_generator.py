"""
GPT Image Gen — Style Preset & Batch Generation
================================================
Inspired by ComfyUI (117K⭐) workflow parameter injection.

GPT Image 2 specific features:
- Style presets with prompt engineering
- Batch generation with size/style variations
- Output quality scoring heuristics
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ImageStylePreset:
    """Style preset for GPT Image 2 generation."""
    name: str
    system_instruction: str
    prompt_template: str
    aspect_ratio: str = "1:1"
    quality: str = "high"

    def build_prompt(self, user_input: str) -> str:
        return self.prompt_template.replace("{input}", user_input)


PRESETS = {
    "产品图": ImageStylePreset(
        name="产品图", aspect_ratio="1:1", quality="high",
        system_instruction="Generate a professional product photograph with clean background",
        prompt_template="Professional product photography of {input}, white studio background, soft lighting, 8k detail",
    ),
    "头像": ImageStylePreset(
        name="头像", aspect_ratio="1:1", quality="high",
        system_instruction="Generate a professional portrait",
        prompt_template="Professional portrait of {input}, studio lighting, sharp focus, natural expression",
    ),
    "海报": ImageStylePreset(
        name="海报", aspect_ratio="3:4", quality="high",
        system_instruction="Generate a marketing poster",
        prompt_template="Marketing poster design for {input}, bold typography, modern layout, eye-catching colors",
    ),
    "Logo": ImageStylePreset(
        name="Logo", aspect_ratio="1:1", quality="high",
        system_instruction="Generate a minimalist logo design",
        prompt_template="Minimalist logo design for {input}, clean lines, scalable vector style, white background",
    ),
    "插图": ImageStylePreset(
        name="插图", aspect_ratio="16:9", quality="standard",
        system_instruction="Generate an illustration",
        prompt_template="Digital illustration of {input}, vibrant colors, detailed, artistic style",
    ),
}


@dataclass
class BatchImageRequest:
    """Batch image generation request."""
    items: list[dict] = field(default_factory=list)  # [{"prompt": str, "style": str, "size": str}]

    @classmethod
    def from_variations(cls, base_prompt: str, styles: list[str] = None) -> "BatchImageRequest":
        batch = cls()
        for style_name in (styles or ["产品图"]):
            preset = PRESETS.get(style_name, PRESETS["产品图"])
            batch.items.append({
                "prompt": preset.build_prompt(base_prompt),
                "style": style_name,
                "aspect_ratio": preset.aspect_ratio,
                "quality": preset.quality,
            })
        return batch

    def to_api_params(self) -> list[dict]:
        """Convert to API-compatible parameters."""
        return [
            {
                "prompt": item["prompt"],
                "size": _ratio_to_size(item.get("aspect_ratio", "1:1")),
                "quality": item.get("quality", "high"),
            }
            for item in self.items
        ]


def _ratio_to_size(ratio: str) -> str:
    mapping = {"1:1": "1024x1024", "16:9": "1792x1024", "9:16": "1024x1792", "3:4": "1024x1365", "4:3": "1365x1024"}
    return mapping.get(ratio, "1024x1024")


if __name__ == "__main__":
    batch = BatchImageRequest.from_variations("AI教育课程", styles=["海报", "Logo", "产品图"])
    for p in batch.to_api_params():
        print(f"[{p['quality']}] {p['prompt'][:70]}... ({p['size']})")
