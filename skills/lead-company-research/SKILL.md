---
name: lead-company-research
description: >
  Use when building prospect lists, researching target companies, finding
  B2B customers, creating company shortlists, or when the user mentions
  company list, target companies, prospect list, company research, emerging
  companies, company profiling, find companies, 公司名单, 目标公司, 公司调研,
  潜在客户, or 新兴公司. Profile ICP-matched buyers with three blocks: domain,
  buying behavior, and decision process. Standard mode writes
  target-companies; emerging mode (under 200 employees, growth signals, no
  overlap) is this skill's second deliverable, not a second entry. Read
  ledger product_context; invent no companies or volumes. Not for
  distributor or retailer lists, contact scraping, or phase navigation.
---

# 目标公司调研

按已批准 ICP 与搜索词找出可核验的买方公司，每家写满三信息块，落到 `deliverables/lead/02-companies/`。新兴名单是同一入口的第二种交付物，不要另开入口。

## 步骤

1. **输入**。读 `skills/marketing-playbook-standards/SKILL.md`。读台账 `state/status.md` 的 `product_context`（默认 `~/Documents/New/CONTEXT.md`；把 `~` 展开为主目录）。存在则读 `deliverables/lead/01-icp/icp-analysis.md` 与已批准的 `deliverables/lead/01-icp/icp-terms.xlsx`。记下品类、选定 ICP、地域、定位词。硬依赖是已批准的搜索词表；未批准且无台账 `user_waiver` → 停，打开 `skills/lead-search-term-expansion/SKILL.md`（文件存在时）。产品上下文与上游仍不够清楚时，打开 `skills/lead-interview/SKILL.md` 并按其做（访谈须 inline）；该文件不存在则把缺口写入台账，不自造问卷。原文不拷进本仓库。完成：能指出买家类型、地域与将使用的定位词各依据哪几条；缺核心项已停或已标缺口。

2. **定模式**。从用户本轮消息或访谈上下文取 `standard` 或 `emerging`；未指定则 `standard`。用户点名新兴公司、emerging、员工数上限时走 `emerging`。两种模式都要时：先标准名单落盘，再做新兴，仍用本文件，不另起 skill。`emerging` 的额外约束读 `references/emerging-mode.md`。完成：交付物抬头已写模式；新兴已核对其对标准名单的硬依赖或 `user_waiver`。

3. **发现**。用网页搜索查证，查询取已批准术语表的 `positioning_term`、`company_type`、地域，轮换组合直到名单达标或术语用尽。共用查询骨架见 `skills/lead-generation/references/search-protocol.md` 的「公司发现」。只收录本次搜索命中的公司，不用训练记忆填名单。排除：目录站与交易平台列表页、与用户同品类的卖方竞品、B2C 零售（零售走 `lead-retailer-research`）、地域不符。目标 10 家可核验公司；术语用尽仍不足 → 报告实际数量，不补假公司。完成：候选表每家有待核验域名与来源查询；数量是搜索所得，不是凑数。

4. **三块采集**。对每家候选：抓取指定 URL 的正文核验官网；再搜并抓取 About / 采购 / 供应商品页（有则抓）。按 `references/three-info-blocks.md` 填三块：域名、采购行为、决策流程。多家并行且需要隔离时 dispatch a subagent, else do it inline。域名抓取失败：换一次查询或按 `skills/lead-generation/references/manual-intervention-protocol.md` 请用户接手；仍不可达 → 不入名单，换下一家。搜索不可用 → 停止并写缺口，不编造。完成：入选每家三块都有；每块能指回 URL 或已标明「未在来源出现」；`url_verified` 为已抓取可达。

5. **质检**。对照选定 ICP；采购行为描述不得在两家之间可互换；年采购量无公开代理则不得写成事实；决策人有公开姓名才写姓名，否则写职能并标缺口。剔除不可达域名、错地域、卖方竞品、B2C 零售。新兴模式另跑 `references/emerging-mode.md` 的重叠与增长信号检查。完成：清单项可逐条勾；被剔除的公司留在搜索日志，不充行数。

6. **落盘**。标准：`deliverables/lead/02-companies/target-companies.md` 与同列 `target-companies.xlsx`（或 csv）。新兴：`emerging-companies.md` 与 `emerging-companies.xlsx`（或 csv）。用下方模板。分析用中文；列名 English snake_case；公司名不翻译。完成：主报告非空；表行列与入选公司一致；含 `## 搜索日志`；教学例子原文零出现。写入后的验证—审查—审批走 `skills/lead-generation/references/orchestration-protocol.md`，本 skill 不自造闸门。

## 默认

- 查证用网页搜索；需要原文时抓取指定 URL；动态页同样抓取；失败则人工接手，不用模型记忆填字段。
- 产品事实只读台账 `product_context`（默认 `~/Documents/New/CONTEXT.md`）。
- 联系人/邮箱发现服务、网页采集服务：仅当用户已配置（付费项须先告知并获准）。本 skill 不采集邮箱；下游打开 `skills/lead-contact-discovery/SKILL.md`。
- 分销商 11 维、零售商规模定位不是本 skill；平行入口是 `lead-distributor-research`、`lead-retailer-research`。
- 单文件、无并行机会的工作 inline 做完，不 dispatch。

## 写法

- 三块都要作为章节存在；缺数据写「未在来源出现」或带依据的估算，不删章节、不编数字。
- 估算必须同时有：公开代理（招标量、产能、门店数、披露支出等）、推理一句、`confidence: low`。没有代理就不要估。
- 每家采购行为必须能把该公司与名单中其他公司分开。写不出差异就回去抓页，不要用套话交差。
- 标准模式优先成长期买方，不要只堆行业巨头；匹配 ICP 的较大买方可以入选。员工数上限与增长信号只约束新兴交付物。
- 新兴 ≠ 查不到。查不到公开页的公司不入选。

## 产出

标准主文件 `deliverables/lead/02-companies/target-companies.md`：

```markdown
# 目标公司名单 — {品类} × {地域} × {ICP}

- source: 台账 product_context（不粘贴原文）
- mode: standard
- icp:
- accessed:
- companies_n:

## 公司概览

### {company_name}
#### 域名
（官网 URL；抓取结果）
#### 采购行为
（年采购量或「未在来源出现」；供应商偏好及依据）
#### 决策流程
（参与职能；选择标准；影响因素）

## 搜索日志
| # | Capability | Query/URL | Results | Useful | Notes |
|---|------------|-----------|---------|--------|-------|
```

表列：`company_name, domain, country, employee_count, industry, annual_purchase_estimate, buying_behavior, supplier_preferences, decision_makers, selection_criteria, icp_category, data_source, url_verified, notes`

新兴列与路径见 `references/emerging-mode.md`。目标行数 10；不足则 `companies_n` 写实数并在缺口说明术语已用尽。

## 例子

> 仅供理解，禁止引用到输出。

采购行为不要写成「重视质量与价格」。应写成可核对的观察：公开招标附件要求某类证书、现有供应商名能在已抓取页核对。数字与供应商名必须来自该页。

新兴模式：员工数来自已抓取页且低于 200，并写一条带 URL 的增长信号（融资、扩招、新品或进入新市场）。不要把标准名单里的公司换表述再列一遍。

域名不可达：从名单删除并换下一家，不要留 `url_verified=false` 充目标行数。

## 易错

- 用训练记忆生成公司名，而不是本轮搜索命中。
- 搜不够 10 家就编造凑行。
- 把目录站、交易平台列表页当成目标公司。
- 把用户的同品类卖方竞品当成买家。
- 三块套话可互换，或无代理的年采购量写成事实。
- 把新兴当成另一个 skill 入口。
- 未读搜索词表或 ICP 就开搜。
- 本 skill 里编造邮箱或联系人。
- 把 skill 例子原文写入交付物。

## 清单

- [ ] 已读 `product_context` 与已批准搜索词；硬依赖或 `user_waiver` 已满足
- [ ] 模式已写进抬头；新兴未另起入口
- [ ] 入选公司均来自本轮搜索；数量未经编造凑齐
- [ ] 每家三块齐全；域名已抓取可达
- [ ] 采购行为彼此不可互换；无来源数字未写成事实
- [ ] 新兴若跑：员工数、增长信号、与标准名单不重叠均已查
- [ ] 搜索日志有查询/URL 与日期；例子原文未进入交付物
- [ ] 文件在 `deliverables/lead/02-companies/`
