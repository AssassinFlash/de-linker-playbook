---
name: marketing-content-strategy
description: >
  Use when the user asks for content strategy, editorial calendar, blog
  strategy, topic clusters, content gap, content calendar, B2B content
  marketing, trending topics, 内容策略, 内容日历, 选题集群, 内容缺口,
  编辑日历, or 外贸内容营销. Audit competitor blogs and public pages, map
  buyer questions onto four pillars, score gaps, and write a sourced
  editorial calendar with topic clusters under
  deliverables/marketing/03-content/. Read the ledger product_context first;
  invent no engagement metrics, search volumes, or competitor URLs. Never
  paste skill examples into the output. Not for drafting conversion copy,
  technical SEO audits, social-channel post batches, or phase navigation.
---

# 内容策略

根据已读产品上下文与可验证公开来源，做竞品内容审计、缺口与选题集群，写出可执行的编辑日历，落到 `deliverables/marketing/03-content/`。不写转化文案定稿，不做技术 SEO 审计。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出根、工具能力化四条。
2. **输入**。读台账 `state/status.md` 的 `product_context`（缺省 `~/Documents/New/CONTEXT.md`；把 `~` 展开为主目录，不当相对路径）。需要参数再读同目录 `fact-base/`。上游若存在则读 `deliverables/marketing/01-foundation/` 与 `deliverables/marketing/02-seo/seo-audit.md`。已有内容清单（博客、产品页、视频、案例、渠道表现）一并列入。完成：能指出品类、目标市场、买家角色、差异化各依据哪几条；原文不拷进本仓库。缺到无法圈定品类或市场则停并写缺口，不编造公司、流量、互动数或竞品事实。
3. **采集**。用网页搜索查证竞品内容、买家问题与趋势；需要原文时抓取指定 URL 的正文。默认一条能力，不并列多引擎。搜索不可用则停止并写缺口。多站点并行时 dispatch a subagent, else do it inline。查询意图、最低条数与校验见 `references/methodology.md`。完成：每条证据有 URL、摘录、访问日期；文章审计达到最低条数，或已把未达标项写入缺口。
4. **分析**。只从已采集证据推导四支柱、缺口、选题集群、角色映射与选题评分。量表、集群结构与表列见 `references/methodology.md`。完成：每个缺口有 ≥2 条来源证明竞品覆盖弱或缺失；每个推荐选题能映射到真实检索词或已观察的买家问题；四支柱与四个漏斗阶段均有着落或显式缺口。
5. **落盘**。写入下方路径。完成：主文档与工作簿非空；表每行 `source` 非空且含 URL；日历有具体 `publish_date` 并对齐已核验的行业周期；教学支架原文零出现；文末 5–10 条可验证断言。

## 默认

- 策略与分析用简体中文；URL、字段名、target keyword、文件名用英文。面客短句跟产品上下文的面客语种，同一段不混用。
- 目标渠道以产品上下文为准，不预设某一电商或社交平台。产品上下文未列的频道记缺口，不编造互动或粉丝数。
- 日历日期对齐产品上下文中的展会、采购旺季或已核官方源的行业周期，禁止只写「某月更新」。
- 数字、搜索量、阅读/播放量只写观察到的值；没有就写「公开源未找到」，禁止估计后写成事实。
- 缺来源或搜索不可用：停止并写缺口，不编造。

## 写法

- 标题必须带具体检索词或场景，不用空的行业洞察、市场趋势当题。
- 格式建议必须能对照资产与专业：无图/视频、无审批带宽则不要把视频或工厂参观标成 P0。
- 角色从产品上下文取；上下文没有则在采购、承包、指定人、经销、质量/合规里选最贴近的一档，并标明「角色未在上下文出现，暂用」。不要用 C 端消费者口吻。
- 缺口必须同时写 recommended format 与 why-now，不只列题。
- `source` 写具体 URL，不写空的工具名。
- P0 数量受资源约束；不把高投入项全部标成必须做。

## 产出

路径：

- `deliverables/marketing/03-content/content-strategy.md`
- `deliverables/marketing/03-content/content-strategy.xlsx`（从 `templates/content-strategy.xlsx` 复制后填；不能写表时改同目录 `content-strategy.json`）
- 按需同目录：`content-calendar.md`、`topic-clusters.md`、`content-briefs.md`、`channel-distribution-plan.md`

章节与表列、最低行数见 `references/methodology.md`。

```markdown
# 内容策略

- source: 台账 product_context（不粘贴原文）
- accessed:
- collected:

## 内容诊断

## 支柱与选题集群

## 内容缺口

## 渠道分发

## 行动清单（P0 / P1 / P2）

## 缺口

## 可验证断言
```

工作簿三表：Content Calendar（≥30 行）、Topic Clusters（≥5 行）、Content Gap Analysis（≥15 行）。每行 `source` 非空。禁止只交空模板。

## 例子

> 仅供理解，禁止引用到输出。

用户要「三个月内容日历」。写成带 `publish_date` 与买家检索词的具体标题，并在 `source` 栏放已抓取 URL；不写无日期的「行业洞察合集」，也不把本节句子粘进交付物。日历日期对齐已核周期这一条，调研材料不替代，故保留本支架。

输入写「按 arena / energy infrastructure 分三个选题集群」。成稿应按目标市场批发货架已核验的品类树分集群（住宅存储、工商业存储各一棵，支持页再按耦合或户内外），支柱页用行业词（如 Heimspeicher / Gewerbespeicher 或其面客语种对译）；不要用自造品类名当分面。

输入写「做一期把买家会问的都列上的 FAQ 日历」。成稿按已观察问句分桶：交易与账号、到货与验收、保修路由、技术诊断分属不同集群与漏斗阶段；店级采购发货问不进产品页集群。问句多、当场零答句的索引页记缺口——路由页不是教育支柱。产品页相邻选题只收订货疑虑与临门一脚（下单前已有的交付阻碍），不收升档问、种下的疑虑、选型作文。

输入把竞品「知识世界 + 学院 + 工具箱」整站标成必须对标的博客量。成稿只借结构：每个知识世界 = 支柱页 + 主题夹 + 可复用工具块；没有对应资产则标缺口，不把 webinar 或对比表标成 P0。工商业教育支柱按已核验用例写支持页（自用、削峰、分时缓冲、备电），不要写成空的行业洞察。

输入把「自有质保平台 / 工厂参观」写成 Trust 支柱必做项。成稿改成保修路由与履约可见的已核验流程（谁受理、谁赔付、要交什么材料）；不把未证实的自有质保、库存或时效承诺当选题。

输入把集群标题写成中英混用的制度词或自造复合词。成稿：同一货架按面客语种用该市场行业词对（Home storage / Heimspeicher），假朋友不进日历题。

## 易错

- 没读产品上下文就套通用内容日历。
- 跳过竞品内容审计，或用 Competitor A/B/C 占位。
- 编造互动数、搜索量或竞品 URL。
- 日历无具体 `publish_date`，或日期未对齐已核验周期。
- 推荐团队无法产出的格式。
- `source` 只写搜索、不附 URL。
- 集群只列标题，不写支柱页路径与内链。
- 把教学例子或无来源假设当事实。
- 只交 Markdown、工作簿仍是空模板。

## 清单

- [ ] 已读共用规则与 `product_context`，原文未拷进本仓库
- [ ] 竞品内容审计 ≥5 家且每条有 URL；文章/缺口达到最低条数或已写缺口
- [ ] 每个缺口 ≥2 条来源；每个推荐选题有检索词或已观察问题
- [ ] 四支柱与 Awareness / Consideration / Decision / Retention-Referral 均有覆盖
- [ ] 日历有具体日期并对齐已核验周期；P0/P1/P2 可执行
- [ ] 主文档与工作簿在 `deliverables/marketing/03-content/`；`source` 无空值
- [ ] 文末 5–10 条可验证断言；教学例子原文未进入交付物
