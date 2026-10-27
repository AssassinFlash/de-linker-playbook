---
mode: 冷启动
phase: 1
phase_name: 基础
next: 做 marketing-positioning，按事实源入口写定位，产出放 deliverables/marketing/01-foundation/
method_skill: marketing-positioning
output_dir: deliverables/marketing/01-foundation/
product_context: docs/fact-sources.md
feedback_read_at: 2026-10-27 22:35
current_action: W-13 / W-24 一次性核查（18 个登记页 + 61 个登记页，结论已写底表备注）
current_action_log:
---

# 营销台账

营销线的进度真源。压缩后以本文件为准，不以对话记忆为准。获客线的进度在 `state/lead-status.md`，本文件不记、不改它。

`product_context` 指向本仓库内的事实源入口；仓外路径只在入口里，交接他机改入口，不改本文件。

## 当前

| 键 | 值 |
| --- | --- |
| mode | 冷启动 |
| phase | 1 |
| phase_name | 基础 |
| next | 做 marketing-positioning，按事实源入口写定位，产出放 deliverables/marketing/01-foundation/ |
| method_skill | marketing-positioning |
| output_dir | deliverables/marketing/01-foundation/ |
| product_context | `docs/fact-sources.md` |
| feedback_read_at | 2026-10-27 22:35 |
| current_action | W-13 / W-24 一次性核查（18 个登记页 + 61 个登记页，结论已写底表备注） |
| current_action_log | |

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

键的意思：

- `mode`：`冷启动`（按下面的阶段打底，反馈 P1、P2 先做）或 `运营`（phase 7 做完后转入，每次「下一步」完全按反馈规则）。
- `feedback_read_at`：上次读底表反馈的时刻（北京时间「年-月-日 时:分」）。下次读反馈时作为 `--since` 传给 `scripts/next_step.py`，用来判断哪些询盘是新的。
- `current_action`：本轮在做的动作，写成「规则编号 + 一句话」（如「W-04 在 GSC 给 6 个页面请求编入索引」）或「phase N：方法 skill」。
- `current_action_log`：这个动作做完后登记的执行登记编号；还没登记就留空。

## 待补登

底表写不进（没网、凭据缺）时，操作者做完的真实动作先记在这里；下次登记时按 `skills/marketing-execution-log/SKILL.md` 补进底表「执行登记」，补完删行。GSC 里请求编入索引用 `scripts/next_step.py log-request` 登记。

| 日期 | 渠道 | 做了什么 | 网址或收件公司 | 查证结果 |
| --- | --- | --- | --- | --- |
| （无） | | | | |

## 豁免（user_waiver）

操作者明确同意跳过某条硬依赖、或接受没过证据闸的某一处时记一行；依赖检查读本表。

| 日期 | 方法 skill | 跳过的硬依赖或证据闸条目 | 操作者原话 |
| --- | --- | --- | --- |
| （无） | | | |

## 已完成

- 2026-10-19：closed-loop「GA4 与同意横幅站点接入」完成；执行登记 E-20261019-01 至 E-20261019-04，见该票 Resolution；冷启动阶段仍为 phase 0。
- 2026-10-27：phase 0 完成。指针 `deliverables/marketing/01-foundation/context-pointer.md`；三条陈述 `deliverables/marketing/00-system/phase-0-三条陈述.md`。三源可读；缺口见指针。进入 phase 1。
- 2026-10-27：W-13 的 18 个登记页、W-24 的 61 个登记页核查完成，结论写进底表备注，`next_step.py` 队列里这两批已清零。发现：整站首字节 4.1–9.7 秒（18 页实测），偏慢，交站点侧；5 个分类归档缺 meta description（其中 4 个按操作者决定不要求收录）。

## 回写

每轮「下一步」后：改 `feedback_read_at`、`current_action`、`current_action_log`，文件头 YAML 与「当前」表同步。

每完成一个 phase：同步改文件头 YAML 与「当前」表，在「已完成」追加一行（日期 + 做了什么 + 产物路径）。`next` 写成下一 phase 的动作。phase 7 完成后 `mode` 改为 `运营`，`next` 写「按反馈规则给下一步」，不写 `stop`。

只写本文件，不碰 `state/lead-status.md`。
