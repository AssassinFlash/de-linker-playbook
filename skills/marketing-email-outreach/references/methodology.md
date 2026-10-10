# 邮件外展方法

读本文件前先确认 `SKILL.md` 已判定本 skill 适用。查询意图、最低条数、框架槽位、序列规格与表结构以本文为准。

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

- `deliverables/marketing/01-foundation/` 价值主张、信息支柱、竞品角度
- 用户本轮提供的外展基线：打开率、回复率、样品申请率、转化率、现用外发/CRM

产品事实不写进 skill，不另写公司档案。品类、目标市场、产地/出运地只引用产品上下文对应字段，不在本文填值。

缺项列缺口后停。

## 采集

默认一条能力：用网页搜索查证。需要原文时抓取指定 URL 的正文。搜索不可用则停止并写缺口，不编造、不并列多引擎菜单。用户已配置网页采集服务时，可用它抓公开页。

联系人/邮箱发现服务仅当用户已配置；否则交付物标「联系人待补」，不编造、不导出发现用域名表充数。外发：用用户已配置的外发工具发信；未配置则只产出文案不发送。

多公司并行需要隔离时 dispatch a subagent, else do it inline。

### 查询意图

把产品上下文的品类与目标市场代入下列意图，每条记下 URL、摘录、访问日期：

1. 该品类 B2B 外贸/制造冷邮件做法
2. 该品类供应商高回复冷邮件结构（只采结构与原则，不把他人原文当己方模板）
3. 培育序列公开基准（打开率、回复率、点击率、转化率）
4. 送达率做法（SPF、DKIM、DMARC、域名预热）
5. 目标市场合规：GDPR（EU/UK）、CAN-SPAM（US）、CASL（加拿大），以及其他已列入上下文的区域

潜客与公司侧再搜：

6. 目标市场该品类的采购/指定/承包/经销决策人公开页
7. 目标公司近期项目、招聘、扩张、展会或公开招标信号
8. 目标渠道（以产品上下文为准）上的询盘或 RFQ 公开痕迹

### 潜客字段

每条潜客至少：

- name, title, company, public_profile_url（公开职业页或公司页）
- industry, company_size, location
- buying_signals（近期项目、招聘、扩张、展会）
- persona, priority, source

搜不到邮箱或直拨：标「联系人待补」，仍保留已核验的公开 URL。禁止编造 LinkedIn 或任何职业页 URL。

目标职称默认从产品上下文取。上下文未列时，在下列中选最贴近的一档并标明「角色未在上下文出现，暂用」：采购经理 / 采购总监 / 买家；项目经理 / 承包；指定人 / 设计负责人；开发或业主方；区域经销 / 寻源代理；电商或零售采购（仅当产品上下文列出该渠道）。

### 工具核验

用网页搜索查证公开可用的：邮箱核验、冷邮件/ESP、CRM 连接与触发、域名预热。不把未核验的工具写成已就绪。不写工具品牌 ID。未配置外发则基础设施节只写要求（SPF/DKIM/DMARC、预热、频率），不写「已接入某平台」。

### 最低数据量

进入分析前至少备齐；达不到的写入缺口，不降低后项装成已完成。

- **50** 条决策人潜客：真实可访问的公开 URL 与 `source`；邮箱未配置发现服务则标「联系人待补」
- **20** 家目标公司：购买信号与 `source`
- **5** 套冷邮件模板（按角色）：subject line、body、CTA、personalization hook、source
- **5** 条自动序列：trigger event、goal、timing、exit condition、source
- 基准数字带 source URL，或写「公开源未找到」
- 产品上下文每个目标区域一条合规说明

### 校验

- 禁止编造回复率、打开率、转化率
- 禁止编造潜客或职业页 URL
- 每个推荐模板能映射到一个已声明角色
- 引用 URL 抽查可访问；失败的列入缺口

## 分析

### 角色切分

按已采集潜客切角色。表列固定为：

| Persona | Pain Point | Value Angle | Primary CTA |
| --- | --- | --- | --- |

痛点、角度、CTA 必须能回溯产品上下文或已抓取页。禁止用通用供应商套话填空。主 CTA 从「要规格 / 要样品 / 要报价 / 要项目案例」里选一条，以该角色决策动作为准。

### 三层个性化

1. **公司层** — 已核验的项目宣布、招聘、公开帖、扩张新闻
2. **角色层** — 该职位在产品上下文中的痛点
3. **市场层** — 目标市场的语气（正式/直接）与合规预期

购买信号只记已观察项：采购/设计/项目招聘、新地点或翻新、公开项目或展会出席、目标渠道上的 RFQ。没有则该格写「公开源未找到」。

### 冷邮件框架

按情境选框架，交付物填槽位，不把教学句子写入成稿：

- **Project trigger → Capability → Proof → Ask**
- **Question → Value → Ask**
- **Trade show → Insight → Ask**
- **Portfolio → Bridge → Ask**

槽位：trigger（已核验信号）、capability（上下文有证据的能力）、proof（可核验项目或认证）、ask（一条 CTA）。缺 proof 就写缺口，不编案例。

### 主题行原则

- 默认建议：2–4 词，小写，无标点技巧
- 与项目或样品相关，不写产品推销
- 无紧迫感套路、无 emoji、不塞收件人名
- 内部备忘录感优于促销感
- A/B 变体可突破词数与大小写；仍须无促销口吻、无 emoji、不塞收件人名

### 生命周期序列

外贸漏斗地图（按产品上下文裁剪，缺段写缺口）：

```
Cold Prospect → Cold Email → Inquiry → Catalog Sent → Sample Requested
  → Sample Shipped → Sample Feedback → Bulk Order Quote
    → PO Received → Production Update → Delivery
      → Satisfaction Check → Repeat Order / Referral
```

至少设计五条；用户收窄则把未做的列入缺口：

1. **Inquiry Response** — Trigger: new inquiry。Goal: inquiry → sample request。5 封 / 14 天。
2. **Post-Sample** — Trigger: sample shipped。Goal: sample → bulk order。4 封 / 21 天。
3. **Post-Order Nurture** — Trigger: PO confirmed。Goal: 交付满意 → 复购 → 推荐。6 封 / 90 天。
4. **Re-Engagement** — Trigger: 静默 ≥90 天。Goal: 再激活。4 封 / 30 天。
5. **Trade Show** — Trigger: 已确认参展或展位到访。Goal: 预约会议 → 跟进线索。共 6 封。

每条序列（含用户收窄后仍交付的那些）须 ≥4 触点且价值角度不重复。此触点规则适用全部五条，不是另写一条跟进序列。

### 时序与合规

时序：

- 询盘自动回复：1 小时内
- 序列前期：间隔 2–3 天
- 序列中期：间隔 5–7 天
- 长期培育：隔周
- 避开已核官方源的当地假日；西方市场避开周五下午；中东市场避开周一上午（有来源才写，否则标「惯例、未核验」）

合规（按产品上下文已列区域输出；未列的区域不编造）：

| Region | Framework | Key Rules |
| --- | --- | --- |
| EU / UK | GDPR | Legitimate-interest 依据；每封有清晰 opt-out |
| US | CAN-SPAM | 物理地址；10 天内执行退订 |
| Canada | CASL | 明示或默示同意；同意约 2 年有效 |
| 其他 | 当地规范 | 无严格法时仍按 GDPR 级谨慎；须注明「非法律意见」 |

## 交付

主文档：`deliverables/marketing/04-acquisition/email-outreach/index.md`

必含：Target Buyer Analysis、Outreach Strategy、Cold Email Template Library、Automated Sequence Designs、Compliance Requirements、Sending Infrastructure Recommendations、Action Plan（P0 / P1 / P2）、缺口、可验证断言。每条建议引用采集来源 URL。

### 工作簿

从 `templates/prospect-research.xlsx`、`templates/sequence-builder.xlsx` 复制后填。不能写表时改同目录 JSON，列名保持一致。

1. `deliverables/marketing/04-acquisition/email-outreach/prospect-research.xlsx`
   - **Prospects** — `name, title, company, linkedin_url, industry, location, buying_signals, persona, priority, source`（`linkedin_url` 可改为任意已核验公开职业页 URL；无则「联系人待补」）
   - **Target Companies** — `company_name, industry, size, location, decision_makers, buying_signals, linkedin_url, website, priority, source`
   - 最低行数：50 / 20

2. `deliverables/marketing/04-acquisition/email-outreach/sequence-builder.xlsx`
   - **Sequences** — `sequence_name, trigger_event, target_segment, total_emails, duration_days, goal, exit_condition, expected_conversion, source`（`expected_conversion` 无公开源则「公开源未找到」）
   - **Email Steps** — `sequence_name, step_number, days_after_trigger, subject_line, email_type, body_framework, cta, personalization, conditional_logic, source`
   - **Variants** — `variant, persona, subject, body, test_metric, source`
   - 最低行数：5 / 25 / 3

每行 `source` 非空。禁止只交空模板。

### 执行附件（按需同目录）

用户未收窄则尽量交齐；收窄则把未做文件列入缺口：

- `email-templates.md` — 按角色的完整冷邮件
- `subject-line-variations.md` — 每套模板 5–10 条主题行变体
- `outreach-sequence.md` — 冷潜客跟进节奏
- `sequence-flows.md` — trigger、封数、间隔、分支、exit
- `trigger-events.md` — trigger 定义与 entry/exit
- `automation-setup.md` — 平台选择（仅已核验可用）、trigger 配置、发送频率
- `personalization-guide.md` — 按行业/项目类型的插入点
- `prospect-criteria.md` — 目标公司筛选规则

策略说明用简体中文；URL、schema 字段、CTA 用 English。

## 反模式

1. 编造打开率、回复率或转化率。
2. 编造潜客或职业页 URL。
3. 用通用供应商模板，不贴角色与品类证据。
4. 忽略 GDPR / CAN-SPAM / CASL。
5. 未核验可用性就推荐外发工具。
6. 用 Dear Sir/Madam 或 I hope this email finds you well 开头。
7. 同一套模板打不同角色。
8. 序列无 trigger 与 exit。
9. 一封邮件多条主 CTA。
10. 终稿残留 `{{...}}` 占位。
11. 未配置外发工具却记录为已发送。

## 质量闸门

- [ ] ≥50 潜客有真实公开 URL 与 `source`，或缺口已写明
- [ ] ≥20 家目标公司有购买信号与 `source`
- [ ] 5 套按角色的冷邮件模板
- [ ] 每条基准数字有 source URL 或「公开源未找到」
- [ ] 5 条自动序列含 trigger、goal、exit
- [ ] 询盘自动回复为 1 小时内第 1 步
- [ ] 每封邮件一条主 CTA
- [ ] 每个目标区域有合规说明
- [ ] 发送基础设施建议已对照公开可用性；未配置则未发送
- [ ] 主题行通过内部备忘录测试（默认 2–4 词小写；A/B 可变）
- [ ] 五条生命周期序列每条 ≥4 触点且角度不重复（适用全部序列，不是另写跟进）
- [ ] 目标市场若惯用即时通讯，已注明备选入口
- [ ] 终稿无未替换占位符

## 可验证断言

交付物文末写 5–10 条。评审可用下列形状核对：

1. `prospect-research.xlsx` 的 Prospects ≥50 行，`source` 非空率 100%
2. Target Companies ≥20 行，`buying_signals` 非空率 100%
3. `email-outreach/index.md` 含 ≥5 套按角色的模板，每套含 subject line、body、CTA
4. Sequences ≥5 行，每行含 `trigger_event`、`goal`、`exit_condition`
5. Email Steps ≥25 行，每步含 `days_after_trigger`、`subject_line`、`cta`
6. 基准数字无 source 的条目数为 0
7. 终稿无未替换的 `{{...}}`
8. 产品上下文涉及的每个 region 均有合规说明
9. 多 CTA 邮件数为 0
10. 跟进序列中重复 value angle 的 step 数为 0
