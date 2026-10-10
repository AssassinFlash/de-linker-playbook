# 营销文案方法

字段级查询、审计量表、页面骨架、跨渠道地图、文案库列与质量闸门。确认本 skill 适用后再读。

## 目录

- [输入](#输入)
- [收集](#收集)
- [审计量表](#审计量表)
- [原则与风格](#原则与风格)
- [页面骨架](#页面骨架)
- [跨渠道地图](#跨渠道地图)
- [七轮与漏斗](#七轮与漏斗)
- [角色校准](#角色校准)
- [文案库列](#文案库列)
- [JSON](#json)
- [执行附件](#执行附件)
- [反模式](#反模式)
- [质量闸门](#质量闸门)
- [可验证断言](#可验证断言)

## 输入

读这些（存在才读，不复制进本仓库）：

- 台账 `product_context`（缺省 `~/Documents/New/CONTEXT.md`）
- 需要参数时 `~/Documents/New/fact-base/`
- `deliverables/marketing/01-foundation/product-positioning.md`
- `deliverables/marketing/01-foundation/competitor-analysis.md`
- `deliverables/marketing/02-seo/` 下关键词与意图稿
- `deliverables/marketing/03-content/` 里已有买家话术或内容策略
- 用户本轮给出的当前页 / 邮件 / 列表页基线

无产品上下文则停并写缺口。已有文案策略时：只总结哪些节已填，问用户刷新哪几节，不整文件覆盖。

## 收集

默认一条能力：用网页搜索查证。需要原文时抓取指定 URL 的正文。搜索不可用则停止并写缺口，不编造、不并列多引擎菜单。用户已配置网页采集服务时，可用它抓公开页。

多域名并行时 dispatch a subagent, else do it inline。

把产品上下文的品类与目标市场代入下列意图，每条记下 URL、摘录、访问日期：

1. 具名竞品产品页：标题公式、价值主张、信任信号、CTA、语气、技术具体程度
2. 第二、第三家竞品产品页或落地页（同上）
3. 品类外、同为 B2B 制造的高转化产品页（对标结构，不抄品类话）
4. 用户当前页基线（有 URL 才抓）
5. 目标渠道（以产品上下文为准）上的列表页标题、子弹点、徽章、贸易条款
6. 当前年份的 B2B 制造产品页文案做法
7. 该品类产品描述的公开写法
8. 公开询盘、评论、职业主页帖里的买家原话

### 最低条数

- 10 条竞品产品描述（结构 + 信息角度 + `source_url`）
- 5 条高转化 B2B 文案要素（具体手法 + 来源）
- 3 条目标渠道列表页（标题公式、子弹点、信任信号 + 来源）
- 20 条买家话术（短语 + 来源）
- 从已分析页抽出的标题公式与 CTA 模式（带来源）

每一条文案模板必须能回溯至少一条真实已分析页。禁止用模型记忆填竞品原文。模板里的证明点用 `[待补充]` 或产品上下文已核验数据，不用示意数字。语气判断必须引用已抓页面的原句，不写印象。

## 审计量表

对每个已抓页面按 1–5 分，并引用 `source_url`：

| 维度 | 完成条件 |
| --- | --- |
| 标题清楚 | 价值在约 10 词内说清 |
| 具体 | 真数字 vs 空话 |
| 买家话 | 用买家实际用词 |
| 信任信号 | 认证、项目、产能有出处 |
| CTA | 有行动 + 对方得到什么 |
| 技术可信 | 规格准、过程可看 |

写入策略稿「竞品文案审计」与文案库 Competitor Copy Audit。

## 原则与风格

- 规格接到项目结果，不堆特性。
- 能核验的天数、认证、市场名，优于空的 hassle / quality。
- 先写结果，再用规格与过程支撑。
- 句子短、主动；删程度副词；B2B 不用感叹号。
- 禁用注册、免费试用、订阅、Get Started。
- 贸易术语与保障条款：仅当产品上下文或已抓渠道页确有。

## 页面骨架

首屏：标题 → 副标题 → 主 CTA。

| 区块 | 作用 |
| --- | --- |
| 信任条 | 认证、项目数、年限、服务市场（有才写） |
| 买家痛点 | 表明懂对方的采购现实 |
| 能力与好处 | 规格接到项目结果 |
| 流程 | 降低复杂度（到访 → 询盘 → 样品 → 下单） |
| 项目组合 | 已完成项目的可视证据 |
| 异议 | 交期、起订量、定制、付款 |
| 末屏 CTA | 重述价值 + 降风险下一步 |

CTA 公式：`[行动动词] + [对方得到什么] + [限定]`。

## 跨渠道地图

每个渠道写漏斗角色、文案重点、字数或形态约束、至少一条 `source`。必覆盖下列八个；培育邮件可另加。

| 渠道 `channel` | 漏斗 | 文案重点 |
| --- | --- | --- |
| homepage | 到访 → 询盘 | 首屏价值主张 + 信任条 |
| product_page | 询盘 → 样品 | 规格转好处 + 异议 |
| target_channel | 高意图询盘 | 标题公式 + 子弹点 + 贸易条款 |
| search_ads | 高意图点击 | 标题与描述按该平台当前字数上限 |
| social_ads | 认知 → 询盘 | 短主文案 + 一条 CTA |
| cold_email | 冷触达 → 回复 | 内部口吻主题、一条 CTA |
| social_post | 认知 → 到访 | 钩子 + 项目证据 + CTA |
| video_script | 认知 → 询盘 | 开场钩子 + 口播骨架 |
| nurture_email | 询盘 → 下单 | 每封只推进一步 |

`target_channel`、广告平台名、职业社媒名一律以产品上下文为准，不在本文件写死。

## 七轮与漏斗

顺序固定，后一轮改完回扫前一轮：

1. 清楚
2. 语气
3. 所以呢
4. 证明
5. 具体
6. 情绪（风险下降与职业声誉；场景须能回溯上下文）
7. 零阻碍（样品、检测、质检影像、下一步时限：上下文有才写）

| 漏斗 | 优先轮次 |
| --- | --- |
| 到访 | 清楚、情绪 |
| 询盘 | 所以呢、证明 |
| 样品 | 具体、零阻碍 |
| 报价 | 零阻碍、证明 |
| 下单 | 零阻碍、具体 |
| 复购 | 语气、所以呢 |

首页与产品页文末必须有「七轮检查」节，逐轮写通过或未通过及改动。成稿精修可另走 `skills/marketing-copy-editing/SKILL.md`（文件存在时）。

## 角色校准

不写死客群名单。对产品上下文里的每个买家角色填：

| 字段 | 要求 |
| --- | --- |
| persona | 与定位稿或产品上下文同名 |
| primary_concern | 能回溯上下文 |
| copy_angle | 该角色会核对的证据 |
| cta | 与漏斗阶段匹配 |

上下文没有角色时：在采购、指定人、承包、经销、进口商里选最贴近的一档，标明「角色未在上下文出现，暂用」，禁止发明岗位与痛点。

## 文案库列

文件：`deliverables/marketing/03-content/copywriting/copy-library.xlsx`（可从 `templates/copy-library.xlsx` 复制后填行）。

**Copy Templates**（≥15 行）列：`template_name, use_case, channel, headline, subheadline, body_framework, cta, target_persona, source_inspiration, source_url`

**Competitor Copy Audit**（≥10 行）列：`competitor, page_type, channel, headline, value_prop, cta, tone, strengths, weaknesses, source_url`

**Power Phrases**（≥20 行）列：`phrase, category, use_case, example_context, source, source_url`

`category` 只取：`trust` / `benefit` / `process` / `urgency` / `risk_reversal`。

`channel` 只取：`homepage` / `product_page` / `target_channel` / `search_ads` / `social_ads` / `cold_email` / `nurture_email` / `social_post` / `video_script`。

对手用真名，禁止 Competitor A/B/C。`example_context` 是该短语的使用场景标签，不是教学例子原文。

## JSON

不能写表时，同目录 `copy-library.json`：

```json
{
  "copy_library": {
    "templates": [
      {
        "template_name": "string",
        "use_case": "string",
        "channel": "homepage|product_page|target_channel|search_ads|social_ads|cold_email|nurture_email|social_post|video_script",
        "headline": "string",
        "subheadline": "string",
        "body_framework": "string",
        "cta": "string",
        "target_persona": "string",
        "source_inspiration": "string",
        "source_url": "string"
      }
    ],
    "competitor_audit": [
      {
        "competitor": "string",
        "page_type": "string",
        "channel": "string",
        "headline": "string",
        "value_prop": "string",
        "cta": "string",
        "tone": "string",
        "strengths": "string",
        "weaknesses": "string",
        "source_url": "string"
      }
    ],
    "power_phrases": [
      {
        "phrase": "string",
        "category": "trust|benefit|process|urgency|risk_reversal",
        "use_case": "string",
        "example_context": "string",
        "source": "string",
        "source_url": "string"
      }
    ]
  }
}
```

## 执行附件

均在 `deliverables/marketing/03-content/copywriting/`。邮件与社媒附件是跨渠道语气片段银行，不是可发送战役；不按角色出成套模板。

- `homepage-copy.md`：首屏、价值主张、信任条、主 CTA；语种以产品上下文为准；文末七轮检查节
- `product-page-copy.md`：产品页模板 + 首批产品线完整文案（按产品上下文的产品线，不发明 SKU）
- `channel-listing-copy.md`：目标渠道列表页的标题公式、子弹点、信任信号、贸易条款
- `cta-variations.md`：≥8 个场景（询盘、样品、目录、报价、案例、验厂、规格、交期）
- `email-template-snippets.md`：首封、跟进、培育语气片段；不可直接发送，不按角色出成套模板（序列走 `marketing-email-outreach`）
- `social-copy-snippets.md`：钩子与正文语气片段；不可直接发送，不按角色出成套模板（日历与平台原生成稿走 `marketing-social-content`）
- `video-hook-snippets.md`：开场钩子 + 一句话价值

面客稿顶部可写：`title`、`skill`（`marketing-copywriting`）、`generated_at`、`version`。策略与分析用简体中文；面客正文、URL、字段名、文件名按产品上下文语种。

## 反模式

- 不研究真实 B2B 制造页就写框架
- 套营销黑话
- 用示意数字冒充数据
- 抄对手措辞
- 忽略买家角色
- 该出现贸易术语的列表页或询盘 CTA 却完全不提（仅当上下文确有条款时才算遗漏）
- 编造统计、引言、项目、认证
- SaaS 式 CTA
- 推荐无收集阶段来源
- 终稿留未解释占位符

## 质量闸门

- 已读产品上下文与存在的上游策略稿
- ≥10 个竞品页有结构化评分与 `source_url`
- ≥20 条买家话术有来源
- 每个模板能回溯一条已分析页
- 数字要么已核验，要么 `[待补充]` / 「未在上下文出现」
- 无 sign up / free trial / subscription / get started
- 贸易术语仅在上下文确有时写入
- CTA 匹配渠道与漏斗
- 每个交付文件有 `source` 列或来源节
- 首页与产品页有七轮检查节
- 终稿无 `{{...}}`

## 可验证断言

1. `copywriting-strategy.md` 含 ≥5 家竞品审计，每家 `source_url`
2. Copy Templates ≥15 行，`channel` 在枚举内，`source_url` 非空
3. Power Phrases ≥20 行，`category` 属于五类之一
4. 首页与产品页无 SaaS CTA
5. 含数字的声明有来源或缺口标记
6. ≥10 条竞品产品描述出现在策略稿或审计表
7. 终稿占位符均已替换或标 `[待补充]` / 「未在上下文出现」
8. `homepage-copy.md` 与 `product-page-copy.md` 含七轮检查节
9. 跨渠道地图覆盖 homepage、product_page、target_channel、search_ads、social_ads、cold_email、social_post、video_script
10. `cta-variations.md` ≥8 个场景
