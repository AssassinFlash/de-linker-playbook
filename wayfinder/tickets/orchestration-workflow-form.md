---
wayfinder: grilling
status: open
assignee:
blocked_by: []
---

# 编排层落地形态

## Question

v3 有 9 个编排系 skill（`marketing-orchestrator`、`marketing-init`、`marketing-profile`、`product-profile`、`marketing-playbook-standards`、`marketing-teach`、`marketing-eval`、`marketing-evolve`、`skill-eval`），原本靠 47 个 slash command + Claude agents 驱动。本仓库跨 harness、没有 slash command。日常营销工作（SEO、内容、获客）在这个仓库里**怎么被驱动、进度怎么被跟踪**？

候选：

- **甲. wayfinder 票驱动**：像 PDP 线一样，每项营销工作开票走图；编排 skill 改写成阶段方法指南，由走图的 session 读取。进度可视，但轻量小活也要开票。
- **乙. orchestrator 自驱动**：任何 agent 进仓库读 AGENTS.md → orchestrator skill 告诉它阶段顺序、怎么读仓库状态判断「现在在哪、下一步是什么、产出放哪」。任何 harness 零准备上手，但进度靠文件约定，没人盯时会漂移。
- **丙. 命令卡片**：`commands/` 放纯 markdown 命令卡（学 Codex 版），人把卡片贴给任何 agent 即触发一个阶段。最直白，但要手动复制粘贴。

此决议直接决定 ③ 抽取规格对编排系 skill 的改写方向（`marketing-init`/`profile` 在我们的设计里要改写成「指路 `~/Documents/New` 读产品上下文」的引导）。
