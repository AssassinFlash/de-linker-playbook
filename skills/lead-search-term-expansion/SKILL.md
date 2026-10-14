---
name: lead-search-term-expansion
description: >
  Use when expanding search keywords, generating positioning terms,
  building prospecting keyword lists, 搜索词, 搜索词扩展, 定位术语,
  关键词扩展, Google search terms, LinkedIn search terms, company
  types, or lead discovery keywords. For each approved ICP, collect
  how target companies describe themselves across four tones
  (Professional, Casual, Cutting-edge, Traditional) and turn those
  phrases into search-ready queries. Read the ledger product_context
  (default ~/Documents/New/CONTEXT.md) and the upstream ICP file;
  verify every term with web search; invent no monthly volumes. Not
  for compiling company lists, scraping contacts, or writing the ICP
  itself.
---

# 搜索词扩展（四语气）

把已批准 ICP 译成目标公司的自我定位用语，并做成可搜索关键词。写入 `deliverables/lead/01-icp/`。四种语气与句式见 `references/tone-variations.md`。

## 步骤

1. **输入**。若存在则先读 `skills/marketing-playbook-standards/SKILL.md`。读台账 `state/lead-status.md` 的 `product_context`（默认 `~/Documents/New/CONTEXT.md`；把 `~` 展开为主目录）。读 `deliverables/lead/01-icp/icp-analysis.md`；需要表时再读同目录 `icp-summary.xlsx`。硬依赖：该 ICP 交付物 `status` 为 `approved` 或 `approved_with_concerns`，或台账已记 `user_waiver`。缺失或未批准 → 停，宣布缺口，打开 `skills/lead-icp-analysis/SKILL.md`（存在则按其做）；不编 ICP、不往下扩词。覆盖哪些 ICP、平台、语种、每条 ICP 词数仍不清楚 → 打开 `skills/lead-interview/SKILL.md`；该文件不存在则把缺口写入台账，不自造问卷。完成：能列出本轮 ICP 名称、目标市场语种、平台范围，并指回 ICP 文件哪几节；原文不拷进本仓库。

2. **拆属性**。对每个要覆盖的 ICP 写属性卡：规模、行业、目标市场、对方卖什么/提供什么服务。完成：每张卡能指回 ICP 原文一节；缺项标「未在上游出现」。

3. **采集自我描述**。用网页搜索查证同类公司如何自称（About、公开职业网络公司页、营销材料），查询用行业 + 市场 + 自称句式（`we are` / `we specialize` / `about`），字段取属性卡，不把查询模板抄进交付物。需要原文时抓取指定 URL。摘 5–12 词真实短语，记下 URL 与访问日期。搜索不可用 → 停止并写缺口，不编造。多 ICP 需要隔离时 dispatch a subagent, else do it inline；单个 ICP inline 做完。完成：每个要覆盖的 ICP 都有带来源的摘录；零摘录的 ICP 标缺口，不进入步骤 4 的无源扩展。

4. **四语气候选**。读 `references/tone-variations.md`。从已有摘录扩写，语气取值仅限 Professional / Casual / Cutting-edge / Traditional。信号词是先验，不是必填填料：该 ICP 真实语料没有的语气，写「无已验证用语」，不编一套时髦词。完成：每条候选能回溯到至少一条摘录，或标明由哪条摘录改写。

5. **验证**。对每条候选用网页搜索查证定位语与派生 `search_keyword`。首页须出现符合该 ICP 的公司，不是纯文章或目录聚合页。0 家匹配 → 丢弃。需要确认时抓取该公司页。保留行必须有 `relevance_verified: true`、`example_company`、可打开的 `example_url`。单复数或只差冠词的变体算一条。搜索量：用户提供关键词工具导出则填整数月量；未配置则用自动补全是否出现 + 结果页匹配公司数作粗热度，`estimated_search_volume` 写粗热度短句或 `unverified`，禁止编造精确月量。完成：保留表每行有公司例证与来源；丢弃列表进搜索日志。

6. **落盘**。按下方模板写 `deliverables/lead/01-icp/icp-terms-strategy.md`，表写 `deliverables/lead/01-icp/icp-terms.xlsx`（一个 ICP 一个 sheet）。当前环境写不了 xlsx 则写同目录 `icp-terms.csv`，列相同。目标：每 ICP ≥10 条已验证、互不相同的术语，四种语气都有已验证行。搜不够 → 如实写条数、未覆盖语气与缺口，不拿未验证词凑行。完成：主文件非空且含搜索日志；表含依赖图要求的列；教学例子原文零出现。

## 默认

- 共用规则若存在则读 `skills/marketing-playbook-standards/SKILL.md`。
- 查证用网页搜索；需要原文时抓取指定 URL；搜索或抓取不可用则停止并写缺口，不编造。
- 关键词量用用户已配置的关键词研究工具（用户导出，本侧解析）；未配置不阻塞。
- 概念型最低查证见 `skills/lead-generation/references/search-protocol.md`：至少 5 次网页搜索，再加每条候选的相关性验证；次数写入搜索日志，搜不够就报告实际已验证条数。
- 术语必须是公司用来描述自己的话，不是行业分类代码，也不是外人给的学名。
- 面客检索词跟目标市场用语（缺省英语，注意 US / UK / 其他英语区用词差）；分析段落用本轮语言。
- 表列名 English snake_case；公司名不翻译。
- 下游 `lead-company-research`、`lead-distributor-research`、`lead-retailer-research`、`lead-contact-discovery` 用本表做发现查询。本 skill 不跑那些步骤，不发送外展。
- 落盘后的验证、六维审查、用户审批由编排器按 `skills/lead-generation/references/orchestration-protocol.md` 做；本 skill 不自造审批流。

## 写法

- 过窄（几乎没有公司用这整句）和过宽（什么公司类型都中）都丢掉。优先能滤出该 ICP、结果页上又能看到多家匹配公司的词。
- 同一意思只留一条；不要靠单复数凑数。
- 不要把用户自己公司的定位句当成目标客户的自称。
- `use_case` 按词实际出现的场合填：Google、LinkedIn、行业名录、本地商家页。LinkedIn 偏 Professional / Cutting-edge；名录偏 Professional / Traditional；本地检索偏 Casual / Traditional。Google 四种都试。
- `search_keyword` 是能直接粘进搜索框的查询，不是定位语的同义重复。

## 产出

主文件 `deliverables/lead/01-icp/icp-terms-strategy.md`。表 `deliverables/lead/01-icp/icp-terms.xlsx`（或 `.csv`）。

必填列：`icp_category, company_type, positioning_term, tone, search_keyword, estimated_search_volume, use_case`。另加：`relevance_verified, example_company, example_url, data_source, retrieved_date`。

```markdown
# ICP Search Terms — {品类} × {市场}

- source: 台账 product_context（不粘贴原文）
- upstream: deliverables/lead/01-icp/icp-analysis.md
- accessed:

## 覆盖的 ICP

## 按 ICP 的搜索词

### {icp_name}

属性卡：

未覆盖的语气与原因：

（表或指向 xlsx 对应 sheet）

平台建议：

## 丢弃的候选

| positioning_term | 原因 |
| --- | --- |

## 搜索日志
| # | Capability | Query/URL | Results | Useful | Notes |
|---|------------|-----------|---------|--------|-------|
Total: N calls, M useful
```

## 例子

> 仅供理解，禁止引用到输出。

输入写「德国小安装商」再按一种英语伞词扩十行。先拆属性卡，再摘车上 / About 自称；不要把批发自动补全里的「品类 + 城市 / 附近」整串当成 `positioning_term`——那是买家找货查询，不是公司自称。

成稿应改成该 ICP 已出现的自称（师傅行、电气专业店），`search_keyword` 能粘进搜索框且首页看得到匹配公司。市场外号只作发现变体，不替代自称。同一货架四国四名，不要机器映射成一个英语伞词。自造段名、英美电表前后场黑话、名录分类号、以及该 ICP 语料没有的「智能平台」口号，都丢掉。无 Cutting-edge 语料就写「无已验证用语」，不硬编。不要把本节句子粘进交付物。完整示意表见 `references/examples.md`。

## 易错

- 未读已批准 ICP 就扩词，或自己编画像。
- 用模型记忆填定位语和月搜索量。
- 用未验证词凑满每 ICP 10 行。
- 四种语气硬编齐，尤其是真实公司并不用的 Cutting-edge 口号。
- 把 SIC / NAICS 或政府采购分类当成定位语。
- 术语只匹配用户自己的公司，不匹配目标客户。
- 忽略目标市场英语变体，把一种拼法当全球通用。
- 把本 skill 例子表写入交付物。
- 扩完词接着去编公司名单或联系人。

## 清单

- [ ] 已读 `product_context` 与已批准 ICP；原文未拷进本仓库
- [ ] 每个覆盖 ICP 有属性卡和带来源的自我描述摘录；零摘录未扩写
- [ ] 保留术语均已搜索验证，有 example_company 与 URL
- [ ] 未编造月搜索量；无导出则粗热度或 `unverified`
- [ ] 四种语气：有语料的已覆盖，无语料的已写缺口，未硬编
- [ ] 每 ICP 已验证条数 ≥10，或已写实际条数与缺口
- [ ] 文件在 `deliverables/lead/01-icp/icp-terms-strategy.md` 与 `icp-terms.xlsx`（或 csv）
- [ ] 搜索日志有查询、日期与结论；例子原文未进入交付物
