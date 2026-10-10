---
phase: 1
phase_name: 基础
next: 用户确认 deliverables/marketing/01-foundation/context-pointer.md 的覆盖四项（业务概览/ICP/差异化/证据点）；确认后执行 marketing-positioning、marketing-competitor-intelligence、marketing-pricing-strategy
method_skill: marketing-positioning
output_dir: deliverables/marketing/01-foundation/
product_context: ~/Documents/New/CONTEXT.md
---

# 台账

进度真源。压缩后以本文件为准，不以对话记忆为准。

`product_context` 交接他机需更新此路径。读文件时把 `~` 展开为用户主目录。

## 当前

| 键 | 值 |
| --- | --- |
| phase | 1 |
| phase_name | 基础 |
| next | 用户确认 `deliverables/marketing/01-foundation/context-pointer.md` 的覆盖四项（业务概览/ICP/差异化/证据点）；确认后执行 `marketing-positioning`、`marketing-competitor-intelligence`、`marketing-pricing-strategy` |
| method_skill | marketing-positioning |
| output_dir | `deliverables/marketing/01-foundation/` |
| product_context | `~/Documents/New/CONTEXT.md` |

## 阶段

| phase | 名称 | 方法 skill | 产出目录 | 完成标准 |
| --- | --- | --- | --- | --- |
| 0 | 读产品上下文 | 只读 `product_context`；需要档案时打开 `skills/marketing-profile/SKILL.md` | 不把原文写入本仓库 | 三条陈述：买家是谁、卖什么、缺口 |
| 1 | 基础 | `marketing-positioning`、`marketing-competitor-intelligence`、`marketing-pricing-strategy` | `deliverables/marketing/01-foundation/` | 各方法 skill 交付物非空，且不是例子原文 |
| 2 | SEO | `marketing-seo-audit`、`marketing-ai-seo`、`marketing-programmatic-seo`、`marketing-site-and-schema` | `deliverables/marketing/02-seo/` | 同上 |
| 3 | 内容 | `marketing-content-strategy`、`marketing-copywriting`、`marketing-visual-content` | `deliverables/marketing/03-content/` | 同上 |
| 4 | 获客 | `marketing-social-content`、`marketing-paid-advertising`、`marketing-email-outreach` | `deliverables/marketing/04-acquisition/` | 同上 |
| 5 | CRO | `marketing-landing-page`、`marketing-inquiry-flow`、`marketing-funnel-optimization` | `deliverables/marketing/05-cro/` | 同上 |
| 6 | 增长 | `marketing-launch-strategy`、`marketing-referral-program`、`marketing-retention` | `deliverables/marketing/06-growth/` | 同上 |
| 7 | 度量 | `marketing-analytics-and-optimization` | `deliverables/marketing/07-measurement/` | 同上 |

## 已完成

- 2026-10-10 phase 0 读产品上下文：`~/Documents/New/CONTEXT.md` 可读，按 marketing-profile 完成 15 节覆盖核对；产物 `deliverables/marketing/01-foundation/context-pointer.md`（仅指针，无事实原文，confirmed: 否，待用户过目）。

## 回写

每完成一个 phase：同步改文件头 YAML 与「当前」表，在「已完成」追加一行（日期 + 做了什么 + 产物路径）。`next` 写成下一 phase 的动作。phase 7 完成后 `next` 为 `stop`。
