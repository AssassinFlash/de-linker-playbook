# 本仓库

跨 harness 的营销/获客 skill playbook。方法写在 skill 里；本文件只指路。

## 台账

营销、SEO、文案、内容、或「下一步」：先读营销台账 [`state/marketing-status.md`](state/marketing-status.md)，再读 [`skills/marketing-orchestrator/SKILL.md`](skills/marketing-orchestrator/SKILL.md) 并按其推进。产出写到 [`deliverables/`](deliverables/)。

「下一步」按反馈规则 [`docs/feedback-rules.md`](docs/feedback-rules.md) 挑动作：底表的反馈经 `uv run scripts/next_step.py` 读出并排好优先级，不手抄表格。

操作者说「我发了 / 上线了 / 更新了」、或新站上线了影响收录或可见内容的 PR：按 [`skills/marketing-execution-log/SKILL.md`](skills/marketing-execution-log/SKILL.md) 查证后写进底表执行登记（两条线共用）。

获客线索（lead）类任务：先读获客台账 [`state/lead-status.md`](state/lead-status.md)，再读 [`skills/lead-generation/SKILL.md`](skills/lead-generation/SKILL.md) 并按其推进。

获客教学与研究先读私有知识库 `deliverables/lead/00-system/knowledge/knowledge-base.json`；提问先用 `lead_kb.py brief` 检索 active 证据，新证据、修订、归档、问题、回答和操作者反馈写回该库。HTML 知识台只供审计，`learning-state.md` 只记学习阶段。

寒暄：可读台账并复述 `phase`，不要改文件。

## 交接说明

- 状态真源：两张台账（营销 [`state/marketing-status.md`](state/marketing-status.md)、获客 [`state/lead-status.md`](state/lead-status.md)，各管各的）与当前地图 [`wayfinder/closed-loop/map.md`](wayfinder/closed-loop/map.md)（补齐闭环，执行中；`wayfinder/map.md`、`wayfinder/feasibility/map.md` 已闭环）。压缩后以文件为准，不以对话记忆为准。
- 执行节奏：一票一新会话。
- 兼容：只承诺 Kimi / Z Code / DeepSeek / OpenCode / Hermes 五家，不为其他 harness 做适配层。
- 五家 headless 冷启动调用矩阵与坑：[`wayfinder/pilot/`](wayfinder/pilot/) 每家一份（如 Hermes 需 `HERMES_HOME` 隔离，Z Code 需桌面同步的 provider 配置）。

## Skill

- 正典：`skills/` 下与 frontmatter `name` 同名的目录里的 `SKILL.md`。
- 适配器：`.agents/skills/` 里对每个 skill 的软链。无扫描器时，按用户任务直接打开对应 `SKILL.md`。
- 用任务匹配 `description`，然后只走那份正文。不要另写一套流程。

`schemas/` = 交付物 JSON Schema；`templates/` = 产出 xlsx 模板与导出脚本；`evals/` = 校验/评测脚本；`scripts/` = 运行脚本（底表见 [`docs/base-table.md`](docs/base-table.md)，「下一步」见 [`docs/feedback-rules.md`](docs/feedback-rules.md)）；`docs/` = 人读说明与事实源入口。

## 事实源

产品与公司事实、对外说法、竞品：先读 [`docs/fact-sources.md`](docs/fact-sources.md)，按其「什么问题查哪个源」去三方（线上站点、新站仓库、竞品调研）取证，冲突按其「谁为准」。只读，不把内容拷进本仓库（指路不复制）。查不到标〔未证实〕，按没有处理。仓外路径只写在入口里，换机只改入口。

## 外部研究

任何需要搜索、外部信息验证、竞品研究、行业规则确认或资料获取的工作，**Apify 是强制主入口**。按 [`docs/apify.md`](docs/apify.md) 执行：先诊断并修复 Apify，不得因首次失败就改用普通搜索、降低研究深度或宣布“找不到”。

Apify 无法完成目标页时，先换关键词、页面、数据源、Actor、抓取方式和请求参数；仍受限时，可用 Scrapling、Scrapy、Crawl4AI、Firecrawl、Computer Use、网站自身 API、WordPress/WooCommerce API、sitemap、feed、页面源码和 structured data 配合取证。所有失败、修复和替代路径都要进搜索日志或阻塞日志。Token 只放仓外 mode-600 配置，绝不进仓库、交付物或对话输出。

公开社媒原帖和评论用 [`docs/social-research-opencli.md`](docs/social-research-opencli.md) 作为 Apify 之后的补充路径。先看完整供应链链路，只有直接采购角色进入主 ICP。

## 例子

skill 内例子是教学支架。标了「仅供理解，禁止引用到输出」的句子不得进入交付物。
