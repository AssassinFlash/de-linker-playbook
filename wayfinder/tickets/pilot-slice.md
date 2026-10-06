---
wayfinder: task
status: closed
assignee: chesterjohn+agent
blocked_by: [generic-orchestration-research]
resolved: 2026-10-06
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

## Resolution

2026-10-06 实测完成（3 家尝试、2 家走通），主模型抽查了 kimi 的日志与交付物后关票。

| harness | 判定 | 说明 |
| --- | --- | --- |
| kimi 2.1.1 | **PASS** | 一次冷启动走通全循环（95s）：读台账 → 调 orchestrator → 读方法 skill → 产出交付物 → 回写台账 phase 0→1→2。`kimi -p` 即无头，不需额外权限 flag |
| codex 0.139.0 | **PASS** | 走通（76s），但需 CLI 层变通：`--ignore-user-config`（本机 config.toml 有类型错误）+ `--skip-git-repo-check` + 显式 `-m gpt-5.5`（默认 gpt-5.4 被账号 400 拒绝） |
| claude 2.1.283 | **FAIL（环境）** | 本机 OAuth 过期、无法刷新，冷启动卡在认证，未进入工作循环——非薄片问题。已确认无头权限组合 `-p --permission-mode acceptEdits`，待刷新登录后可补测 |

**核心结论**：

1. **假设升级为证据**：通用 harness 冷启动、仅靠仓库内文件（AGENTS.md + `.agents/skills/` + 台账）跑通「下一步」工作循环，在两家独立 harness 上验证通过。orchestrator skill + 台账的编排模式可行——⑨ 的裁定有了实测依据。
2. **可移植性摩擦在 CLI 调用层，不在 playbook 内容**：两家 PASS 的 harness 都自动注入了 AGENTS.md 与 skill 目录；所有失败点都是 flag/配置/认证问题。
3. 遗留：Claude Code 需 `.claude/skills/` 适配层（研究票已预言，本次因认证未能实测）；copywriting skill 有小瑕疵（自报字数 85 实际 107），供 ③ 规格票的验收清单参考。
4. 实测记录与交付物证据：`wayfinder/pilot/{kimi,codex,claude}.md` 及同名目录。薄片本体提交 `a166ffd`。

**结论：走通 → 可以跑量。** ②（正式骨架）与 ⑨（编排形态裁定）解锁。
