# 一念成画 · 快速上手指南

## 这是什么

一句话告诉 AI：**"帮我做一张海报 / 一个PPT / 一个原型 / 一段动画"**，就能得到设计级的视觉产出。

| 你说 | AI 做什么 | 产出格式 |
|------|----------|---------|
| "帮我做一张海报" | 设计级单页视觉 | .png / .pdf |
| "帮我做个PPT/deck" | HTML幻灯片 | .html → .pdf / .pptx |
| "我要客户能改的PPT" | 原生可编辑PPTX | .pptx（文字/图形可编辑） |
| "我要线下分享，带讲稿" | 演讲者模式 | HTML + 当前页/下一页/逐字稿/计时器 |
| "做成小红书图文/知识卡片" | 图片型社交Deck | .png/.jpg 组图 → PDF/PPTX |
| "把这个链接/文章做成PPT" | 资料摄取→结构化brief→设计 | source-brief.md → deck |
| "帮我做个App原型" | 可交互界面mockup | .html |
| "帮我做段动画" | Motion动画 | .mp4 / .gif |

---

## 做 Deck（最常用）

### 一句话开始

```
帮我做一个关于 [主题] 的幻灯片，大概 [N] 页
```

### AI 的工作流程

1. **问你 5-10 个问题**（受众、风格、要不要PDF/PPTX）
2. **做 2 页示例**发给你确认方向（封面 + 一个内容页）
3. **你确认后**批量推剩下 N-2 页
4. **逐页截图验证**确保字体加载、布局正确
5. **导出 PDF/PPTX/HTML** 发给你

### 四条新路线

| 你要的是 | 走哪条路线 | 注意 |
|---|---|---|
| 最好看，能网页展示 | HTML Deck Mode | 视觉自由度最高 |
| 客户能在 PowerPoint 里改字改图 | Editable PPTX Mode | 从一开始遵守 PPTX 约束 |
| 现场演讲不忘词不超时 | Presenter Mode | 每页写 notes，按 S 开讲者窗口 |
| 手机传播/社交图文 | Image Deck Mode | 一页一图，少字高密度 |
| 长文/视频/网页转PPT | Source Intake | 先产出 source-brief.md |

### 你能控制什么

| 你说 | 效果 |
|------|------|
| "用深色风格" | 暗底 + 亮字 |
| "用浅色/白底" | 纸白底 + 深字 |
| "要瑞士风/极简" | 22种瑞士版式系统 |
| "要杂志风" | 编辑排版 + chrome/foot 栏 |
| "字要大一点" | 标题放大，留白更多 |
| "这页内容太多" | 拆成两页 |
| "我要可编辑PPTX" | AI 从第一行就按PPTX约束写 |
| "只要PDF" | 视觉完全自由 |

### 导出命令

```bash
# 单文件 deck → PDF
bash scripts/export-pdf.sh ./my-deck.html ./output.pdf

# 多文件 deck → PDF
node scripts/export_deck_pdf.mjs --slides ./slides/ --out deck.pdf

# deck → 可编辑 PPTX
node scripts/export_deck_pptx.mjs --slides ./slides/ --out deck.pptx
```

---

## 做海报 / 品牌物料

```
帮我做一张 [活动/产品] 的海报
```

- 海报有**防裁切铁律**：重要内容不能贴边
- 中文场景有**文化色彩禁忌**（黑色用 #3D3630 代替纯黑）
- 出现品牌名 → AI 自动搜索官方 logo（品牌资产协议 5 步流程）

---

## 做原型

```
帮我做一个 [iOS/Android/Web] App 的原型，[N] 个页面
```

默认平铺 4-6 台设备，可点击跳转。支持 Playwright 自动化测试。

---

## 做动画 / 视频

```
帮我做一段 [描述] 的动画，大概 [N] 秒
```

支持 SFX 音效 + BGM 背景音乐 + TTS 解说配音。

```bash
node scripts/render-video.js --input scene.html --out animation.mp4
bash scripts/add-music.sh animation.mp4 bgm.mp3 output.mp4
```

---

## 可用模板（30 套）

AI 会根据内容类型自动推荐，你也可以指定：

| 你的内容 | 推荐模板 | 风格 |
|----------|---------|------|
| 知识科普/教育/长文 | **Signal** | 编辑克制，海军蓝+暖纸白+古金 |
| 商务汇报/数据 | **Studio** | 极简二元，近黑+酸黄，大字冲击 |
| 杂志/时尚/品牌 | **Emerald Editorial** | 翡翠绿+深海蓝，Bodoni戏剧感 |
| 技术/产品/极客 | **Cobalt Grid** / **Cartesian** | 蓝灰网格，工程感 |
| 活泼/年轻/社交 | **Playful** / **Coral** | 暖色轻快 |
| 暗色/科技/未来 | **8-bit Orbit** / **Creative Mode** | 深底+霓虹 |
| 极简/纯文字 | **Monochrome** / **Broadside** | 黑白二色 |

所有模板在 `assets/bold-template-pack/templates/` 下，每个有 `design.md`（完整规范）和 `preview.md`（预览）。

---

## 常见问题

**Q: 做出来有乱码？**
A: 字体没加载。中文用系统字体栈（Noto Sans SC / PingFang SC）不依赖CDN。

**Q: PDF导出报 "No .slide elements found"？**
A: HTML容器类名必须是 `.slide`。

**Q: 做的PPT太丑？**
A: 告诉 AI "用 Signal 模板"或"用 Studio 模板"，不要让它从零写CSS。

**Q: 把现有PPT转成好看的HTML？**
A: 说"把这个PPT重新设计成HTML deck"，AI 会提取内容再重设计。

**Q: 用我品牌的设计系统？**
A: 提供品牌指南/色彩/字体规范，AI 按品牌资产协议执行。

**Q: 动画加配音？**
A: AI 自动生成解说稿 → TTS → 合成。也可提供自己的音频。
