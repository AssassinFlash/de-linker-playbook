---
wayfinder: map
created: 2026-10-14
---

# 地图：按可行性裁定补齐闭环（执行）

## Destination

[可行性裁定](../feasibility/tickets/feasibility-verdict.md) 的补齐顺序 0–6 全部落地，营销线与获客线都用真实动作跑通一次：**执行登记 → 反馈回流 → 底表 / 看板 → AI 据此给出下一步**。两张验收票（「营销线闭环验收」「获客线闭环验收」）关闭即到达终点。

## Notes

术语以 [`CONTEXT.md`](../../CONTEXT.md) 为准（反馈分级、执行登记、底表、看板、站点接入、冷启动阶段、运营循环、证据闸、反馈闸、激活名单）。裁定的 Q1–Q10 只在「可行性裁定」票里，本图不复述。

**本图的约定（用户定 2026-10-14，除注明外）**

- **本图包含执行**：票做完即活干完，不只产决策。task 票是主力；research / grilling / prototype 只在执行前确有事实或形态要定时出现。
- **一票一新会话**：新会话进场先读本图，按「怎么找前沿」认领一张票，干完关票、回写本图 Decisions so far。不在长会话里连走多票。
- **不留口头传话**：票的 Resolution 只记结论与后续票依赖的事实（路径、ID 所在位置、行数）；凡「后续票要注意 X」，当轮直接写进那张后续票的正文。不靠用户跨窗口传话。
- **调研派 Grok Build**：research 票不用 Claude 子代理，经 grok_build MCP（bridge 在 `~/Documents/grok-build-bridge`）派给 Grok Build；主模型只派工、跟进、验收。**每交回一份就向用户汇报，并抽查来源**（至少两条关键事实对原文复核，写进 Resolution）。产出落 `wayfinder/closed-loop/research/<票名>.md`，每条事实带来源 URL 或仓内文件路径。
- **事实源 = 三方映射**：竞品调研（vault `deliverables/marketing/00-research/`）+ 线上站点 `https://de-linker.com/` + 新站仓库 `~/Documents/de-linker`（读路径时把 `~` 展开为用户主目录）。**`~/Documents/New` 已过期，不读其内容**（改写指针的票只 grep 路径字符串，不打开文件）。
- **不写任何「问老板 / 待老板确认」**：未知标〔未证实〕，以线上站点与新站仓库为准，查不到就按没有处理。
- **公私分层**：私有数据与个人账号（真实邮箱、表格 ID、服务账号邮箱、名单、询盘与回信内容）只进私有 vault（`deliverables/` 软链 → `../de-linker-vault`，本地 + GitHub 私有双份）；公开仓库只写角色名（`所有者账号`、`日常账号`、`服务账号`、`团队邮箱`）。vault 只收成品，过程产物不进。
- **密钥不进任何仓库**：服务账号密钥 JSON、IMAP 客户端专用密码、Woo REST 密钥放两个仓库之外（如 `~/.config/` 下，权限 600）；vault 只记「放在哪、谁建的、何时建」，不记内容。
- **执行手动、反馈自动**：内容发布与发信由操作者手动（任意渠道），每次口述 → AI 查证 → AI 写执行登记。自动发信、自动发布不做。
- **站点接入归 agent**：GSC 验证、GA4 代码、同意横幅由 agent 在新站仓库做，**完全按 `~/Documents/de-linker/AGENTS.md` 的规矩**（一票一会话、分支 → PR → CI 绿 → 合并、验收三件套、客户可见文案走对抗评审、复刻面像素零差异只容「裁定过的变更」、不买付费插件、不走 Code Snippets）。操作者只验收（看是否生效），不部署；Google 后台里只有所有者才能点的那几下，给操作者一份精确清单。
- **GSC 先，GA4 后**。GA4 的调研可先行，站点改动排在 GSC 之后。
- **底表 / 看板写给初学者**：操作者正在学 Google 表格与 Looker Studio。中文列名、每张表有说明页（这列是什么、从哪来、谁写、怎么读）、看板配逐步图文指南；清晰、详细优先于简洁。
- **操作者是新入行者**：系统不依赖操作者的行业判断；质量靠证据闸（执行前 AI 自查来源与〔未证实〕）+ 反馈闸（执行后看 L1–L3）。HITL 票问操作者的只能是「发不发 / 上不上」与「看得懂吗、好用吗」，不问「写得好不好」「行业里该怎么做」。
- **脚本跨 harness**：取数与写表是仓内脚本，任何 harness 能跑；方法文本保持可移植（五家兼容降级，见上一张地图）。
- **自建看板是后备**：只在「Looker Studio 看板」票证明 Looker Studio 走不通时启用，由该票就地切新票。
- **质量优先，无时间预算。**

**已知事实（2026-10-14 只读核查，供各票起步）**

- 线上已切换到新站：首页加载 `plugins/linker-commerce`、`plugins/linker-tools`，`/wp-json/linker/v1/engineering-feed` 返回 200。站点改动走新站仓库管线（本地 → 评审站 → 线上，规格 `docs/specs/17-cutover.md`）。
- Google 侧为零：无 GSC 资源、无 GA4、无 Cloud 项目；无 DNS 权限 → GSC 用网址前缀资源 `https://de-linker.com/`（API 标识带尾斜线）。账号角色见「Google 账号现状清点」（真实明细在 vault `deliverables/marketing/00-system/google-account-inventory.md`）。
- 邮箱：只读 `chester@de-linker.com`（腾讯企业邮，IMAP `imap.exmail.qq.com:993`）；站点询盘通知发 `团队邮箱`（sales@），不读。
- 询盘：Woo 订单状态 `inquiry-received` → `proforma-issued` → `completed` / `cancelled`；每日 09:00 摘要（新站 `docs/specs/74-daily-digest.md`）。联系页 `/contact/`、`/de/kontakt/` 线上仍是「改发团队邮箱」的回退块（`/kontakt/` 404），新表单未挂上且只发邮件不落库——联系表单与直接来信的询盘不可计（见「询盘数据从哪读」）。
- 写死 `~/Documents/New` 的文件：`skills/` 下 101 个，另有 `CONTEXT.md`、`AGENTS.md`、`README.md`、`docs/getting-started.md`、`state/status.md`（`wayfinder/` 下的历史记录不改）。

**怎么找前沿**（本地 markdown 追踪）：票在 `tickets/*.md`，frontmatter 有 `status`、`assignee`、`blocked_by`、`step`（补齐顺序 0–6，验收为 7）。前沿 = `status: open`、`assignee` 为空、`blocked_by` 里每张票都已 `status: closed`。多张可取时按 `step` 小者先，同 step 任取。认领 = 先把 `assignee` 写成自己（会话名 + 日期）再开工。

```sh
grep -l "^status: open" wayfinder/closed-loop/tickets/*.md | xargs grep -H -E "^(assignee|blocked_by|step):"
```

## Decisions so far

<!-- 每关一票加一行：[票名](tickets/x.md)：一句话 gist -->

- [反馈分级行动规则调研](tickets/feedback-action-rules-research.md)：冷启动可执行的只有技术阻断、退信状态码、标题/摘要缺陷三类；比率类（零展示、点击率、回复率、跟进次数间隔、询盘数、上移时点）均无通用阈值，只记账。
- [同意横幅与 GA4 选型调研](tickets/consent-ga4-research.md)：Complianz 免费版 + WP Consent API + Site Kit，Consent Mode 走 Basic（同意前不传数据），第一层同等接受/拒绝；Script Center 能否挡住 Site Kit 的 gtag.js 须先实测。另发现线上已在无横幅时写 Woo 订单归因 Cookie。
- [询盘数据从哪读](tickets/l3-inquiry-source.md)：L3 主路径 = Woo REST 只读密钥读四个询盘状态 + 签发 meta；联系表单（未挂、只发信）与直接来信不可计；表格只留 id、单号、公司、创建时刻、状态、签发时刻。

## Not yet specified

- **非 Google 渠道的 L1/L2**：操作者可在任意渠道发布（LinkedIn、行业论坛、目录站……）。执行登记能记 L0；这些渠道的到达与互动怎么回流（口述 + 截图？平台导出？）要等底表与反馈规则定形后才看得清。
- **从冷启动到逐级上移的切换条件**：反馈分级规定冷启动只决策在 L0–L1，数据积累后上移。上移的条件（多少天、多少展示 / 点击 / 询盘）在「反馈分级规则定稿」里可能只能定冷启动段；之后的段落等有了真实数据再切票。
- **询盘归因到动作**：一条询盘来自哪次执行（哪页、哪封信）。GSC 不带到访者路径，GA4 受同意率限制。**首选候选：WooCommerce 订单来源（Order Attribution）**——线上已在运行，把来源类型、UTM（source / medium / campaign / content / term）、设备类型、本次会话浏览页数直接记在询盘订单上；操作者在任意渠道发的链接带上 UTM，就能把询盘接回那次执行登记（也部分回答「非 Google 渠道」的 L3）。限制：横幅上线后只记同意了的访客；自建的形式发票申请页是否把这些字段提交进订单〔未证实〕；订单上的字段名与能否经 REST 读出〔未证实〕。「询盘回流 L3」首次真实调用时一并核实，有了结论再切票。
- **联系表单与直接来信的询盘**：现在不可计，北极星只含形式发票申请。要不要让联系表单落库（新站仓库改动）、以及挂上新表单（新站迁移 68），等 L3 回流跑起来、看清询盘量与缺口后再判断。
- **定时任务跑在哪**：回流脚本在操作者的 Mac 上定时跑，还是放到服务 VPS 上。首个回流票（「GSC 数据回流」）会先定一个；若操作者的机器不常开导致断档，再切票。

## Out of scope

- 自动发信、自动发布（执行由人手动）。
- Google Ads 的投放数据与投放执行：不在补齐顺序 0–6 里。
- 方法层 skill 的内容重写：裁定方法层留用；本图只改事实源指针、台账、编排、证据闸 / 反馈闸，以及激活名单入口涉及的两三个获客 skill。
- 上两张地图（`wayfinder/map.md`、`wayfinder/feasibility/map.md`）及其票：不改。
