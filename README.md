# 🎨 艺游未境 · Wanderix

> **视觉创作全链路引擎** — 从一句话描述到设计级视觉产出，覆盖海报、幻灯片、原型、动画、视频、AI生图、手账涂鸦。  
> 设计哲学驱动 × 96种模板/风格/版式 × 质量门禁体系

[![License](https://img.shields.io/badge/license-Apache_2.0-blue.svg)](LICENSE)
[![Templates](https://img.shields.io/badge/templates-34%20Bold%20Templates-orange.svg)](assets/bold-template-pack/)
[![Swiss](https://img.shields.io/badge/layouts-22%20Swiss-brightgreen.svg)](references/layouts-swiss.md)
[![Styles](https://img.shields.io/badge/styles-40%20种风格库-purple.svg)](references/design-styles.md)

**作者：** [AtomCollide-智械工坊团队](https://github.com/503496348-ops)

---

## 📋 能力总览

| 能力域 | 来源 | 输出格式 | 核心优势 |
|--------|------|----------|----------|
| 🖼️ 海报 / 宣传画 | Canvas Design | `.png` / `.pdf` | 设计哲学驱动，博物馆品质定位 |
| 📊 演示幻灯片 | Canvas Design | HTML deck → PDF / PPTX | 34套Bold Templates + 22种瑞士版式 |
| 🧩 原生可编辑PPTX | Canvas Design | `.pptx` | 960×540pt物理画布 + 原生shape/text/image |
| 🎤 演讲者模式 | Canvas Design | HTML presenter view | 当前页/下一页/逐字稿/计时器，按 `S` 打开 |
| 🧵 图片型社交Deck | Canvas Design | `.png` / `.jpg` / PDF | 小红书/公众号/课程卡片，一页一图 |
| 📥 多源资料摄取 | Canvas Design | `source-brief.md` | URL/MD/TXT/HTML → 结构化 brief |
| 📱 交互原型 | Canvas Design | iOS / Android mockup | `ios_frame.jsx` + 平铺多台可操作 |
| 🎬 Motion动画 | Canvas Design | `.mp4` / `.gif` | `render-video.js` 25fps + 60fps + SFX/BGM |
| 🎙️ 解说视频 | Canvas Design | `.mp4` | 解说稿 → TTS → 配音驱动动画 |
| 🤖 AI生图 | GPT Image 2 API | `.png` | 批量生成 + 风格控制 |
| 📓 PLOC手账涂鸦 | Wanderix Pipeline | `.png` | 旅行/风景照片 + ins风手绘装饰 |
| 👤 肖像身份锚定 | Wanderix Portrait | 跨次一致性肖像 | `portrait_prompt.py` 多视角锚定 |

---

## 🚀 快速开始（小白5步版）

### 第1步：克隆仓库

```bash
git clone https://github.com/503496348-ops/canvas-design.git ~/.hermes/skills/canvas-design
```

### 第2步：安装依赖

```bash
cd ~/.hermes/skills/canvas-design

# Node.js 工具链（渲染/导出/验证）
npm install

# Python 工具链（PPT提取/生图/流水线）
pip install -r requirements.txt  # 如果存在
pip install python-pptx Pillow   # PPT提取 + 图像处理
```

### 第3步：第一次使用

直接对 AI 说：

```
帮我做一个关于 [主题] 的幻灯片，大概 [N] 页
```

AI 会自动执行：
1. **问你 5-10 个问题** — 受众、风格、输出格式偏好
2. **做 2 页示例** — 封面 + 内容页，发给你确认方向
3. **你确认后** — 批量推剩下 N-2 页
4. **逐页截图验证** — Playwright 检查字体加载、布局正确
5. **导出交付** — PDF / PPTX / 部署链接

### 第4步：常用命令

```bash
# 导出 PDF
bash scripts/export-pdf.sh ./my-deck.html ./output.pdf

# 导出 PPTX（多文件 slide deck → 原生可编辑 PPTX）
node scripts/export_deck_pptx.mjs --slides ./slides --out ./output.pptx

# 资料摄取：URL/Markdown/HTML/TXT → source-brief.md
python3 scripts/source_intake.py --input ./article.md --out ./source-brief.md

# 瑞士版式验证
node scripts/validate-swiss-deck.mjs index.html

# 一键部署到 Vercel
bash scripts/deploy.sh

# Motion 视频渲染
node scripts/render-video.js ./scene.json ./output.mp4

# AI 生图
python3 scripts/gpt_image_api.py "赛博朋克风格的城市海报"
```

### 第5步：飞书怎么用

在飞书群聊或私聊中 @ 你的 AI 助手，直接说：

```
帮我做一个关于Q2业务复盘的PPT，10页左右，深色风格
```

AI 会在飞书内完成设计 → 截图确认 → 导出 PDF → 直接发送文件到飞书聊天窗口。

支持的飞书触发词：`海报` `宣传画` `艺术品` `幻灯片` `PPT` `deck` `演示` `可编辑PPTX` `客户要改` `讲稿` `逐字稿` `计时器` `小红书图文` `知识卡片` `原型` `动画` `视频` `做个好看的` `推荐风格` `选个风格`

---

## 🎨 模板速查

### 34 套 Bold Templates

每套模板在 `assets/bold-template-pack/templates/` 下有完整的 `design.md` + `preview.md`。

| 模板名 | 风格关键词 |
|--------|-----------|
| `8-bit-orbit` | 像素风 · 复古游戏 |
| `biennale-yellow` | 双年展 · 明黄海报 |
| `block-frame` | 方块框架 · 粗线条 |
| `blue-professional` | 商务蓝 · 稳重专业 |
| `bold-poster` | 大胆海报 · 高冲击力 |
| `broadside` | 横幅大字 · 信息密集 |
| `capsule` | 胶囊形状 · 圆润柔和 |
| `cartesian` | 笛卡尔网格 · 理性精确 |
| `cobalt-grid` | 钴蓝网格 · 科技感 |
| `coral` | 珊瑚色 · 温暖活力 |
| `creative-mode` | 创意模式 · 实验性排版 |
| `daisy-days` | 雏菊 · 清新自然 |
| `editorial-forest` | 森系编辑 · 自然主义 |
| `editorial-tri-tone` | 三色调编辑 · 杂志感 |
| `emerald-editorial` | 翡翠绿编辑 · 高端质感 |
| `grove` | 林地 · 有机纹理 |
| `long-table` | 长桌 · 信息列表排版 |
| `mat` | 垫子质感 · 低调克制 |
| `monochrome` | 单色极简 · 黑白对比 |
| `neo-grid-bold` | 新网格 · 粗体现代 |
| `peoples-platform` | 民众平台 · 社会议题 |
| `pin-and-paper` | 图钉纸张 · 手工拼贴 |
| `pink-script` | 粉色手写 · 柔美文艺 |
| `playful` | 活泼童趣 · 色彩丰富 |
| `raw-grid` | 原始网格 · 粗糙真实 |
| `retro-windows` | 复古窗口 · Win95美学 |
| `retro-zine` | 复古杂志 · 拼贴风 |
| `sakura-chroma` | 樱花色相 · 日系柔和 |
| `scatterbrain` | 散点思维 · 自由发散 |
| `signal` | 信号 · 高对比现代 |
| `soft-editorial` | 柔和编辑 · 留白优雅 |
| `stencil-tablet` | 模板板 · 工业风 |
| `studio` | 工作室 · 专业简洁 |
| `vellum` | 羊皮纸 · 古典质感 |

> 📖 完整设计规范：`assets/bold-template-pack/templates/<name>/design.md`

### 22 种瑞士版式 (Swiss Layouts)

编号 `S01` ~ `S22`，定义在 `references/layouts-swiss.md`。每个版式严格锁定在 `<section data-layout="Sxx">` 上。

| 版式编号 | 用途 | 核心骨架 |
|----------|------|----------|
| S01 | 封面/标题页 | 大标题居中 + 副标题 |
| S02 | 双栏内容 | 左文右图 / 左图右文 |
| S03 | 三栏网格 | 信息并列展示 |
| S04 | 引言/金句 | 大字引用 + 署名 |
| S05 | 时间线 | 水平/垂直时间轴 |
| S06 | 数据表格 | 结构化数据展示 |
| S07 | 图表页 | 数据可视化 |
| S08 | 地图/空间 | Swiss Map Component |
| S09 | 列表页 | 有序/无序清单 |
| S10 | 对比页 | A vs B 双栏对比 |
| S11 | 流程图 | 步骤/决策流程 |
| S12 | 团队/人物 | 头像 + 简介网格 |
| S13 | 价格表 | 定价方案对比 |
| S14 | FAQ页 | 问答折叠 |
| S15 | 图片矩阵 | 多图网格排列 |
| S16 | 小报拼贴 | 杂志式图片排版 |
| S17 | 全屏图片 | 单张大图铺满 |
| S18 | 分屏 | 50/50 或 30/70 分割 |
| S19 | 侧边栏 | 左侧导航 + 右侧内容 |
| S20 | 卡片流 | 自适应卡片网格 |
| S21 | 时间轴+内容 | 左侧时间线 + 右侧详情 |
| S22 | Image Hero | 单张大图 + 叠加文字 |

> ⚠️ **重要约束**：一份 deck 只能选一套版式系统（Bold 或 Swiss），不能混用。

### 40 种风格库

定义在 `references/design-styles.md`，分两大类：

| 分类 | 数量 | 说明 |
|------|------|------|
| 网页风格库 | 20 种 | 适合 Web 页面、交互原型、在线 deck |
| PPT风格库 | 20 种 | 适合传统幻灯片、正式演示、PDF 输出 |

每种风格标注：还原度等级、视觉温度（暖/冷/中性）、HTML/CSS 实现要点。

> 📖 完整列表：`references/design-styles.md`

---

## 📂 文件结构

```
canvas-design/
├── SKILL.md                          # AI 内部执行规范（开发者必读）
├── README.md                         # 本文件
│
├── references/                       # 设计规范文档库（45篇）
│   ├── QUICKSTART.md                 # 快速上手指南
│   ├── design-styles.md              # 40种风格库
│   ├── layouts.md                    # 10种基础布局骨架
│   ├── layouts-swiss.md              # 22种瑞士版式
│   ├── STYLE_PRESETS.md              # 12种预设风格配色方案
│   ├── themes.md                     # 主题系统
│   ├── themes-swiss.md               # 瑞士版式主题
│   ├── animations.md                 # 动画规范
│   ├── animation-patterns.md         # 动画模式库
│   ├── animation-best-practices.md   # 动画最佳实践
│   ├── brand-asset-protocol.md       # 品牌资产5步协议
│   ├── components.md                 # UI组件库
│   ├── checklist.md                  # 质量门禁清单（40项）
│   ├── verification.md               # 验证规范
│   ├── content-guidelines.md         # 内容规范
│   ├── cinematic-patterns.md         # 电影化模式
│   ├── slide-decks.md                # 幻灯片制作指南
│   ├── image-prompts.md              # AI生图提示词
│   ├── sfx-library.md                # 音效库
│   ├── video-export.md               # 视频导出规范
│   ├── ppt-skills-fusion.md          # PPT Skills 融合增强路线
│   ├── editable-pptx.md              # 原生可编辑 PPTX 硬约束
│   ├── presenter-mode.md             # 演讲者模式/逐字稿/计时器
│   ├── image-deck-mode.md            # 图片型社交 Deck
│   ├── source-intake-adapter.md      # 多源资料摄取入口
│   ├── wanderix-ploc-template.json   # PLOC手账模板
│   ├── wanderix-templates-registry.json  # 模板注册表
│   └── ...                           # 更多专业文档
│
├── assets/                           # 模板与静态资源
│   ├── template.html                 # 核心 HTML 模板（CSS系统）
│   ├── template-swiss.html           # 瑞士版式 HTML 模板
│   ├── bold-template-pack/           # 34套 Bold Templates
│   │   ├── selection-index.json      # 模板选择索引
│   │   └── templates/
│   │       ├── 8-bit-orbit/          # 每个模板含 design.md + preview.md
│   │       ├── bold-poster/
│   │       ├── studio/
│   │       └── ...                   # 共34个模板目录
│   ├── showcases/                    # 展示案例
│   ├── director-notes-samples/       # 导演笔记示例
│   ├── presenter-runtime.js          # 演讲者窗口运行时
│   ├── animations.jsx                # After Effects 动画脚本
│   └── viewport-base.css             # 幻灯片基础样式
│
└── scripts/                          # 工具脚本（25个）
    ├── export-pdf.sh                 # PDF 导出
    ├── export_deck_pdf.mjs           # Deck → PDF（Node.js）
    ├── export_deck_pptx.mjs          # Deck → PPTX
    ├── html2pptx.js                  # HTML → PPTX 转换
    ├── extract-pptx.py               # PPTX 提取 + 风格重设计
    ├── source_intake.py              # 多源资料 → source-brief.md
    ├── deploy.sh                     # Vercel 一键部署
    ├── render-video.js               # Motion 视频渲染（25fps/60fps）
    ├── render-video-seek.js          # 视频渲染（带定位）
    ├── render-narration.sh           # 解说视频渲染
    ├── validate-swiss-deck.mjs       # 瑞士版式验证器
    ├── gpt_image_api.py              # GPT Image API 封装
    ├── batch_generator.py            # 批量图片生成
    ├── wanderix_pipeline_engine.py   # Wanderix 流水线引擎
    ├── portrait_prompt.py            # 肖像提示词生成
    ├── tts-doubao.mjs               # 豆包 TTS 语音合成
    ├── gen_deck_thumbs.mjs           # Deck 缩略图生成
    └── ...                           # 更多工具脚本
```

---

## 🔗 融合状态

本仓库是 Canvas Design 的统一产品化版本。2026-06-30 已完成 PPT Skills 增强，新增四个确定增量：

| 增强模块 | 吸收能力 | 融合状态 |
|------|----------|----------|
## 🔗 融合状态

本仓库是 Canvas Design 的统一产品化版本。2026-06-30 已完成 PPT Skills 增强，新增四个确定增量：

| 增强模块 | 吸收能力 | 融合状态 |
|------|----------|----------|
| 原生可编辑 PPTX | 物理画布约束、HTML 硬规则、逐元素转 PowerPoint 原生对象 | ✅ 已落地 |
| 演讲者模式 | 当前页/下一页/逐字稿/计时器/双窗口同步 | ✅ 已落地 |
| 图片型社交 Deck | 小红书/公众号/课程卡片，一页一图，prompt 留痕 | ✅ 已落地 |
| 多源资料摄取 | URL/MD/TXT/HTML → `source-brief.md`，其它资料走前置文档/转写工具 | ✅ 已落地 |
| 旧有审美体系 | 34套 Bold Templates、22种瑞士版式、40种风格库、质量门禁 | ✅ 已内化 |

**融合验证**：不保留外部竞品品牌作为运行依赖；AGPL 来源只吸收模式，不复制代码。新增能力入口见 `references/ppt-skills-fusion.md`.

**融合验证**：不保留外部竞品品牌作为运行依赖；AGPL 来源只吸收模式，不复制代码。新增能力入口见 `references/ppt-skills-fusion.md`。

---

## ❓ FAQ / 踩坑指南

### Q: 做 deck 时字体加载失败怎么办？
**A:** 确保 HTML 中引入了 Google Fonts CDN 链接，且 Playwright 截图验证时网络畅通。本地离线环境需预装字体。

### Q: Bold Templates 和 Swiss 版式能混用吗？
**A:** **不能。** 一份 deck 只能选择一套版式系统。类名同名但语义不同（例如 `h-hero` 在 Bold 是衬线，在 Swiss 是无衬线极细 200）。

### Q: 中文大标题字号怎么选？
**A:** Swiss 版式中，中文方块字视觉面积比英文更重，需按长度降级：
- 1行 ≤ 8个汉字：`min(6.4vw, 11.2vh)`
- 2行，每行 ≤ 8个汉字：`min(5.8vw, 10.2vh)`

### Q: 导出 PPTX 时样式丢失？
**A:** 从第一行就按 PPTX 约束写 HTML，不要先写"纯视觉自由版"再转换。PPTX 不支持 CSS Grid 高级特性，需用 flexbox 兼容方案。

### Q: ≥10 页的 deck 推荐什么架构？
**A:** **多文件架构** — 每页独立 HTML + `deck_index.html` 聚合。单文件架构 CSS 全局污染风险高，超过 10 页几乎必出样式冲突。

### Q: AI 生图的环境变量怎么配？
**A:** 复制 `references/wanderix-env.example` 或 `references/gpt-image-env.example` 为 `.env`，填入 API Key：
```bash
cp references/wanderix-env.example .env
# 编辑 .env 填入 GRSAPI_KEY=your-real-key
```

### Q: 为什么禁止跳过 showcase 流程？
**A:** ≥5 页的 deck 必须先做 2 页 showcase（封面 + 内容页）让用户确认 grammar，再批量推。跳过 = 方向全错 = 全部返工。这是实战踩坑总结的铁律。

### Q: 如何使用 PLOC 手账涂鸦功能？
**A:** 需要 VLM（视觉语言模型）支持。提供旅行/风景照片后，Wanderix Pipeline 会自动叠加 ins 风白色手绘线条 + 繁体大字标注，输出 3:4 比例的手账风格图片。

### Q: 验证 Swiss 版式合规性？
**A:** 运行自动化验证器：
```bash
node scripts/validate-swiss-deck.mjs index.html
```

---

## 📄 许可证

详见 [LICENSE.txt](LICENSE.txt)

---

> **一句话开始创作 →** 对 AI 说：*"帮我做一个关于 [主题] 的 [海报/PPT/原型/动画]"* ✨

---



---

## 🚀 加入AtomCollide-AI智能体实验室

**元素碰撞-AtomCollide-AI 智能体实验室** 是一个专注于AI领域的开源组织，汇聚了众多优秀学习者。

### 核心价值

**找工作：更省力，也更精准**
- 一线大厂内推通道（字节、阿里、腾讯等）
- 全链路求职赋能包（面试题库、简历优化、晋升指导）
- 线下技术沙龙 & 人脉网络

**学AI测试：真正落地，拒绝空谈**
- 从0到1实战落地体系（Skills、MCP、RAG、AI IDE等）
- 独家自研资料与工具矩阵
- 前沿技术同步与提效方案

### 知识库

- [踩坑合集](https://vcnvmnln7wit.feishu.cn/wiki/CjV9wG8IHiIpWikCdFEcxfErnne)
- [商业化案例库](https://vcnvmnln7wit.feishu.cn/wiki/LdIxwlrKGibFEVkWMocc2K9KnBh)
- [科普专栏](https://vcnvmnln7wit.feishu.cn/wiki/K1RPwM8zji9ZchkxlOmcivUgnJe)
- [Open Build](https://vcnvmnln7wit.feishu.cn/wiki/CThswol0PiNJJbkhgT1cZIxanLb)
- [LLM/Agent/研究报告知识库](https://vcnvmnln7wit.feishu.cn/wiki/KwGQwS2TciT2EdkSBBtcYnbsnSd)
- [Skill封装合集](https://vcnvmnln7wit.feishu.cn/wiki/PDfpwqJZUibTyBkUa7TcZZ6Onpd)
- [社区治理运营知识库](https://vcnvmnln7wit.feishu.cn/wiki/MSEGwrdnTiiF9Dk8qCVcNW6InJg)

### 加入社群

| 社群 | 链接 |
|------|------|
| AI探索交流1区 | [加入](https://applink.feishu.cn/client/chat/chatter/add_by_link?link_token=074vd565-6084-455c-ac52-9703e89a0697) |
| AI探索交流2区 | [加入](https://applink.feishu.cn/client/chat/chatter/add_by_link?link_token=60bj94f0-1a67-48a7-abbb-9172b161c2b0) |
| AI探索交流3区 | [加入](https://applink.feishu.cn/client/chat/chatter/add_by_link?link_token=13do1920-db46-4444-b635-005680beaf58) |
| AI探索交流4区 | [加入](https://applink.feishu.cn/client/chat/chatter/add_by_link?link_token=f17o1b86-06f6-4f10-911a-69a299a25fe3) |
| AI探索交流5区 | [加入](https://applink.feishu.cn/client/chat/chatter/add_by_link?link_token=2bbh6ab6-22c2-4753-b973-74bb1a2edcc9) |
| AI探索交流6区 | [加入](https://applink.feishu.cn/client/chat/chatter/add_by_link?link_token=d19r19f7-2f47-42ba-b1ec-cb0342cf2e80) |
| AI探索交流7区 | [加入](https://applink.feishu.cn/client/chat/chatter/add_by_link?link_token=fe9vdacc-7316-4b4d-ae4a-fdbcf56315e6) |
| AI探索交流8区 | [加入](https://applink.feishu.cn/client/chat/chatter/add_by_link?link_token=103kfae8-1fd7-424f-984f-d66c210e42d1) |
| AI探索交流9区 | [加入](https://applink.feishu.cn/client/chat/chatter/add_by_link?link_token=239p3cad-2f83-4baa-a230-f40386067548) |
| AI探索交流10区 | [加入](https://applink.feishu.cn/client/chat/chatter/add_by_link?link_token=880r7cf5-3638-45ff-afb9-7944de991872) |
| AI探索交流-网文作家 | [加入](https://applink.feishu.cn/client/chat/chatter/add_by_link?link_token=6a3v579b-ab43-4e1a-87f9-be63bab88da7) |
| AI探索交流群-音乐达人 | [加入](https://applink.feishu.cn/client/chat/chatter/add_by_link?link_token=76at299e-73da-4eeb-9eba-32161e98f2f8) |
| AI探索交流群-微笑驿站 | [加入](https://applink.feishu.cn/client/chat/chatter/add_by_link?link_token=f2av73d0-6bb4-4a9f-9095-5fbbe83e49ec) |

---

*AtomCollide-智械工坊团队出品*

