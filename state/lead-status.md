---
mode: 冷启动
phase: 0
phase_name: 读产品上下文
next: 读 product_context（事实源入口 docs/fact-sources.md），按其指路取证；需要档案时执行 marketing-profile；写出三条陈述（买家、所卖、缺口）后进入 phase 1 画像
method_skill: marketing-profile
output_dir: deliverables/lead/
product_context: docs/fact-sources.md
feedback_read_at: 2026-10-15 16:31
current_action: phase 0：marketing-profile（获客线还没有反馈：没发过外展邮件，邮件反馈、询盘在等回流）
current_action_log:
---

# 获客台账

获客线的进度真源。压缩后以本文件为准，不以对话记忆为准。营销线的进度在 `state/marketing-status.md`，本文件不记、不改它。

`product_context` 指向本仓库内的事实源入口；仓外路径只在入口里，交接他机改入口，不改本文件。

## 当前

| 键 | 值 |
| --- | --- |
| mode | 冷启动 |
| phase | 0 |
| phase_name | 读产品上下文 |
| next | 读 `product_context`（事实源入口 `docs/fact-sources.md`），按其指路取证；需要档案时执行 marketing-profile；写出三条陈述（买家、所卖、缺口）后进入 phase 1 画像 |
| method_skill | marketing-profile |
| output_dir | deliverables/lead/ |
| product_context | `docs/fact-sources.md` |
| feedback_read_at | 2026-10-15 16:31 |
| current_action | phase 0：marketing-profile（获客线还没有反馈：没发过外展邮件，邮件反馈、询盘在等回流） |
| current_action_log | （无） |

## 阶段

| phase | 名称 | 方法 skill | 产出目录 | 完成标准 |
| --- | --- | --- | --- | --- |
| 0 | 读产品上下文 | 只读 `product_context`；需要档案时打开 `skills/marketing-profile/SKILL.md` | 不把原文写入本仓库 | 三条陈述：买家、所卖、缺口 |
| 1 | 画像 | `lead-icp-analysis`、`lead-search-term-expansion` | `deliverables/lead/01-icp/` | 见 `skills/lead-generation/SKILL.md` 阶段表 |
| 2 | 公司 | `lead-company-research`、`lead-distributor-research`、`lead-retailer-research` | `deliverables/lead/02-companies/` | 同上 |
| 3 | 联系人 | `lead-contact-discovery` | `deliverables/lead/03-contacts/` | 同上 |
| 4 | 市场 | `lead-competitor-analysis`、`lead-market-analysis` | `deliverables/lead/04-market/` | 同上 |
| 5 | USP | `lead-usp-extraction`、`lead-product-knowledge` | `deliverables/lead/05-usp/` | 同上 |
| 6 | 外展 | `lead-cold-email-gen`、`lead-warm-email-transform`、`lead-followup-sequence`、`lead-email-sequence-strategy`、`lead-magnet-gen` | `deliverables/lead/06-outreach/` | 同上 |
| 7 | 定向 | `lead-targeted-research`、`lead-targeted-outreach` | `deliverables/lead/07-targeted/` | 同上 |
| 8 | LinkedIn | `lead-linkedin-topic-research` 及各 `lead-linkedin-*` 帖类型 | `deliverables/lead/08-linkedin/` | 同上 |
| 9 | SEO | `lead-seo-editorial-guidelines`、`lead-seo-outline-gen`、`lead-seo-content-gen`、`lead-seo-content-edit` | `deliverables/lead/09-seo/` | 同上 |
| 10 | 销售 | `lead-service-first-contact`、`lead-service-quotation`、`lead-service-objection`、`lead-service-first-order`、`lead-service-delivery`、`lead-service-retention`、`lead-buyer-psychology` | `deliverables/lead/10-sales/` | 同上 |

键的意思：

- `mode`：`冷启动`（按上面的阶段打底，反馈 P1、P2 先做）或 `运营`（phase 10 做完后转入，每次「下一步」完全按反馈规则）。
- `feedback_read_at`：上次读底表反馈的时刻（北京时间「年-月-日 时:分」）。下次读反馈时作为 `--since` 传给 `scripts/next_step.py --line 获客`，用来判断哪些询盘是新的。
- `current_action`：本轮在做的动作，写成「规则编号 + 一句话」（如「M-01 起草给某公司的报价回信」）或「phase N：方法 skill」。
- `current_action_log`：这个动作做完后登记的执行登记编号；还没登记就留空。

## 待补登

底表写不进（没网、凭据缺）时，操作者做完的真实动作（发出的外展邮件等）先记在这里；下次登记时按 `skills/marketing-execution-log/SKILL.md` 补进底表「执行登记」，补完删行。收件人姓名、邮箱地址不记。

| 日期 | 渠道 | 做了什么 | 收件公司或网址 | 外展序列与第几封 |
| --- | --- | --- | --- | --- |
| （无） | | | | |

## 审批与过期

每份获客交付物一行，记它过没过证据闸、过没过期。`status` 取值和营销线同一套：`approved`（六维审查通过且已过证据闸，由 AI 自查后写，不需要操作者批准）| `draft`（还没过）| `stale`（过闸后因上游重写过期）| `missing`（文件不在）。`evidence_gate` 是最近一次过证据闸的日期，「运营里只剩记账时」按它挑最早的那份重查。含义见 `skills/lead-generation/references/orchestration-protocol.md` 步骤 6、7。交付物 frontmatter 是这份文件自己的记录，本表是全线索引：两边不一致时以 frontmatter 为准，当轮改正本表。

| 交付物 | 方法 skill | status | evidence_gate | review_score | stale_reason | stale_date |
| --- | --- | --- | --- | --- | --- | --- |
| （无） | | | | | | |

## 豁免（user_waiver）

操作者明确同意跳过某条硬依赖、或接受没过证据闸的某一处时记一行；依赖检查读本表。

| 日期 | 方法 skill | 跳过的硬依赖或证据闸条目 | 操作者原话 |
| --- | --- | --- | --- |
| （无） | | | |

## 已完成

- （无）

## 回写

每轮「下一步」后：改 `feedback_read_at`、`current_action`、`current_action_log`，文件头 YAML 与「当前」表同步。

每写入一份交付物（编排协议步骤 7）：改「审批与过期」里它那一行；被标为 `stale` 的下游行同步改。

每完成一个 phase：同步改文件头 YAML 与「当前」表，在「已完成」追加一行（日期 + 做了什么 + 产物路径）。`next` 写成下一动作。phase 10 完成后 `mode` 改为 `运营`，`next` 写「按反馈规则给下一步」，不写 `stop`。

只写本文件，不碰 `state/marketing-status.md`。
