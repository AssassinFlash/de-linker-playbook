---
wayfinder: task
status: closed
assignee: chesterjohn+agent
blocked_by: [pilot-slice]
resolved: 2026-10-06
---

# 仓库骨架建立

## Question

在 `~/Documents/de-linker-playbook` 建立通用骨架（不依赖抽取规格的目录细节，先立、后随规格微调）：

- 目录：`skills/`（正典）、`schemas/`、`templates/`、`evals/`、`docs/`（`wayfinder/` 已存在）
- 发现适配器：`.agents/skills/<name>` → `../../skills/<name>` 软链层。**兼容目标五家 = Kimi / Z Code / DeepSeek / OpenCode / Hermes**（用户定）：无原生 skill 扫描器的（如 DeepSeek）走 AGENTS.md 指路 + 各家人工/配置入口；不为 Claude/Codex 等非目标 harness 做适配
- 根级 `AGENTS.md`（跨 harness 入口：仓库是什么、skills 在哪、怎么取用、例子定位规则、交接说明、**与 `~/Documents/New` 的互相指路**——本仓库指过去；如用户同意，在 New 侧加一行回指）
- `README.md`（人读版）、`CONTEXT.md`（词汇表，从地图 Notes 已定术语起步：正典/适配器、例子定位、指路不复制）
- `.gitignore`（OS 垃圾、`.venv/`、`downloads/`、`cookies*.txt`、密钥模式）
- 完成后补一次 git 提交

规格票定稿后如目录布局有出入，随规格调整即可，不阻塞本票先行。

**顺序调整（2026-10-06）**：试点薄片会先建最小骨架；本票在薄片实测验证后补全正式骨架（全量目录、AGENTS.md 终稿、CONTEXT.md 词汇表）。

## Resolution

2026-10-06 完成，四线子代理并行、主模型 review 后关票。

- **目录**：`schemas/`、`templates/`、`evals/`、`docs/` 已建（各带 `.gitkeep`，标注为预留、随抽取规格填充）；`skills/`、`wayfinder/`、`state/`、`deliverables/` 已有。
- **发现适配器**：`.agents/skills/` 软链层已有 2 条（试点 2 skill），`readlink` + `ls -L` 验证可 resolve；后续 skill 抽取时按同一模式（`../../skills/<name>`）补链。
- **`AGENTS.md` 终稿**（33 行）：台账指针置顶；新增交接说明（状态真源 = 台账+地图、一票一新会话、兼容仅五家）；预留目录一句；New 指路保留 `~` 形式。
- **`README.md`**（新建，30 行）：人读版——仓库是什么、目录一图、当前状态、怎么用。
- **`CONTEXT.md`**（新建）：词汇表 11 词条——正典/适配器/例子定位/指路不复制/台账/交付物/去不锈钢化/兼容目标五家/无上位法/相对路径/当轮清账，均按地图 Notes 口径定义。
- **`.gitignore`**：审计无缺口（OS 垃圾、`.venv/`、`downloads/`、`cookies*.txt`、密钥模式全覆盖），未改。
- **New 侧回指**：已在 `~/Documents/New/CONTEXT.md` 末尾加一行回指（用户授权做完为止）。
- 提交只含本票产出；`extraction-spec.md` 有他窗口在改，未纳入。
