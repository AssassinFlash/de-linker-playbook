# 分销商简研

本文件只用于 `brief` 模式。详研读 `eleven-dimensions.md`。简研是 `lead-distributor-research` 的第二种交付物，不是新 skill、不是新入口。

## 何时用

- 用户只要对照表，或详研已批准后要另一批快筛名单。
- 硬依赖：详研交付物 `status` 为 `approved` 或 `approved_with_concerns`，或台账已记 `user_waiver`。未满足且用户只要简研 → 先做详研，或记录豁免后再写本模式。
- 发现、验域名、员工数上限、分销商角色判定与详研相同，见 `SKILL.md` 步骤 3–5。

## 每家只填

1. **Company Overview** — 公司名、网站域名、沿革、市场位置、进入该品类的年限。
2. **Target Audience** — 主要客户群；在本轮品类里的细分焦点。

不要展开 11 维。不要把简研写成缩短版详研报告。

## 重叠

简研名单的 `company_name` 与 `domain` 不得出现在已批准的 `distributors.xlsx` / `distributors-analysis.md` 里。重复的剔除并换候选；换不够则少写行并在缺口节说明。

## 查证

- 每条事实能指回搜索或已抓取正文。
- 每家域名本轮抓取可达，否则不入表。
- 员工数规则与详研相同（默认上限 200，除非本轮另定）；超上限剔除；缺数字标缺口，不编。

## 落盘

表：`deliverables/lead/02-companies/distributors-brief.xlsx`（或同列 csv）

列：`company_name, domain, years_in_business, market_position, primary_customers, niche_focus, data_source, url_verified, retrieved_date`

companion（审批闸门需要 Markdown `status`，仅有表不能批准）：`deliverables/lead/02-companies/distributors-brief.md`

```markdown
# 分销商简研 — {品类} × {市场}

- source: 台账 product_context（不粘贴原文）
- accessed:
- mode: brief
- employee_cap:
- cap_source:
- detailed_list_ref: deliverables/lead/02-companies/distributors-analysis.md

## 名单摘要

## 与详研不重复声明

## 搜索日志
| # | Capability | Query/URL | Results | Useful | Notes |
|---|------------|-----------|---------|--------|-------|

## 缺口
```

目标约 10 行已验证、且不与详研重复的分销商；不足则如实行数加缺口，不补假公司。

## 完成

- 表非空；列名为 English snake_case；公司名不翻译。
- companion 非空；含搜索日志与不重复声明。
- `url_verified` 仅为已抓取可达的 `yes`。
- 教学例子原文零出现。
