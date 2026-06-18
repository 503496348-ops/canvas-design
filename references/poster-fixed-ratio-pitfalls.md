# Fixed-Ratio Poster Design Pitfalls

Learned from JKL教务官 poster creation session (2026-06-09). 13+ iterations of feedback revealed critical patterns.

## The Core Problem

Fixed-aspect-ratio posters (4:6 = 948×1422, 3:4, 1:1, etc.) have a hard content boundary. Unlike web pages that scroll, anything below the viewport is silently clipped. This causes:

1. **Bottom content cropping** — most common failure. User sees incomplete information.
2. **Spacing bloat** — generous margins/padding from web design habits eat vertical space.
3. **Information overload** — trying to fit too much content into a fixed canvas.

## Mandatory Pre-Render Checklist

For ANY fixed-ratio poster:

- [ ] Set viewport to EXACT requested dimensions (e.g. 948×1422)
- [ ] Use `full_page=False` in Playwright to enforce boundary
- [ ] Calculate total content height before writing HTML
- [ ] If total > viewport height: reduce spacing, shrink fonts, or split into 2 posters
- [ ] After screenshot, verify bottom content is visible (use vision or manual check)

## Spacing Rules for Fixed-Height Layouts

When height is constrained, every pixel matters. Default web spacing is too generous:

| Element | Web Default | Fixed-Height Poster |
|---------|------------|-------------------|
| Header padding | 40-60px | 30-40px |
| Section margins | 40-50px | 20-30px |
| Card gaps | 16-20px | 12-16px |
| Card padding | 24-30px | 16-20px |
| Section title margin | 30-40px | 20-25px |
| Footer padding | 30-40px | 15-20px |

## Multi-Poster Splitting Strategy

When content is too dense for one poster, split by user journey:

**Poster 1 (Awareness/Features):**
- Brand header
- Hero title + subtitle
- Core features OR pain points (pick one)
- Price section (if space allows)

**Poster 2 (Conversion/Data):**
- Brand header (compact)
- Data highlights (big numbers)
- Pricing details + service list
- CTA button

Each poster must be self-contained. Never split a single logical section across posters.

## Color Comfort Iteration Pattern

Users often find high-contrast promotional colors overwhelming after initial approval. The progression:

1. **v1**: High contrast (deep blue #1a2a6c + bright orange #FFB347) — "太刺眼"
2. **v2**: Add white/light elements, reduce saturation — "舒服多了"
3. **v3**: Fine-tune glassmorphism, soft glows — "刚好"

**Comfort color palette:**
- Deep background: #2a3a7c (not #1a2a6c)
- Accent text: #e8d8b0, #f0c878 (not #FFD700)
- Cards: `rgba(255,255,255,0.06)` with `backdrop-filter: blur()`
- Decorations: radial-gradient glows, not solid circles

## Mascot/Character Handling

**User expectation:** Real illustrated characters (AI-generated or hand-drawn)
**What NOT to do:** Use emoji as mascot substitutes
**What NOT to do:** Use SVG-drawn "ugly" mascots — user said "去除顶部信息栏两边丑得要死的奇怪吉祥物"

Options by capability:
1. **FAL_KEY available**: Use `image_generate` for cute character illustrations
2. **No image gen**: Omit mascots entirely — clean design > ugly placeholders
3. **NEVER**: Use emoji as mascot substitutes (user explicitly banned this)

## Feature Icons

Every feature item needs a visual icon for quick scanning. Options:
- **Emoji**: 👥📄✅📈⏰📅💬📊💻 (fast, universal — OK for feature icons, NOT for mascots)
- **SVG icons**: Custom, brand-consistent but more work
- **Unicode symbols**: ◆ ● ▶ ★ (minimal, clean)

Place icon ABOVE feature name, 28-32px size, with 8px bottom margin.

## Iteration Versioning

Save each version for comparison and rollback:
```
/tmp/poster_v1.html → /tmp/poster_v1.png
/tmp/poster_v2.html → /tmp/poster_v2.png
...
```

Common correction → fix mapping:
| User Feedback | Fix |
|--------------|-----|
| "底部被裁切" | Reduce spacing, verify with `full_page=False` |
| "信息太多" | Split into 2 posters |
| "字体太小" | Increase all sizes 20-30% |
| "间距太大" | Reduce margins/padding by 30-50% |
| "配色太刺眼" | Lower saturation, add white balance |
| "吉祥物丑" | Remove entirely or use AI-generated images |
| "缺少图标" | Add emoji/SVG icons to features |
| "名字错了" | Check Chinese terminology (九大 vs 十大) |

## Chinese Poster Terminology

Common feature count naming:
- 6 features: 六大核心功能
- 9 features: 九大核心功能
- 10 features: 十大核心功能

Always match the ACTUAL number of items. If you have 9 items, say "九大" not "十大".

## Price Card Layout Pattern

For commercial posters with multiple price tiers, use a left-right split layout:

```
┌─────────────────────────────────────────┐
│ 价格标题                                │
├────────────┬────────────────────────────┤
│ ¥499       │ 1对1深度咨询               │
│ /小时       │ 定制AI工作流方案           │
├────────────┼────────────────────────────┤
│ ¥599       │ 包含咨询诊断               │
│ 一次性      │ 国内服务器实际部署         │
├────────────┼────────────────────────────┤
│ ¥199/月    │ 持续运维保障               │
│            │ 日常巡检+故障排查          │
└────────────┴────────────────────────────┘
```

CSS pattern:
```css
.price-row {
    display: flex;
    align-items: center;
    padding: 12px 0;
    border-bottom: 1px solid rgba(0,0,0,0.05);
}
.price-left { width: 180px; flex-shrink: 0; }
.price-right { flex: 1; padding-left: 20px; border-left: 1px solid rgba(0,0,0,0.06); }
```

**Detail text rule**: Right-side details are ACCENT, not primary content. Keep to 2-3 short lines max. Use `<span>` for emphasis on key phrases. Don't fill all space — let breathing room be part of the design.

## Glassmorphism Effect

Modern commercial posters benefit from glassmorphism (frosted glass) effects:

```css
.glass-card {
    background: rgba(255,255,255,0.06);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 24px;
}
```

Use for: feature sections, data highlight sections. NOT for price sections (price needs solid white background for readability).

## Soft Glow Decorations

Replace solid colored circles with radial-gradient glows for depth:

```css
/* Instead of: background: #FFB347; opacity: 0.1; */
.bg-glow {
    background: radial-gradient(circle, rgba(255,220,150,0.12) 0%, transparent 70%);
}
```

Place glows at corners (top-right, bottom-left) with 500-600px diameter.

## Vision API Hallucination Pitfall

**CRITICAL**: When analyzing images for recreation, NEVER claim to see visual features without actual verification.

**What happened**: Agent analyzed a poster and described "two mascots" and "orange-yellow + deep blue contrast" without actually seeing the image (vision_analyze failed with 401).

**Rule**: If vision_analyze fails, use the Xiaomi mimo-v2-omni API fallback (see vision-fallback reference). If ALL vision APIs fail, tell the user "I cannot see the image clearly, please describe the key visual features" — do NOT hallucinate descriptions.

**Verification step**: After any image analysis, ask yourself: "Did I actually receive and process image data, or am I guessing?"

## Price Information Hierarchy

In commercial posters, price information must have **THE HIGHEST** visual priority:

**User's explicit rule**: "价格信息的重要等级是最高的" — Price information importance level is the highest.

1. **White/light background** for price section (stands out from dark poster background)
2. **Large price numbers** (48-56px, bold, dark color) — must be the LARGEST font on the poster
3. **Price section near bottom** but above CTA
4. **Price card shadow** (`box-shadow: 0 15px 45px rgba(0,0,0,0.25)`) for depth
5. **Clear price labels** (16-18px, gray)
6. **Service descriptions** as subtle accent (13-14px, lighter gray)

Don't bury prices in small text or same-background cards. They need to POP.

**Font size priority**: Price numbers > Hero title > Feature names > Descriptions > Brand info

## Iterative Design Workflow

The poster creation process is inherently iterative. Expect 5-10 rounds of feedback.

**Version naming**: `/tmp/poster_v{N}.html` and `/tmp/poster_v{N}.png`

**Common iteration sequence**:
1. v1: Initial layout + content
2. v2: Adjust spacing (usually reduce)
3. v3: Fix color comfort (reduce contrast)
4. v4: Fix information completeness (add/remove sections)
5. v5: Fix specific content errors (names, counts, prices)
6. v6: Add visual elements (icons, details)
7. v7: Update pricing/CTA information
8. v8: Fine-tune detail placement and density

**After each iteration**: Screenshot → send to user → wait for feedback. Never assume the design is final.

## Detail Text as Accent

When adding detail text to price cards or feature descriptions:
- Use as DECORATIVE ACCENT, not primary information
- 2-3 short lines maximum per price item
- Highlight key phrases with `<span>` color change
- Leave breathing room — don't fill all white space
- Font size: 13-14px (smaller than main text)
- Color: #6a7a9a (muted, not competing with prices)

## Critical Pitfall: Modify the Correct Poster

**User frustration**: "我要的是修改这张海报 不是发其他的两张海报给我" (I want you to modify THIS poster, not send me two other posters)

**Rule**: When user sends an image and asks to modify it:
1. Analyze the image content first (use vision API)
2. Identify which poster it is
3. Modify ONLY that poster's HTML
4. Send ONLY the modified poster
5. Do NOT create new posters or modify different ones

**Verification**: Before sending, confirm: "Am I sending the poster the user asked me to modify, or a different one?"

## Critical Pitfall: No Cropping Allowed

**User frustration**: "不要让我再强调别出现不完整的信息了" (Don't make me emphasize no incomplete info again)

**Rule**: ALL content must be fully visible within the canvas boundary. No exceptions.

**If content doesn't fit**:
1. Reduce spacing (priority 1)
2. Reduce font sizes (priority 2)
3. Split into 2 posters (priority 3)
4. NEVER let content get cropped

**Verification**: After every render, check the bottom edge of the screenshot for any cut-off content.

## Critical Pitfall: Flex Layout for Bottom Content

**Technique**: Use CSS flex layout to automatically position bottom content:

```css
.poster {
    display: flex;
    flex-direction: column;
    overflow: hidden;
}
.footer { margin-top: auto; } /* Pushes footer to bottom */
```

This prevents the common issue where bottom content (price, CTA, footer) gets cropped because the content height exceeds the canvas height.