---
name: lead-retailer-research
description: >
  Use when researching retail brands, finding niche retailers, building a
  retail prospect list, 零售商, 品牌零售, 零售市场, 零售品牌调研, or retail
  research, or when the user mentions retailer, niche retail, retail
  prospect, or retail profiling. Identify and profile retail brands in a
  target market for a product niche; default size cap is under 200
  employees. Classify each as market leader, emerging player, niche focus,
  or regional specialist, with a specific observable niche focus. Write to
  deliverables/lead/02-companies/. Read the ledger product_context; invent
  no companies or headcount. Not for distributor lists, end-customer
  company research, or contact scraping.
---

# 零售商调研（品牌画像）

在目标市场找出经营指定品类的零售品牌，核验域名与规模，标市场地位和可观察的细分聚焦，写入 `deliverables/lead/02-companies/`。默认员工数上限 200；搜不够按实有数量交付，不编造。

## 步骤

1. **输入**。读 `skills/marketing-playbook-standards/SKILL.md`（存在则读）。读台账 `state/lead-status.md` 的 `product_context`（默认 `~/Documents/New/CONTEXT.md`；把 `~` 展开为主目录，不当相对路径）。原文不拷进本仓库。存在则再读：`deliverables/lead/01-icp/icp-analysis.md`、`deliverables/lead/01-icp/icp-terms.xlsx`、`deliverables/lead/02-companies/target-companies.md`、`deliverables/lead/02-companies/distributors.xlsx`（及 `distributors-brief.xlsx`）。记下品类、目标市场、渠道偏好（线上 / 实体 / 都要）、员工数上限（未指定则 200）。品类或市场仍不清：打开 `skills/lead-interview/SKILL.md`（存在则按其做）；不存在则本轮只补这两项，不另写问卷。完成：能指出品类与市场各依据哪几条；规模上限已写入本轮口径。

2. **发现**。用网页搜索查证零售品牌，查询模板见 `references/eligibility.md`。优先用已批准的 ICP 术语；没有术语就用产品上下文的品类词 + 市场。候选必须是自有品牌门店或品牌站点、把该品类卖给终端消费者或作为品牌门店卖给企业客户。完成：候选表每条有发现用查询与来源 URL；目录站、交易平台列表页不当成一家公司。

3. **入围**。对每条候选：抓取指定 URL 的正文，按 `references/eligibility.md` 判定是否零售商、是否经营该品类、员工数是否低于上限。员工数来自已抓取的关于我们页、新闻或可打开的公开职业网络公司页；取区间时用上限，仍须低于本轮上限。搜索或抓取不可用则停止并写缺口，不编造。多家核验需要隔离时 dispatch a subagent, else do it inline。完成：已核验表每家 `url_verified` 为抓取成功；未过筛的写入排除理由，不进主表。

4. **画像**。对已入围每家写：公司名（不翻译）、域名、品类经营年数、简史、主要客群、`market_position`、可观察的 `niche_focus`。标签枚举与证据规则见 `references/classification.md`。地位与细分都必须能指回已抓取页或搜索摘录。完成：每家两个标签都有一句证据；年数或简史缺则写 `unknown`，不补故事。

5. **去重**。对照已有分销商表与目标公司表。同一域名不得同时作为零售商和分销商交出，除非公开材料证明双渠道且零售是主业（批发为主的归分销商调研）。完成：主表无与分销商名单的未解释重叠。

6. **落盘**。按下方模板写 `deliverables/lead/02-companies/retailer-analysis.md`，表写 `deliverables/lead/02-companies/retailers.xlsx`（写不出 xlsx 则同目录 `retailers.csv`，列相同）。目标 10 家已核验；不足则按实有数量交付，在缺口节写还差几家、已试查询、为何不拿不合格公司凑数。完成：主文件非空；表列齐；有 `## 搜索日志`；教学例子原文零出现。

7. **出门检查**。对照清单。完成：主表每家低于规模上限、域名已抓取、地位与细分有证据；未把分销商、平台店、纯铺货站点算进已核验。

## 默认

- 查证用网页搜索；需要原文或验域名时抓取指定 URL；不可用则停止并写缺口，不编造公司、域名或员工数。
- 规模上限默认 200 人；用户或访谈另定则从其，并写进交付物抬头。
- 名单型最低查证：发现用搜索；每家必须抓取官网（或等价品牌站）；搜不够报告实际数量。
- 硬依赖 `lead-search-term-expansion` 由编排闸门处理；本 skill 有术语表就用，没有则用产品上下文品类词并标缺口。
- 分析用本轮语言（缺省中文）；表列名 English snake_case；公司名不翻译。
- 本 skill 只产名单与画像；验证—审查—审批按 `skills/lead-generation/SKILL.md` 协议，不在此标 `approved`。

## 写法

- 先判商业模式再画像：零售是品牌门店卖给终端（或企业客户走进来买）；批量供给其他商店的是分销商。
- 市场地位按公开信号打，不按「是否听过」。
- `niche_focus` 列写可观察的细分（客群、价位带、用途），不要只写 `premium` 这类空标签。
- 未经营该品类的品牌店不进表，即使规模合适。

## 产出

主文件 `deliverables/lead/02-companies/retailer-analysis.md`。表 `deliverables/lead/02-companies/retailers.xlsx`（或 `.csv`）。

表列：`company_name, domain, years_in_business, market_position, primary_customers, niche_focus, employee_count, data_source, url_verified`

`market_position` 只取：`market_leader` / `emerging_player` / `niche_focus` / `regional_specialist`。

```markdown
# Retailer Research — {品类} × {市场}

- source: 台账 product_context（不粘贴原文）
- employee_cap:
- verified_count:
- accessed:

## 口径
品类、市场、线上/实体、规模上限

## 零售商概览
每家：域名、员工数与来源、地位 + 一句证据、客群、细分聚焦 + 一句证据

## 按 niche_focus 分组
分组对比，不重复粘贴概览

## 排除与缺口
排除理由；已核验不足目标时的缺口

## 与分销商/公司名单去重
无重叠或已解释的双渠道

## 搜索日志
| 查询或 URL | 日期 | 结论 |
```

## 例子

> 仅供理解，禁止引用到输出。

输入：官网写 we supply retailers nationwide、没有面向终端的品牌店；或站点有品类 mega-menu、产品卡、购物车，但注册要工商证明、匿名价要登录才见（Memodo/Krannich 这类批发店），页眉把终端访客导向「找安装商」而不是结账（Segen/BayWa 双入口）。成稿：排除，交给分销商调研；主入口须是面向走进来的人的品牌门店，才进本表。不要把「有目录的网店」写成零售品牌。抓取只拿到注册摘要或防护失败：写入缺口，不把摘要里的批发店头衔当已核验行。

输入：已入围站把目录按「品类 × 品牌」切、家用与工商业是分开的一级栏目。成稿：`niche_focus` 写成能从该目录复核的客群或用途，而不是 they sell premium products。锚定材料是贸易批发店与平台栏目结构，没有品牌零售画像，故正向入围仍用通用支架：自有品牌站、About 有低于上限的员工数来源、首页能核验在卖该品类。搜到的全是贸易店时按实有零售数交付，不把批发店改头换面凑满 10 行。

地位：没听过 ≠ `emerging_player`。要有新店、融资或第三方报道等已抓取信号；站点自称 leader 而无第三方信号则不进已核验。

## 易错

- 把分销商、批发商、平台第三方店、无库存纯铺货站点当成零售品牌。
- 用训练记忆填满 10 行，或拿超规模连锁凑数。
- 员工数无来源仍写入已核验表。
- 域名未抓取就标 `url_verified`。
- 与已有分销商表重叠且不解释。
- 把产品上下文原文或本 skill 例子写进交付物。

## 清单

- [ ] 已读 `product_context`；品类与市场可回溯
- [ ] 已核验每家员工数低于本轮上限，有来源
- [ ] `market_position` 为四值之一且有证据
- [ ] `niche_focus` 具体可观察，不是空标签
- [ ] 全部域名已抓取；`url_verified` 与抓取结果一致
- [ ] 未与分销商名单未解释重叠
- [ ] 不足 10 家已如实报告并写缺口，未编造
- [ ] 文件在 `deliverables/lead/02-companies/`；有搜索日志；例子原文未进入交付物
