# 第一次使用指南

本指南面向非技术背景的用户。你不需要懂代码。在兼容的助手里打开本仓库即可（Kimi / Z Code / DeepSeek / OpenCode / Hermes）。

入口不是斜杠命令。要做某项工作，打开对应的 `skills/<name>/SKILL.md`，按正文「步骤」执行。

## 从你的业务目标开始

| 你现在的情况 | 打开并按其步骤做 |
|---|---|
| 第一次打开这个项目 | `skills/marketing-init/SKILL.md` |
| 还没有确认公司、产品和目标市场可读 | `skills/marketing-profile/SKILL.md` |
| 不知道先做 SEO、内容还是广告 | 先读 `state/marketing-status.md`，再打开 `skills/marketing-orchestrator/SKILL.md` |
| 已经知道要做文案或价值主张 | `skills/marketing-copywriting/SKILL.md` |
| 已经知道要做定位 / 竞品 / 定价等具体方法 | 打开对应 `skills/marketing-<方法>/SKILL.md`（见下方阶段表） |

## 开始前

1. 工作目录是本仓库根（含 `AGENTS.md`、`state/`、`skills/`）。
2. 产品事实在仓外，入口在仓内：`docs/fact-sources.md`（两张台账的 `product_context` 都指向它）。入口告诉助手什么问题去线上站点、新站仓库还是竞品调研查。
3. 产出只进本仓库的 `deliverables/marketing/` 与 `deliverables/lead/`，不在仓外另建产出根。

## 第一步：预检项目状态

打开 `skills/marketing-init/SKILL.md` 并按其步骤做。

助手会：

- 确认两张台账 `state/marketing-status.md`、`state/lead-status.md` 是否存在
- 确认 `deliverables/marketing/` 与 `deliverables/lead/` 阶段目录齐全（缺则创建）
- 核对两张台账里的 `product_context`（应为 `docs/fact-sources.md`）
- 把初始化报告写到 `deliverables/marketing/00-system/init-report.md`

若产品上下文不可读，下一步打开 `skills/marketing-profile/SKILL.md`；否则打开 `skills/marketing-orchestrator/SKILL.md`。

## 第二步：确认产品上下文（只指路，不复制）

打开 `skills/marketing-profile/SKILL.md` 并按其步骤做。

助手会：

1. 读事实源入口 `docs/fact-sources.md`（即台账 `product_context`）
2. 按入口的「什么问题查哪个源」去线上站点、新站仓库或竞品调研取证；查不到的标〔未证实〕
3. 在 `deliverables/marketing/01-foundation/context-pointer.md` 写下指针和覆盖表，**不把产品原文拷进本仓库**

**你需要做的**：什么都不用确认。事实以线上站点和新站仓库为准；要改事实，改站点（经新站仓库），不改本仓库。

更深的规格 / 价值链 / 买家角色读，打开 `skills/marketing-profile/SKILL.md`。

## 第三步：让编排器规划

有具体目标但不确定从哪开始时：先读 `state/marketing-status.md`，再打开 `skills/marketing-orchestrator/SKILL.md` 并按其步骤做。

编排器会：

- 读出台账的 `phase`、`next`、`method_skill`、`output_dir`、`product_context`
- 宣布当前阶段、下一方法 skill、产出路径
- 按方法 skill 做到交付物落地（需要隔离时 dispatch a subagent, else do it inline）
- 回写台账

寒暄只复述 `phase`，不改文件。

## 第四步：按阶段执行

没有单独的「阶段聚合」skill。阶段目录是产出位置；方法在各自 `skills/<name>/SKILL.md` 里。不确定选哪个时，走编排器。

| 目标 | 方法 skill（示例） | 产出根 |
|------|------|------|
| 定位、竞品、定价 | `skills/marketing-positioning/SKILL.md`、`skills/marketing-competitor-intelligence/SKILL.md`、`skills/marketing-pricing-strategy/SKILL.md` | `deliverables/marketing/01-foundation/` |
| SEO | `skills/marketing-seo-audit/SKILL.md`、`skills/marketing-ai-seo/SKILL.md`、`skills/marketing-site-and-schema/SKILL.md` | `deliverables/marketing/02-seo/` |
| 内容策略 / 文案 | `skills/marketing-content-strategy/SKILL.md`、`skills/marketing-copywriting/SKILL.md` | `deliverables/marketing/03-content/` |
| 获客（社媒 / 广告 / 邮件） | `skills/marketing-social-content/SKILL.md`、`skills/marketing-paid-advertising/SKILL.md`、`skills/marketing-email-outreach/SKILL.md` | `deliverables/marketing/04-acquisition/` |
| 转化优化 | `skills/marketing-landing-page/SKILL.md`、`skills/marketing-inquiry-flow/SKILL.md`、`skills/marketing-funnel-optimization/SKILL.md` | `deliverables/marketing/05-cro/` |
| 增长（上市 / 推荐 / 留存） | `skills/marketing-launch-strategy/SKILL.md`、`skills/marketing-referral-program/SKILL.md`、`skills/marketing-retention/SKILL.md` | `deliverables/marketing/06-growth/` |
| 数据体系 | `skills/marketing-analytics-and-optimization/SKILL.md` | `deliverables/marketing/07-measurement/` |
| 获客名单与外联 | 打开对应 `skills/lead-*/SKILL.md` | `deliverables/lead/` 下对应小写阶段目录 |

教学笔记与评测史进 `deliverables/marketing/00-system/`（与 `00-research/` 战役阶段分开）。

## 第五步：直接做一项方法

已经知道任务时，打开该方法的 `skills/<name>/SKILL.md`，不要另写一套流程。步骤 0 若要求共用规则，先读 `skills/marketing-playbook-standards/SKILL.md`。

## 第六步：评审交付物

重要交付物完成后，打开 `skills/marketing-eval/SKILL.md`（以及需要时的 `skills/marketing-skill-eval/SKILL.md`），按 `evals/` 与抽取规格验收。

仓库级校验：

```
python3 evals/validate_project.py
python3 evals/validate_deliverables.py
```

## 第七步：持续改进

某个 skill 用起来不顺时，先按 `skills/marketing-eval/SKILL.md` 评，再打开 `skills/marketing-evolve/SKILL.md`，按评测回写本仓库 skill（当轮清账）。

告诉助手：

- 你期望它怎么做
- 它实际做了什么
- 哪里不对

## 语言规则

- **你输入**：中文
- **策略文档**：中文
- **面客文案**（广告、邮件、网站文案）：英文
- **Excel 字段名**：英文
- **Excel 表头**：中文

## 重要原则

1. **产品上下文优先**：事实只从 `docs/fact-sources.md` 进。本仓库只指路、不复制。
2. **真实数据**：不要允许助手编造 CPC、市场规模、竞品数据。要求它标注来源。
3. **先小规模测试**：第一次用，先做一个很小的任务（例如只分析 3 家竞品），确认流程顺了再扩大。
4. **保存交付物**：营销产出在 `deliverables/marketing/`，获客产出在 `deliverables/lead/`，阶段目录一律小写。

## 术语速查

| 术语 | 你可以理解为 |
|---|---|
| 产品上下文 | 仓外的公司/产品事实，入口 `docs/fact-sources.md`（`product_context`） |
| 台账 | 进度真源，营销 `state/marketing-status.md`、获客 `state/lead-status.md` 各一张 |
| 交付物 | `deliverables/` 里的产出 |
| Skill | `skills/<name>/SKILL.md` 里可重复运行的工作流 |
| 编排器 | `skills/marketing-orchestrator/SKILL.md`，读台账并分派方法 skill |

## 遇到问题

| 问题 | 解决方法 |
|------|---------|
| 助手说找不到 skill | 运行 `python3 evals/validate_project.py`；正典在 `skills/<name>/SKILL.md` |
| 产出质量差 | 确认已按台账路径读过产品上下文；再跑 `skills/marketing-eval/SKILL.md` |
| Excel 没有生成 | 空表在 `templates/`；导出脚本在 `templates/scripts/`（填写工作簿需要本机已装相应库） |
| 不知道下一步该做什么 | 营销：读 `state/marketing-status.md`，打开 `skills/marketing-orchestrator/SKILL.md`；获客：读 `state/lead-status.md`，打开 `skills/lead-generation/SKILL.md` |

## 旧入口怎么办？

若你以前用过斜杠命令或阶段聚合入口，它们已改为打开 `skills/<name>/SKILL.md`。对照表见 `docs/legacy-command-migration.md`。
