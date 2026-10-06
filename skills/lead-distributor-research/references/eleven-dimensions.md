# 分销商 11 维（详研）

详研模式逐家填完本文件 11 维。简研不要用本文件，改读 `brief-mode.md`。无来源的格子写「未在来源出现」并记下尝试过的 URL，不留空、不编造。

## 目录

- [维 1 Company Overview](#维-1-company-overview)
- [维 2 Target Audience](#维-2-target-audience)
- [维 3 Annual Revenue / Size](#维-3-annual-revenue--size)
- [维 4 Geographic Coverage](#维-4-geographic-coverage)
- [维 5 Product Portfolio](#维-5-product-portfolio)
- [维 6 Market Positioning](#维-6-market-positioning)
- [维 7 Unique Selling Proposition](#维-7-unique-selling-proposition)
- [维 8 Customer Satisfaction / Reviews](#维-8-customer-satisfaction--reviews)
- [维 9 Supply Chain / Logistics](#维-9-supply-chain--logistics)
- [维 10 Partnership Potential](#维-10-partnership-potential)
- [维 11 Website and Contact](#维-11-website-and-contact)
- [表列](#表列)

## 维 1 Company Overview

回答：公司是谁、分销该品类多久、市场位置、可核验的里程碑。

完成：有成立或进入该品类的年份（或已标缺口）；有一句话角色（批发 / 授权分销 / 进口商），且与官网自我描述一致。

## 维 2 Target Audience

回答：主要客户是谁（零售、安装、其他商家、行业用户）；在本轮品类里聚焦哪一细分；服务哪些行业或场景。

完成：客群能与产品上下文的渠道角色对照；对照不上则标缺口，不改写成终端消费者画像充数。

## 维 3 Annual Revenue / Size

回答：已披露或可引用的年营收（写年份）、员工数、运营体量（仓库数、区域网点、车队若有公开数字）。

完成：员工数来自公开资料交叉，不凭网站气派估计。对照本轮上限（默认 200，除非用户或产品上下文另定）。超上限剔除。缺员工数：标缺口；仅当其他证据仍表明是可合作的渠道商时才保留，并在缺口节说明。营收无来源则写「未在来源出现」，不编区间。

## 维 4 Geographic Coverage

回答：在目标市场覆盖哪些区域；全国还是区域；线上目录还是实体仓 / 门店；是否做跨境分销。

完成：区域名称用来源中的地名，不套用某一国的方位标签。覆盖范围与维 9 仓库区位不互相矛盾，矛盾则记下并标低置信。

## 维 5 Product Portfolio

回答：分销哪些产品类型；公开材料里的主销或主推品类；是否有独家或自有线；常合作的制造商或品牌。

完成：主销品类有页面或目录依据。现有品牌列表用于维 10，不在本维写成「没有供应商」。

## 维 6 Market Positioning

回答：相对其他分销商如何差异化；定价相对竞品偏高 / 中 / 低（须有公开价目、报价口径或第三方评述）；被强调的价值（交期、服务、配套设计、库存深度等）。

完成：差异化有摘录或 URL，不用「靠品质差异化」这种无对照句。定价无来源则标缺口。

## 维 7 Unique Selling Proposition

回答：相对其他分销商，对方用什么留住下游客户。查证方向：品质口径、价格竞争力、面向客户的交期、支持、物流选项；以及设计咨询、组装、质保包一类增值服务。

完成：至少一条 USP 能指回已抓取原文。本维写**该分销商对自己客户的主张**，不要写成用户产品的卖点。

## 维 8 Customer Satisfaction / Reviews

回答：可核验的客户评价、评分、证言（B2B 客户、下游用户、公开平台）；行业认证、奖项、质量或服务认可；主要评论渠道上的口碑方向。

完成：每条评价或认证带 URL 与日期。找不到则写「未在来源出现」，不编五星或奖项。

## 维 9 Supply Chain / Logistics

回答：仓储与库存安排；能否接批量并维持供货；面向客户的交期基准；是否备安全库存。

完成：至少有仓库区位或数量、覆盖区域、交期、备货四项中的两项有来源，其余标缺口。禁止用「供应链可靠」单独成段。

## 维 10 Partnership Potential

本维禁止一句表态。五个问题都要有证据或「未在来源出现」：

1. 对海外供应商，公开材料里他们在找哪类产品或服务。
2. 是否已有国际采购；从哪些国家或地区进货。
3. 新制造商门槛（证书、MOQ、交期、独家、付款、验厂）。
4. 目录或品牌页上相对本轮品类的缺口。
5. 什么情况下会加线或换供应商（合同锁期、授权冲突、缺货、品类扩张）。

完成：五问都有答；至少两问能指回已抓取页（供应商入口、品牌目录、新闻或招聘）。现有授权或长期协议当作约束写进合作潜力，不省略。

## 维 11 Website and Contact

回答：官网、产品目录或品牌页链接；公开询问路径；销售或采购团队是否可公开触达（邮箱、电话、职业页）；公开出现的联系人姓名。

完成：官网必有且已抓取。邮箱或人名未在公开页出现 → 标「联系人待补」，不编造。至少有一条可用联系路径（联系页、表格、公开电话或职业页）。

## 表列

`deliverables/lead/02-companies/distributors.xlsx`（或同列 csv）：

`company_name, domain, years_in_business, target_audience, revenue_estimate, employee_count, geographic_coverage, product_portfolio, best_selling_category, market_positioning, pricing_strategy, usp, customer_reviews, supply_chain_reliability, partnership_potential, sourcing_countries, contact_info, data_source, url_verified, retrieved_date`

- `url_verified`：`yes` 仅当本轮已抓取且可达。
- `data_source`：主依据 URL 或查询。
- `retrieved_date`：`YYYY-MM-DD`。
- `contact_info`：公开路径；无邮箱则含「联系人待补」。
