---
name: lead-data-validation
description: >
  Use when the user asks for 数据验证, 验证, 核查, data validation, URL
  验证, 公司真实性, 联系人真实性, domain match, employee-count check,
  or to verify a company list, contact list, or lead dataset before
  approval. Run five checks (URL reachability, company cross-check,
  domain match, contact authenticity, employee count) with one default
  fetch or search plus one fallback; mark url_verified and related
  fields, never delete rows. Prioritize high ICP matches, cache the
  same domain in-session, and write the validation report beside the
  dataset under deliverables/lead/. Not for six-dimension review, user
  approval, outreach sending, or inventing missing firms.
---

# 数据验证

对获客名单与来源 URL 做五项检查，只标记不删除。报告写在被验证数据同一阶段目录。六维审查与证据闸不在本文件，见 `skills/lead-generation/references/orchestration-protocol.md`。

## 步骤

1. **输入**。读台账 `state/lead-status.md` 的 `phase`、`output_dir`。产品与公司事实读事实源入口 `docs/fact-sources.md`，查不到标〔未证实〕。用户本轮点名了文件就用该文件；否则取当前 `output_dir` 里刚落地的名单或报告。存在则读 `deliverables/lead/01-icp/icp-analysis.md`，只用于排序，不改画像。原文不拷进本仓库。完成：待检路径、阶段目录、记录条数、每条适用哪几项检查都已确定。无数据集 → 停并写缺口，不编名单、不编 URL。

2. **排队**。高 ICP 匹配优先。同一域名下多个页面只排队一次域名可达性。本会话已验过的域名写入缓存，不重复抓。完成：有序队列；同域合并结果可复用。

3. **五项检查**。对队列逐条做适用项；不适用写 `not_applicable`，不留空、不编造。每满 10 条报一次已检数与当前 `url_verified` 通过率。Apify 修复与替代取证后仍不可得 → 停止并写缺口，已检记录的标记保留。完成：每条在范围内的记录五项都有值。

   1. **URL 可访问性**。默认：抓取指定 URL 的正文。跟随重定向后最终成功打开 → `url_verified: true`。超时 / 403 / 5xx / 最终 404 或 410 → 逃逸一次：抓取指定 URL 的正文（含动态页）。仍失败 → `url_verified: false`。无 URL → `not_applicable`。
   2. **公司真实性**。用 Apify 搜索查证公司名。结果里出现该公司（域名匹配或名称匹配）→ `cross_verified: true`，否则 `false`。
   3. **域名匹配**。从公司名去掉 Inc / Ltd / LLC / GmbH / Corp / Co. 等后缀，取关键词。域名含该词 → `domain_match: true`。不含则再用 Apify 搜索确认域名与公司的关联；确认 → `true`；无法确认 → `false`，列入需人工复核。
   4. **联系人真实性**。用 Apify 搜索查证公开职业页（姓名 + 公司）。完整匹配 → `confidence: high`；部分匹配（同名不同公司，或同公司不同职位）→ `medium`；未找到 → `low`。无联系人行 → `not_applicable`。邮箱：仅当用户已配置联系人/邮箱发现服务才补；否则标「联系人待补」，不编造。
   5. **员工数**。把记录里的声称人数与公开资料对照。同量级且不互相否定 → `employee_count_verified: match`；明显矛盾 → `mismatch`；缺公开资料或记录未声称 → `gap`。无公司行 → `not_applicable`。

4. **落盘**。按下方模板写入被验证数据所在阶段的 `data-validation.md`（公司名单 → `deliverables/lead/02-companies/`，联系人 → `deliverables/lead/03-contacts/`，其他阶段同理）。失败行保留，只改标记。通过率按实际已检条数算，不拿未检行凑。完成：报告非空；通过率与标记一致；教学例子原文零出现。

## 默认

- 查证用 Apify 搜索；需要原文或验域名时抓取指定 URL。默认一条能力 + 一次逃逸，不并列引擎。不可用则停止并写缺口，不编造。
- 单次失败不删除记录。本 skill 只产出验证标记与报告；六维审查、审批、写入批准态由编排协议接着做。
- `url_verified` 通过率交给 Data Accuracy：>80% 建议 PASS，50–80% 建议 CONCERN，<50% 建议 FAIL。其他四项只报分布，不另造阈值。
- 联系人/邮箱发现服务、网页采集服务：仅当用户已配置；付费项须先告知并获准。
- 共用规则若存在则读 `skills/marketing-playbook-standards/SKILL.md`。
- 验证报告不进 `deliverables/lead/00-system/`（那是教学与评测元产出），除非被验证的就是该目录里的文件。

## 写法

- 列名 English snake_case：`url_verified`、`cross_verified`、`domain_match`、`confidence`、`employee_count_verified`。
- 布尔用 `true` / `false`；联系人置信度用 `high` / `medium` / `low`；员工数用 `match` / `mismatch` / `gap`；不适用 `not_applicable`。
- 公司名不翻译。分析用语跟本轮语言。
- 每条标记带来源：已抓取 URL 或搜索查询 + 访问日期。无来源的 `true` 不算完成。

## 产出

主文件：被验证数据同一 `deliverables/lead/<阶段>/data-validation.md`。不改战役 `phase`。表列若回写原名单，与原文件同目录。

```markdown
# 数据验证报告

- dataset:
- stage_dir:
- source: 台账 product_context（不粘贴原文）
- accessed:
- records_total:
- records_checked:

## 通过率

- url_verified: true/false/not_applicable
- cross_verified:
- domain_match:
- confidence: high/medium/low/not_applicable
- employee_count_verified: match/mismatch/gap/not_applicable
- url_verified 通过率:  → Data Accuracy 建议 PASS / CONCERN / FAIL

## 需人工复核

（domain_match false 或其他无法确认项，一行一条）

## 缺口

## 搜索日志
```

## 例子

> 仅供理解，禁止引用到输出。

输入把线上在售目录、站点地图、过期本地快照三份条数混成「已验证公司数」。成稿应先写各源口径，以当前可打开的自有站为权威；地图缺条不自动 `url_verified: false`（索引子集不等于站死）；过期快照只作线索，冲突以线上为准，而不是对差集删行或拿旧表当事实。

输入一条带自有域名、无联系人的公司行。成稿应：跟随重定向后首页打开 → `url_verified: true`；搜索同时出现公司名与该域名 → `cross_verified: true`；去掉 Inc / Ltd / GmbH 后关键词落在域名中 → `domain_match: true`；无联系人 → `confidence: not_applicable`，标「联系人待补」（联系人检查无对账语料，故保留此通用支架，不编姓名或邮箱）；声称人数与同期公开资料同量级且不互相否定 → `employee_count_verified: match`。不是用目录站或旧快照代替这五项。

输入把「公司站 / 网店」双域，或把目录站、比价列表、杂志文写成公司官网。成稿应：双域各抓一次，都能打开则两条均可 `url_verified: true`，关键词落在其中任一域 → `domain_match: true`；目录站/比价页即使 200 也 `domain_match: false` 并列人工复核，而不是当公司域名通过。

输入把注册墙、价格门、错误语区失败、或 429/5xx 写成公司不存在。成稿应：说明页已打开则公司 URL 为 `true`，墙内目录不闯门；错误语区逃逸一次规范语区；超时/429/5xx 逃逸一次动态页仍失败 → `url_verified: false`，行保留，不按搜索摘要推断有无站点。正文 200 但「不可用」不能当 `cross_verified: true`。

输入用过期通稿人数与关于我们页对不上就删公司，或把同层批发对手标成已通过客户。成稿应：量级矛盾 → `mismatch` 并列人工复核；缺公开资料 → `gap`；五项通过只证明记录可核，不改 ICP 身份。行都保留。

## 易错

- 验证失败就删行，或用训练记忆补公司、域名、邮箱、员工数。
- 无 URL 时编一个再去「验证」。
- 把默认抓取 + 一次动态页逃逸再展开成多引擎菜单。
- 同域名反复抓；或把目录站、平台列表页当成公司域名通过。
- 未配置发现服务仍写出邮箱。
- 在本文件做六维审查或证据闸，或写 `status: approved`。
- 把报告写到 `00-system/`，而数据在别的阶段。
- 把 skill 例子原文写入交付物。

## 清单

- [ ] 待检文件与阶段目录已确定；无数据时已停
- [ ] 五项检查均已标记；失败行未删
- [ ] URL 只走默认抓取 + 一次逃逸；搜索/Apify 与替代取证仍不可得已写缺口
- [ ] 高 ICP 优先；同域名会话内不重复验可达性
- [ ] 无编造联系人或员工数；未配置发现服务已标「联系人待补」
- [ ] 报告在数据同一阶段目录；例子原文未进入交付物
- [ ] `url_verified` 通过率已按阈值写成 Data Accuracy 建议
