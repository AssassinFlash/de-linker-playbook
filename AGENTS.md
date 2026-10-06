# 本仓库

跨 harness 的营销/获客 skill playbook。方法写在 skill 里；本文件只指路。

## 台账

营销、SEO、文案、内容、或「下一步」：先读 [`state/status.md`](state/status.md)，再读 [`skills/marketing-orchestrator/SKILL.md`](skills/marketing-orchestrator/SKILL.md) 并按其推进。产出写到 [`deliverables/`](deliverables/)。

寒暄：可读台账并复述 `phase`，不要改文件。

## 交接说明

- 状态真源：[`state/status.md`](state/status.md) 与 [`wayfinder/map.md`](wayfinder/map.md)。压缩后以文件为准，不以对话记忆为准。
- 执行节奏：一票一新会话。
- 兼容：只承诺 Kimi / Z Code / DeepSeek / OpenCode / Hermes 五家，不为其他 harness 做适配层。

## Skill

- 正典：`skills/` 下与 frontmatter `name` 同名的目录里的 `SKILL.md`。
- 适配器：`.agents/skills/` 里对每个 skill 的软链。无扫描器时，按用户任务直接打开对应 `SKILL.md`。
- 用任务匹配 `description`，然后只走那份正文。不要另写一套流程。

试点：`marketing-orchestrator`（导航）、`marketing-copywriting`（phase 1 方法）。

`schemas/`、`templates/`、`evals/`、`docs/` 是预留目录，随抽取规格填充。

## 产品上下文

事实在 `~/Documents/New`（先读 `CONTEXT.md`，需要参数再读 `fact-base/`）。只读，不把内容拷进本仓库（指路不复制）。读文件时把 `~` 展开为用户主目录，不要把 `~` 当相对路径。交接他机需更新此路径。

## 例子

skill 内例子是教学支架。标了「仅供理解，禁止引用到输出」的句子不得进入交付物。
