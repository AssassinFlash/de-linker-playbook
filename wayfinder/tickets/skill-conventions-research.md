---
wayfinder: research
status: open
assignee:
blocked_by: []
---

# 跨 harness skill 约定与最新编写最佳实践调研

## Question

两个事实问题，答案直接喂养「抽取规格定稿」与最终验收标准：

1. **Anthropic Agent Skills 官方最新编写最佳实践**：SKILL.md frontmatter 官方字段集、`description` 写法、渐进式披露（progressive disclosure）、正文长度指引、examples/references 组织方式、官方点名的反模式。来源优先级：官方文档站、官方工程博客、agentskills 规范站。
2. **2026 年各 agent harness 的项目级 skill / 指令发现机制现状**：Claude Code、OpenAI Codex、Kimi Code、Cursor、Zed、DeepSeek CLI/harness、Gemini CLI、Aider 等各自读什么（`.claude/skills`、`.agents/skills`、`AGENTS.md`……）；哪些是事实标准、哪些需要薄适配器。产出一张对照表 + 可移植性建议。

产出写到 `wayfinder/research/skill-conventions-best-practices-2026-10.md`，带来源 URL，面向决策而非百科。
