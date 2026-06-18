# Poster Analysis & Recreation Workflow

When the user provides an existing poster and asks to "do something similar" or "analyze and recreate", follow this pipeline.

## Phase 1: Design Analysis (8 Dimensions)

Use vision model (or fallback chain) to analyze the reference poster:

1. **整体结构布局** — How many zones? Position and size ratios?
2. **信息层级设计** — Visual weight distribution across title/subtitle/features/price
3. **色彩运用** — Primary, secondary, accent colors and how they guide the eye
4. **字体与排版** — Font size, weight, style differences across hierarchy levels
5. **留白与间距** — Inter-zone spacing, line height, margins
6. **视觉引导路径** — Where does the eye land first? How does it flow?
7. **设计风格** — Flat/skeuomorphic/minimal? Overall aesthetic?
8. **亮点与不足** — What works, what could improve?

Save analysis to `/tmp/poster_analysis.md` for reference during recreation.

**IMPORTANT:** Use vision FIRST, text extraction SECOND. Text extraction misses visual hierarchy, character placement, color relationships. The user will correct you if your "analysis" doesn't match what they see.

## Phase 2: Content Extraction

If the poster contains text that needs to be reused:
- Use vision model to extract all text content
- Structure into: brand identity, product info, pain points, features, data highlights, pricing
- Save to `/tmp/extracted_content.json` for template population

## Phase 3: HTML/CSS Template Creation

Build a self-contained HTML file applying the analyzed design principles:

### Layout Structure (vertical progressive)
```
┌─────────────────────┐
│  Header (brand+tag) │  ~10%
├─────────────────────┤
│  Title + Subtitle   │  ~15%
├─────────────────────┤
│  Pain Points Grid   │  ~25% (2×3 or 3×2 cards)
├─────────────────────┤
│  Features Grid      │  ~30% (3×3 colored blocks)
├─────────────────────┤
│  Data Highlights    │  ~10% (big numbers)
├─────────────────────┤
│  Price + CTA        │  ~10% (gradient block)
├─────────────────────┤
│  Footer             │  ~5%
└─────────────────────┘
```

### CSS Best Practices
- Use CSS Grid for card/block layouts
- CSS variables for brand colors
- `border-radius: 10-12px` for modern card feel
- `box-shadow: 0 4px 20px rgba(0,0,0,0.08)` for depth
- Gradient backgrounds for CTA sections: `linear-gradient(135deg, primary, secondary)`
- Responsive width: 800px default, scales on mobile

### Brand Color Application
- Background: warm cream (#F4F0E8) — never pure white
- Text: warm dark brown (#3D3630) — never pure black
- Primary accent: for CTAs, key highlights
- Secondary accent: for feature blocks, supporting elements
- Feature blocks: rotate 2-3 colors for visual variety

## Phase 4: HTML → PNG Conversion

Use Playwright for reliable HTML-to-image conversion:

```python
import asyncio
from playwright.async_api import async_playwright

async def html_to_image(html_path, output_path, width=900, height=1200):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.set_viewport_size({"width": width, "height": height})
        await page.goto(f"file://{html_path}")
        await page.wait_for_load_state("networkidle")
        await page.screenshot(path=output_path, full_page=False, type="png")
        await browser.close()
```

**Key settings:**
- `full_page=False` for fixed-ratio posters (enforces boundary)
- `full_page=True` only when you want to capture entire scrollable page
- `type="png"` — lossless, better for text-heavy designs
- Viewport = EXACT user-requested dimensions
- Wait for `networkidle` to ensure fonts/styles are loaded

## Phase 5: Quality Validation

Use vision model to evaluate the generated poster:
1. **整体印象** — First impression, professionalism
2. **信息完整性** — All necessary info included? Bottom not cropped?
3. **视觉层次** — Clear hierarchy? Can user find key info fast?
4. **色彩搭配** — Colors harmonious? Match product positioning?
5. **排版质量** — Text aligned? Spacing appropriate?
6. **改进建议** — Specific optimization suggestions

Score each dimension 1-10. Iterate if any score < 7.

## Pitfalls

### Vision Analysis Before Recreation
**Never assume content from text extraction alone.** When recreating a poster:
1. FIRST use vision to observe actual visual elements (mascots, colors, layout)
2. THEN extract text content
3. Compare both — text extraction misses visual hierarchy, character placement, color relationships

The user will correct you if your "analysis" doesn't match what they see. Trust the user's description over your assumptions.

### Iterative Poster Refinement
Poster design is inherently iterative. Expect 3-8 rounds. Save each version as `poster_v{N}.html` + `poster_v{N}.png` for rollback. Common feedback → fix mapping in `references/poster-fixed-ratio-pitfalls.md`.

### Vision API Key Exhaustion
The Xiaomi mimo-v2-omni API keys have rate limits. When one key returns 429 (quota exhausted), rotate to the next key. The KEYS array in the analysis script handles this automatically.

### Playwright Font Loading
If custom fonts don't render in the screenshot, add `await page.wait_for_timeout(1000)` after `networkidle` to give fonts extra loading time.

### Poster Width vs Phone Screen
Promotional posters are read on phones. Ensure:
- Hero title ≥ 64px
- Body text ≥ 14px
- Price numbers ≥ 36px
- CTA text ≥ 18px
- All text readable on 5.5" screen

### Color Contrast on Feature Blocks
White text on colored blocks needs sufficient contrast. Test with:
- Green blocks: use darker shades (#5A7A5E+)
- Blue blocks: use darker shades (#4A7A86+)
- Brown blocks: use darker shades (#7B6D5B+)
- Avoid light pastels as block backgrounds when text is white
