# 本仓库

跨 harness 的营销/获客 skill playbook。方法写在 skill 里；本文件只指路。

## 台账

营销、SEO、文案、内容、或「下一步」：先读 [`state/status.md`](state/status.md)，再读 [`skills/marketing-orchestrator/SKILL.md`](skills/marketing-orchestrator/SKILL.md) 并按其推进。产出写到 [`deliverables/`](deliverables/)。

获客线索（lead）类任务：读 [`skills/lead-generation/SKILL.md`](skills/lead-generation/SKILL.md) 并按其推进。

寒暄：可读台账并复述 `phase`，不要改文件。

## 交接说明

- 状态真源：[`state/status.md`](state/status.md) 与当前地图 [`wayfinder/closed-loop/map.md`](wayfinder/closed-loop/map.md)（补齐闭环，执行中；`wayfinder/map.md`、`wayfinder/feasibility/map.md` 已闭环）。压缩后以文件为准，不以对话记忆为准。
- 执行节奏：一票一新会话。
- 兼容：只承诺 Kimi / Z Code / DeepSeek / OpenCode / Hermes 五家，不为其他 harness 做适配层。
- 五家 headless 冷启动调用矩阵与坑：[`wayfinder/pilot/`](wayfinder/pilot/) 每家一份（如 Hermes 需 `HERMES_HOME` 隔离，Z Code 需桌面同步的 provider 配置）。

## Skill

- 正典：`skills/` 下与 frontmatter `name` 同名的目录里的 `SKILL.md`。
- 适配器：`.agents/skills/` 里对每个 skill 的软链。无扫描器时，按用户任务直接打开对应 `SKILL.md`。
- 用任务匹配 `description`，然后只走那份正文。不要另写一套流程。

`schemas/` = 交付物 JSON Schema；`templates/` = 产出 xlsx 模板与导出脚本；`evals/` = 校验/评测脚本；`docs/` = 人读说明与事实源入口。

## 事实源

产品与公司事实、对外说法、竞品：先读 [`docs/fact-sources.md`](docs/fact-sources.md)，按其「什么问题查哪个源」去三方（线上站点、新站仓库、竞品调研）取证，冲突按其「谁为准」。只读，不把内容拷进本仓库（指路不复制）。查不到标〔未证实〕，按没有处理。仓外路径只写在入口里，换机只改入口。

## 例子

skill 内例子是教学支架。标了「仅供理解，禁止引用到输出」的句子不得进入交付物。
