---
wayfinder: research
status: closed
assignee: chesterjohn+agent
blocked_by: []
resolved: 2026-10-06
---

# 跨 harness skill 约定与最新编写最佳实践调研

## Question

两个事实问题，答案直接喂养「抽取规格定稿」与最终验收标准：

1. **Anthropic Agent Skills 官方最新编写最佳实践**：SKILL.md frontmatter 官方字段集、`description` 写法、渐进式披露（progressive disclosure）、正文长度指引、examples/references 组织方式、官方点名的反模式。来源优先级：官方文档站、官方工程博客、agentskills 规范站。
2. **2026 年各 agent harness 的项目级 skill / 指令发现机制现状**：Claude Code、OpenAI Codex、Kimi Code、Cursor、Zed、DeepSeek CLI/harness、Gemini CLI、Aider 等各自读什么（`.claude/skills`、`.agents/skills`、`AGENTS.md`……）；哪些是事实标准、哪些需要薄适配器。产出一张对照表 + 可移植性建议。

产出写到 `wayfinder/research/skill-conventions-best-practices-2026-10.md`，带来源 URL，面向决策而非百科。

## Resolution

2026-10-06 研究子代理完成，产出 `wayfinder/research/skill-conventions-best-practices-2026-10.md`（514 行；来源：agentskills.io 规范站、Anthropic 官方文档与工程博客、Codex/Cursor/Gemini/Kimi/Zed/Copilot 第一方文档、agents.md）。要点：

1. **正典极小**：frontmatter 必需字段只有 `name` + `description`；可选 `license`/`compatibility`/`metadata`。`name` 须与目录同名（小写连字符、≤64 字符、禁含 `claude`/`anthropic`）。`allowed-tools`/`model`/`context`/`mcp__*` 等厂商字段一律不进正典——与本图既定原则一致。
2. **description 是触发器**：须同时写清「做什么 + 何时用」，硬上限 1024 字符；~80 个 skill 的目录规模建议 300–700 字符、触发关键词前置（Codex 可能截断目录）。
3. **渐进式披露**：SKILL.md 本体 <500 行 / <5k token；references 只从 SKILL.md 向下走一层、相对路径（正斜杠）、用「read when…」句式而非「see references/」。
4. **发现层（关键结论）**：**没有任何 harness 自动扫描裸 `skills/`**。事实标准 = `.agents/skills/<name>/SKILL.md`（Codex、Cursor、Gemini 别名、Kimi、Zed、Copilot/VS Code 都读）；Claude Code 官方只认 `.claude/skills/`；Zed/Gemini 只支持扁平目录（不支持嵌套分类）。→ 正典放 `skills/`，发现适配器 = `.agents/skills/<name>` 软链到 `../../skills/<name>`；Claude 需要时再生成 `.claude/skills/`。
5. **AGENTS.md 是真标准**（AAIF/Linux Foundation 托管）：Codex（32 KiB 上限）、Cursor、Copilot、Zed、Kimi、Claude Code 均读取；Gemini 需 `context.fileName` 配置、Aider 需 `.aider.conf.yml` 一行。不要复制成 CLAUDE.md，不要在 AGENTS.md 内联 80 个 skill 正文。
6. DeepSeek/Continue 无第一方 SKILL.md 扫描器，继承其宿主 harness 的约定。

全部结论与验收闸模板见研究文档 §2。
