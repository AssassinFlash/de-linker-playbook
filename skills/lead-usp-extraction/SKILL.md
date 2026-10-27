---
name: lead-usp-extraction
description: >
  Use when extracting USPs, unique selling points, differentiation, competitive
  advantage, gap analysis, value proposition, proof kit, 卖点提炼,
  差异化, 竞争优势, or 外发定位短句. Run a seven-step competitive differentiation
  pipeline: niche and persona, competitor map, UVP mining on seven axes, gap
  matrix, capability overlay, differentiator options, then an outreach
  positioning line plus proof kit. Match each USP to an ICP for outreach.
  Read the ledger product_context and upstream ICP, positioning, or competitor
  files when present; invent no competitor claims. Not for writing full email
  sequences, SEO pages, ICP research itself, or the Kotler product-positioning
  document.
---

# USP 提炼（竞品差异化）

从产品上下文和已有 ICP/竞品材料跑七步差异化管线，产出可对外使用的定位短句、USP 清单和证据包。写入 `deliverables/lead/05-usp/`。步骤 1 为输入；步骤 2–8 即七步管线（利基与买家 → 竞品盘点 → UVP 挖掘 → Gap 矩阵 → 能力叠加 → 差异化方案 → 定位与证据包），对应 `references/seven-step-pipeline.md` 步骤 1–7；步骤 9 为 USP-ICP 匹配并落盘。逐步字段、轴定义与重跑规则见 `references/seven-step-pipeline.md`、`references/gap-matrix-template.md`。

## 步骤

1. **输入**。产品与公司事实读事实源入口 `docs/fact-sources.md`，按其「什么问题查哪个源」取证；查不到标〔未证实〕，按没有处理。存在则读 `deliverables/lead/01-icp/icp-analysis.md`、`deliverables/lead/04-market/competitor-positioning.md`、`deliverables/lead/04-market/market-analysis.md`。存在 `deliverables/marketing/01-foundation/product-positioning.md` 则读入，后续外发短句与证据不得与其矛盾。记下品类、可做菜单（3–6 项）、目标区域、已知能力数字、定位偏好（成本效率 / 灵活伙伴 / 溢价共创）。缺关键项时本轮最多问两问。完成：能指出买家、可做产品和已知优势各依据哪几条陈述；原文不拷进本仓库。上游文件缺失则在交付物标缺口，不编 ICP。

2. **利基与买家**。已有批准的 `deliverables/lead/01-icp/` 则摘编其决策人/痛点作买家卡片，不另开利基短名单。TAM / CAGR 有 `deliverables/lead/04-market/market-analysis.md` 则引用，不另估；该稿也没有则标「未在来源出现」。只补本步仍缺的进入容易度等字段（无来源同样标「未在来源出现」）。无批准 ICP 时才做微利基短名单表：利基 | TAM | 3 年 CAGR | 需求驱动 | 进入容易度/100（附一句依据）| 致命缺陷。推荐一个利基，写市场动态、价值链、进入壁垒。此时才写买家卡片：职位、KPI、日常、痛点、触发、交易破裂点。列 2–3 个不选的利基及红旗。默认：有来源的进入容易度 <60 或 CAGR <5% 不推荐；产品上下文已锁定的利基只记分数、不拒绝。完成：推荐利基与买家卡片齐全（有上游则引用、不重开）；无来源的 TAM/CAGR 写「未在来源出现」。

3. **竞品盘点**。已有 `deliverables/marketing/01-foundation/competitor-analysis.md` 或 `deliverables/lead/04-market/competitor-positioning.md` 时，复用已核验名单与摘录，不从零找 15 家；不足再补。七轴 UVP 与我方行仍按步骤 4、6 补全。无现成名单时，在该利基与区域找目标 15 家，默认大（>$500M）/中（$50–500M）/小（<$50M）各 5。营收用最近已披露财年并写年份。每家：HQ、营收、旗舰、渠道、最近战略动作、官网。写约 150 词格局评论，以及竞争强度（有份额才算 HHI，否则定性高/中/低并说明）。完成：表内每家有可访问官网或已标 unverified。不足 15 家或美元档不适用时，按该利基相对体量分在位者 / 挑战者 / 利基商，写明分档依据与缺口，不拿无关公司凑数。

4. **UVP 挖掘**。以竞品稿（`deliverables/lead/04-market/competitor-positioning.md` 或 `deliverables/marketing/01-foundation/competitor-analysis.md`）的 Key Selling Points 为 UVP 种子；七轴已覆盖的公司不重抓官网。缺轴的公司才用 Apify 搜索查证，再抓取官网首页与 About（或等价页）正文。需要评价或证书时再搜一次并抓取能打开的来源页。每家最多 4 条 UVP，标 Explicit Claim 或 Implied Proof，打七轴标签（Speed, Cost, Quality, Customization, Sustainability, Service, Digital Tool；对不上的标 Other），附 5–12 词摘录或 URL 片段。写约 120 词热力：哪些轴过挤、哪些被冷落。完成：每条 UVP 能指回竞品稿或已抓取原文；抓不到的公司标 unverified，不编 UVP。Apify 修复与替代取证后仍不可得则停止并写缺口。

5. **Gap 矩阵**。行=公司，列=七轴；该轴 ≥1 条 UVP 为 check，沉默为 —。覆盖 ≥70% 为过挤轴，≤30% 为空白轴。空白轴必须对照买家痛点；买家卡片或 ICP 未提到的不记为机会。完成：矩阵与过挤/空白两节都有；空白轴有交叉引用。符号与阈值见 `references/gap-matrix-template.md`。

6. **能力叠加**。用用户真实数字填「我方」行：交期、MOQ、不良率、证书、独特工艺、可持续资质。缺数据标 `?`，不假设。符号：明显优于该轴领先者 `double-check`；跟上 `check`；沉默 `—`；差于领先者 20% 以上 `cross`；无数据 `?`。对每个 `cross` 写瓶颈（人 / 设备 / 政策 / 供应链）。空白轴里，已有优势或 ≤6 个月可达到的标为快赢。完成：我方行全部有符号；快赢列表非空，或明示无快赢及原因；强但易被抄的轴写入风险说明。

7. **差异化方案**。每个快赢给 3 个选项（服务承诺、技术附加、担保、内容资产、可持续角度等）。每项写 Buyer Impact（H/M/L + 拉动的 KPI）、Ease（Easy / Moderate / Hard）、Cost Band（$ / $$ / $$$）、Time-to-Market（≤30 天 / 1–3 月 / 3–6 月 / >6 月）、Imitation Barrier（Thin / Moderate / High）。排出 Top-3，写为何第 1 优于 2–3，并标 P0 / P1 / P2。完成：选项不超过用户已陈述的能力、预算与合规；未陈述的约束标待补，不发明预算。

8. **定位与内容**。一句外发定位短句 ≤14 词，含主差异化 + 买家 KPI。此短句供外发使用；公司定位句以 `deliverables/marketing/01-foundation/product-positioning.md` 为准，二者不得矛盾。说服层：Hook → Pain Amplifier → Proof → Risk-Reversal → CTA。证据包按说服力排序，每项标已有或待补（指标截图、案例短故事、证书、省钱测算、45 秒产线视频、质保条款等）。冷邮件草稿走 `lead-cold-email-gen`，本步不写邮件；本 skill 只产 USP 与证据包。30 秒价格异议话术：镜像句 → 校准问句（How would you ...）→ 有条件让步。完成：面客文字用买家语言（缺省英语），分析用语跟本轮；证据包无未标明的虚构材料。

9. **匹配并落盘**。产出 4–6 条 USP，类型用实际用到的：产品级 / 运营 / 信任 / 战略价值。每条：Headline → Buyer Angle → Proof → 目标 ICP → Competitive Frame（Unlike many suppliers who [常见弱点], you offer [优势]）。一封外发信一条主 USP。按下方模板写入 `deliverables/lead/05-usp/usp-strategy.md` 与 `deliverables/lead/05-usp/usp-matrix.xlsx`（写不了 xlsx 则同目录 `usp-matrix.csv`，列相同）。完成：主报告非空；矩阵每行有 `data_source`；教学例子原文零出现。

## 默认

- 查证用 Apify 搜索；需要原文时抓取指定 URL；Apify 修复与替代取证后仍不可得则停止并写缺口，不编造。
- 数字、营收、证书、评价只来自：产品上下文、用户本轮、搜索结果或已抓取正文。交付物写 URL 与访问日期。
- 公开源常无 TAM / CAGR / HHI；来源未出现则标「未在来源出现」，禁止用训练记忆或同业近似值填数字。
- 面客句跟目标市场习惯，不把同一稿用于所有区域。
- 重跑：有 30 天市场或转化反馈后从步骤 5；新进入者或并购从步骤 3；产品菜单变了从步骤 2。
- 冷邮件走 `lead-cold-email-gen`；本 skill 只产 USP 与证据包。公司定位句以 `deliverables/marketing/01-foundation/product-positioning.md` 为准；本 skill 的 ≤14 词短句供外发用，二者不得矛盾。

## 写法

- 每条 USP 必须能指出改善买家哪一项 KPI。只列证书或参数、不接买家结果的，不算完成。
- 空白轴只在「竞品公开材料确实未主张」且「买家在乎」时成立。
- 排序看模仿壁垒：交期体系、工艺、合规与可核验数据排前，单纯降价排后。
- 竞品「说过」记 Explicit Claim，「被第三方证明」记 Implied Proof，二者不混成同一格。
- 不同 ICP 不复用同一套 USP 主句。OEM 偏定制与共创，分销商偏毛利与售卖支持。

## 产出

主文件 `deliverables/lead/05-usp/usp-strategy.md`。表 `deliverables/lead/05-usp/usp-matrix.xlsx`（写不了 xlsx 则同目录 `usp-matrix.csv`；列名英语 snake_case）。分析段落用本轮语言；外发定位短句、证据包面客句、话术用买家语言。

```markdown
# USP Strategy Report — {品类} × {市场}

- source: 台账 product_context（不粘贴原文）
- accessed:

## 1. Micro-Niche & Buyer Persona
### Short-List of Micro-Niches（有上游则引用，不重开）
### Recommended Niche (Deep Dive)
### Buyer Persona Card（有上游则引用，不重开）
### No-Go Niches

## 2. Competitive Intelligence
### Competitor Table
### Strategic Patterns Commentary
### Competitive Intensity Gauge

## 3. Competitor USP Mining
### Company-by-Company UVP Blocks
### Cross-Competitor Heat-Map Summary

## 4. Gap Matrix
### Coverage Matrix
### Over-Served Axes
### Under-Served Axes / White-Spaces

## 5. Capability Overlay
### Annotated Matrix (Us Included)
### Diagnostic Commentary
### Risk Note

## 6. Differentiator Options
### Opportunity-by-Opportunity Table
### Prioritised Short-List (Top-3)

## 7. Positioning & Content
### One-Sentence Positioning Line
### Persuasion Layer-Cake
### Proof-Kit Checklist
### 30-sec Price Push-Back Talk-Track

## 8. USP-ICP Matching Matrix
### USP × ICP mapping table
### Per-ICP recommended lead USP

## 搜索日志
| 查询或 URL | 日期 | 结论 |
```

`usp-matrix.xlsx`（或 `.csv`）两段（或两个文件）：

- 竞品：`company_name, size_tier, speed, cost, quality, customization, sustainability, service, digital_tool, data_source`
- USP：`usp_headline, usp_type, buyer_angle, proof, target_icp, competitive_frame, priority`

目标：竞品行 = 已核验名单（目标 15），USP 行至少 4。

## 例子

> 仅供理解，禁止引用到输出。

借定位对照公式和「配对语言 vs halo」的取证形状；下列句子禁止写入交付物。

输入写「一线品牌、无缝兼容」→ 成稿应改成：该组合是否出现在厂家现行清单（文件 + 版本 + 日期），缺一边标单向；而不是把厂家自我超级形容词继承成我方 USP。四种证据状态（已列入 / 单向 / 双方未列入 / 封闭无配对）不要压成 Headline 里的「兼容」。

输入写「一站式批发」→ 成稿应改成：For〔买家〕who〔兼容/交付/质保风险〕, 〔你〕is the〔品类〕that〔可核验动作〕. Unlike〔自称 Großhändler / Hersteller、服务只在页脚的目录商〕that〔交货后沉默〕, you〔跟到哪一步〕。H1 追溯不到这句就删。未在产品上下文确认的能力不进定位。

UVP 条目形状：`公司 — 主张 (**轴, Explicit|Implied**) — 「5–12 词摘录」— URL`。About 页奖项 = Explicit Claim / Quality，不是 Implied Proof；登录墙后的价格不是可引用的 Cost UVP。标题只占批发/制造、服务当附加时，Service 轴记沉默，不要把学院或网店工具记成 Service 覆盖。

证书接到买家 KPI 才算 USP：不要停在「有某项认证」，要写清它降低哪项采购风险，且数字来自产品上下文或已抓取页。

定位句形状：主差异化 + 买家 KPI，≤14 词。目录商已占用的品类口号不算差异化。

不同 ICP 不共用主句：安装商落到配对核验与备份供应商；规划/采购型买家落到可核验清单与投标材料。自己已是分销层时，二阶转售商不是客户，不给这层写 USP。身份越界（把厂家质保签发人、现场安装方写成我方）直接作废。

## 易错

- 用模型记忆填竞品格，而不是已抓取页。
- 把无人在乎的沉默轴叫作空白机会。
- 不同 ICP 共用同一条主 USP。
- 推荐超出已陈述能力或预算的差异化。
- 核验失败仍编 UVP，而不是标 unverified。
- 在本 skill 起草冷邮件，而不是交给 `lead-cold-email-gen`。
- 外发短句与 `product-positioning.md` 定位句互相矛盾。

## 清单

- [ ] 已读 `product_context`；上游缺失已标缺口；有 `product-positioning.md` 已读入且短句不矛盾
- [ ] 七步管线（步骤 2–8）按序有各自交付物；买家卡片在步骤 8 被再次使用
- [ ] 竞品均为已核验或 unverified；无来源营收 / TAM / CAGR / HHI 未编造
- [ ] Gap 矩阵七轴齐全；空白轴对照过买家痛点
- [ ] 我方行用真实数字或 `?`；Top-3 含 Impact / Ease / Cost / Time / Imitation
- [ ] 外发定位短句 ≤14 词；冷邮件未在本 skill 起草
- [ ] 每条 USP 映射至少一个 ICP，且有 Buyer Angle 与 Competitive Frame
- [ ] 搜索日志有 URL 与日期；例子原文未进入交付物
- [ ] 文件在 `deliverables/lead/05-usp/usp-strategy.md` 与 `usp-matrix.xlsx`（或 `.csv`）
