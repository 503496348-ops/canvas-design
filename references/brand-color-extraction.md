# Brand Color Extraction from Logo Images

## When to Use
User provides a logo or brand image and wants design work (poster, UI, document) that matches their brand.

## Method: PIL Color Analysis

```python
from PIL import Image
import collections

def extract_brand_colors(image_path, sample_size=100):
    """Extract dominant brand colors from a logo image."""
    img = Image.open(image_path)
    img_small = img.resize((sample_size, sample_size))
    pixels = list(img_small.getdata())
    
    # Separate accent colors (non-white, non-black, non-gray)
    accents = []
    for p in pixels:
        r, g, b = p[:3]
        # Skip near-white
        if r > 230 and g > 230 and b > 230: continue
        # Skip near-black
        if r < 20 and g < 20 and b < 20: continue
        # Skip grays (R≈G≈B)
        if abs(r-g) < 15 and abs(g-b) < 15: continue
        accents.append((r, g, b))
    
    # Quantize and count
    color_count = collections.Counter()
    for r, g, b in accents:
        qr, qg, qb = (r//16)*16, (g//16)*16, (b//16)*16
        color_count[(qr, qg, qb)] += 1
    
    return color_count.most_common(8)
```

## Interpreting Results

1. **Most frequent accent** → PRIMARY color (headers, CTA, key elements)
2. **2nd-3rd most frequent** → SECONDARY colors (cards, variety elements)
3. **Colors appearing <10% of primary frequency** → ACCENT (rare decorative gestures)
4. **Warm grays/taupes** → NEUTRAL BRIDGE (text, dividers, subtle elements)

## Palette Construction Rules

| Role | Usage | Surface Area |
|------|-------|-------------|
| Primary | Headers, CTA, key accents | 40-50% of colored area |
| Secondary | Cards, blocks, variety | 30-40% of colored area |
| Accent | Lines, dots, highlights | <10% of colored area |
| Neutral | Text, dividers, backgrounds | Functional, not decorative |
| Background | Page/canvas base | Largest single color |

## Anti-Patterns

- **NEVER guess colors** — always extract first
- **NEVER use 3+ competing colors** at equal weight — pick ONE primary
- **NEVER use pure black (#000)** for text — use warm dark (#3D3630)
- **NEVER use pure white (#FFF)** for background — use warm cream (#F4F0E8)
- **NEVER use high-saturation colors** unless the logo demands it

## Cultural Notes

- Chinese market: black is unlucky, purple+gold perceived as tacky
- When in doubt: muted > saturated, warm > cool, restrained > bold
