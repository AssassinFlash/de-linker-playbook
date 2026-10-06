---
wayfinder: research
status: closed
assignee: chesterjohn+agent
blocked_by: []
resolved: 2026-10-06
---

# 通用 harness 编排机制调研

## Question

用户的质疑：Claude 的编排能跑是因为 slash command / subagent / skill 激活全是它的内置设施；「通用 harness 也行」目前只是假设。需要证据：在没有 slash command 的 harness 里，多阶段工作流实际怎么被驱动？

要回答：

1. **orchestrator skill 模式**（一个 skill 读仓库状态文件、告诉 agent「现在在哪、下一步干什么、产出放哪」）在各家 harness 里是否真可行？有没有真实开源仓库这么干（如 obra/superpowers 的引导 skill 模式、其他跨 harness skill 集）？
2. **子代理能力的可移植性**：Claude Code / Kimi / Codex / Cursor / Gemini / opencode 各自有没有 subagent/Task 等价物？能否被 skill 指令触发？哪些没有、缺了怎么办？
3. **prompt/命令复用约定**：`.claude/commands`、Codex prompts、Cursor commands……是否存在可移植的 prompt 文件约定，还是全是各家的？
4. **AGENTS.md 驱动的实际极限**：上下文预算（Codex 32KiB 等）、长指令遵循的现实表现。

产出：`wayfinder/research/generic-orchestration-2026-10.md`，带来源；末尾给「试点薄片该实测哪些点」的建议清单。

## Resolution

2026-10-06 研究子代理完成，产出 `wayfinder/research/generic-orchestration-2026-10.md`。要点：

1. **用户的质疑被证实**：多步工作流「自动触发」不是 SKILL.md 的属性。野外真实模式 = 会话启动注入 + skill 目录 + 能扛压缩的台账文件。Superpowers 的 bootstrap 是 per-harness 注入（Claude SessionStart hook、Kimi sessionStart.skill、Gemini @import、OpenCode context hook）；Codex v4.2 反而删掉了 AGENTS.md bootstrap、改押原生 skill 发现。**可移植的部分是台账/状态文件，不是自动启动**。本仓库不发插件，所以「AGENTS.md + .agents/skills 冷启动」是试点必须实测的假设。
2. **子代理能力**：Claude（Task）、Kimi（Agent）、Codex（默认开，文档说 AGENTS.md/skills 可请求委派）、Cursor、Gemini、OpenCode 都有；Aider 没有。正典写法 = "dispatch a subagent, else do it inline"，禁止 `context: fork`/`Agent`/`spawn_agent` 等具体工具名。
3. **命令约定**：无可移植 prompt 文件约定。Claude 已把 commands 并入 skills；Codex `~/.codex/prompts/` 已废弃且不入仓库；Cursor 也在往 skills 迁移。可移植的 prompt 载体 = SKILL.md；命令卡片只是人工粘贴的 fallback。
4. **AGENTS.md 极限**：Codex 对项目文档静默截断 32 KiB；常驻指令是上下文不是强制执行，越短越被遵守；只放指针、状态文件指针放顶部；压缩（compaction）就是台账必须存在的原因。

试点必测清单见调研文档 §7（冷 prompt「做这个仓库设置好的下一步」→ 是否读 AGENTS.md → 是否调用 orchestrator → 是否读台账 → 是否跑方法 skill → 是否写 deliverables/ → 是否更新台账）。
