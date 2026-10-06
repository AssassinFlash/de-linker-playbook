---
wayfinder: research
status: open
assignee:
blocked_by: []
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
