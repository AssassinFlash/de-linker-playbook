---
phase: 1
phase_name: 基础
next: 执行 marketing-positioning 与 marketing-competitor-intelligence（无硬依赖，可并行）；两者 approved 后执行 marketing-pricing-strategy
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
| next | 执行 `marketing-positioning` 与 `marketing-competitor-intelligence`（无硬依赖，可并行）；两者 approved 后执行 `marketing-pricing-strategy` |
| method_skill | marketing-positioning |
| output_dir | deliverables/marketing/01-foundation/ |
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

- 2026-10-10：phase 0 读产品上下文完成。三条陈述：买家=德国/欧洲太阳能安装商与 EPC（B2B）；所卖=Linker「工程伙伴+批发平台」的逆变器/LFP 电池/一体机/电表/互感器/EMS 网关（GoodWe/SAJ/Pylontech/EcoFlow/Chint/MBS）；缺口=竞品 C&I 档与 ETC 留白 + 调试风险/配对核验/电网合规导航。phase 0 不落盘，无产物文件。

## 回写

每完成一个 phase：同步改文件头 YAML 与「当前」表，在「已完成」追加一行（日期 + 做了什么 + 产物路径）。`next` 写成下一 phase 的动作。phase 7 完成后 `next` 为 `stop`。
