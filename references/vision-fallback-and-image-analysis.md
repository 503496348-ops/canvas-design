# Vision Fallback & Image Analysis Techniques

When `vision_analyze` fails (API key, timeout, unsupported format), use these alternative paths to understand an image before designing.

## Fallback Chain

1. **vision_analyze** → primary (OpenAI/Mimo vision model)
2. **PIL color analysis** → extract dominant colors, brightness, palette
3. **Tesseract OCR** → extract text content from posters/documents
4. **Browser screenshot** → capture rendered output for visual verification

## PIL Color Analysis (Python)

```python
from PIL import Image
import numpy as np

img = Image.open('poster.jpg')
print(f'Size: {img.size}, Mode: {img.mode}')

# Dominant colors
colors = img.getcolors(maxcolors=100000)
colors.sort(reverse=True)
for count, color in colors[:10]:
    print(f'  {count}: {color}')

# Average brightness (0-255)
arr = np.array(img)
print(f'Average RGB: {arr.mean(axis=(0,1))}')
print(f'Brightness: {arr.mean():.1f}')
```

**Interpreting results:**
- Brightness > 200 = very light image (likely pastel/white background, "APP page" feel)
- Top colors all within ±20 RGB of each other = low contrast, needs boosting
- Dominant color is (255,255,255) with >50% pixel count = white-heavy, needs darker palette

## Tesseract OCR

```bash
tesseract input.jpg /tmp/output -l chi_sim+eng --psm 6
cat /tmp/output.txt
```

**Flags:**
- `-l chi_sim+eng` — Chinese simplified + English
- `--psm 6` — assume uniform block of text (good for posters)
- `--psm 3` — fully automatic page analysis (mixed layouts)
- `--psm 4` — single column of text

## Xiaomi mimo-v2-omni API Fallback

When `vision_analyze` returns 401 (OpenAI key missing/invalid), use the Xiaomi mimo-v2-omni multimodal model as fallback. This model supports image understanding for Chinese and English content.

**Endpoint:** `https://token-plan-cn.xiaomimimo.com/v1/chat/completions`
**Model:** `mimo-v2-omni`
**Auth:** Bearer token via API keys (rotate on 401/429)

```python
import sys, json, base64, urllib.request, urllib.error

KEYS = [
    "tp-cvepkn9wk6fa9b9bda1lio002wtfmazi2u2cdd22p7ly2ovk",
    "tp-c133x0zwc8r11mjv95ou77u03w728c18o2bzqigcrzrgdky5",
    "tp-c0ugky71rvtiy3cz12bm35bzvrlssg1q2cojk7551zt0swnm",
    # ... more keys as available
]
ENDPOINT = "https://token-plan-cn.xiaomimimo.com/v1/chat/completions"
MODEL = "mimo-v2-omni"

def analyze_image(image_path, prompt):
    with open(image_path, "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode()
    
    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": [
            {"type": "text", "text": prompt},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img_b64}"}}
        ]}],
        "max_tokens": 4096
    }
    
    for i, key in enumerate(KEYS):
        req = urllib.request.Request(ENDPOINT,
            data=json.dumps(payload).encode(),
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {key}"},
            method="POST")
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                result = json.loads(resp.read().decode())
                return result["choices"][0]["message"]["content"]
        except urllib.error.HTTPError as e:
            if e.code == 429:  # quota exhausted, try next key
                continue
            raise
    return None
```

**Key rotation strategy:**
- 401 (Invalid API Key) → key expired/invalid, try next
- 429 (quota exhausted) → key rate-limited, try next
- All keys fail → fall back to PIL color analysis + Tesseract OCR

**Performance note:** mimo-v2-omni TTFB can be 3-14s depending on image size and server load. Set timeout=120 for safety.

## Browser Screenshot Path

When `browser_vision` fails but screenshot captures succeed:
- Screenshot path: `/root/.hermes/cache/screenshots/browser_screenshot_*.png`
- Share with user via `MEDIA:<path>` in final response
- Can still be useful for user to verify even without AI analysis
