---
name: marketing-execution-log
description: >
  Use when the operator reports a real action is done (我发了, 上线了,
  更新了, 改了, 发出去了, 发帖了, 下线了, 点完了) on any channel, when the
  new-site repo has deployed merged PRs that change what Google indexes or
  visitors see, or when a failed verification in 执行登记 needs rechecking.
  Verify the action live, then write one row per URL into the base table
  执行登记 with scripts/execution_log.py. Both lines (营销, 获客) use this one
  flow; ledgers only quote the 登记编号. Not for GSC request-indexing, which
  uses scripts/next_step.py log-request.
---

# 执行登记

执行登记是 L0 的唯一来源，也是后面所有反馈挂回动作的锚（`CONTEXT.md`「执行登记」）。一次动作 = 一个网址（或一封信）在一天里的一次变化 = 一行。先**查证**，后写；查证由脚本抓线上做，AI 负责问清、选动作、挑**核对字样**。

脚本：`scripts/execution_log.py`（用法见文件头，`uv run scripts/execution_log.py --help`）。列与下拉以 `schemas/base-table.schema.json` 的 `$defs.执行登记` 为准；动作清单不够用记「其他」，内容说明写清。编号 `E-执行日期-当天序号`，脚本按执行日期顺延，全表唯一。

## 操作者说「我发了……」

1. **问清**，只问缺的：哪个渠道、做了什么、网址（或收件公司）、哪天（默认今天）。线：网站与社媒内容归营销，对具体公司的外展邮件归获客。对应交付物从台账与 `deliverables/` 找。对外文字再问一句「发出去的和稿子一样吗」：操作者发前自己改过的，请操作者贴出实际版本，交付物改成实际版本并在「## 审稿记录」记一轮「发前自改」（`docs/feedback-rules.md` 第 10 节第 7 条），再挑核对字样。完成：能填出渠道、动作、一句话内容说明、网址或收件公司。
2. **挑核对字样**（网站必填，其他平台有网址时也给）：1–3 段因为这次动作才出现在页面上的文字——新标题、改过的那句、新加的小标题。改正文就挑改后的新句，挑页面原本就有的字等于没查。改网址另给 `--old-url`，脚本会核旧址 301 到新址。完成：每段字样都说得出「改之前页面上没有它」。
3. **登记**：`uv run scripts/execution_log.py add --channel … --action … --desc … --url … --expect …`（邮件加 `--line 获客 --company 公司名 --sequence S-公司名 --nth N`，计划共几封、下一封日期从外展交付物取；收件人姓名和邮箱地址不进表）。按结果走：
   - 已查证 / 未查证（无法公开访问）/ 待邮箱接入后查证：告诉操作者编号和查到了什么。邮件的查证由「邮箱 IMAP 回流」在「已发送」里找到后回填。
   - 查证失败：行照写（「下一步」会按 E-01 排队）。用一句话告诉操作者看到了什么（如「打开是 404」），问：链接给错了，还是还没上线？弄清后 `recheck --id 编号 [--url 正确网址] --expect … --note "原因"`。
   - 退出码 3（重复）：说出已有的编号。操作者确认同一天确实又做了一次，加 `--again` 再登。
   - 退出码 2（线上抓不到）：过几分钟再登；底表写不进（没网、凭据缺）时，先记进台账「待补登」表，下次登记时补进底表，补完删行。
4. **回写台账**：编号写进本线台账的 `current_action_log`。台账只引用编号，不抄登记内容。完成：操作者听到了编号，台账已回写。

## 新站上线了改动

新站仓库（位置见 `docs/fact-sources.md`）合并并部署的 PR，影响收录或可见内容的同样是执行，来源记「新站 PR」（追记历史时记「补登」）。只读新站仓库和它的 PR，不改它。

1. **找新上线的**：`uv run scripts/execution_log.py show --source "新站 PR" --source 补登` 看最后登到哪天；在新站仓库 `gh pr list --state merged` 列出之后合并的 PR，对照新站 `docs/acceptance/<日期>/deploy/` 的部署记录和线上，定每个 PR 哪天上了生产。只合并、未上线的不登。
2. **筛**：留下改 robots、noindex、canonical、站点地图、网址或 301、标题或描述、正文、页面模板或页面上看得见的部件的；纯文档、测试、后台、接口、部署工具不登。完成：每个被筛掉的 PR 说得出属于哪一类。
3. **拆成行**：
   - 执行日期 = 上生产那天，不是合并那天。
   - 同一天上线、改同一网址的几个 PR 合成一行，证据列出全部 PR。
   - 一套模板管的一组页（博客文章、产品分类、分类归档）逐页一行；全站共用部件（页头、页脚、全站样式）只登首页英、德两行，内容说明写明「全站」。
   - 没有固定网址的（站内搜索结果）登一行、网址留空，用 `--verify 已查证 --evidence "…"` 写明怎么核的。
   - 改网址同时记新旧网址。
4. **挑核对字样**：从线上 HTML 里确认过再用——这次改动新带来的文案、类名、脚本名。证据前缀固定写成 `新站 PR #n（链接）… 已合并，<日期> 生产部署上线（部署记录路径）；线上复核`，`recheck` 会保留「线上复核」之前的部分。多行用 `add --from-json`（字段用中文列名，另带 `expect`、`证据前缀`）。
5. **线上复核时发现的新缺陷**照实写进那一行的备注，并告诉操作者；修它是新站仓库的事，按那边的规矩走。完成：每个筛进来的 PR 都落在至少一行的证据里，查证失败的行都弄清了原因。

## 例子

> 仅供理解，禁止引用到输出。

操作者说「我把产品页 A 的参数表更新了」。AI 问到网址，挑改后才有的那行参数名作核对字样，`add --channel 网站 --action 改正文`；脚本回「已查证」，AI 报出编号并写进台账 `current_action_log`。若脚本回「查证失败：HTTP 404」，AI 只问一句「链接是不是给错了」，拿到正确网址后 `recheck`。
