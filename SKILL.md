---
name: canvas-design
description: "一念成画——从设计哲学宣言到视觉产出的完整创作引擎。静态艺术(.png/.pdf) + 演示幻灯片(HTML deck/PPTX/PDF) + 交互动原型(iOS/Android) + Motion动画(MP4/GIF) + 解说视频。34套Bold Templates + 22种瑞士版式 + 40种风格库 + Motion引擎 + 品牌资产协议 + 质量门禁。作者：AtomCollide-智械工坊团队。触发词：海报/宣传画/艺术品/幻灯片/PPT/deck/演示/原型/动画/视频/做个好看的/推荐风格/选个风格。"
author: AtomCollide-智械工坊团队
license: Complete terms in LICENSE.txt

triggers:
  - 视觉创作
  - 海报设计
  - UI设计
  - canvas-design
  - 艺游未境
---

# 一念成画 · Canvas Design

> **📖 新用户？先读 [QUICKSTART.md](references/QUICKSTART.md)** — 30秒了解能做什么、怎么用、有哪些模板。
>
> 本文档是 AI 内部执行规范，面向开发者和贡献者。普通用户只需知道说"帮我做个PPT"就够了。

从设计哲学宣言到视觉产出的完整创作引擎。你是一位用代码工作的设计师，不是程序员。用户是你的manager，你产出深思熟虑、做工精良的设计作品。

**HTML/CSS是工具，但你的媒介和产出形式会变**——做幻灯片时别像网页，做动画时别像Dashboard，做海报时别像说明书。**根据任务embody对应领域的专家**：平面设计师/动画师/UX设计师/幻灯片设计师/原型师。

## 🔴 致命反模式（2026-06-18 实战踩坑，违反=返工）

以下任何一条违反都会导致产出质量暴跌，必须逐条自检：

1. **禁止跳过 showcase 流程**：≥5 页的 deck，必须先做 2 页 showcase（视觉差异最大的两种页面类型）让用户确认 grammar，再批量推。跳过 = 全部返工。
2. **禁止自己发明 CSS**：必须用 `assets/template.html` 的 CSS 系统（字体栈、class 命名、布局工具）。自己写 CSS = 视觉质量断崖下降。
3. **禁止自己发明布局**：必须用 `references/layouts.md` 的 10 种成熟布局骨架。自己拼布局 = 信息层级混乱。
4. **禁止盲交付**：每页必须 Playwright 截图验证（字体加载、布局正确、无空白）。不验证 = 交付垃圾。
5. **禁止不规划主题节奏**：动笔前必须画 light/dark/hero 交替表。连续 3 页同主题 = 视觉疲劳。
6. **≥10 页推荐多文件架构**：每页独立 HTML + `deck_index.html` 聚合。单文件架构 CSS 全局污染风险高。
7. **禁止不问需求直接开干**：新任务必须先问清 design context、variations、fidelity。跳过 = 方向全错。
8. **禁止不读 QUICKSTART 就开工**：用户说"帮我做个PPT"时，先加载 `references/QUICKSTART.md` 了解完整能力边界和可用模板。不读 = 不知道自己能做什么，用户问"有哪些模板"答不上来。
9. **禁止混淆技能库存与产品仓库**：做竞品/仓库对比时，先查用户的 Bitable 产品表确认真实产品清单。本地 `skills_list` 返回的 300+ 是 Hermes 生态安装的外部技能，不是我们的产品仓库。报错数字 = 信任崩塌。
10. **禁止重复执行已有分析**：用户说"竞品你已经每天在追踪了"= 已有数据。先查 session_search / Bitable / 已有文档，确认是否需要增量更新而非从零重做。重复 = 浪费时间。
11. **禁止融合后残留外部品牌**：合并外部 skill 后必须做 IP 去污染。扫描所有文本文件，替换作者名/品牌名/平台名，grep 验证零残留。"加归属注释"不够——用户说"彻底改造"= 零痕迹。详见 `branding-migration` skill 的"Skill 内容 IP 去污染"章节。

---

## ⚡ 能力全景

| 能力域 | 来源 | 核心优势 |
|--------|------|----------|
| **设计哲学驱动** | canvas-design | 先写美学运动宣言，再视觉表达；博物馆/画廊品质定位 |
| **40种风格库** | canvas-design | 网页20种+PPT 20种，每种标还原度/温度/HTML实现 |
| **品牌资产协议** | canvas-design | 5步硬流程：问→搜→下载→验证→固化brand-spec.md |
| **反AI slop体系** | canvas-design | 7类slop元素+正向做法+反例隔离 |
| **设计方向顾问** | canvas-design | Fallback模式：三套逻辑并行出3版真实视觉 |
| **Motion Design引擎** | canvas-design | render-video.js 25fps + 60fps + SFX/BGM双轨 |
| **解说视频pipeline** | canvas-design | 解说稿→TTS→narration_stage→render-narration |
| **风格发现流程** | frontend-slides | 3张预览卡选择，Show Don't Tell |
| **PPT转换** | frontend-slides | extract-pptx.py+风格重设计 |
| **Vercel部署** | frontend-slides | deploy.sh一键部署 |
| **PDF/PPTX导出** | canvas-design | export-pdf.sh + export_deck_pdf/pptx.mjs |
| **Bold Template Pack** | frontend-slides | 34个大胆风格模板+deck-stage.js运行时+风格发现流程 |
| **瑞士版式系统** | canvas-design | 22个S编号版式+Swiss locked mode |
| **WebGL shader背景** | canvas-design | 流体/等高线/色散/网格/点阵 |
| **质量门禁** | canvas-design | 40项P0-P3 checklist+validate-swiss-deck.mjs |
| **iOS/Android原型** | canvas-design | ios_frame.jsx+平铺多台可操作 |
| **5维专家评审** | canvas-design | 哲学一致性/视觉层级/细节执行/功能性/创新性 |

**融合状态（2026-06-19 验证）**：canvas-design 已是三家的超集——canvas-design 24/24个references完全一致、canvas-design 4/4个assets全含、frontend-slides 34个Bold Templates已集成。新增只有 `assets/frontend-slides-viewport-base.css` 和 `references/frontend-slides-html-template.md`。

---

## 使用前提

### 适用场景
- **静态视觉**：海报、宣传画、信息图、品牌物料→.png/.pdf
- **演示幻灯片**：HTML deck(1920×1080)→PDF/PPTX→Vercel
- **交互动原型**：iOS/Android/Web mockup
- **Motion动画**：MP4/GIF+SFX/BGM
- **解说视频**：5-20分钟配音驱动动画

### 不适用场景
- 生产级Web App→`frontend-design`
- 优化已有前端→`frontend-optimization`

---

## 核心原则

### #0 事实验证先于假设
> 任何涉及具体产品/技术的事实性断言，第一步必须WebSearch验证。

硬流程：WebSearch→确认→写product-facts.md→搜不到问用户
反例：大疆Pocket 4凭记忆说没发布→实际4天前已发布→返工2小时

### #1 从已有上下文出发
先问design system/UI kit/Figma。没有→设计方向顾问模式。

#### 1.a 核心资产协议
🔴 铁律：出现品牌名→官方logo必需资产
5步：问→搜→下载→验证→固化brand-spec.md
> `references/brand-asset-protocol.md`

### #2 Junior Designer模式
assumptions+placeholders→show→确认→填内容→show→迭代

### #3 给variations不给最终答案
3+个变体跨不同维度

### #4 Placeholder>烂实现
灰色方块+标签>烂SVG

### #5 系统优先不要填充
警惕data/iconography/gradient slop

### #6 反AI slop
紫渐变/emoji图标/圆角卡片+左border/SVG画人/CSS剪影替产品图/Inter作display/GitHub-dark偷懒
正向：text-wrap:pretty+CSS Grid+oklch()+AI配图+一个细节120%
> `references/content-guidelines.md`

---

## 设计方向顾问（Fallback）

触发：需求模糊/要推荐风格/没design context

### 7个Phase
1. 对话澄清(3问题+索要参考)
2. 顾问式重述(≥200字)
3. 固化spec(≥500字，尺寸必填)
3.5. 🔴 图片素材前置(fetch_images.py，失败三级兜底)
4. 三套逻辑并行subagent：
   - 🎲 秒数轮盘(20选1从design-styles.md)
   - 🏆 现实参照(获奖作品拆解迁移)
   - 🧠 最佳设计师(预算无上限)
   - 并行：用户真实内容/纯HTML/deck走deck模板/存design-demos/确认3个.html
5. 用户基于真实视觉选择
6. 进入主干执行
> `references/design-styles.md` 40种风格库

---

## 工作流程

### Step 0 任务分类
| 输入 | 输出 | 路径 |
|------|------|------|
| 海报/艺术品 | .png/.pdf | Canvas Art |
| PPT/deck | HTML→PDF/PPTX | Deck |
| 原型 | 交互HTML | 原型 |
| 动画/视频 | MP4/GIF | Motion |

---

### Canvas Art路径
1. 设计哲学创建(命名+4-6段阐述)
2. 推导微妙参考
3. Canvas创作(单页PDF/PNG)
4. 精修(第二遍cohesive)

---

### Deck路径
Phase 1 内容发现(7问一次性)
Phase 2 风格发现(3预览卡)
Phase 3 生成(1920×1080固定舞台不可妥协)

🔴 **铁律：禁止从零生成deck CSS。** 从零写的CSS再怎么描述"modern editorial"也只是通用渐变+圆角卡片，视觉上限很低。必须先选定一个模板设计系统，读其 design.md，严格遵循其色彩/字体/间距/组件规范生成HTML。只有模板库里确实没有匹配的风格时，才允许从 design-styles.md 取风格参数组合。

#### Phase 2.5 模板选择（强制，Phase 2之后、Phase 3之前）

从 `assets/bold-template-pack/templates/` 中选一个设计系统，读其 `design.md`，把色彩、字体、间距、组件规范注入生成prompt。

**快速选型指南：**

| 内容类型 | 推荐模板 | 理由 |
|----------|----------|------|
| 知识科普/教育/长文 | **Signal** | 编辑克制、双面系统(海军蓝+暖纸白)、古金点缀、CJK支持好 |
| 商务汇报/数据驱动 | **Studio** | 极简二元(近黑+酸黄)、大字冲击力、stat卡片系统完整 |
| 杂志/时尚/品牌展示 | **Emerald Editorial** | 翡翠绿+深海蓝、Bodoni 900戏剧感、双线装饰签名 |
| 技术/产品/极客 | **Cobalt Grid** / **Cartesian** | 网格系统、蓝灰调、工程感 |
| 活泼/年轻/社交 | **Playful** / **Coral** / **Daisy Days** | 暖色、圆角(少数允许圆角的模板)、轻快节奏 |
| 暗色/科技/未来感 | **8-bit Orbit** / **Creative Mode** | 深底+霓虹、数字美学 |
| 极简/纯文字/声明式 | **Monochrome** / **Broadside** | 黑白二色、字重即设计 |

**读取 design.md 后必须注入prompt的要素：**
1. 色彩token（每个颜色的hex值和用途）
2. 字体栈（display/body/label各用什么、weight多少）
3. 间距系统（pad-x/pad-y/gap的具体值）
4. 签名处理（如Signal的gold italic `<em>`、Emerald的double-rule ornament、Studio的uppercase 900）
5. 禁忌清单（如Signal禁止圆角阴影、Studio禁止第三色）
6. CJK适配规则（中文字体替换、line-height调整、letter-spacing归零）

#### 瑞士版式(风格B Swiss locked mode)
22个S编号：S01-S22。硬规则：正文只用登记版式/data-layout必写/不发明未登记/7-8页至少6个不同S
> `references/layouts-swiss.md` `references/swiss-layout-lock.md`

#### 杂志风(风格A)
> `references/layouts.md` `references/components.md` `references/themes.md`

#### 质量门禁
> `references/checklist.md` 40项P0-P3。瑞士风：`scripts/validate-swiss-deck.mjs`

---

### PPT转换
`python scripts/extract-pptx.py`→确认→风格发现→转换

### 原型路径
默认单文件inline React+平铺4-6台可交互。iOS框：`assets/ios_frame.jsx`。Playwright测试。

### Motion路径
render-video.js→convert-formats.sh→add-music.sh+SFX→ffprobe确认
解说：解说稿→narrate-pipeline.mjs→narration_stage.jsx→render-narration.sh

### 分享导出
Vercel：`scripts/deploy.sh` | PDF：`scripts/export-pdf.sh` | PPTX：`scripts/export_deck_pptx.mjs`

---

## 品位锚点
字体：衬线display+system body | 色彩：温暖底色+单accent | 签名：一处120%质感

## 海报专用
字号：Hero 64-88px/价格最大48-56px。密度>留白。防裁切铁律。
> `references/poster-fixed-ratio-pitfalls.md`

## 文化色彩
黑→#3D3630 紫+金→除非要求 不确定→品牌资产提取
> `references/brand-color-extraction.md`

## Vision API回退
vision失败→PIL+Tesseract→mimo-v2-omni→告诉用户。永远不hallucinate。
> `references/vision-fallback-and-image-analysis.md`

## 海报重建
8维分析→提取→HTML→Playwright→vision验证
> `references/poster-recreation-workflow.md`

---

## 异常处理
需求模糊→列3方向 | 拒绝回答→best judgment+assumption | 矛盾→指出让选 | 失败→降级纯HTML | 时间紧→跳Junior标"未经验证"

## 踩坑录
> `references/deck-production-pitfalls.md` — 2026-06-18 实战总结：5次失败版本复盘 + 正确生产路径 + 技术要点。做 deck 前必读。

---

## 🔴 Deck 导出踩坑（实战铁律）

### 禁止：盲目委派子Agent写Deck HTML
子Agent没有加载设计系统的完整CSS/组件/字体栈，只会生成通用CSS渐变+圆角卡片——网页不像幻灯片。**必须自己写或自己加载模板后填内容。**

### 禁止：重型模板直接用于Playwright导出
template.html 依赖以下技术，在 Playwright 截图时**全部会崩**：
- WebGL canvas 背景（GPU渲染在headless浏览器中不可靠）
- ES Module 动态 import（`motion.min.js` 本地+CDN双重失败）
- CDN 字体加载（headless 环境网络受限，Google Fonts 不稳定）
- `file://` 协议下 ES Module import 直接报错

**导出PDF的正确路径：**
1. 用轻量级HTML（内联CSS、系统字体栈、零外部依赖）
2. 自己写每一页，不委派
3. 浏览器打开确认 `console_errors === 0` 后再跑 export-pdf.sh
4. 不能用 vision API 时，至少用 `browser_console` 检查JS错误

### 系统字体栈（零CDN依赖版）
```css
font-family: Georgia, 'Noto Serif SC', serif;        /* 衬线标题 */
font-family: 'Noto Sans SC', 'PingFang SC', system-ui, sans-serif;  /* 正文 */
font-family: 'Courier New', monospace;                /* kicker/meta标签 */
```
中文环境预装 Noto Sans SC / PingFang SC，不依赖CDN。

### export-pdf.sh 的 .slide 类名要求
导出脚本硬编码查找 `document.querySelectorAll('.slide')`。如果自定义类名（如 `.s`），必须改为 `.slide`，否则报 "No .slide elements found"。

### 标题占位符陷阱
template.html 的 `<title>` 默认是 `[必填] 替换为 PPT 标题 · Deck Title`，**必须替换**，否则PDF文件名和浏览器标签页都会暴露占位符。

### 轻量Deck模板（可复制起点）
HTML结构：`<div class="slide">` × N → `export-pdf.sh` 直接兼容。
最小骨架：1920×1080舞台 + transform缩放 + 键盘/滚轮导航。
参考：`/root/.hermes/output/prompt-deck-v4.html` 作为已验证的起点。

---
## 资源导览

### 轻量级Deck骨架（零依赖，Playwright导出安全）
> `references/lightweight-deck-skeleton.html` — 可直接复制的起点模板。系统字体栈、1920×1080舞台、键盘/滚轮导航、`.slide` 类名兼容 export-pdf.sh。替换 `SLIDES_HERE` 占位符和 `DECK_TITLE` 即可。

```
canvas-design/
├── SKILL.md
├── references/ (45 files, 含QUICKSTART.md): design-styles, brand-asset-protocol, content-guidelines,
│   STYLE_PRESETS, html-template, animation-patterns, layouts, layouts-swiss,
│   swiss-layout-lock, themes, themes-swiss, components, checklist,
│   critique-guide, voiceover-pipeline, video-export, ...
├── scripts/ (12 files): fetch_images.py, html2pptx.js, render-video.js,
│   export_deck_pdf.mjs, export_deck_pptx.mjs, validate-swiss-deck.mjs,
│   extract-pptx.py, deploy.sh, export-pdf.sh, ...
├── assets/: deck_index.html, ios_frame.jsx, narration_stage.jsx,
│   template.html, template-swiss.html, viewport-base.css, motion.min.js,
│   bold-template-pack/ (34 templates), sfx/, screenshot-backgrounds/, canvas-fonts/
└── design-philosophy.md
```

---

## 检查点
碰到🛑就停下告诉用户，然后真的**等**。

---

## 融合来源与竞品对标

### 能力来源（内部追溯，非对外品牌）
| 能力模块 | 原始来源 | 融合内容 | 状态 |
|---------|---------|---------|------|
| 核心引擎 | 内部原创 | 设计哲学驱动 + 40种风格库 + Motion引擎 + 品牌资产协议 | ✅ 100% |
| 瑞士版式 | 内部整合 | 22个S编号版式 + 质量门禁 + validate脚本 + 4个模板资产 | ✅ 100% |
| Bold Templates | 内部整合 | 34个模板 + deck-stage.js运行时 + 风格发现流程 + PPT转换 | ✅ 100% |

### canvas-design 独有优势
- 设计哲学宣言驱动（先写美学运动，再视觉表达）
- 博物馆/画廊品质定位
- 海报防裁切铁律
- 文化色彩禁忌（中文场景）
- 5维专家评审
- Vision API回退链路

### 仓库地址
- `https://github.com/503496348-ops/canvas-design`
