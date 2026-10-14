---
wayfinder: task
status: open
assignee:
step: 6
blocked_by: [lead-loop-orchestrator, fact-source-rewire-skills]
---

# 激活名单入口

## Question

（HITL 交名单 + AFK 改 skill）按裁定 Q7 接上激活名单：名单放私有 vault `deliverables/lead/00-system/`；获客第 2 阶段以名单公司为起点逐家调研，第 3 阶段联系人以名单为准；其余按陌生开发。

- 名单格式：列定义写进 `schemas/`（公开，无数据）；操作者把老板给的表放进 vault（agent 可帮转格式，原件不动）。名单本身绝不进公开仓库。
- 改获客台账与编排（「获客编排改循环」之后的形态）：第 2 / 3 阶段的输入多一个「名单」来源；改 `lead-company-research`、`lead-contact-discovery` 及 `lead-generation/references/dependency-graph.md` 中相关处，只加入口，不改方法。
- 「已同意」只解除发信顾虑，不提供客户认知：skill 里写明按陌生开发先调研再接触（`CONTEXT.md`「激活名单」）。

## 完成标准

- 用名单中一家公司走一次第 2 阶段：产出落 `deliverables/lead/02-companies/`，来源列齐；台账显示名单进度（已调研 n / 共 N）。
