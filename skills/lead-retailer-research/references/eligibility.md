# 零售商入围与发现

条件：做 SKILL 步骤 2–3、5（发现、入围、去重）时读本文。花括号是字段，不要把查询句抄进交付物当结论。

## 谁算零售商

零售品牌：以**自有品牌门店或品牌站点**把商品卖给终端消费者，或作为品牌门店卖给走进来的企业客户。

分销商 / 批发商：批量采购后再卖给其他商店或承包商，自己通常不是面向公众的品牌店。主业是批发 → 交给 `skills/lead-distributor-research/SKILL.md`，不进本表。

双渠道：公开材料证明既有批发又有零售时，看主业。零售门店/品牌站是主入口才留在本表；批发是主入口则只去分销商表。同一 `domain` 不得在两张已核验表各算一行还不解释。

目标客户公司（工厂、项目业主、采购方本人）走 `skills/lead-company-research/SKILL.md`，即使他们有采购部。

## 必须同时满足

1. 经营用户本轮品类（站点、目录或店内能核验在售，不是「也许也卖」）。
2. 员工数 **低于本轮上限**（默认 200）。数字必须有已抓取或可打开来源；取区间用上限。无数字 → 列入排除/缺口，不进已核验。
3. 官网或等价品牌站抓取成功。`url_verified` 只在抓取成功时为 true。

## 排除（写进排除节，不进主表）

- 员工数达到或超过上限的连锁
- 分销商、批发商、现金批发俱乐部（对公众无品牌零售门店）
- 仅在第三方市场开店、没有可抓取的自有品牌站
- 无自有库存与品牌识别的纯铺货站点
- 目录站、黄页、协会名单页（那是发现源，不是零售商）
- 不经营该品类的品牌店
- 域名抓取失败（验证码或登录墙：该条停、写入缺口，请用户接手后再核验；未解决不进已核验）

## 发现查询

用网页搜索查证。品类、国家、市场取产品上下文与已批准 ICP 术语。

```
"{product_category}" retail brand {country}
"{product_category}" shop online {market}
"{product_category}" retail store {region}
```

有 `icp-terms` 时，把已验证术语替换进 `{product_category}` 再搜一轮。每家仍须落到可抓取域名。

不要把搜索结果里的市场平台类目页、询盘平台店铺列表当成零售品牌行。

## 逐家核验查询

抓取：`{domain}` 首页与 About / Our Story（或等价页）。

再用网页搜索查证：

```
"{retailer_name}" employees OR "team of" OR headcount
"{retailer_name}" "about us" OR history
"{retailer_name}" award OR recognition OR "market share"
"{retailer_name}" store opening OR funding OR expansion
```

规模与地位以已打开页为准。职业网络公司页可作为员工数来源之一，仍须记下 URL；打不开则换源，不把记忆中的人数写进去。

## 去重

读已有 `deliverables/lead/02-companies/distributors.xlsx`、`distributors-brief.xlsx`、`target-companies.xlsx`（存在才读）。匹配 `domain` 或未翻译的 `company_name`。冲突时：批发主业 → 留分销商表；零售主业 → 留本表并在去重节写一句依据；无法判断 → 两边都不进已核验，放入缺口。
