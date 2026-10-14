# 分析与优化方法

读本文件前先确认 `SKILL.md` 已判定本 skill 适用。查询意图、最低条数、事件分级、实验分档、管道与表结构以本文为准。

## 目录

- [输入](#输入)
- [采集](#采集)
- [分析](#分析)
- [交付](#交付)
- [反模式](#反模式)
- [质量闸门](#质量闸门)
- [可验证断言](#可验证断言)

## 输入

先读事实源入口 `docs/fact-sources.md`（台账 `product_context` 即指向它），按其「什么问题查哪个源」取证；查不到标〔未证实〕，按没有处理。上游若已存在则读：

- `deliverables/marketing/02-seo/site-and-schema.md` 站点结构与转化页
- `deliverables/marketing/04-acquisition/` 付费与邮件战役、已有 UTM
- `deliverables/marketing/05-cro/` 落地页与漏斗摩擦

动手前确认（未知则记缺口，不编造）：

1. 现有分析状态 — GA4 媒体资源是否安装、GTM 容器是否上线、已有事件
2. 在用渠道 — 仅产品上下文已列出者（付费搜索、展会、开发信、社媒、直访、目标渠道中的市场平台等）
3. 转化目标 — 询盘量、渠道归因、样品申请、或复购
4. 流量现实 — 月独立访问、当前询盘/样品基线
5. 销售作业 — CRM 或表格、即时通讯、团队规模、询盘最常变冷的阶段
6. 站点表单（联系、询盘、样品）、客单价与销售周期、目标市场、是否需要把转化回传给已开通的付费账户

产品事实不写进 skill，不另写公司档案。品类、目标市场、产地、展会名只引用产品上下文对应字段，不在本文填值。

缺项列缺口后停。

## 采集

默认一条能力：用网页搜索查证。需要原文时抓取指定 URL 的正文。搜索不可用则停止并写缺口，不编造、不并列多引擎菜单。多页并行时 dispatch a subagent, else do it inline。

### 本站测量面

抓取并摘录：

1. 首页 — 页面源码中的 GA4/GTM 痕迹、主 CTA
2. 询盘/联系表页 — 字段、提交触发、成功态
3. 产品目录或规格下载页 — 高意向资产与下载触发

### 查询意图

把产品上下文的品类与目标市场代入下列意图，每条记下 URL、摘录、访问日期：

1. 该品类 B2B 站点 GA4 / GTM 事件设置（当前或下一自然年）
2. B2B 询盘追踪事件分级
3. 低流量 B2B 制造站点 A/B 测试做法
4. 询盘到订单的 RevOps 管道与 CRM
5. 外贸询盘转化率公开基准（只作参考，不写成用户目标）
6. 低流量贝叶斯或 90% 置信实验方法

结果不够时再补同一能力，不换工具品牌。

### 最低数据量

进入分析前至少备齐；达不到的写入缺口，不降低后项装成已完成。

- 已确认的站点表单清单：名称、URL、字段、成功行为
- 已确认在用渠道（供 UTM 与渠道分组）
- 现有 GA4/GTM 状态：已安装 / 部分 / 无
- 目标市场与主要买家角色
- 月访问量与当前询盘/样品基线；未知则整项记缺口，实验按定性档
- 当前销售工具与团队规模
- 询盘最常变冷的阶段

### 校验

- 每个事件映射到本站真实页面元素或用户动作
- UTM 只覆盖实际在用渠道
- 转化价值无观测则标 `[YOUR_VALUE]`，禁止编造
- 管道转化目标无观测则标 `[YOUR_TARGET]`，公开基准只作参考并标明「行业参考值，实际以你的数据为准」
- 每条建议引用采集来源（URL 与访问日期）

## 分析

### 漏斗映射

测量对齐这条漏斗。`inquiry_form_submitted` 是主转化，对应零售场景里的成交，除非产品上下文确认站点有直销成交。

```
AWARENESS → INTEREST → INTENT → CONVERSION → RETENTION
page_view → product_page_viewed → catalog_downloaded → inquiry_form_submitted → repeat_inquiry
                   │                      │
             即时通讯点击            sample_requested
                   │
             video_played
```

即时通讯事件仅当产品上下文已出现对应入口时写入；未出现则记缺口，不编造点击。

### 事件分级

**Tier 1 — 转化**

| Event | Trigger | Key Parameters |
| --- | --- | --- |
| `inquiry_form_submitted` | 询盘/联系表成功 | `form_type`, `product_interest`, `source_channel` |
| `sample_requested` | 样品表成功 | `product_sku`, `product_category`, `source_channel` |
| `whatsapp_clicked` | 即时通讯按钮点击（仅已确认入口） | `click_location`, `page_path` |
| `phone_number_revealed` | 「显示号码」交互 | `page_path` |

**Tier 2 — 高意向**

| Event | Trigger | Key Parameters |
| --- | --- | --- |
| `catalog_downloaded` | PDF/规格下载 | `catalog_name`, `product_category` |
| `product_page_viewed` | 产品详情加载 | `product_name`, `product_category`, `application_type` |
| `quote_cta_clicked` | 要报价 / 要定价 CTA | `product_name`, `cta_location` |
| `media_gallery_viewed` | 图库或规格表交互 | `product_name`, `items_viewed` |

**Tier 3 — 参与**

| Event | Trigger | Key Parameters |
| --- | --- | --- |
| `scroll_depth` | 25/50/75/100% 滚动 | `depth`, `page_path` |
| `video_played` | 产品或工厂视频开始 | `video_title`, `page_path` |
| `outbound_link_clicked` | 点到市场店面或社交主页 | `link_url`, `link_text` |

**全部事件的标准属性**

| Category | Properties |
| --- | --- |
| Product | `product_name`, `product_category`, `application_type`, `material_grade` |
| Source | `source_channel`, `utm_source`, `utm_medium`, `utm_campaign` |
| Lead | `form_type`, `buyer_type`, `buyer_region` |
| Geography | `visitor_region` |

命名：`object_action`，小写加下划线。参数不含 PII。表中事件若本站无对应元素则删除该行，不保留空事件。先让 Tier 1 打通再配 Tier 2/3。同一表单提交禁止重复事件。

### UTM 与渠道分组

只为产品上下文已确认的渠道填行。小写，空格改下划线。部署前写入二维码与邮件签名。

| 渠道 | `utm_source` | `utm_medium` | `utm_campaign` 形状 |
| --- | --- | --- | --- |
| 搜索广告 | `google` | `cpc` | 品类字段_年份 |
| 展示广告 | `google` | `display` | 目标市场字段_segment_年份 |
| 目标渠道中的市场平台 | 该平台约定标识 | `marketplace` | `storefront` |
| 展会二维码 | 产品上下文中的展会名称 | `trade_show` | 季节_年份 |
| 开发信 | `cold_email` | `email` | 目标市场字段_procurement_季度 |
| 职业社交 | `linkedin` | `social` | 活动名_月份 |

未确认的渠道整行删除。`utm_campaign` 形状里的品类、市场、展会名从产品上下文取，不在 skill 里填值。

**GA4 自定义渠道分组**（同样只留已确认渠道）：

| Channel | Condition |
| --- | --- |
| Marketplace | `utm_medium` 精确匹配 `marketplace` |
| Paid Search | `utm_medium` 精确匹配 `cpc` |
| Trade Show | `utm_medium` 精确匹配 `trade_show` |
| Email | `utm_medium` 精确匹配 `email` |
| Organic Search | 默认 |

### 再营销受众

角色从产品上下文取；上下文没有则标明「角色未在上下文出现，暂用」。

| Audience | Signal | Remarketing Content |
| --- | --- | --- |
| 指定/设计 | 看应用页、下设计目录 | 设计向内容 |
| 采购 | 看批量/项目页、提交询盘 | 价格/交期内容 |
| 开发/终端 | 看案例、页深高 | 项目证据 |
| 经销 | 多品类回访 | 合作/MOQ 内容 |

### 低流量实验分档

B2B 站点月访问常低于 1,000。先按已观测月访问量分档；未知则按定性档，并写缺口。

| 月访问 | 做法 |
| --- | --- |
| < 300 | 仅定性：热图、会话回放、买家访谈 |
| 300–800 | 贝叶斯 A/B，90% 置信；预期 8–16 周 |
| 800–2,000 | 常规 A/B，90% 置信；4–10 周 |
| > 2,000 | 常规 A/B，95% 置信；常规周期 |

低流量规则：90% 置信、优先贝叶斯、接受 ≥20% MDE、最少 4 周、始终 50/50。月访问低于 1,500 时不做 3+ 变体。假期或大型展会周不开测。数据变好也不提前停测。

样本量用本站已观测基线算，不用行业平均冒充本站基线。

### 假设结构

每条假设写成：

```
Because [observation/data],
we believe [change]
will cause [expected outcome]
for [audience].
We'll know this is true when [primary metric].
```

预期升幅无观测区间时写待填，不编造百分点。

### 默认测试方向

仅当对应页面元素在本站已确认存在时列入队列。P0 适合低流量 B2B；P1 在 P0 完成后再测。

**P0**

| Test | Control | Variant | Primary Metric | Best Persona |
| --- | --- | --- | --- | --- |
| 主视觉：安装现场 vs 棚拍 | 棚拍产品图 | 目标市场的已安装项目照 | 询盘表点击率 | 指定人 |
| CTA 文案 | Contact Us | Request Free Sample | CTA 点击率 | 全角色 |
| 信任标识位置 | 认证只在页脚 | 认证贴在 CTA 旁 | CTA 点击率 | 采购 |
| 询盘表长度 | 8 字段 | 5 字段（name, email, country, product, message） | 提交率 | 全角色 |
| 产品系列画廊 | 单主图 | 系列/规格网格 | 画廊到询盘点击 | 指定人 |
| 技术强调 | 利益向文案 | 规格向文案 | 询盘提交率 | 工程师/指定人 |

**P1**：价格展示布局、样品申请流、产品页布局。

### 指标分层

- **Primary**：绑定假设的单一指标（询盘提交率等）
- **Secondary**：解释路径（CTA 点击率、滚动深度）
- **Guardrail**：显著变差则停（跳出率、线索质量）

### ICE

Impact / Confidence / Ease 各 1–10。低流量站加重 Ease：需要约 6 个月才出结果的实验，即使 Impact 高也不标 P0。

### RevOps 阶段

| Stage | Entry Criteria | Exit Criteria | Typical Duration | Owner |
| --- | --- | --- | --- | --- |
| New Inquiry | 任一渠道收到 | 已确认收到并完成初评 | 当日 | 销售 / 助理 |
| Qualified Inquiry | 项目匹配与意向确认 | 样品或拜访确认 | 1–5 天 | 销售 |
| Sample Stage | 样品费与规格确认 | 样品已发、反馈到期 | 7–21 天 | 销售 |
| Bulk Quote | 规格、数量、目的港确认 | 正式报价已发并已审 | 3–10 天 | 销售 / 负责人 |
| Order Confirmed | PI 已签、定金到 | 已投产 | 1–3 天 | 负责人 |
| In Production | 生产单已下 | 质检通过待发 | 按交期 | 生产 |
| Shipped | 提单号、ETD、ETA 确认 | 买方确认收货 | 按航程 | 销售 |
| Delivered | 交付确认、反馈已记 | 启动复购跟进 | 7 天内 | 销售 |
| Closed Lost | 已记丢失原因 | 丢失后备注已写 | — | 销售 |

每阶段必须有进入条件、退出条件、具名负责人。阶段定义尚未手工跑通，不上自动化。

### 线索评分

**显性（匹配）**

| Signal | Score | Category |
| --- | --- | --- |
| 买家类型匹配 ICP | +15 | Fit |
| 主市场匹配产品上下文的目标市场 | +10 | Fit |
| 已能核实的在营企业 | +8 | Fit |
| 项目类型匹配核心供给 | +10 | Fit |

**隐性（意向）**

| Signal | Score | Category |
| --- | --- | --- |
| 询盘含具体规格 | +15 | Intent |
| 数量贴近 MOQ | +10 | Intent |
| 点名具体产品 | +8 | Intent |
| 愿意支付样品 | +10 | Intent |
| 资质问题回复快 | +8 | Intent |

**负向**：跟进后仍无项目细节（−15）、数量远低于 MOQ（−10）、目的港含糊（−10）、只问价格（−8）。

合格询盘阈值：`[YOUR_THRESHOLD]`。每 6 个月用 ≥5 条真实历史询盘校准。无历史则阈值保持待填，不编造。

### 响应时效

| 首次实质回复 | 位置 |
| --- | --- |
| 工作时间内 < 4 小时 | 优势 |
| 4–24 小时 | 可接受 |
| > 24 小时 | 偏冷 |
| > 48 小时 | 接近丢失，除非项目仍早 |

表内数字是作业标准，不是编造的本站实测；本站实测另行列出或标未知。

### CRM 选型

| Option | Best For | Limitations |
| --- | --- | --- |
| HubSpot Free/Starter | 3–10 人、要管道报表与自动化 | 至少 1–2 小时配置 |
| 即时通讯 + 表格 | 1–3 人、立刻开记 | 活跃询盘 >30 时容易散 |
| 单一市场渠道自带 CRM | 约 80% 询盘来自该渠道 | 多渠道差、无自动化 |

1–3 人且尚未追踪：从即时通讯 + 表格起。月询盘超过 30 或团队超过 3 人：再迁到 HubSpot Free 档。禁止把企业套件推荐给 1–5 人团队。

### 管道指标

| Metric | Formula | Target |
| --- | --- | --- |
| Inquiry-to-QI rate | 合格询盘 / 全部询盘 | `[YOUR_TARGET]`（参考 20–40%，只作参考） |
| QI-to-sample rate | 已发样品 / 合格询盘 | `[YOUR_TARGET]`（参考 40–60%） |
| Sample-to-order rate | 确认订单 / 已发样品 | `[YOUR_TARGET]`（参考 30–50%） |
| Avg response time | 询盘到达 → 首次实质回复 | < 4 小时（作业标准） |
| On-time delivery rate | 按约定交期送达 / 全部订单 | `[YOUR_TARGET]`（参考 >90%） |
| Repeat order rate | 2+ 次下单买家 / 全部买家 | `[YOUR_TARGET]`（参考 >30%） |

### 交付后跟进

1. 7 天内确认收货
2. 问质量、包装、沟通
3. 30 天内同步新品或季节更新
4. 无新询盘则设 60 天回访
5. 第二次确认订单后在 CRM 标 Repeat Customer

## 交付

路径根：`deliverables/marketing/07-measurement/`。所有文件必须对应采集阶段确认的站点、渠道和销售工具。

### 主文档

`analytics-and-optimization.md` 必含：

1. **现状审查结论** — GA4/GTM 状态、表单清单、数据质量
2. **事件分级方案** — Tier 1/2/3：名称、触发、参数、GA4/GTM 配置
3. **UTM 参数体系** — 仅已确认渠道的模板
4. **GA4 配置清单** — 自定义维度、转化事件、渠道分组、受众
5. **GTM 配置清单** — Tag / Trigger / Variable 与参数
6. **A/B 测试优先级队列** — ICE 假设、样本量、周期、成功标准
7. **统计方案** — 频率派 vs 贝叶斯、置信、MDE
8. **RevOps 管道定义** — 阶段、进出条件、负责人、时效
9. **线索评分与路由规则** — 模型、阈值、路由
10. **指标看板规格** — 销售视图 + 管理视图字段与筛选
11. **行动建议** — P0 / P1 / P2，指向执行附件
12. **缺口**
13. **可验证断言**

每条建议必须写到可配置，不只写「安装 GA4」或「上 CRM」。

### 工作簿

从 `templates/analytics-and-optimization.xlsx` 复制后填。不能写表时改同目录 JSON。

| Sheet | Columns |
| --- | --- |
| Event Taxonomy | `event_name`, `category`, `trigger`, `parameters`, `ga4_event_name`, `gtm_tag`, `priority`, `source` |
| Experiment Queue | `experiment_id`, `page`, `hypothesis`, `variant_a`, `variant_b`, `primary_metric`, `sample_size`, `duration_weeks`, `ice_score`, `priority`, `source` |
| Pipeline Stages | `stage`, `entry_criteria`, `exit_criteria`, `expected_duration`, `conversion_rate`, `automation`, `owner`, `source` |
| Lead Scoring | `signal`, `score_points`, `category`, `data_source`, `weight`, `source` |
| KPIs | `metric`, `formula`, `target`, `frequency`, `data_source`, `source` |

最低行数：15 事件、8 实验、8 管道阶段、12 评分信号、10 KPI。每行 `source` 非空。禁止只交空模板。

### 按需附件

- `event-taxonomy.md` — 事件定义与 GA4/GTM 步骤
- `utm-parameter-system.md` — 命名、渠道模板、URL 生成规则
- `tag-manager-config.md` — Tag / Trigger / Variable
- `test-queue.md` — ICE 列表
- `test-specs.md` — 前 3 条：control/variant、样本量、周期、成功标准
- `pipeline-stages.md` — 阶段定义与作业说明
- `lead-scoring-model.md` — 维度、权重、阈值
- `crm-setup-guide.md` — 工具、字段、管道、自动化（自动化仅在阶段已手工跑通后）
- `dashboard-specs.md` — GA4 自定义报告或 Looker Studio 字段与筛选

## 反模式

1. 未确认站点有无直销成交就关掉电商追踪。
2. 编造转化价值、询盘价值或管道基准后写成事实。
3. 把企业 CRM 推荐给 1–5 人团队。
4. 为未使用渠道造事件或 UTM。
5. 月访问低于 1,500 时跑 3+ 变体。
6. 数据变好就提前停测。
7. 在假期或大型展会周开测。
8. 跳过资质、把所有询盘同等处理。
9. 阶段定义尚未手工跑通就上自动化。
10. 只追踪单一市场渠道询盘。
11. 任何交付物行的 `source` 为空。

## 质量闸门

- [ ] 每个事件映射到本站已确认元素
- [ ] Tier 1 打通后再配 Tier 2/3；同一提交无重复事件
- [ ] UTM 只覆盖已确认渠道
- [ ] 已写排除办公网 IP
- [ ] 转化价值无观测则标 `[YOUR_VALUE]`
- [ ] 流量分档与实验方法一致；月访问未知则定性档 + 缺口
- [ ] 每条假设符合结构模板
- [ ] 样本量来自本站基线或已标明未知
- [ ] 实验周期含最少 4 周
- [ ] 每条实验有 primary / secondary / guardrail
- [ ] 管道覆盖 New Inquiry 到 Repeat 跟进，含 Closed Lost
- [ ] 每阶段有进出条件与具名负责人
- [ ] 评分模型对照 ≥5 条真实历史询盘，或阈值保持待填
- [ ] CRM 建议匹配团队规模
- [ ] 交付后跟进已写出
- [ ] 每条建议引用采集 URL
- [ ] 每个工作表有 `source` 列且无空值

## 可验证断言

交付物文末写 5–10 条。评审可用下列形状核对：

1. `analytics-and-optimization.md` 位于 `deliverables/marketing/07-measurement/`
2. 工作簿含 5 表：Event Taxonomy、Experiment Queue、Pipeline Stages、Lead Scoring、KPIs
3. 行数分别 ≥15 / ≥8 / ≥8 / ≥12 / ≥10，且每行 `source` 非空
4. 每个已确认的 Tier 1 事件写了触发、关键参数与对应 GTM tag；本站无该元素则显式删除并记缺口
5. 每条 A/B 假设遵循 Because → believe → will cause → for → We'll know，并标三层指标
6. 实验队列每条含 ICE、预计样本量、最少 4 周
7. RevOps 管道覆盖 New Inquiry 到 Closed Lost，每阶段有进出条件与具名负责人
8. 货币数值、转化率目标、阈值无观测时为 `[YOUR_VALUE]` 或 `[YOUR_TARGET]`，无编造数字
9. UTM 仅覆盖采集中确认在用的渠道
10. 每条策略建议引用采集来源 URL 与访问日期；抽 20% URL 可访问比例应 ≥80%，否则列入缺口
