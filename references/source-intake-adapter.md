# Source Intake Adapter：多源资料摄取入口

一念成画不做资料抓取平台，但必须能把用户给的资料变成可设计的 brief。Source Intake Adapter 是设计流程前置步骤：先把长材料压成结构，再进入海报/Deck/视频/图片卡模式。

## 输入类型

| 输入 | 处理方式 |
|---|---|
| Markdown / TXT | 直接读取，保留标题层级 |
| PDF / DOCX / PPTX / XLSX | 优先用对应文档技能或解析脚本提取为 Markdown |
| 网页 URL | 抽取正文、标题、链接、发布时间（能查则查） |
| B站 / YouTube / 播客 | 先取转写/字幕，再摘要为结构化 brief |
| 公众号文章 | 能抓正文则抓，不能抓时要求用户提供链接或正文截图 |
| 多文件 ZIP | 解压后按类型分别摄取，最后合并 brief |

## 输出文件

默认生成 `source-brief.md`：

```md
# Source Brief

## 来源
- source: ...
- fetched_at: ...
- confidence: high/medium/low

## 一句话主题
...

## 核心观点
1. ...
2. ...
3. ...

## 可视化线索
- 可画成图的结构：...
- 可做成数据页的事实：...
- 可做成封面的隐喻：...

## 推荐输出形态
- HTML Deck / Editable PPTX / Image Deck / Poster / Motion

## 待确认问题
- ...
```

## 路由建议

- 信息完整、逻辑强 → HTML Deck / Editable PPTX
- 金句多、适合传播 → Image Deck
- 产品发布/营销 → Poster + Motion
- 教学内容 → Deck + 讲者备注 + 练习页

## 风险控制

- 资料来源不清时必须标 `confidence: low`。
- 搜不到字幕/正文时不能编，必须让用户补材料。
- 对事实性数字、时间、人物、产品名，进入设计前必须二次核验。
- Source Brief 是中间产物，不是最终设计；不能拿摘要冒充成品。
