# Deck 生产踩坑录（2026-06-18 实战总结）

## 背景

10 页中文知识科普 deck（AI 提示词工程），连续失败 4 版后才找到正确路径。以下是每版的失败原因和最终成功的方法。

---

## 失败版本复盘

### V1：子Agent从零生成（❌ 自己写CSS）
- **做法**：把任务描述扔给子Agent，让它从零写HTML/CSS
- **结果**：CSS渐变+圆角卡片，像网页不像幻灯片；无字体加载、无设计系统
- **根因**：没有使用 template.html 的 CSS 系统

### V2：给设计规范让子Agent写（❌ 子Agent没执行细节）
- **做法**：把 Signal 设计规范传给子Agent，让它"照着做"
- **结果**：子Agent没有真正加载规范细节，输出和V1差不多
- **根因**：子Agent上下文有限，无法执行复杂设计规范；应该自己写

### V3：用 canvas-design 完整模板（❌ 重型依赖在截图时崩溃）
- **做法**：用 template.html + WebGL + Motion One + CDN字体
- **结果**：WebGL在Playwright headless中渲染失败、ES Module导入失败、字体没加载
- **根因**：template.html 的 WebGL/motion 依赖在纯截图流程中不可靠；应该用简化版

### V4：自己写极简版（❌ 没用模板CSS系统）
- **做法**：扔掉模板，自己从零写CSS
- **结果**：浏览器零JS错误，但视觉质量差——用了系统默认字体、布局缺乏设计感
- **根因**：没有使用 template.html 的字体栈和 class 系统

---

## 正确路径（V5，最终成功版）

### 核心原则
1. **用 template.html 的 CSS 变量和 class 命名**（字体栈、间距、布局工具），但不依赖 WebGL/motion
2. **用 layouts.md 的成熟布局骨架**，不自己发明
3. **多文件架构**：每页独立 HTML + index.html iframe 聚合
4. **先做 2 页 showcase**，用户确认后再批量推
5. **逐页 Playwright 截图验证**

### 具体步骤

#### Step 1：规划主题节奏表
```
| 页 | 主题   | 布局           |
|----|--------|----------------|
| 1  | hero dark  | Layout 1 封面    |
| 2  | light  | Layout 9 对比    |
| 3  | dark   | Layout 2 章节幕封 |
| 4  | light  | Layout 9 对比    |
| 5  | dark   | Layout 3 数据网格 |
| 6  | light  | Layout 3 数据网格 |
| 7  | dark   | Layout 6 Pipeline |
| 8  | light  | Layout 3 数据网格 |
| 9  | dark   | Layout 6 Pipeline |
| 10 | light  | Layout 8 大引用   |
```

#### Step 2：做 2 页 showcase（封面 + 一种内容页）
- 用 template.html 的 CSS 变量（`--ink`, `--paper`, `--mono`, `--serif-zh` 等）
- 用 layouts.md 的 class（`h-hero`, `h-xl`, `kicker`, `chrome`, `foot`, `stat-card` 等）
- 每页是独立 HTML 文件，只引用 Google Fonts CDN + 自己的 `<style>`
- **不依赖** WebGL canvas、motion.min.js、lucide 等外部脚本

#### Step 3：Playwright 截图验证 showcase
```python
from playwright.sync_api import sync_playwright
import http.server, threading, os

os.chdir('/path/to/deck')
server = http.server.HTTPServer(('localhost', 8766), http.server.SimpleHTTPRequestHandler)
t = threading.Thread(target=server.serve_forever, daemon=True)
t.start()

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width': 1920, 'height': 1080})
    page.goto('http://localhost:8766/slides/01-cover.html', wait_until='networkidle')
    page.wait_for_timeout(2000)  # 等字体加载
    page.screenshot(path='showcase-01.png')
    browser.close()
    server.shutdown()
```

#### Step 4：用户确认后批量推剩余页
- 复用 showcase 建立的 grammar（字体、色板、间距、chrome/foot 结构）
- 每页保持独立 HTML 文件

#### Step 5：建聚合页 + 导出 PDF
- `index.html` 用 iframe 拼接所有 slides
- Playwright 逐页截图 + Pillow 合成 PDF

---

## 技术要点

### 字体加载
- Google Fonts CDN 在 Playwright headless 中**可以正常加载**，前提是通过 HTTP 服务（不能用 file:// 协议）
- 必须 `wait_until='networkidle'` + `wait_for_timeout(2000)` 等待字体下载完成
- 如果字体仍然不加载，检查 `<link>` 标签是否正确、网络是否可达

### CSS 系统选择
- **使用**：template.html 的 CSS 变量、class 命名（`h-hero`, `h-xl`, `kicker`, `chrome`, `foot`, `stat-card`, `pipeline`, `step` 等）
- **不使用**：WebGL canvas 背景、Motion One 动效引擎、lucide 图标（这些在截图流程中不可靠或不需要）
- **简化版**：只保留 CSS 变量 + 排版 class + 布局工具，去掉 JS 依赖

### 多文件 vs 单文件
- **多文件**（推荐 ≥5 页）：每页独立 HTML，iframe 聚合。CSS 天然隔离，可单页验证。
- **单文件**（≤4 页）：所有 slide 在一个 HTML 里，用 JS 切换。注意 CSS 特异性冲突。

### 导出 PDF
```python
from PIL import Image
imgs = [Image.open(f'thumbs/{slide.stem}.png').convert('RGB') for slide in slides]
imgs[0].save('deck.pdf', 'PDF', save_all=True, append_images=imgs[1:], resolution=150)
```

---

## 关键教训

1. **技能再好，不按流程走 = 废品**。canvas-design 有完整的 workflow/layouts/themes/checklist，跳过任何一步都会返工。
2. **子Agent 不适合做精细设计工作**。设计需要逐像素控制，子Agent 上下文有限且无法视觉验证。自己写。
3. **先 show 再批量**。2 页 showcase 的成本远低于 10 页全部返工。
4. **视觉验证是必须的**。没有 Playwright 截图 = 盲人摸象。Vision API 不可用时，把截图发给用户确认。
5. **简化 > 复杂**。WebGL + motion 看起来酷，但在生产流程中增加脆弱性。CSS-only 的视觉质量已经足够好。
