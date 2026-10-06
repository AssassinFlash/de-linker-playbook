---
wayfinder: grilling
status: closed
assignee: chesterjohn+agent
blocked_by: [pilot-slice]
resolved: 2026-10-06
---

# 编排层落地形态

## Question

v3 有 9 个编排系 skill（`marketing-orchestrator`、`marketing-init`、`marketing-profile`、`product-profile`、`marketing-playbook-standards`、`marketing-teach`、`marketing-eval`、`marketing-evolve`、`skill-eval`），原本靠 47 个 slash command + Claude agents 驱动。本仓库跨 harness、没有 slash command。日常营销工作（SEO、内容、获客）在这个仓库里**怎么被驱动、进度怎么被跟踪**？

候选：

- **甲. wayfinder 票驱动**：像 PDP 线一样，每项营销工作开票走图；编排 skill 改写成阶段方法指南，由走图的 session 读取。进度可视，但轻量小活也要开票。
- **乙. orchestrator 自驱动**：任何 agent 进仓库读 AGENTS.md → orchestrator skill 告诉它阶段顺序、怎么读仓库状态判断「现在在哪、下一步是什么、产出放哪」。任何 harness 零准备上手，但进度靠文件约定，没人盯时会漂移。
- **丙. 命令卡片**：`commands/` 放纯 markdown 命令卡（学 Codex 版），人把卡片贴给任何 agent 即触发一个阶段。最直白，但要手动复制粘贴。

此决议直接决定 ③ 抽取规格对编排系 skill 的改写方向（`marketing-init`/`profile` 在我们的设计里要改写成「指路 `~/Documents/New` 读产品上下文」的引导）。

**裁定方式改为证据先行（用户定 2026-10-06）**：不做纯假设——先等「通用 harness 编排机制调研」与「试点薄片」的实测记录，再在甲/乙/丙中裁定或提出新方案。

## Resolution

2026-10-06 用户裁定（证据先行后拍板）：**乙为骨 + 甲为重活**。

- **骨**：orchestrator skill + 台账自驱动——任何 agent 冷启动读 AGENTS.md → orchestrator → `state/status.md`，自判断「现在在哪、下一步干什么、产出放哪」。已由试点薄片实测支撑（kimi / codex 双 PASS）。
- **重活**：多阶段、大体量的营销工作仍开 wayfinder 票驱动（与 PDP 线工作方式一致）。
- **命令卡片（丙）不进正典**，需要时作为某 harness 的薄适配器按需生成。
- 编排系 skill 的改写方向随之确定：`marketing-orchestrator` = 阶段导航（试点版已验证形态）；`marketing-init`/`marketing-profile`/`product-profile` 改写为「指路 `~/Documents/New` 读产品上下文」的引导型 skill。
