# 🔍 Hermes Agent 生态竞争分析报告

> 生成日期: 2026-06-19 | 基于 GitHub 趋势数据 + 生态定位分析
> 分析范围: 7 大竞争赛道, 18 个核心竞品, 18 个我们的仓库

---

## 一、分赛道竞品对比

### 1. AI 生图 / 视觉创作引擎

| 维度 | 竞品 (SD WebUI / ComfyUI / Flux) | 我们 (canvas-design / Wanderix / hermes-skill-gpt-image-gen) | 差距 | 行动建议 |
|------|----------------------------------|-------------------------------------------------------------|------|----------|
| **Stars** | 163K / 117K / 25K | <1K (起步期) | 巨大 | 不追Star，追场景差异化 |
| **技术栈** | 本地部署 Stable Diffusion, 开源模型, 节点式工作流 | GPT Image 2 API 调用, 飞书集成, Agent原生 | 架构差异 | API模式是优势——零GPU门槛,强化"一句话出图"体验 |
| **用户门槛** | 需GPU, 需学习节点编排, 需配置模型 | 对话式交互, Agent编排, 飞书直达 | 我们更低 | ✅ 已有优势,持续降低 |
| **能力范围** | 图片生成/编辑/ControlNet/IPAdapter/LoRA | 海报/PPT/原型/动画(canvas-design) + 图片生成(Wanderix) | 竞品更深 | 在Agent层面做编排,组合多个API |
| **生态** | 海量插件/模型/社区 | 326 skills + Agent原生调度 | 社区小,集成强 | 利用Agent生态做"创意工作流自动化" |
| **商业化** | 开源免费+云服务 | Skill付费+Agent订阅 | 模式差异 | 明确定位: 企业级Agent创意自动化 |

**关键洞察**: 我们不应正面对标SD/ComfyUI的开源模型赛道，而应定位为**"Agent-Native创意引擎"**——用户不需要懂模型、不需要GPU，通过自然语言驱动canvas-design + GPT Image 2完成创意任务。核心差异化是**飞书/企业IM直达 + Agent编排 + 零部署**。

---

### 2. 安全检测

| 维度 | 竞品 (SkillSpector/AI-Infra-Guard/agentic_security) | 我们 (genesisix / genesisix-hermes) | 差距 | 行动建议 |
|------|-----------------------------------------------------|-----------------------------------|------|----------|
| **Stars** | 7.4K / 3.9K / 1.9K | <500 | 中等 | 开源genesisix核心,争取社区关注 |
| **背景** | NVIDIA / Tencent / 社区 | 独立团队 | 背书弱 | 争取企业合作/论文发表 |
| **定位** | 通用AI安全/模型安全/Agent安全 | Agent安全检测框架 | 高度重合 | ✅ 赛道正确,需加速 |
| **差异化** | 偏模型层/基础设施层 | 偏Agent行为层/技能层 | 我们更垂直 | 深耕"Skill安全审计"细分领域 |
| **集成** | 独立工具,需额外接入 | 原生Hermes Agent集成 | 我们更强 | 强调"Agent自免疫"概念 |
| **覆盖** | 提示注入/数据泄露/越权 | 技能审计/权限检测 | 互补 | 合并能力,覆盖全链路 |

**关键洞察**: Agent安全是2026年爆发赛道。genesisix + genesisix-hermes + hermes-doctor组合可形成"**Agent安全三件套**": 检测(genesisix) + 诊断(hermes-doctor) + 防护(genesisix-hermes)。建议开源核心检测引擎，打"NVIDIA SkillSpector之后的Agent安全第二极"定位。

---

### 3. 智能体运维 / Agent平台

| 维度 | 竞品 (Dify / LangChain / MetaGPT) | 我们 (hermes-agent / dag-workflow-engine / feishu-multi-agent-relay) | 差距 | 行动建议 |
|------|----------------------------------|--------------------------------------------------------------------|------|----------|
| **Stars** | 145K / 139K / 68K | ~1K (fork起步) | 极大 | 不追通用平台,深耕垂直场景 |
| **定位** | 通用Agent框架/LLM编排/多Agent模拟 | 个人AI Agent + DAG工作流 + 多Agent协作 | 差异化明显 | ✅ 坚持"个人AI助手"定位 |
| **用户群** | 开发者/企业 | 终端用户(飞书/Telegram) | 不同 | 不需要抢开发者,做好终端体验 |
| **技术深度** | 成熟框架,丰富API/SDK | 326 skills + Agent原生调度 | 我们场景更广 | 持续扩展skill生态 |
| **运维能力** | 可视化部署/监控/日志 | hermes-doctor自诊断 + DAG工作流 | 竞品更成熟 | 强化hermes-doctor为Agent可观测性核心 |
| **多Agent** | MetaGPT模拟团队/对话式 | feishu-multi-agent-relay跨Agent协作 | 我们更实用 | ✅ 已有差异化,强化relay能力 |

**关键洞察**: 我们不是Dify/LangChain的竞品——我们是**它们的上层用户**。Hermes Agent定位为"个人AI操作系统"，使用这些框架的能力但不与之竞争。差异化在于: 326个垂直skills + 飞书/Telegram原生 + 多Agent relay + Agent自诊断。

---

### 4. 白板 / 画布生成

| 维度 | 竞品 (Excalidraw / tldraw) | 我们 (nichecraft / canvas-design) | 差距 | 行动建议 |
|------|--------------------------|----------------------------------|------|----------|
| **Stars** | 125K / 47K | <200 | 巨大 | 不追,做Agent集成层 |
| **产品形态** | 独立Web应用,开源绘图工具 | 飞书白板集成,Agent驱动生成 | 形态不同 | ✅ 差异化正确 |
| **技术** | Canvas渲染,协作编辑,端到端加密 | AI生成白板内容,飞书API集成 | 互补 | 考虑接入Excalidraw作为渲染层 |
| **用户** | 设计师/开发者/PM | 飞书企业用户 | 更垂直 | 深耕飞书生态,做"AI白板助手" |
| **AI能力** | 逐步集成AI辅助 | 原生AI驱动 | 我们更强 | 强化"描述即白板"能力 |

**关键洞察**: nichecraft定位为**"飞书版AI白板助手"**，不与Excalidraw/tldraw竞争底层能力。建议接入它们作为渲染引擎，我们专注AI理解+内容生成+飞书集成。

---

### 5. 视频创作

| 维度 | 竞品 (diffusers / Wan2.1 / KrillinAI) | 我们 (hermes-skill-ideasphere / hermes-skill-aestheflow / hermes-skill-minimax-creative) | 差距 | 行动建议 |
|------|---------------------------------------|------------------------------------------------------------------------------------------|------|----------|
| **Stars** | 33K / 16K / 10K | <200 | 大 | 组合Agent能力做差异化 |
| **定位** | 视频生成模型/工具链 | 自媒体视频剪辑 + 抖音分析 + MiniMax多媒体 | 更垂直 | ✅ 场景导向正确 |
| **技术** | 扩散模型训练/推理 | API调用(MiniMax) + 平台分析(抖音) | 架构差异 | Agent编排多模态API是优势 |
| **用户** | AI研究者/视频创作者 | 自媒体运营者/抖音创作者 | 更精准 | 深耕"AI短视频工作流" |
| **完整度** | 单一能力(生成) | 分析→创意→生成→剪辑 全链路 | 我们更全 | 强化全链路Agent自动化 |

**关键洞察**: 三个skills组合形成**"AI短视频全链路"**: aestheflow(分析) → ideasphere(创意/剪辑) → minimax-creative(生成)。这是竞品不具备的Agent编排优势。建议发布"短视频Agent工作流"作为整体方案。

---

### 6. 金融量化

| 维度 | 竞品 (QuantDinger / AutoHedge) | 我们 (Stratapro) | 差距 | 行动建议 |
|------|------------------------------|------------------|------|----------|
| **Stars** | 8K / 3.4K | <100 | 大 | 垂直深耕A股场景 |
| **定位** | 通用量化平台 | A股选股决策 | 更垂直 | ✅ 差异化正确 |
| **技术** | 回测引擎/因子库/风控 | LLM驱动选股+分析 | 架构差异 | 补充回测能力 |
| **合规** | 开源通用 | A股特化(证监会规则/涨跌停) | 我们更合规 | 强化A股合规能力 |
| **用户** | 量化开发者 | A股散户/个人投资者 | 更广 | 降低使用门槛 |

**关键洞察**: Stratapro定位**"AI选股助手"**而非量化平台，面向个人投资者。建议补充: (1) 历史回测模块 (2) 风险提示系统 (3) 与飞书定时推送集成。

---

### 7. 长文创作

| 维度 | 竞品 (gpt_academic / gpt-researcher) | 我们 (fission-creative) | 差距 | 行动建议 |
|------|-------------------------------------|------------------------|------|----------|
| **Stars** | 70K / 27K | <100 | 巨大 | 做差异化场景 |
| **定位** | 学术论文辅助/深度研究 | 长篇网文创作 | 场景不同 | ✅ 避开学术红海,做网文蓝海 |
| **技术** | 论文润色/翻译/总结/联网搜索 | 网文大纲/章节生成/风格控制 | 互补 | 可借鉴联网搜索能力 |
| **用户** | 学术研究者 | 网文作者/内容创作者 | 不同 | 深耕网文场景,做"AI网文助手" |
| **商业模式** | 开源+API付费 | Skill付费 | 类似 | 差异化定价 |

**关键洞察**: fission-creative避开学术赛道(被gpt_academic垄断)，选择**网文创作蓝海**。建议: (1) 增加多平台发布(起点/番茄/七猫) (2) 增加读者反馈分析 (3) 与ideasphere联动做"文字→短视频"。

---

## 二、优先级排序 & 机会矩阵

### 🔴 P0 — 立即行动 (1-2周)

| # | 机会 | 涉及仓库 | 预期影响 | 行动 |
|---|------|----------|----------|------|
| 1 | **Agent安全三件套开源** | genesisix + genesisix-hermes + hermes-doctor | 抢占Agent安全品牌高地 | 整理核心检测引擎,发布开源README,提交HN/Reddit |
| 2 | **短视频Agent工作流发布** | ideasphere + aestheflow + minimax-creative | 首个"AI短视频全链路Agent" | 组合为统一workflow,发布使用案例 |
| 3 | **canvas-design Agent化** | canvas-design + nichecraft | 一句话生成海报/PPT/白板 | 强化自然语言→视觉内容的Agent调用链 |

### 🟡 P1 — 近期推进 (2-4周)

| # | 机会 | 涉及仓库 | 预期影响 | 行动 |
|---|------|----------|----------|------|
| 4 | **Stratapro回测能力** | Stratapro | 从选股工具升级为量化助手 | 增加历史回测+风险系统 |
| 5 | **fission-creative多平台** | fission-creative | 网文创作→多平台发布 | 接入起点/番茄API |
| 6 | **hermes-doctor可观测性** | hermes-doctor | Agent自诊断→企业级可观测性 | 增加监控dashboard+告警 |
| 7 | **dag-workflow-engine可视化** | dag-workflow-engine | DAG工作流可视化编辑 | 接入Web DAG编辑器 |

### 🟢 P2 — 中期布局 (1-3月)

| # | 机会 | 涉及仓库 | 预期影响 | 行动 |
|---|------|----------|----------|------|
| 8 | **feishu-multi-agent-relay标准化** | feishu-multi-agent-relay | 多Agent协作标准协议 | 制定relay协议规范,争取其他Bot接入 |
| 9 | **数字分身商业化** | awake-differently | 个人IP数字化 | 增加社交媒体自动运营 |
| 10 | **Wanderix LoRA微调** | Wanderix | 定制化图片生成 | 支持用户自训练风格模型 |
| 11 | **开源Hermes skill市场** | hermes-agent | 326 skills生态开放 | 建立skill发布/安装/评分机制 |

---

## 三、融合升级计划

### 🏗️ Phase 1: 核心能力整合 (立即启动)

```
┌─────────────────────────────────────────────────┐
│              Hermes Agent 主仓                    │
│  ┌──────────┐ ┌──────────┐ ┌──────────────────┐  │
│  │ Agent安全 │ │ 创意引擎 │ │  智能体运维       │  │
│  │ 三件套    │ │ 三合一   │ │  诊断+工作流      │  │
│  │genesisix │ │canvas-   │ │hermes-doctor     │  │
│  │genesisix │ │design    │ │dag-workflow-     │  │
│  │-hermes   │ │Wanderix  │ │engine            │  │
│  │hermes-   │ │gpt-image │ │feishu-relay      │  │
│  │doctor    │ │-gen      │ │                  │  │
│  └──────────┘ └──────────┘ └──────────────────┘  │
└─────────────────────────────────────────────────┘
```

**具体动作:**

1. **合并图片生成**: `Wanderix` + `hermes-skill-gpt-image-gen` → 统一 `hermes-skill-image-gen`，支持GPT Image 2 + 未来模型扩展
2. **统一安全套件**: `genesisix`(核心引擎) + `genesisix-hermes`(Agent集成) + `hermes-doctor`(诊断) → `hermes-security-suite`
3. **创意引擎升级**: `canvas-design` 作为主引擎，`nichecraft` 降级为飞书白板skill，`minimax-creative` 作为多媒体生成后端

### 🚀 Phase 2: 场景工作流 (2-4周)

| 工作流名称 | 组合仓库 | 目标场景 | 竞争对手 |
|-----------|---------|---------|---------|
| **AI短视频工作流** | aestheflow + ideasphere + minimax-creative | 抖音/小红书短视频全链路 | KrillinAI(10K⭐) |
| **AI网文工厂** | fission-creative + ideasphere | 长篇网文创作+改编短视频 | gpt_academic(70K⭐)但场景不同 |
| **AI选股助手** | Stratapro + dag-workflow-engine | A股选股→回测→推送 | QuantDinger(8K⭐) |
| **AI白板助手** | nichecraft + canvas-design | 飞书会议白板自动生成 | Excalidraw(125K⭐)但Agent原生 |
| **Agent免疫系统** | genesisix + hermes-doctor | Agent自检→自诊→自愈 | SkillSpector(7.4K⭐) |

### 📈 Phase 3: 生态开放 (1-3月)

1. **Skill市场**: 建立 `hermes-skill-registry`，开放326 skills的发布/安装/评分
2. **安全框架开源**: genesisix 核心引擎独立开源，建立社区
3. **多Agent Relay标准**: 制定跨Bot协作协议，邀请第三方Bot接入
4. **数字分身平台**: awake-differently 升级为"个人IP数字化平台"

---

## 四、竞争定位总结

```
          开发者工具 ←──────────────────→ 终端用户
               │                            │
   Dify(145K)  │   LangChain(139K)          │
   ComfyUI     │   SD WebUI(163K)           │
   Excalidraw  │                            │
               │         ┌──────────┐       │
               │         │ Hermes   │       │
               │         │ Agent    │       │
               │         │ (我们)   │       │
               │         └──────────┘       │
               │                            │
               │    gpt_academic(70K)        │
               │    QuantDinger(8K)          │
               │                            │
          学术/专业 ←──────────────────→ 大众/自媒体
```

**我们的独特定位**: **面向终端用户的Agent-Native AI操作系统**
- 竞品大多是**开发者工具**(需要编程/部署/配置)
- 我们是**对话式Agent**(一句话完成任务)
- 核心壁垒: 326 skills + 飞书/Telegram原生 + 多Agent协作 + Agent自愈

---

## 五、风险 & 缓解

| 风险 | 严重性 | 缓解措施 |
|------|--------|----------|
| 竞品Agent化(Excalidraw/Dify集成AI) | 🔴 高 | 加速场景化,做深垂直 |
| GPT Image 2 API变动/涨价 | 🟡 中 | 多模型后端(支持Flux/SD) |
| Agent安全赛道被大厂抢占 | 🔴 高 | P0开源,先发优势 |
| Skills生态碎片化 | 🟡 中 | 统一skill规范+市场 |
| 个人AI助手赛道拥挤 | 🟡 中 | 强化飞书/企业IM差异化 |

---

## 六、关键指标追踪

| 指标 | 当前 | 1月目标 | 3月目标 |
|------|------|---------|---------|
| GitHub Stars(总计) | ~500 | 2,000 | 10,000 |
| Skills数量 | 326 | 400 | 600 |
| 活跃Agent用户 | - | 100 | 1,000 |
| 安全框架Stars | <100 | 500 | 3,000 |
| 短视频工作流使用 | 0 | 50 | 500 |

---

> **一句话总结**: 我们不应在Stars数量上追赶163K的SD WebUI或145K的Dify，而应深耕**"Agent-Native + 企业IM原生 + 326 skills垂直场景"**的独特定位，在Agent安全、短视频全链路、AI网文、A股选股四个细分赛道建立不可替代的优势。
