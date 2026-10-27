---
name: lead-contact-discovery
description: >
  Use when finding buyer contacts, collecting decision-maker emails,
  building contact lists, 联系人采集, 采购邮箱, 找联系方式, 邮箱采集,
  contact discovery, find contacts, buyer email, procurement manager
  email, sourcing manager, decision-maker contacts, email finder,
  contact list, Snov.io, Apollo, or Hunter, including phase 3 of this
  repo's lead run. Read approved ICP and at least one company list;
  verify with web search then fetch contact-page URLs; use a contact
  or email finder service only if already configured, else mark
  联系人待补. Tag every row by ICP, company type, and job title. Not
  for outreach copy or company research itself.
---

# 联系人采集

从已批准的 ICP 与公司名单采集决策人的公开商务联系方式，按 ICP / 公司类型 / 职位分列，写入 `deliverables/lead/03-contacts/`。查证顺序与置信度见 `references/lookup-protocol.md`；已配置发现服务时的批量补全见 `references/contact-finder-workflow.md`。

## 步骤

1. **输入**。产品与公司事实读事实源入口 `docs/fact-sources.md`，按其「什么问题查哪个源」取证；查不到标〔未证实〕，按没有处理。硬依赖：已批准的 `deliverables/lead/01-icp/icp-analysis.md`，以及 `ANY(deliverables/lead/02-companies/target-companies.xlsx, deliverables/lead/02-companies/distributors.xlsx, deliverables/lead/02-companies/retailers.xlsx)`（有对应 `.md` 也可）。软依赖存在则读：`deliverables/lead/02-companies/emerging-companies.xlsx`、其余公司名单。职位、每家人数、名单范围、质检标准仍不清时，打开 `skills/lead-interview/SKILL.md`（存在则按其做）；不存在则把缺口写入台账，不自造访谈。完成：能指出买家角色与目标公司名单各依据哪份已批准文件；原文不拷进本仓库。硬依赖未满足且无 `user_waiver` → 停。
   - **名单公司**（激活名单里、已按 `skills/lead-company-research/references/list-mode.md` 调研的公司）：联系人以名单为准。硬依赖换成这家的调研文件 `deliverables/lead/02-companies/activation/<list_id>.md` 为 `approved` 且 `list_verdict: 可接触`（按陌生开发：先调研再接触）；ICP 是软依赖，没有已批准的 ICP 就进 sheet `unassigned`。联系人从 `uv run scripts/activation_list.py show --id <list_id>` 取，每位一行，`data_source` 写「激活名单 <list_id> 原件第 n 行」，名单给的邮箱照录（免费邮箱也照录，在采集概况里列出是哪几行）；`job_title` 名单没有就从公开页查证，查不到写「待补」。不另找名单以外的人，除非操作者点名要。公司名照名单原文。名单只在私有 vault，联系人不进公开仓库。

2. **编域名**。从已读名单抽出 `company_name, domain, icp_category, company_type`。无已验证域名的公司不进采集表，记入失败分析。域名去重。用户或访谈限定了 ICP / 公司类型则只保留该子集。完成：目标域名表非空；若无可用域名，跳到步骤 7，报告只写失败分析，不编造联系人。

3. **定范围**。缺省职位（可被 ICP 或本轮消息覆盖）：Buyer, Procurement Manager, Sourcing Manager, Supply Chain Manager, Category Manager, Owner, CEO, VP of Purchasing, Director of Procurement。每家至少落一行；用户指定人数则以其为准。完成：本轮职位列表与人数上限写进采集概况，不在过程中改口径。

4. **公开页查证**。对每个域名：用 Apify 搜索查证，再抓取指定 URL 的正文（联系页 / About / Team，含动态页）。查询与通过标准见 `references/lookup-protocol.md`。Apify 修复与替代取证后仍不可得 → 停止并写缺口，不编造。同一站点限流或验证码 → 停止对该域的抓取，记入搜索日志，不循环硬试。公司多、需隔离时按 ICP 或域名批 dispatch a subagent, else do it inline；单家 inline。完成：每个目标域名有搜索日志；找到的联系人能指回已抓取页。

5. **发现服务**。仅当用户已配置联系人/邮箱发现服务时，按 `references/contact-finder-workflow.md` 补邮箱。付费项须先告知并获准。未配置或未批准 → 缺邮箱的字段标「联系人待补」，不编造，不导出发现用域名表。已配置且本侧可调用 → 调用后合并。已配置但须用户在控制台操作 → 导出 `deliverables/lead/03-contacts/domains-for-contact-finder.csv`，先落盘公开页结果（缺的标「联系人待补」），用户交回后再合并，不空等。完成：主表已含公开页结果；服务结果已合并或缺口已标「联系人待补」。

6. **分类**。每条联系人（含待补行）必须有 `icp_category`、`company_type`、`job_title`。按 ICP 分 sheet，不得混进一张无标签总表。上游缺 ICP 且匹配不上 `icp-analysis.md` → 该行 `icp_category` 标待补，放入 sheet `unassigned`，并在失败分析点名。只采公开商务联系方式；消费邮箱域名不入库。完成：每行三标签齐全；sheet 名与 ICP 一致。

7. **落盘**。写入下方三个路径（CSV 仅步骤 5 需要时）。报告用中文；列名 English snake_case；公司名不翻译。完成：主报告非空且含搜索日志；`contacts.xlsx` 每个目标域名至少一行；教学例子原文零出现。验证—审查—审批走 `skills/lead-generation/references/orchestration-protocol.md`，本 skill 不代替审批。

## 默认

- 查证用 Apify 搜索；需要原文时抓取指定 URL（含动态页）。不并列搜索引擎菜单。
- 联系人/邮箱发现服务、网页采集服务：仅当用户已配置；付费前告知并获准。否则标「联系人待补」。
- 共用规则若存在则读 `skills/marketing-playbook-standards/SKILL.md`。
- 产品事实只读台账 `product_context`，不在本仓库另存一份。
- 覆盖率只报实际（有邮箱或公开职业页 URL 的行 / 公司行），不凑数。
- 进度只认台账。产出只进 `deliverables/lead/03-contacts/`。

## 写法

- 分类不可省：下游外展按 ICP 写不同序列，无标签名单不能用。
- 置信度按 `references/lookup-protocol.md` 如实标，不抬高。
- 有姓名的决策人优先于通用邮箱；`info@` / `sales@` 可记，`job_title` 为 `generic_inbox`，不把通用邮箱写成虚构人名。
- 每条有 `data_source` 与 `collected_date`。多源不混成一条无出处记录。
- 不抓登录墙后的内容（无用户授权）。遇登录墙或验证码：停止该域，记入搜索日志，从下一域名续，不重头开始。

## 产出

主文件 `deliverables/lead/03-contacts/collection-report.md`。表 `deliverables/lead/03-contacts/contacts.xlsx`（一 ICP 一 sheet）。辅助 `deliverables/lead/03-contacts/domains-for-contact-finder.csv` 仅在将使用已配置发现服务时导出。

```markdown
# 联系人采集报告

- source: 台账 product_context（不粘贴原文）
- accessed:
- finder_service: configured | not_configured

## 采集概况
目标公司数、域名数、找到联系人的公司数、待补行数、实际覆盖率、职位列表、名单范围。

## 查证统计
Apify 搜索次数、抓取 URL 数、发现服务是否使用（未用则写原因）。

## 失败分析
无域名 / 公开页无联系人 / 限流或登录墙 / 无法匹配 ICP。每条写公司与原因，不编造补齐。

## 数据隐私提醒
只采公开商务联系方式。外展须遵守 GDPR、CAN-SPAM 及收件人所在地同类规则。本报告不是法律意见。

## 搜索日志
| # | Capability | Query/URL | Results | Useful | Notes |
|---|------------|-----------|---------|--------|-------|
Total: N calls, M useful
```

`contacts.xlsx` 列：`company_name, domain, contact_name, job_title, email, phone, linkedin_url, icp_category, company_type, data_source, confidence, collected_date`。

找不到联系人时仍保留一行：`contact_name`、`job_title`、`email` 均为「联系人待补」；`confidence` 留空；`data_source` 写未找到的原因。`linkedin_url` 列只填已抓取的公开职业页 URL。

`domains-for-contact-finder.csv`：默认每行一个域名、无表头。用户的发现服务要求表头时加一列 `domain`。

## 例子

> 仅供理解，禁止引用到输出。

材料无目标公司联系人名册或邮箱语料，具名采集仍用通用支架。下面只借批发公开面与买家人格的结构，不抄竞品原句，不写入页脚电话或邮箱。

公开联系页写着采购部商务邮箱 → 填入该行，`data_source` 为该 URL，置信度按 lookup-protocol。公开页只有公司名、没有人名或商务邮箱 → 仍保留一行并标「联系人待补」，不编人名、不编邮箱、不把覆盖率凑上去。

贸易店常见形状（批发画像 / 平台对标）：匿名可见通用收件箱，具名客户经理只在登录后的账户里。通用收件箱可入库且 `job_title` 为 `generic_inbox`，`contact_name` 不编；登录墙后的具名经理 → 「联系人待补」，不凭「常见邮箱格式」补人。公司站与网店分域时（双站结构），只采已抓取的公开页，不把两站混成一条无出处记录。制造商服务热线名录不是买家联系人。

ICP 职位不要一律写成 Procurement Manager。小安装商人格是所有人一人决策；公开页是 Owner / Geschäftsführer 就填该职，不要虚构采购部，也不要把后台行政当成买家。EPC / C&I 人格是商务谈判与技术批准分开、后者可否决 → 公开到两个人就两行、各写 `job_title`；空职位标待补，不要为填满委员会表编造职称。注册表上的「职位」下拉不是已采到的联系人。

上游把某层标成对手或与本方同层的分销，而不是买家 ICP → 该公司不进采集表。

## 易错

- 所有联系人倒进一个未分 ICP 的 sheet。
- 用模型记忆或「常见邮箱格式」编造邮箱，凑「每家一人」或覆盖率。
- 未配置发现服务仍假装已查出邮箱。
- 把消费邮箱当商务联系人入库。
- 未先公开页查证就动用付费发现服务。
- 将使用发现服务却未导出 `domains-for-contact-finder.csv`。
- 多源合并时丢掉 `data_source`。
- 把 skill 例子原文写入交付物。

## 清单

- [ ] 已读 `product_context` 与已批准 ICP；至少一份公司名单；硬依赖未满足则已停
- [ ] 每个目标域名有搜索日志；Apify 修复与替代取证后仍不可得时已停并写缺口
- [ ] 每行有 ICP / 公司类型 / 职位；按 ICP 分 sheet
- [ ] 未配置发现服务的缺邮箱已标「联系人待补」，无编造
- [ ] 覆盖率为实际值；隐私提醒含 GDPR / CAN-SPAM
- [ ] 文件在 `deliverables/lead/03-contacts/`；例子原文未进入交付物
