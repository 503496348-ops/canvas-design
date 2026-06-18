# Bold Template Pack — 快速选型指南

基于实战踩坑（2026-06-18）：从零生成deck CSS → 用户反馈"效果太差"；切换到Signal设计系统后通过。

## 核心教训

**从零写的CSS无论怎么描述风格，视觉上限都很低。** 原因：
- 缺乏成熟的色彩token系统（只是随手挑几个hex）
- 字体栈随意（system-ui + sans-serif）
- 没有签名处理（无kick、无ornament、无chrome bar）
- 没有禁忌约束（容易加渐变/圆角/阴影，落入AI slop）

**必须用模板设计系统。** 读 design.md → 提取全部token → 注入生成prompt。

---

## 12个模板速查

### Signal — 文学编辑（推荐：知识/科普/教育）
- **气质**：The Economist × 情报简报，克制、权威、贵族感
- **色彩**：海军蓝 #1C2644 + 暖纸白 #F0ECE3 + 古金 #C8A870（唯一accent）
- **字体**：Source Serif 4（标题）+ DM Sans（正文）+ IBM Plex Mono（标签/计数器）
- **签名**：gold italic `<em>` 混排、36px gold rule、em-dash gold bullet、80px网格纹理
- **禁忌**：禁止圆角、阴影、渐变、纯白文字
- **CJK**：全角色用 Noto Sans SC；gold italic 退化为 gold color-only
- **适合**：7-15页知识类/教育类/科普类deck

### Studio — 设计工作室（推荐：商务/数据/冲击力）
- **气质**：Pentagram/Anti 极简主义，类型即图形
- **色彩**：近黑 #1C1C1C + 酸黄 #F5D200（二元系统，无第三色）
- **字体**：Barlow 900 uppercase（所有标题）+ IBM Plex Mono（元数据）
- **签名**：12vw超大字、三栏mono footer lockup、2px stat-card top rule
- **禁忌**：禁止第三色、圆角、阴影、小写标题、weight<900的display
- **CJK**：Noto Serif SC 700 替代 Barlow；uppercase身份消失
- **适合**：短deck（5-8页）、数据驱动、需要冲击力的场景

### Emerald Editorial — 时尚杂志（推荐：品牌/创意/戏剧感）
- **气质**：Harper's Bazaar × 19世纪戏剧海报
- **色彩**：翡翠绿 #3CD896 + 深海蓝 #0F1A5C + 燕麦纸 #F1E9D6
- **字体**：Bodoni Moda 900（标题）+ Manrope（正文/标签）
- **签名**：双线ornament（4px stacked rules bracketing words）、0圆角、4px ink rules
- **禁忌**：禁止阴影渐变、第三色、圆角、Bodoni weight<700
- **CJK**：LXGW WenKai（标题）+ Noto Serif SC（正文）+ Noto Sans SC（标签）
- **适合**：品牌展示、创意提案、需要戏剧感的deck

### Blue Professional — 蓝色商务
- **气质**：企业级、专业、保守
- **适合**：正式汇报、投资人deck、企业内部

### Soft Editorial — 柔和编辑
- **气质**：温暖、亲切、轻量编辑
- **适合**：社区分享、内部培训、非正式知识传播

### Playful / Coral / Daisy Days — 活泼系
- **气质**：年轻、社交、轻快
- **适合**：社交媒体分享、产品发布、年轻受众

### 8-bit Orbit / Creative Mode — 暗色科技
- **气质**：未来感、数字美学、霓虹
- **适合**：技术分享、黑客松、极客社区

### Monochrome / Broadside — 极简声明
- **气质**：黑白二色、字重即设计
- **适合**：声明式内容、极简主义、文字密集型

### Cartesian / Cobalt Grid — 网格工程
- **气质**：精确、工程感、蓝灰调
- **适合**：技术文档、架构说明、工程汇报

### Retro Zine / Retro Windows — 复古
- **气质**：90年代/千禧年复古
- **适合**：需要怀旧感的特殊场景

### Biennale Yellow / Block Frame / Long Table / Mat / Vellum / Pin and Paper / Sakura Chroma / Scatterbrain / Stencil Tablet / Capsule / Neo Grid Bold / Bold Poster / Grove / Editorial Forest / Editorial Tri-Tone / Pink Script / Peoples Platform / Creative Mode
- 详见各目录下的 design.md

---

## 选型决策树

```
内容是什么类型？
├── 知识/科普/教育 → Signal
├── 商务/数据/汇报 → Studio 或 Blue Professional
├── 品牌/创意/展示 → Emerald Editorial
├── 技术/工程/架构 → Cartesian 或 Cobalt Grid
├── 年轻/社交/活泼 → Playful / Coral / Daisy Days
├── 科技/未来/极客 → 8-bit Orbit / Creative Mode
└── 不确定 → Signal（最安全的默认选择）
```

## 使用流程

1. 根据上表选模板
2. `skill_view(name='canvas-design', file_path='assets/bold-template-pack/templates/<name>/design.md')`
3. 提取：colors token、typography token、spacing token、components、Do's/Don'ts、CJK rules
4. 把这些token作为硬约束注入deck生成prompt
5. 生成HTML → export-pdf.sh → 验证 → 发送
