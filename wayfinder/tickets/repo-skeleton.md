---
wayfinder: task
status: open
assignee:
blocked_by: []
---

# 仓库骨架建立

## Question

在 `~/Documents/de-linker-playbook` 建立通用骨架（不依赖抽取规格的目录细节，先立、后随规格微调）：

- 目录：`skills/`（正典）、`schemas/`、`templates/`、`evals/`、`docs/`（`wayfinder/` 已存在）
- 发现适配器：`.agents/skills/<name>` → `../../skills/<name>` 软链层（研究票结论：这是跨 harness 自动发现的事实标准；Claude Code 的 `.claude/skills/` 需要时再生成）
- 根级 `AGENTS.md`（跨 harness 入口：仓库是什么、skills 在哪、怎么取用、例子定位规则、交接说明）
- `README.md`（人读版）、`CONTEXT.md`（词汇表，从地图 Notes 已定术语起步：正典/适配器、例子定位、指路不复制）
- `.gitignore`（OS 垃圾、`.venv/`、`downloads/`、`cookies*.txt`、密钥模式）
- 完成后补一次 git 提交

规格票定稿后如目录布局有出入，随规格调整即可，不阻塞本票先行。
