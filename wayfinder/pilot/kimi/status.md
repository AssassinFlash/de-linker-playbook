---
phase: 2
phase_name: 试点完成
next: stop
method_skill: marketing-copywriting
output_dir: deliverables/
product_context: ~/Documents/New/CONTEXT.md
---

# 台账

进度真源。压缩后以本文件为准，不以对话记忆为准。

`product_context` 交接他机需更新此路径。读文件时把 `~` 展开为用户主目录。

## 当前

| 键 | 值 |
| --- | --- |
| phase | 2 |
| phase_name | 试点完成 |
| next | stop |
| method_skill | marketing-copywriting |
| output_dir | deliverables/ |
| product_context | `~/Documents/New/CONTEXT.md` |

## 阶段

| phase | 名称 | 做什么 | 完成标准 |
| --- | --- | --- | --- |
| 0 | 读产品上下文 | 只读 `product_context`，不把原文写入本仓库 | 三条陈述：买家是谁、卖什么、上下文里没有的数字/证据；frontmatter `phase: 1` |
| 1 | 写价值主张草稿 | 读并执行 `skills/marketing-copywriting/SKILL.md` | `deliverables/value-proposition.md` 非空，且不是 skill 例子原文；frontmatter `phase: 2` |
| 2 | 试点完成 | 报告产物路径后停止 | 不发明下一阶段 |

## 已完成

- 2026-10-06｜phase 0 读产品上下文：读取 `~/Documents/New/CONTEXT.md` 确认可读；三条陈述——买家：de-linker.com PDP 上下单储能设备的工程/采购型买家（下单前有具体订货疑虑）；所卖：Linker 在售储能 SKU（224 个，权威清单在 WooCommerce Store API）；缺口：CONTEXT.md 为词汇表/流程表，无任何具体参数、价格、认证数字，具体数字须读 `fact-base/`。无文件产物，仅台账回写。
- 2026-10-06｜phase 1 写价值主张草稿：按 `skills/marketing-copywriting/SKILL.md` 执行，正文 85 字，未编造数字，未引用 skill 例子。产物：`deliverables/value-proposition.md`。

## 回写

每完成一个 phase：同步改文件头 YAML 与「当前」表，在「已完成」追加一行（日期 + 做了什么 + 产物路径）。`next` 写成下一 phase 的动作。phase 2 的 `next` 为 `stop`。
