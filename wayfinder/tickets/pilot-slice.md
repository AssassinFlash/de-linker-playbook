---
wayfinder: task
status: open
assignee:
blocked_by: [generic-orchestration-research]
---

# 试点薄片：最小骨架 + 2 个 skill + 多 harness 实测

## Question

先做一个能走通的最小薄片，走通才跑量（用户定，与 ET 试点先行同一打法）。薄片内容：

1. **最小骨架**：`AGENTS.md` 草稿、`skills/`、`.agents/skills/` 软链层、`.gitignore`
2. **抽 2 个代表性 skill**：一个独立方法 skill（候选 `marketing-seo-audit` 或 `copywriting`，做简化版）+ 一个迷你 orchestrator（阶段导航：读状态文件 → 判断下一步 → 指引产出位置）
3. **实测矩阵**：本机已装六个 harness CLI——`kimi`（必测，主 harness）、`claude`、`codex`、`cursor-agent`、`gemini`、`opencode` 中再选至少 1 个，共 ≥2 家
4. **通过标准**：冷启动一个全新会话，agent 只读 AGENTS.md、无人解释就能：找到 skill → 理解阶段 → 用 skill 方法产出一个真实小交付物到 `deliverables/`。逐 harness 记录：什么行、什么不行、差在哪

产出：薄片本体 + 实测记录。记录喂给「编排层落地形态」的裁定与「抽取规格定稿」。

执行：子代理搭建与驱动各 harness CLI 实测，主模型组织 review。
