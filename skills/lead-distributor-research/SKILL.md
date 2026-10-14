---
name: lead-distributor-research
description: >
  Use when researching distributors, finding wholesalers, 分销商, 经销商,
  批发商, 渠道合作伙伴, channel partner, distribution network, wholesale
  partner, find distributors, 简研, or wholesale research. Profile
  channel partners: detailed mode fills eleven dimensions including
  partnership potential; brief mode is this skill's second table, not
  a separate entry. Read the fact-source entry docs/fact-sources.md. Discover with web search; fetch each
  domain. Aim for about ten verified names; report the real count.
  Default headcount cap 200 unless user or context sets another.
  Invent no headcount or emails. Not for end-customer lists, retailer
  lists, or contact harvesting.
---

# 分销商调研

按目标市场给批发商 / 分销商做详研（11 维）或简研。简研是本 skill 的第二种交付物，不是新入口。写入 `deliverables/lead/02-companies/`。维定义见 `references/eleven-dimensions.md`；简研字段见 `references/brief-mode.md`。

## 步骤

1. **输入**。读 `skills/marketing-playbook-standards/SKILL.md`。产品与公司事实读事实源入口 `docs/fact-sources.md`，按其「什么问题查哪个源」取证；查不到标〔未证实〕，按没有处理。本会话还没读过就现在读。原文不拷进本仓库。硬依赖：存在则读 `deliverables/lead/01-icp/icp-terms.xlsx`（或 `.csv`）。有则再读 `deliverables/lead/01-icp/icp-analysis.md`、`deliverables/lead/02-companies/target-companies.md`。硬依赖未批准且无 `user_waiver` → 停，宣布缺口，打开 `skills/lead-search-term-expansion/SKILL.md`（文件存在时），不自造发现词。产品上下文加已批准上游仍不够清楚时，打开 `skills/lead-interview/SKILL.md`（存在则按其做）；不存在则把缺口写入台账，不另写问卷。缺品类或目标市场：先看用户本轮；仍缺则停，只要这两项。完成：能指出品类、市场、渠道角色各依据哪几条陈述。

2. **模式**。`detailed`（缺省）或 `brief`。简研不是独立 skill：详细版未批准且用户只要简研 → 先做详研，或记录 `user_waiver` 后再做简研。员工数上限：用户或产品上下文有则用；否则默认 200。完成：交付物抬头写明 `mode`、市场、员工数上限及其来源。

3. **发现**。用网页搜索查证。查询取已批准术语与产品上下文的品类 / 市场；模板见 `skills/lead-generation/references/search-protocol.md` 的分销商节。目标约 10 家**分销商或批发商**（向制造商采购、卖给零售 / 安装 / 其他商家），不要把同品类制造商、品牌商官网、目录站或交易平台列表页算进名单。需要隔离时对入围对象 dispatch a subagent, else do it inline。完成：每家候选有拟用域名；不足 10 家已写缺口与已排除类型，不拿无关公司凑数。

4. **画像**。详研：读 `references/eleven-dimensions.md`，11 维逐家填完；合作潜力按该文件五个问题作答，不是一句表态。简研：读 `references/brief-mode.md`，只填概览与客群，且不与已批准详研名单重复。数字、营收、评价、员工数只来自产品上下文、用户本轮、搜索结果或已抓取正文。查不到的格子写「未在来源出现」，记下尝试过的 URL，不留空、不编。完成：无未标明的空白维；每条事实能指回来源。

5. **验证**。对拟写入的每一域名抓取指定 URL 的正文，记录可达性。员工数用公开资料交叉（注册信息、关于页、新闻、职业网络公司页）；不要凭网站气派估计。超过本轮上限的剔除。搜或抓不可用 → 停止并写缺口，不编造。完成：留下的每家 `url_verified` 为可达；员工数有来源或已标缺口。

6. **落盘**。详研：`deliverables/lead/02-companies/distributors-analysis.md` 与同目录 `distributors.xlsx`（或同列 csv）。简研：`deliverables/lead/02-companies/distributors-brief.xlsx`（或 csv）加 companion `distributors-brief.md`（否则仅有表无法批准）。表列名 English snake_case；公司名不翻译。分析用本轮语言。末尾必须有 `## 搜索日志`。完成：主文件非空；教学例子原文零出现。

7. **出门检查**。对照清单。验证—审查—审批—写入按 `skills/lead-generation/references/orchestration-protocol.md` 接手，本文件不另写闸门。完成：清单全过，或已记录 `user_waiver`。

## 默认

- 查证用网页搜索；需要原文或验域名时抓取指定 URL。不并列搜索引擎菜单，不规定每家搜索次数。搜索不可用则停止并写缺口。
- 联系人 / 邮箱发现服务仅当用户已配置；否则 `contact_info` 写官网公开联系路径，邮箱标「联系人待补」，不编造。
- 网页采集服务仅当用户已配置；付费前告知并获准。
- 进度只认台账。产出只进 `deliverables/lead/02-companies/`。
- 下游联系人采集走 `skills/lead-contact-discovery/SKILL.md`；本 skill 不收割邮箱列表。
- 平行名单：终端客户走 `skills/lead-company-research/SKILL.md`，零售商品牌走 `skills/lead-retailer-research/SKILL.md`，文件存在时打开，不在本文件复制其步骤。

## 写法

- 合作潜力是最有用的一维：写清目录缺口、现有海外采购国、新供应商门槛、什么情况下会加或换供应商。一句话「可能有兴趣」不算完成。
- 定位与 USP 从分销商决策看：毛利、供货稳定性、区域排他，而不是「他们要最便宜的货」。
- 供应链写仓库数量或区位、覆盖区域、面向客户的交期、是否备货；写不出就标缺口，不用「供应链可靠」代替。
- 已有品牌授权或长期供货协议能查到就写，作为合作潜力的约束，不假装空白市场。

## 产出

详研主文件 `deliverables/lead/02-companies/distributors-analysis.md`。表列见 `references/eleven-dimensions.md`。简研路径与列见 `references/brief-mode.md`。

```markdown
# 分销商分析 — {品类} × {市场}

- source: 台账 product_context（不粘贴原文）
- accessed:
- mode: detailed
- employee_cap:
- cap_source:

## 分销商概览

## 合作潜力分析

## Top 3 建议

## 各分销商 11 维

## 搜索日志
| # | Capability | Query/URL | Results | Useful | Notes |
|---|------------|-----------|---------|--------|-------|

## 缺口
```

目标：详研表约 10 行已验证分销商；不足则如实行数加缺口。简研另约 10 行，与详研公司名 / 域名不重复。

## 例子

> 仅供理解，禁止引用到输出。

画像顺序：定位 → 品类树 IA → 注册墙/价格门 → 工具/学院，再填 11 维。输入只写「B2B 批发、登录可见价」→ 成稿应改成：自我定位是光伏专科批发还是电气全品类里的光伏子目录；主导航有无本轮品类分支（按场景分夹，不抄货号表）；匿名价签是登录见价还是询价；是否公开学院、对比表或兼容清单。不要把集团口号写成 USP，也不要把库存深度或交期承诺当卖点。

双站与多名不要并成一行。输入把集团站与网店、或一国两柜台品牌揉成一家 → 成稿应改成：公司页填维 1/4，网店填维 5/7/10 的目录与门槛；柜台品牌与集团名分列或注明别名。员工数多源不一致时并列来源与日期，不静默取一个数；默认 200 人上限会刷掉跨国电气批发，超限剔除并在缺口写类型。

角色闸：本名单只要「向制造商采购、卖给安装/零售/其他商家」的批发或授权分销。电气全品类把光伏放在能源子夹、专科光伏批发以下游安装商为客群，均可作候选（过员工上限另论）。制造商、目录站、以及从批发再转售的 Wiederverkäufer / Fachhändler 不要进表——本产品方自己已在分销层时，那一层是同级或下游转售，不是本轮客户。注册表「行业」选项用来填维 2，不在本 skill 收割联系人。

合作潜力接到目录与门槛，不要停在「该司愿意看海外供应商」。可写成：公开品牌夹只有 A/B 类、不见本轮品类；部分货号要求制造商培训/证书才可购；已披露从某国进货——缺口是本轮品类与该证书。现有授权当约束。数字与国名只来自已抓取页。

名单形状：7 家域名已抓取、角色确认的分销商优于凑满 10 家却混进制造商、目录站或二阶转售。

## 易错

- 把制造商、自有品牌零售商或行业目录页当成分销商。
- 用模型记忆填 11 维或员工数。
- 把 brief 当成另一个入口另写流程。
- 为凑 10 行写入超规模或未验证公司。
- 编造邮箱或联系人。
- 详细与简研名单重复。
- 未抓取就标 `url_verified`。
- 把 skill 例子原文写入交付物。

## 清单

- [ ] 已读 `product_context`；硬依赖已批准或已记录 user_waiver
- [ ] 抬头有 mode、市场、员工数上限来源
- [ ] 名单均为分销 / 批发角色；不足目标数已写缺口
- [ ] 详研 11 维无未标明空白；合作潜力五个问题都有证据或缺口
- [ ] 简研不与详研名单重复；有 companion `.md`
- [ ] 每家域名已抓取；员工数有来源或已标缺口，未编造
- [ ] 搜索日志有查询 / URL 与日期；例子原文未进入交付物
- [ ] 文件在 `deliverables/lead/02-companies/`
