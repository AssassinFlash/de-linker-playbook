---
name: marketing-competitor-intelligence
description: >
  Use when the user asks for battle cards, channel prices, MOQ, vs page,
  vs-page inputs, procurement path, alternative sourcing analysis,
  alternative supplier comparison, marketplace benchmarking, 战斗卡,
  渠道价, 起订量, vs 页, 采购路径, or competitor evidence for B2B trade
  decisions, including phase 1 of this repo's marketing run. Collect public
  evidence, cite every claim, write battle cards and comparison tables, and
  save them under deliverables/marketing/01-foundation/. Invent no prices or
  competitor facts. Strategy maps and ICP whitespace belong to
  `lead-competitor-analysis`. Not for SEO keyword strategy, price
  architecture, or phase navigation.
---

# 竞品情报

把公开竞品证据变成可执行的定位、销售回应和对比表，落到 `deliverables/marketing/01-foundation/`。缺证据就写缺口，不编造。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出根、工具能力化。
2. **输入**。产品与公司事实读事实源入口 `docs/fact-sources.md`，按其「什么问题查哪个源」取证；查不到标〔未证实〕，按没有处理。已有定位稿则读 `deliverables/marketing/01-foundation/` 里相关文件。完成：能指出品类、目标市场、已知对手、买家角色各依据哪几条；原文不拷进本仓库。上下文缺到无法圈定品类或市场则停并写缺口，不编造公司、价格、流量或对手事实。
3. **收集**。用 Apify 搜索查证公开页；需要原文时抓取指定 URL 的正文。默认先搜再抓；Apify 修复与替代取证后仍不可得则停止并写缺口。多域名并行时 dispatch a subagent, else do it inline。每条声明记下 URL、访问日期、摘录。完成：至少 5 家直接竞品有可访问域名；至少 3 家在目标渠道（以产品上下文为准）有价格、起订量或评价摘录，否则在缺口写明。查询清单、三层量尺、表结构或页纲要：读 `references/methodology.md`。
4. **分析**。分三层，不要混写：直接竞品（同品类、同目标市场）、替代方案（买家会换成的材料或做法）、采购路径（进口 vs 买家本地）。逐维对比规格、交期、起订量、认证、渠道、异议。每家同时写优势与弱点；战斗卡只使用已核验数据。完成：三层都有结论或显式缺口；战斗卡有可引用的话术，不是套话。
5. **落盘**。写入下方产出路径与模板。策略与分析用简体中文；面客文案、URL、字段名、文件名按产品上下文语种（默认英文文件名）。完成：主分析稿非空且 ≥ 可验证断言 5 条；表或 JSON 每行有 `source_urls`；教学支架原文零出现。

## 默认

- 本 skill 产出进 `deliverables/marketing/01-foundation/`。不要用它做完整 SEO 审计或价格架构。
- 策略×公司配额与 ICP 空白走 `lead-competitor-analysis`；本 skill 不写策略×公司配额。
- 定位句 / USP 清单走 `lead-usp-extraction`，冷邮件走 `lead-cold-email-gen`；本 skill 不写这三类。
- 数字、价格、流量、评分只来自：产品上下文、用户本轮提供、已搜索或已抓取的公开页。价格必须来自渠道列表、公开价目或 RFQ，禁止估计后写成事实。
- 目标渠道以产品上下文为准，不在本文件写死平台。
- 对手优势如实写。禁止无出处的「他们质量不行」。
- 终稿禁止占位 URL、禁止把未核验字段写成事实。缺的进缺口栏。
- 表格式交付物每行有 `source` 或 `source_urls`。

## 写法

- 先地图后深挖：先 5 家可访问域名，再补渠道页与产品页。
- 战斗卡按产品上下文的买家角色裁剪，不发明角色。
- 建议标 P0 / P1 / P2，并指向可执行页或话术，不写空泛「加强品牌」。
- 公开对比页只到内容纲要，SEO 规格走 `marketing-seo-audit`；内部战斗卡不公开。

## 产出

主文件 `deliverables/marketing/01-foundation/competitor-analysis.md`：

```markdown
# 竞争格局

- source: 台账 product_context（不粘贴原文）
- accessed:
- competitors_n:

## 摘要

## 来源

| 声明 | URL | 访问日期 | 摘录 |
| --- | --- | --- | --- |

## 直接竞品

## 替代方案

## 采购路径

## 优势与缺口

## 建议（P0 / P1 / P2）

## 可验证断言

## 下一步
```

同目录一并写入（列与 schema 见 `references/methodology.md`）：

- `competitor-profiles.xlsx` — 可从 `templates/competitor-profiles.xlsx` 复制后填行；至少 5 行；每行 `source_urls` 非空
- `competitor-profiles.json` — `competitors` 数组，字段与表一致
- `competitor-profiles.md` — 每家叙事档案
- `battle-cards.md` — 至少 3 家逐维对比与话术
- `gap-opportunities.md` — 至少 3 个产品 / 市场 / 服务缺口
- `monitoring-checklist.md` — 监控对象、频率、责任人

## 例子

> 仅供理解，禁止引用到输出。

输入只有首页口号。成稿按四栏填画像：定位（谁可买、钱怎么走）→ 品类树（品类×品牌，应用只作筛选）→ 注册墙/价格门（匿名可见规格与货号，价与库存是否登录后才开）→ 工具/学院（规划、培训、下载是否接到下单）。缺栏进缺口，不把口号扩成全貌。

输入把同一集团的企业站与商店首页摘录混在一行。成稿先画实体图再分站摘录（哪一站、哪一页、访问日期）。企业站管故事，商店管贸易词与价格门；不把企业站口号写进战斗卡渠道栏。

输入写成「都是批发，同一张表」。成稿拆层：专营光伏批发进直接竞品；电气全能批发把光伏挂在能源子目录，进采购路径，并写买家为何会两边进货。不把两层并进直接竞品表。

输入是匿名页、没有渠道价目或 RFQ。成稿只记公开机制（登录可见 / 询价），交期或评价只摘带 URL 与日期的差。支付或库存在登录墙后则写未核验。不估净价区间，不写「他们更便宜」或「我们质量更好」。

输入抄到一串问句。成稿先分桶（交易：账号、运费、退货；技术：故障、兼容），再比当场答句密度——页上作答，还是标题当路由、正文在工单或知识库。产品页无问答就记「无」，不从页脚店级 FAQ 推断产品页也有；Apify 与替代取证仍不可得记未核验，不推断有无。不把对手答句粘进战斗卡。

输入三处网点或人数口径冲突。成稿并列来源、标「来源冲突、不采用」，先定权威源再写规模。不静默取最大或最新写进优势栏。

## 易错

- 没读产品上下文就按通用营销建议开写。
- 把教学例子或模型记忆当事实。
- 只交 Markdown，漏掉已承诺的表或 JSON。
- 用占位域名或编造价格区间。
- 只写对手优势或只写弱点。
- 三层竞品混在一张表里。
- 只看官网首页，不核验目标渠道与产品页。
- 复制对手营销句，而不是基于摘录分析。

## 清单

- [ ] 已读共用规则与 `product_context`，原文未拷进本仓库
- [ ] ≥5 家直接竞品有可访问域名；≥3 家有目标渠道价格或起订量摘录，否则已写缺口
- [ ] 每条价格与对外建议有 URL 与访问日期
- [ ] 每家同时有优势与弱点；战斗卡话术能回溯摘录
- [ ] 产出在 `deliverables/marketing/01-foundation/`；表或 JSON 行含 `source_urls`
- [ ] 终稿无占位 URL；教学例子原文未进入交付物
- [ ] 工具只写能力；需要隔离时为 dispatch a subagent, else do it inline
