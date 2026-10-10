---
name: marketing-copywriting
description: >
  Use when copywriting, product description, ad copy, email copy,
  landing page copy, social copy, video script, conversion copy, value
  proposition, headline, landing-page hero, 文案, 产品描述, 广告文案,
  邮件文案, 社媒文案, or 价值主张, including phase 3 content. Audit
  competitor messaging, extract buyer language, and write a sourced
  copy library plus homepage, product-page, ads, email, social, and
  video snippets under deliverables/marketing/03-content/copywriting/.
  Read the ledger product_context first; invent no numbers or
  testimonials; never paste skill examples into the output. Not for
  polishing an existing draft, SEO audits, competitor battle cards,
  outreach sequences, social calendar, or phase navigation.
---

# 营销文案

根据已读产品上下文与可核验公开页，写转化导向的 B2B 外贸文案框架与可复用文案库，落到 `deliverables/marketing/03-content/copywriting/`。缺证据标缺口，不编造。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出根、工具写能力。
2. **输入**。读台账 `state/status.md` 的 `product_context`（缺省 `~/Documents/New/CONTEXT.md`；把 `~` 展开为主目录，不当相对路径）。需要参数再读 `~/Documents/New/fact-base/`。上游若存在则读：`deliverables/marketing/01-foundation/` 的定位与竞品稿、`deliverables/marketing/02-seo/` 的关键词与意图、`deliverables/marketing/03-content/` 里已有买家话术。用户本轮给出的首页、产品页、目标渠道页或邮件基线一并读。完成：能指出受众、差异化、证据、语气各依据哪几条；原文不拷进本仓库。品类或受众缺到无法下笔则停并写缺口。
3. **收集**。用网页搜索查证竞品标题、价值主张、信任信号与买家话术；需要原文则抓取指定 URL 的正文。先抓竞品产品页、用户基线、品类外对标页，再搜做法与公开评论。多页并行时 dispatch a subagent, else do it inline。搜索不可用则停止并写缺口，不编造竞品原文。查询意图与最低条数见 `references/methodology.md`。完成：≥10 条竞品产品描述、≥5 条高转化 B2B 文案要素、≥3 条目标渠道（以产品上下文为准）列表页、≥20 条买家话术，每条有 URL 或摘录；不足则再搜一轮或在缺口写明。
4. **分析**。按审计量表给已抓页面打 1–5 分；抽出标题公式、信任信号、CTA、语气；标出对手没说、我们有证据能说的角度；按渠道画出漏斗角色与字数约束。角色只取产品上下文；上下文没有则在采购、指定人、承包、经销、进口商里选最贴近的一档，并标明「角色未在上下文出现，暂用」。量表、页面骨架、跨渠道地图见 `references/methodology.md`。完成：≥5 家竞品有结构化评分与 `source_url`；每个推荐框架能回溯一条已分析页；差异化角度有对应证据或已标缺口。
5. **落盘**。写入「产出」所列文件。首页与产品页草稿按「写法」起稿后跑完七轮审查；未知数字在文案库用 `[待补充]`，终稿面客段禁止残留 `{{...}}`，缺事实写「未在上下文出现」。完成：主策略稿与文案库非空；表行列达到下方断言；教学支架原文零出现。用户明确收窄范围时，未做附件列入缺口，不算全量完成。

## 默认

- 产品事实只读 `product_context`（需要参数再读 `~/Documents/New/fact-base/`），不在本仓库另存档案。
- 默认渠道写「目标渠道（以产品上下文为准）」，不预设某个平台。
- 数字、证书、案例、项目名、产能、交期、价格：产品上下文或已抓取页里有才写。没有就写「未在上下文出现」或 `[待补充]`，禁止补造。
- 禁止编造统计、客户引言、项目细节、未持有的认证、满意度或复购率。
- 语气：直接、具体、可核验。不用 DTC 口语，不用注册 / 免费试用 / 订阅口吻。下一步用「要规格 / 要报价 / 要样品」。
- 贸易术语（FOB、CIF、T/T、L/C）与平台保障、第三方检测：产品上下文确有才写进 CTA 或列表页。
- 查证用网页搜索；需要原文时抓取指定 URL。用户已配置采集服务时，可用它抓公开页。不写工具 ID。
- 精修已有成稿走 `skills/marketing-copy-editing/SKILL.md`（文件存在时）。对手战卡走 `skills/marketing-competitor-intelligence/SKILL.md`（文件存在时）。本文件不写 SEO 审计。
- 邮件/社媒片段是跨渠道语气片段银行，不是可发送战役；序列走 `marketing-email-outreach`，日历与平台原生成稿走 `marketing-social-content`。
- 产出只进 `deliverables/marketing/03-content/copywriting/`。

## 写法

- 先结果后规格：规格必须接到买家可感到的项目结果，不堆特性。
- 空话（high quality、world-class、leading）无证据则删或改成可核验能力。
- 短句、主动语态；删 almost / very / really；B2B 正文不用感叹号。
- 页面骨架：首屏标题 → 副标题 → 主 CTA；其下信任条、痛点、能力与好处、流程、项目组合、异议、末屏 CTA。细节见 `references/methodology.md`。
- CTA 公式：`[行动动词] + [对方得到什么] + [限定]`。询盘、样品、报价、规格，不用 Sign Up / Get Started。
- 七轮按序：清楚 → 语气 → 所以呢 → 证明 → 具体 → 情绪（风险下降与职业声誉，不编事故）→ 零阻碍。每轮后回扫上一轮。漏斗优先轮次见 `references/methodology.md`。
- 跨渠道：首页管到访→询盘；产品页管询盘→样品；目标渠道列表页管高意图询盘；广告、冷邮件、社媒、视频各用该渠道字数与一条 CTA。地图必覆盖的八个渠道见 `references/methodology.md`。
- 面客语种以产品上下文为准；用户点名双语再出对照，同一段不混用。品类名、材质、认证一篇一译并锁定。

## 产出

目录：`deliverables/marketing/03-content/copywriting/`

主文件 `copywriting-strategy.md`：

```markdown
# 文案策略

- source: 台账 product_context（不粘贴原文）
- accessed:
- competitors_n:
- personas:

## 摘要

## 来源

| 声明 | URL | 访问日期 | 摘录 |
| --- | --- | --- | --- |

## 竞品文案审计

## 文案差距

## 文案框架

## 关键词与话术

## 跨渠道地图

## 建议（P0 / P1 / P2）

## 可验证断言

## 缺口

## 下一步
```

同目录一并写入（列与 schema 见 `references/methodology.md`）：

- `copy-library.xlsx` — 可从 `templates/copy-library.xlsx` 复制后填行；不能写表时改同目录 `copy-library.json`
- `homepage-copy.md` — 首屏价值主张、信任条、主 CTA；文末含七轮检查节
- `product-page-copy.md` — 产品页模板与首批产品线文案；文末含七轮检查节
- `channel-listing-copy.md` — 目标渠道列表页：标题公式、子弹点、信任信号、贸易条款
- `cta-variations.md` — ≥8 个场景（询盘、样品、目录、报价、案例、验厂、规格、交期）
- `email-template-snippets.md` — 首封、跟进、培育语气片段；不可直接发送，不按角色出成套模板
- `social-copy-snippets.md` — 钩子与正文语气片段；不可直接发送，不按角色出成套模板
- `video-hook-snippets.md` — 开场钩子 + 一句话价值

断言（未满足则不算全量完成）：

- 竞品审计 ≥5 家，每家 `source_url` 非空
- Copy Templates ≥15 行；Competitor Copy Audit ≥10 行；Power Phrases ≥20 行；每行 `source` 或 `source_url` 非空
- `channel` 只取 `references/methodology.md` 的枚举
- 跨渠道地图覆盖八个必选渠道
- 首页与产品页无 SaaS CTA，无未解释占位符
- 含数字的声明有来源或 `[待补充]` / 「未在上下文出现」
- 教学支架原文零出现

## 例子

> 仅供理解，禁止引用到输出。

形状借自竞品侧定位句、禁套话与 NEVER-SAY；New 页面文案已过时，只借「卡内无则不写」和「不种新疑虑」，不借页面句子。

输入写「一站式 / 跳过中间商 / 我们是桥梁」。成稿应改成：目录批发卖箱子、交货后沉默 vs 工程伙伴做工程 BOM、配对核验、调试支持与厂家质保协调。不要套 one-stop shop / skip the middleman / we are your bridge。库存数量、到货天数、自有仓不当卖点。

输入写「缩短采购周期、品质可靠」或「行业领先 / tier-1 / proven」。成稿改成上下文里可核验的动作与后果；没有数字或项目就写「未在上下文出现」，不写「行业领先的一站式高品质交付」，不借厂家光环形容词。

输入写「我们生产 / 自有质保 / 我们安装 / 我们的监控平台」。成稿改成身份边界内的话：协调厂家质保与 RMA、调试支持（不登屋顶）、证书来自公告机构。不要写成制造商、备件库或承保方。

输入用自造品类名，或把 BESS、hybrid 当全系标签。成稿用行业已有品类名；hybrid 只指逆变器，BESS 不覆盖全系。不要照抄竞品原句。

输入把家族共性写成「本机独有」，或用 FAQ 种出保修金额、退款、换型升档。成稿只写卡内差异，只清下单前已有阻碍。没有来源的人名证言不编，内部证言稿不当真实形状。

CTA 用「要规格 / 要报价 / 要样品」，不用「立即开始」或注册/试用口吻。不要把本节句子粘进交付物。

## 易错

- 没读产品上下文、没抓竞品页就发明框架。
- 把教学例子或模型记忆当事实。
- 编造统计、客户引言、证书或项目。
- 抄对手原句，而不是分析角度。
- 忽略买家角色，用同一套句子面对指定人与经销商。
- 用注册、试用、订阅口吻写贸易询盘。
- 终稿残留 `{{...}}` 或把文案库的 `[待补充]` 假装成已核实数字。
- 推荐框架却不写收集阶段来源。
- 默认某个电商平台当唯一渠道。
- 把本文件当文案精修器，跳过七轮或该走审查 skill 的成稿。

## 清单

- [ ] 已读共用规则与 `product_context`，原文未拷进本仓库
- [ ] ≥10 条竞品产品描述、≥20 条买家话术，每条有来源；缺搜索已停并写缺口
- [ ] ≥5 家竞品有评分与 `source_url`；每个模板能回溯一条已分析页
- [ ] 首页与产品页已跑七轮；无 SaaS CTA；无未解释占位符
- [ ] 文案库三表行数达标，`source` / `source_url` 无空值
- [ ] 跨渠道地图覆盖八个必选渠道；CTA 与漏斗阶段匹配
- [ ] 贸易术语仅在上下文确有时出现；数字未编造
- [ ] 文件在 `deliverables/marketing/03-content/copywriting/`
- [ ] 教学例子原文未进入交付物
- [ ] 工具只写能力；需要隔离时为 dispatch a subagent, else do it inline
