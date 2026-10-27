# 名单模式（第三种交付物）

条件：模式为 `list`（调研激活名单里的公司），或操作者点名「名单」「激活名单」「名单下一家」时读本文。这是 `lead-company-research` 的第三种交付物，同一入口，不另起 skill。方法照 `SKILL.md` 与 `three-info-blocks.md`，本文只写输入、命名和与标准模式不同的几处。

## 目录

- [名单是什么](#名单是什么)
- [输入](#输入)
- [依赖](#依赖)
- [与标准模式的不同](#与标准模式的不同)
- [产出](#产出)
- [质检](#质检)

## 名单是什么

激活名单（`CONTEXT.md`「激活名单」）是操作者交来的已同意客户表，只有名字和联系方式，背后的关系、历史、需求一概未知。按陌生开发对待：先调研再接触。「已同意」只解除发信的合规顾虑，不提供任何客户认知：不写成老客户、不假设对方认识我们、买过、有需求。

名单只在私有 vault：原件 `deliverables/lead/00-system/activation-list/original/`（原样，不改），转出的 `deliverables/lead/00-system/activation-list/activation-list.csv`（列定义 `schemas/activation-list.schema.json`，转格式 `uv run scripts/activation_list.py convert`）。公司名、联系人不进公开仓库；台账只写数字和 vault 相对路径。

## 输入

1. 跑 `uv run scripts/activation_list.py progress`：拿到「已调研 n / 共 N」和下一家的 `list_id`。操作者点名某家时用那家。
2. 跑 `uv run scripts/activation_list.py show --id <list_id>`：这家在名单里的全部行（公司名、地址、国家、网站、联系人）。
3. 产品与公司事实照 `SKILL.md` 步骤 1 读事实源入口；已批准的 ICP、搜索词有则读（软依赖，见下）。

完成：知道这家的 `list_id`、名单上的公司名原文、城市与国家、名单给的网站或邮箱域名。

## 依赖

- 硬依赖：激活名单 CSV 存在，加上全局的 `product_context`。名单模式不做发现，所以不要求已批准的搜索词（`skills/lead-generation/references/dependency-graph.md` 的 `lead-company-research/list`）。
- 软依赖：`lead-icp-analysis`、`lead-search-term-expansion`。有已批准的 ICP 就给这家标 `icp_category`；没有就写「待补」，在缺口里说明，等 ICP 过闸后回填。

## 与标准模式的不同

- **不做步骤 3 发现**：公司来自名单，不靠搜索找。仍要用 Apify 搜索和抓取核实它是谁。
- **官网**：先用名单的 `homepage`；没有就用名单邮箱的域名（免费邮箱如 gmx、gmail、web.de、t-online 不算官网）；都没有就搜「公司名 + 城市」。抓取后核对名称、地址或城市与名单一致，才算 `url_verified: true`。
- **公司名**：`company_name` 一律照名单原文，不翻译、不改写。这样名单、调研、外展、执行登记里是同一种写法，「运营里只剩记账时」和询盘归因按它对。官网上的写法不同，另记在 `official_name`。
- **不剔除，写结论**：标准模式会把不合格的公司剔掉；名单公司不剔，每家都落一份，写 `list_verdict`：
  - `可接触`：查实是一家可核验的公司，角色可能是我们的买家。
  - `暂不接触`：查实了，但现在不该接触（同品类卖方、已停业或被并购、角色明显不是买家），写一句原因和来源。
  - `查无此公司`：官网抓不到，搜索也核实不了。写清试过哪些查询。
  三种都算「已调研」。只有 `可接触` 的公司进第 3 阶段联系人和之后的外展。
- **不抄联系人**：调研文件不写名单上的姓名、邮箱、电话；联系人在第 3 阶段从名单按 `list_id` 取。决策流程块照常写职能，公开页上有姓名的可以写。

## 产出

一家一份：`deliverables/lead/02-companies/activation/<list_id>.md`（文件名只用编号，不用公司名）。frontmatter 按 `skills/lead-generation/references/orchestration-protocol.md` 步骤 7，`skill: lead-company-research`，另加 `mode: list`、`list_id`。

```markdown
# 名单公司调研 — {list_id}

- source: 台账 product_context（不粘贴原文）
- mode: list
- list: deliverables/lead/00-system/activation-list/activation-list.csv，{list_id}（原件第 n 行）
- accessed:
- list_verdict: 可接触 | 暂不接触 | 查无此公司

## {company_name}
#### 域名
#### 采购行为
#### 决策流程
#### 公开社媒与信息圈层
#### 结论
（list_verdict 及一句依据；暂不接触、查无此公司写原因与来源）

## 表行
（一行，列 = 标准 14 列 + list_id, official_name, list_verdict）

## 缺口

## 数据验证
（`skills/lead-data-validation/SKILL.md` 五项，一家一张小表，写在本文件里，不另写 data-validation.md）

## 六维审查
（编排协议步骤 5；依赖图「lead-company-research（list）」清单逐条 ✅/❌）

## 搜索日志
| # | Capability | Query/URL | Results | Useful | Notes |
|---|------------|-----------|---------|--------|-------|

## 证据闸
```

一家一份，审查和证据闸也一家一过；获客台账「审批与过期」一家一行（路径写到编号为止），「激活名单」节的「已调研 n / 共 N」按 `progress` 的输出改。

## 质检

- [ ] 公司来自名单（`list_id` 对得上），名称照原文
- [ ] 官网已抓取，并与名单的名称、城市或地址对上；对不上就不算 `url_verified`
- [ ] 三块齐全，缺的写「未在来源出现」；没有把「已同意」写成客户认知
- [ ] 公开社媒矩阵、账号内容、可见 follower/互动、产业与渠道内容已查证；账号结论来自多个带日期帖子，不能由单帖外推；私人浏览与登录墙后数据标缺口
- [ ] `list_verdict` 有，且有依据
- [ ] 文件里没有名单上的姓名、邮箱、电话
- [ ] 文件在 `deliverables/lead/02-companies/activation/`，文件名是 `list_id`
