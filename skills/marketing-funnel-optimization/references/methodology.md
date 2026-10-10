# 漏斗优化方法

读本文件前先确认 `SKILL.md` 已判定本 skill 适用。查询意图、最低条数、漏斗阶段、评分与表结构以本文为准。与 `SKILL.md` 冲突时以 `SKILL.md` 为准。

## 目录

- [输入](#输入)
- [采集](#采集)
- [分析](#分析)
- [交付](#交付)
- [反模式](#反模式)
- [质量闸门](#质量闸门)
- [可验证断言](#可验证断言)

## 输入

先读台账 `product_context`（缺省 `~/Documents/New/CONTEXT.md`；需要参数再读同目录 `fact-base/`）。上游若已存在则读：

- `deliverables/marketing/01-foundation/` 定位、买家角色、定价、样品政策
- `deliverables/marketing/03-content/` 内容与日历约束
- `deliverables/marketing/05-cro/` 已批准的 `landing-page.md` 与 `inquiry-flow.md`（缺则记缺口，不重做页上入口或提交后话术）
- `deliverables/marketing/06-growth/` 下 `launch-strategy.md`、`referral-program.md`、`retention.md`（缺则记缺口，不从零写佣金或赢回）

再列出（未知则记缺口，不编造）：

- 询盘量、首次回复时长、询盘→报价、询盘→样品、报价→订单、复购率、主要流失阶段
- 团队人数、工时、语种、已用渠道、CRM 或表格
- 是否在投广告、是否有独立落地页、近期上市或展会节点

产品事实不写进 skill，不另写公司档案。品类、目标市场、产地只引用产品上下文对应字段，不在本文填值。

缺项列缺口后停。用户只给站点 URL、上下文仍缺品类或市场：抓该站能核实的事实后停，不进入落盘装成已完成。

## 采集

默认一条能力：用网页搜索查证。需要原文时抓取指定 URL 的正文。搜索不可用则停止并写缺口，不编造、不并列多引擎菜单。

### 本站漏斗体验

抓取并摘录（对照已批准稿，只为标矛盾与缺口，不据此重做 CTA/字段/话术）：

1. 首页 — 价值主张、信任信号、主 CTA
2. 产品 / 品类页 — 规格、CTA 位置、询盘入口
3. 询盘 / 联系页 — 字段、必填/选填、布局、回复承诺
4. 落地页（有投放则抓，无则记缺口）— 与广告/检索词的信息匹配、单一 CTA

字段数、CTA 原文、信任信号必须来自已抓取正文。页面不可访问则记下状态原因，不编造。

### 竞品漏斗（≥3）

每个竞品记录：首页/产品页价值主张、询盘表字段数与 CTA 原文、弹窗或潜客捕获（无则「未观察到」）、流程页、伙伴/转介绍页、上市宣布。页面不可访问则记下原因并换下一个，不编造。

### 查询意图

把产品上下文的品类与目标市场代入下列意图，每条记下 URL、摘录、访问日期。查询 1–4 只为竞品对照与跨阶段矛盾提供证据，不据此重做 CTA、字段清单或回复话术。查询 7–9 读既有产出，不重搜做法。

1. 该品类 B2B 询盘表字段数与 CTA 原文（竞品页）
2. B2B 制造落地页 CTA 与信任信号原文（竞品页）
3. 制造网站退出意向弹窗与潜客捕获（有则摘原文，无则「未观察到」）
4. B2B 询盘回复时效与转化的公开基准
5. 制造供应商新客户 onboarding 与复购
6. B2B 制造报价阶段升级与交叉销售
7. 不重搜上市做法；读 `deliverables/marketing/06-growth/launch-strategy.md`，记下路径或缺口
8. 不重搜转介绍佣金；读 `deliverables/marketing/06-growth/referral-program.md`，记下路径或缺口
9. 不重搜留存赢回；读 `deliverables/marketing/06-growth/retention.md`，记下路径或缺口
10. 目标市场该品类采购路径（当前或下一自然年）

结果不够时再补：展会日历、回复时效案例、样品政策公开页。仍用同一条搜索能力。第 3–6 章不另搜「如何改落地页/表单」的做法清单；以已批准稿 + 已抓页对照为准。

多页抓取需要隔离时 dispatch a subagent, else do it inline。

### 最低数据量

进入分析前至少备齐；达不到的写入缺口，不降低后项装成已完成。

- 本站：首页 + 产品页 + 询盘页已完整分析；落地页有则分析、无则缺口
- 已批准 `landing-page.md` 与 `inquiry-flow.md` 已读，或显式缺口
- `06-growth/` 上市 / 转介绍 / 留存既有产出已读，或显式缺口
- **3** 个竞品完整漏斗：落地/首页 → 表单 → CTA → 信任信号
- 询盘率、按字段数的表单完成、回复时效影响、复购率：有公开源则记下并标「行业参考值，实际以你的数据为准」；无则缺口
- 用户漏斗指标已采集，或显式写「用户数据未知」
- 目标市场买家行为、贸易条款（FOB/CIF 以产品上下文为准）、已出现渠道

### 校验

- 每个被分析页面须可访问；不可访问则换源并记原因
- 竞品数据来自已抓取正文，不靠假设
- 转化率、回复时长有来源；行业数字必须带「行业参考值，实际以你的数据为准」
- 禁止编造统计、竞品 URL 或未抓取页面的字段清单
- `source` 必须含可访问 URL，禁止只写能力名

## 分析

把每条发现映射到标准漏斗（入口名称以产品上下文已出现渠道为准，不默认某一平台）：

```
访问 → 落地/产品页 → 询盘 → 首次回复与资质判定
      → 报价/样品 → 订单 → 复购 → 转介绍
```

### 落地页（第 3 章）

读已批准 `deliverables/marketing/05-cro/landing-page.md`。对照已抓首页 / 产品页 / 落地页，只填跨阶段矛盾与缺口，不重做价值主张、标题、CTA 层级或异议文案。

跨阶段核对字段（写入第 3 章与工作簿 Page Audit；每条能指回已批准稿路径或已抓 URL）：

| 字段 | 用途 |
| --- | --- |
| live_cta | 已抓页 CTA 原文 |
| approved_cta | 着陆页稿已定 CTA |
| next_stage | 该 CTA 应接到的阶段（Inquiry / Quote / Sample） |
| contradiction_or_gap | 页与稿、或 CTA 与下游表单 / 回复承诺不一致；无则「无矛盾」 |
| priority | P0 / P1 / P2；只服务跨阶段优先级，不定稿改法 |

评分必须能指回已抓取段落或已批准稿。无已批准稿则整章记缺口，不另起落地页方案。

### 询盘表单（第 4 章）

读已批准 `landing-page.md` 的表单入口与已抓询盘页。只标字段数 / 必填与下游资质、回复承诺的矛盾，不另起删 / 留 / 改字段清单或布局定稿。

| 字段 | 用途 |
| --- | --- |
| live_field_count | 已抓表单字段数（来自原文） |
| approved_fields | 着陆页稿已定字段 |
| downstream | 与询盘流资质量表或首次回复承诺是否打架 |
| contradiction_or_gap | 页与稿、或表单与下游不一致；无则「无矛盾」 |
| priority | P0 / P1 / P2 |

即时通讯是否与表单并列，以目标市场与产品上下文已出现频道为准；本 skill 只标与已批准入口策略的偏差，不定稿是否启用。

### 弹窗与潜客捕获（第 5 章）

读已批准 `landing-page.md` 弹窗 / 捕获节（缺则缺口）。对照已抓页是否观察到弹窗。只标与主 CTA、询盘入口抢注意力或频次冲突，不定稿弹窗文案、触发、合规勾选或移动端行为。

| 字段 | 用途 |
| --- | --- |
| live_popup | 已抓页观察到的弹窗（无则「未观察到」） |
| approved_capture | 着陆页稿已定捕获策略（无则缺口） |
| contradiction_or_gap | 与主入口 / 询盘流抢注意力或频次冲突；无则「无矛盾」 |
| priority | P0 / P1 / P2 |

### 询盘流程（第 6 章）

读已批准 `deliverables/marketing/05-cro/inquiry-flow.md`。资质量表与回复时效以该稿七维四档为准，不在本文件另开计分或档位。只填与第 3–5 章入口、第 7 章 onboarding 起点的跨阶段矛盾与缺口，不重写回复话术或步骤定稿。

| 字段 | 用途 |
| --- | --- |
| approved_sla | 询盘稿首次回复目标 |
| approved_scorecard | 七维四档（以询盘稿为准） |
| live_promise | 已抓页回复承诺（无则「未声明」） |
| contradiction_or_gap | 页承诺 vs 询盘稿、或入口 vs onboarding 起点不一致；无则「无矛盾」 |
| priority | P0 / P1 / P2 |

方法默认（工作时间内 2 小时）仅在询盘稿缺失时写入缺口对照，不覆盖已批准稿。

### 首单 onboarding

旅程：`首次询盘 → 报价 → 样品 → 样品质检 → 首单生产 → 生产更新 → 出运前检验 → 运输与追踪 → 到货确认 → 到货后跟进 → 复购`。

每阶段写：时机、渠道、内容类型、负责人。包含主动生产照片、请款前质检报告、全套运输文件加清关指引、到货后 3–5 天满意度核验。

样品政策：快递；收费样品可在大货抵扣；规格事先写清；交期明确。

### 升级与交叉销售

按产品上下文的品类字段映射升级路径：材质/等级、表面处理、厚度/尺寸、服务加项（包装、五金、检验、指南）、数量阶梯。禁止在 skill 里填具体牌号或产地。

报价结构模板（填用户真实规格，不把本段当交付物原文）：

```
BASE OPTION
Product: [standard spec] | Price: [observed or user-provided] | Total: [sum]

RECOMMENDED UPGRADE
Product: [premium spec]
Why: [one sentence citing project environment or buyer type]
Price: [observed or user-provided] | Total: [sum] ([premium %])

PROJECT NOTE
Environment: [from inquiry]
Recommendation: [technical advice]
```

不得删除基础选项。每条报价最多一个清晰升级建议。

### 上市策略（第 9 章）

指向 `marketing-launch-strategy` 既有产出：`deliverables/marketing/06-growth/launch-strategy.md`（及同目录工作簿）。本 skill 只写上市节点接到 Visit → Inquiry → Order 的跨阶段优先级。不重写 ORB、三阶段日历、样品物流。缺产出则整章缺口。

工作簿 Launch Timeline：`source` 必须是上述路径；缺则达不到行数时写入缺口，禁止用方法默认周数编造任务。

| 字段 | 用途 |
| --- | --- |
| upstream_path | 已读上市稿路径（或「缺口」） |
| funnel_join | 上市动作接到的漏斗阶段 |
| cross_stage_priority | P0 / P1 / P2 |
| source | 上游路径或「缺口」 |

### 转介绍与合作伙伴（第 10 章）

指向 `marketing-referral-program` 既有产出：`deliverables/marketing/06-growth/referral-program.md`。本 skill 只写 Referral 与 Repeat / Order 的衔接优先级。不重写佣金档、激活序列或追踪表。缺产出则整章缺口。

工作簿 Referral Program：`source` 必须是上述路径；禁止从本文件填佣金百分比。

| 字段 | 用途 |
| --- | --- |
| upstream_path | 已读转介绍稿路径（或「缺口」） |
| funnel_join | Referral 接到 Repeat / Order 的方式 |
| cross_stage_priority | P0 / P1 / P2 |
| source | 上游路径或「缺口」 |

### 留存与流失预防（第 11 章）

指向 `marketing-retention` 既有产出：`deliverables/marketing/06-growth/retention.md`。本 skill 只写 Repeat 流失如何回灌 Inquiry / Order 的优先级。不重写 health score 公式、触点日历或赢回步骤。缺产出则整章缺口。

工作簿 Retention Signals：`source` 必须是上述路径；禁止从本文件编造赢回正文。

| 字段 | 用途 |
| --- | --- |
| upstream_path | 已读留存稿路径（或「缺口」） |
| funnel_join | Repeat 流失回灌的阶段 |
| cross_stage_priority | P0 / P1 / P2 |
| source | 上游路径或「缺口」 |

### 实验优先级

每个想法写：hypothesis、漏斗阶段、metric、priority（P0/P1/P2）、effort（Low/Medium/High）、expected_impact 并带来源。无来源的提升幅度写「未验证」，禁止编造百分点。第 3–6 章实验只验证跨阶段矛盾是否成立，不定稿页面改法。第 9–11 章实验只排跨阶段优先级，不另起上市 / 转介绍 / 留存战役。

## 交付

根目录：`deliverables/marketing/05-cro/`。每条对外建议引用采集来源 URL。

### 主文档

`funnel-optimization.md`，12 章均须有内容或显式缺口：

1. **漏斗现状评估** — 分阶段转化与流失；未知标明；至少引用 3 个本站不同页面 URL
2. **竞品漏斗对比** — ≥3 家：落地/首页、表单、CTA、信任、流程
3. **落地页优化建议** — 对照已批准 `landing-page.md` 与已抓页，只填跨阶段矛盾与缺口；不重做 CTA / 标题
4. **询盘表单优化方案** — 对照已批准稿与已抓表单，只填字段 / 必填与下游的矛盾；不另起字段定稿
5. **弹窗与潜客捕获策略** — 对照已批准稿与已抓页，只填与主入口抢注意力的矛盾；不定稿弹窗
6. **询盘流程优化方案** — 对照已批准 `inquiry-flow.md`，资质量表以该稿七维四档为准；只填与入口 / onboarding 的矛盾
7. **首单 onboarding 方案** — 触点、样品政策、跟进
8. **升级与交叉销售策略** — 升级路径、报价结构、交叉矩阵
9. **发布上市计划** — 指向 `06-growth/launch-strategy.md`；只写跨阶段优先级；缺则缺口
10. **转介绍与合作伙伴计划** — 指向 `06-growth/referral-program.md`；只写跨阶段优先级；缺则缺口
11. **留存与流失预防策略** — 指向 `06-growth/retention.md`；只写跨阶段优先级；缺则缺口
12. **行动建议** — P0/P1/P2，每条有负责人和来源

已有该文件则增量更新，文首保留版本说明。

### 工作簿

复制 `templates/funnel-redesign.xlsx` 为 `funnel-redesign.xlsx`。禁止只交空模板。每行 `source` 非空。不能写表时改 `funnel-redesign.json`，数组对应下表，字段同列名。品类、市场、所在地从产品上下文填写，不留 `{{...}}`。

| Sheet | 最少行 | 列 |
| --- | --- | --- |
| Funnel Analysis | 7 | stage, current_rate, benchmark_rate, gap, primary_friction, priority_fix, source |
| Experiments | 15 | experiment_name, funnel_stage, hypothesis, metric, priority, effort, expected_impact, source |
| Page Audit | 5 | page_url, page_type, value_prop_score, cta_count, form_fields, mobile_score, issues, competitor_comparison, source |
| Form Benchmark | 5 | competitor_url, form_type, field_count, required_fields, cta_copy, response_promise, source |
| Launch Timeline | 15 | task, phase, timing, owner, deliverable, dependency, source |
| Referral Program | 5 | referrer_type, reward_model, commission_pct, agreement_type, enablement, source |
| Retention Signals | 8 | signal, risk_level, detection_method, timeframe, response_action, source |

填写约束：

- `current_rate` 无用户数据则空并在缺口说明，禁止填估计值冒充实测
- `benchmark_rate` 必须带来源，并在主文档标行业参考值
- `expected_impact` 无来源则写「未验证」，禁止编造百分点
- `cta_copy`、`response_promise` 用页面原文；无承诺写「未声明」
- `priority`：P0 / P1 / P2
- `source` 必须含可访问 URL
- 模板已有列名时以模板为准，并保证含 `source`
- Page Audit / Form Benchmark 引用 `landing-page.md` 与已抓页面，不另起 CTA 或字段定稿
- Launch Timeline / Referral Program / Retention Signals 引用对应 skill 既有产出路径，缺则缺口，不重写佣金或赢回正文

### 执行附件（按需，同目录）

对应主文档里有 P0 的切片才写，不空交。不替代已批准的 `landing-page.md`、`inquiry-flow.md` 或 `06-growth/` 下上市 / 转介绍 / 留存正文。

- `landing-page-audit.md` — 跨阶段矛盾（页 vs 已批准稿），不定稿 CTA
- `form-redesign-spec.md` — 字段矛盾与缺口，不另起字段定稿
- `popup-designs.md` — 与主入口冲突，不定稿文案
- `inquiry-flow-spec.md` — 与入口 / onboarding 的衔接缺口，不重写回复话术
- `onboarding-playbook.md` — 首单触点与模板要点
- `upsell-playbook.md` — 升级路径与报价话术要点
- `launch-timeline.md` — 引用 `launch-strategy.md` 的跨阶段优先级，不重写任务日历
- `referral-program-design.md` — 引用 `referral-program.md`，不重写佣金
- `retention-playbook.md` — 引用 `retention.md`，不重写赢回
- `ab-test-plan.md` — 带变体与指标的跨阶段实验

## 反模式

1. 套用试用开通、套餐升级、激活等 SaaS CRO 话术。
2. 不抓本站与竞品页面就给修改建议。
3. 忽略目标渠道的表单与页面限制。
4. 编造转化基准或回复时长，或不标行业参考值。
5. 目标市场需要即时通讯却完全不写入口策略。
6. 升级报价删掉基础选项。
7. 跟进只有客套问候。
8. 用 C 端网红带货或病毒 stunt 打 B2B 制造。
9. 一条报价推多个升级。
10. 任何交付物行的 `source` 为空。
11. 已有着陆页或询盘稿仍重做 CTA、字段或回复话术。
12. 把上市、转介绍、留存从零写一遍，而不引用对应 skill 产出。

## 质量闸门

- [ ] 本站首页 + 产品页 + 询盘页已抓取；落地页有则抓、无则缺口
- [ ] ≥3 个竞品完整漏斗含字段数、CTA 原文、信任信号
- [ ] 每条建议引用采集来源 URL
- [ ] 主转化保持询盘/订单，无试用开通话术
- [ ] 即时通讯策略按目标市场写，或缺的写缺口
- [ ] 已读已批准 `landing-page.md` 与 `inquiry-flow.md`（缺则缺口，未重做 CTA / 字段 / 回复话术）
- [ ] 第 3–6 章只填跨阶段矛盾与缺口；每条能指到已批准稿或已抓 URL
- [ ] 资质量表与询盘稿不一致处已注明以 `inquiry-flow.md` 七维四档为准
- [ ] onboarding 含样品政策与生产/质检触点
- [ ] 升级矩阵含基础选项 + 单一升级 + 项目说明
- [ ] 第 9–11 章指向 `marketing-launch-strategy` / `marketing-referral-program` / `marketing-retention` 既有产出或显式缺口；未重写佣金或赢回正文
- [ ] 工作簿七表达到最低行数；每行有带 URL 的 `source`（第 9–11 章表允许 `source` 为上游路径或「缺口」）
- [ ] 行业基准均标注「行业参考值，实际以你的数据为准」

## 可验证断言

交付物文末写 5–10 条。评审可用下列形状核对：

1. `funnel-optimization.md` 含 12 个必需章节（或显式缺口）
2. `funnel-redesign.xlsx`（或 json）含 7 张表且达到最低行数
3. 现状评估引用 ≥3 个本站不同页面 URL
4. 竞品对照 ≥3 行完整漏斗（落地 → 表单 → CTA → 信任）
5. 第 3–6 章每条矛盾 / 缺口能指到已批准 `landing-page.md` / `inquiry-flow.md` 或已抓页面；无重做的 CTA / 字段 / 回复话术
6. 第 9–11 章指向 `06-growth/` 既有产出路径或显式缺口；无重写的佣金或赢回正文
7. Experiments ≥15 行（或主文档列出 ≥10 个实验），每条有 hypothesis、metric、priority、effort
8. 每张表 `source` 非空率为 100%
9. 行业基准均带「行业参考值，实际以你的数据为准」
10. 终稿不存在未替换的 `{{...}}` 占位；SaaS 术语（free trial、premium plan、activation）出现次数为 0
