---
wayfinder: prototype
created: 2026-10-06
status: final
resolved: 2026-10-06
feeds: [marketing-skills-extraction, lead-skills-extraction, repo-skeleton, acceptance-review-and-smoke]
---

# 抽取规格

状态：**已定稿（2026-10-06 用户拍板）**。子代理照本文干活，主模型照本文验收；与本文冲突时停，不发明第二套规则。

依据：`wayfinder/tickets/extraction-spec.md`；`wayfinder/research/skill-conventions-best-practices-2026-10.md`；`wayfinder/research/generic-orchestration-2026-10.md`；`wayfinder/tickets/orchestration-workflow-form.md` Resolution；试点 `skills/marketing-orchestrator/SKILL.md`、`skills/marketing-copywriting/SKILL.md`；根 `AGENTS.md`；源扫描（2026-10-06）。

范围：从 `~/Documents/marketing-playbook-v3/.claude/skills/` 抽 **38** 个；从 `~/Documents/lead-generation_副本/skills/` 抽 **43** 个。不抽 v3 根目录 `skills/`（legacy）。不抽 lead-gen 的 `.kimi/`、`.codex/`、各 skill 内 `AGENTS.md`。lead-gen 方法论来自用户自购付费 prompt：**自用、不对外分发**；只迁已写入 `SKILL.md` 的方法，不迁付费原文、不把 `instruction_source` 写入正典 frontmatter。

兼容目标五家：Kimi、Z Code、DeepSeek、OpenCode、Hermes。不为 Claude / Codex 建适配层。

---

## 0. 编排系 9 skill 改写方向

依据 Resolution：**乙为骨 + 甲为重活**。骨 = orchestrator + `state/status.md`；重活开 wayfinder 票。命令卡片不进正典。

| 源 name | 目标 name | 改写 |
| --- | --- | --- |
| marketing-orchestrator | 同名 | 保持试点导航：读台账 → 宣布 phase / 下一方法 skill / 产出路径 → dispatch a subagent, else do it inline → 回写台账。全量迁入后只扩「阶段」表，不改导航合同。 |
| marketing-init | 同名 | 引导型：确认 `state/status.md`、`deliverables/marketing/` 与 `deliverables/lead/` 存在；`product_context` 指向 `~/Documents/New/CONTEXT.md`。禁止建外部 vault、禁止写 `config.md` 的 `vault_path`、禁止 `/slash`。 |
| marketing-profile | 同名 | 引导读 `~/Documents/New/CONTEXT.md`，需要参数再读 `fact-base/`。禁止在本仓库另写一份公司档案。 |
| product-profile | marketing-product-profile | 同上，只指路不复制。 |
| marketing-playbook-standards | 同名 | 短共用规则：数据锚定、例子禁引用、产出只进 `deliverables/`、工具写能力。去掉 `disable-model-invocation`。方法 skill 步骤 0 用相对路径引用本文件；禁止 session-start 注入。 |
| marketing-teach | 同名 | 教学方法；产出进 `deliverables/marketing/00-system/`。去掉 `${CLAUDE_SKILL_DIR}` 与产品锁。 |
| marketing-eval | 同名 | 按 `evals/` 与本规格验收清单评 skill。 |
| marketing-evolve | 同名 | 按评测回写本仓库 skill；当轮清账。 |
| skill-eval | marketing-skill-eval | 与 eval/evolve 同族；源 `references/` 里的不锈钢例子删除或改标后的通用支架。 |

试点已有的 `marketing-orchestrator` / `marketing-copywriting`：全量抽取时按本规格回写覆盖薄片，**name 不变**。

---

## 1. SKILL.md 正典格式

正典位置：`skills/<name>/SKILL.md`。目录名 = frontmatter `name`。只允许字段 **`name` + `description`**。可选 `license`、`metadata.author`、`metadata.version`（字符串 map）；除此之外一律删除。

`name`：`^[a-z0-9]+(-[a-z0-9]+)*$`，1–64 字符，不以内外 `-`、不含 `--`、不含 `claude`/`anthropic`、无 XML。必须匹配 `^(marketing|lead)-`。

`description`：300–700 字符（硬顶 1024）。同时写 what + when；触发词前置（含用户不说 skill 名的说法）；禁止 `<` `>`；YAML 用 `>` 块标量。源实测：v3 37/38 条 <300，必须扩；lead-gen 31/43 条 >700、5 条 >1024，必须砍到 300–700。把源 `when_to_use` 里的触发词并进 `description` 后删除该字段。

禁止出现在正典 frontmatter 的字段（源已测到或研究列入）：`allowed-tools`、`disallowed-tools`、`model`、`effort`、`context`、`agent`、`hooks`、`paths`、`globs`、`disable-model-invocation`、`disableModelInvocation`、`user-invocable`、`when_to_use`、`whenToUse`、`arguments`、`argument-hint`、`type`、`icon`、`color`、`background`、`shell`。源实测：v3 **38/38** 有 `when_to_use` 与 `disable-model-invocation`（3 个为 `true`：`marketing-playbook-standards`、`marketing-psychology`、`copy-editing`）；**37/38** 有 `allowed-tools`；lead-gen **2/43** 有 `metadata`（`data-validation`、`lead-generation`）——抽取时整段删。

正文结构（试点已验证，必须用这套标题，禁止另起英文平行骨架）：

1. `#` 标题（无 `/slash`）
2. 一两句目的（不锁产品、无工具 ID）
3. `## 步骤`：编号；每步有可检查的完成条件
4. 按需：`## 默认` / `## 写法` / `## 产出` / `## 例子` / `## 易错`
5. `## 清单`

长度：`SKILL.md` **<500 行且 <5000 tokens**。源全部 <500（最长 v3 `copywriting` 395、lead `usp-extraction` 398）；改写后仍超则把百科切到 `references/`，SKILL.md 用「若条件 C，读 `references/foo.md`」。引用只准一层、正斜杠、相对 skill 根。`references/` 里 >100 行的文件开头必须有目录。

工具：只写能力（第 4 节表）。子代理句固定为英文：`dispatch a subagent, else do it inline`。禁止 `Task(`、`Agent(`、`spawn_agent`、`context: fork`。

---

## 2. 去不锈钢化规则

原则：**A 为骨 C 为例**。正文是通用方法，不锁任何产品/工厂/城市/SKU。例子优先用 `~/Documents/New` 的真实材料改写成短支架，但**产品事实不写进 skill**（避免第二真相源）。

### 2.1 禁止残留词

扫描范围：`skills/` 与将迁入的 `references/`（大小写不敏感；中文精确）。下表各词在方法正文、步骤、产出模板、未标注段落中出现次数必须为 **0**。已按第 3 节标注的例子块内允许残留，但必须带「仅供理解，禁止引用到输出」，且不得进入交付物。频道主题 skill 的例外见 2.2。验收第 5 条按此口径执行。

| 词 | v3 canonical 频次（典型文件） | lead-gen canonical 频次（典型文件） |
| --- | --- | --- |
| vault / `{{VAULT}}` / Marketing-Vault / LeadGen-Vault | vault 578（`marketing-orchestrator/references/dependency-graph.md` 128） | vault 224（`lead-generation/references/dependency-graph.md` 42） |
| Alibaba | 62（`copywriting/SKILL.md` 18） | 4（`lead-generation/references/search-protocol.md`） |
| Shopify | 21（`site-and-schema`、`seo-audit/references`） | 0 |
| 屏风 | 25（几乎全在 `skill-eval/references/`） | 8（`evals.json`） |
| stainless / stainless steel | 16 / 4（`skill-eval`、`marketing-teach`） | 75 / 74（几乎全在 `evals.json`） |
| 不锈钢 | 8（`skill-eval/references/`） | 10（`evals.json`） |
| PVD | 7（`skill-eval/references/`） | 7（linkedin `evals.json`） |
| Made-in-China | 5（`funnel-optimization` 等） | 3 |
| 佛山 / Foshan | 3 / 1（`skill-eval/references/`） | 0 |
| Canton Fair / 广交会 | 5（`content-strategy` 等） | 2（`evals.json`） |
| Linker / 金达 / Jinda / 316L | 0 | 0（仍列入扫描，防回写） |
| Obsidian | 0 | 4（`lead-generation/references/obsidian-write.md` 等） |

改写规范：

- 产品/材质/产地/SKU → 「产品上下文中的品类/材质/产地」，或删。
- 默认渠道 Alibaba/Shopify/Made-in-China → 「目标渠道（以产品上下文为准）」。
- `{{PRODUCT_CATEGORY}}` → 产品上下文的品类字段，不在 skill 里填值。
- 源 `evals.json` **不迁入**（不锈钢样本库）。评测夹具以后用 `evals/` 另做。

### 2.2 允许保留的词

- 技能主题本身是该频道：`lead-linkedin-*` 与 `marketing-social-content` 可保留 LinkedIn；`marketing-paid-advertising` 可保留 Google/Meta 等广告平台名。
- 通用品类词（B2B、OEM、MOQ、Incoterms）可保留。
- 教学例子里出现禁止词：必须落在已标注的例子块内，且交付物禁引（第 3 节）。优先改成 New 侧支架，而不是继续用屏风。

---

## 3. 例子标注格式

固定句（一字不改）：

```
仅供理解，禁止引用到输出。
```

放置：

- **正文内嵌**：`## 例子` 节第一行必须是引用块 `> 仅供理解，禁止引用到输出。`，然后才是例子正文。每则内嵌例子都在该节内；一节多例共用这一句即可。
- **`references/examples.md`**：文件第 1 个非标题段落必须是同一句引用块，并补一句「本文全部例子都是教学支架，禁止把原文写入任何交付物。」文件内每个三级标题例子块开头再重复该引用块。
- skill 其他节禁止出现未标注的「例如 / e.g. / Example」长段；需要形状时用产出模板（非例子）或把例子挪到上述两处。

交付物检测：交付物文本不得等于任何已标注例子的原文（试点清单已用此门）。

---

## 4. 工具能力化对照表

默认一条能力 + 一个逃逸，禁止并列五引擎菜单。源 `contact-discovery` 的 WebSearch/Exa/Perplexity/LinkedIn/PinchTab/Apify 五段链改成：默认「用网页搜索查证」；需要原文时「抓取指定 URL」；搜索不可用则停止并写缺口，不编造。

| 源写法（实测） | 正典写法 |
| --- | --- |
| `mcp__tavily__tavily_search`（v3 24 个 skill × 出现 30） | 用网页搜索查证 |
| `mcp__exa__exa_search`（同上） | 用网页搜索查证 |
| `mcp__perplexity__search`（同上） | 用网页搜索查证 |
| `WebSearch`（v3 24；lead 40） | 用网页搜索查证 |
| `WebFetch`（v3 24；lead 10） | 抓取指定 URL 的正文 |
| `Read` | 读本仓库相对路径文件 |
| `Write` / `Edit` | 写入或修改本仓库相对路径文件 |
| `Bash` | 运行 shell 命令 |
| `Glob` | 按文件名模式查找本仓库文件 |
| `Grep` | 在本仓库内搜索文本 |
| `Agent` / `Task` / `spawn_agent` | dispatch a subagent, else do it inline |
| PinchTab | 抓取指定 URL 的正文（含动态页） |
| Apify | 用网页采集服务抓取公开页（仅当用户已配置） |
| Snov.io / Apollo / Hunter | 用联系人/邮箱发现服务（仅当用户已配置）；否则交付物标「联系人待补」 |
| Instantly | 用用户已配置的外发工具发信；未配置则只产出文案不发送 |
| `${CLAUDE_SKILL_DIR}` / `${KIMI_SKILL_DIR}`（v3 `retention`、`marketing-teach`） | skill 根相对路径，如 `references/foo.md` |
| `$ARGUMENTS`、`$0`–`$9`、`$skill` | 删除。改读用户本轮消息。注意源里 `$1`/`$5` 多为金额，禁止当占位符误删 |
| `{{VAULT}}/...` | `deliverables/marketing/...` 或 `deliverables/lead/...`（第 7 节） |
| `{{PRODUCT_CONTEXT}}` / `.claude/product-profile.md` | 台账 `product_context`（默认 `~/Documents/New/CONTEXT.md`） |
| `config.md` 的 `vault_path` | 删除。产出根固定为 `deliverables/` |
| `/marketing-*`、`/lead-*` | 打开 `skills/<name>/SKILL.md` 并按其步骤做 |
| `.omc/state/`、Obsidian 写入协议 | 进度只写 `state/status.md`；产物只写 `deliverables/` |

v3 `allowed-tools` 实测 token：Read 37、Agent 37、Write/Edit/Bash 30、三 MCP+WebSearch+WebFetch 24、Glob 2、Grep 1。正典不保留该字段。

> 仅供理解，禁止引用到输出。
>
> 源步骤「`mcp__tavily__tavily_search` 查竞品标题」改写成「用网页搜索查证竞品首页标题；把 URL 与摘录写入交付物来源栏」。

---

## 5. 命名规则

- v3 已是 `marketing-*`：保持。
- v3 无此前缀的 23 个：加 `marketing-`（与地图 Destination 一致）。`copywriting` → `marketing-copywriting`（覆盖试点，不另起名）。`product-profile` → `marketing-product-profile`。`skill-eval` → `marketing-skill-eval`。
- lead-gen 已是 `lead-*` 的 4 个保持、禁止双重前缀：`lead-generation`、`lead-interview`、`lead-magnet-gen`、`lead-teach`。
- 其余 39 个加 `lead-`。全表见附录 A。重叠对**原样迁入**，合并交给 `wayfinder/tickets/overlap-dedup-adjudication.md`。

v3 无前缀映射：`ai-seo`→`marketing-ai-seo`；`analytics-and-optimization`→`marketing-analytics-and-optimization`；`competitor-intelligence`→`marketing-competitor-intelligence`；`content-strategy`→`marketing-content-strategy`；`copy-editing`→`marketing-copy-editing`；`copywriting`→`marketing-copywriting`；`email-outreach`→`marketing-email-outreach`；`funnel-optimization`→`marketing-funnel-optimization`；`inquiry-flow`→`marketing-inquiry-flow`；`landing-page`→`marketing-landing-page`；`launch-strategy`→`marketing-launch-strategy`；`paid-advertising`→`marketing-paid-advertising`；`positioning`→`marketing-positioning`；`pricing-strategy`→`marketing-pricing-strategy`；`programmatic-seo`→`marketing-programmatic-seo`；`referral-program`→`marketing-referral-program`；`retention`→`marketing-retention`；`seo-audit`→`marketing-seo-audit`；`site-and-schema`→`marketing-site-and-schema`；`social-content`→`marketing-social-content`；`visual-content`→`marketing-visual-content`；`product-profile`→`marketing-product-profile`；`skill-eval`→`marketing-skill-eval`。

---

## 6. 上下文指路策略

Linker / 任何当前产品的事实只存在 `~/Documents/New`（先 `CONTEXT.md`，需要参数再 `fact-base/`）。skill、台账、AGENTS.md **只指路、不复制**。读时把 `~` 展开为用户主目录，禁止把 `~` 当相对路径。交接他机：只改 `AGENTS.md` 与 `state/status.md` 的 `product_context`。

路径规则：

- 本仓库内一律相对路径：`skills/<name>/SKILL.md`、`state/status.md`、`deliverables/...`。
- **唯一允许的仓外路径形式**：`~/Documents/New/...`。
- 禁止：`/Users/...`、`/home/...`、`~/Documents/Marketing-Vault-v3`、`~/Documents/LeadGen-Vault`、`${CLAUDE_SKILL_DIR}`、源 `config.md` 的绝对 vault。

源产出原址（改写依据，禁止继续写入）：营销缺省 `~/Documents/Marketing-Vault-v3`（阶段 `00-Research`…`07-Measurement`，另有 teach/eval 用的 `00-System/`）；获客 `~/Documents/LeadGen-Vault`（`00-System`…`10-Sales` + `99-Archive`，另有遗留 `{{VAULT}}/lead-generation/*.xlsx`）。

---

## 7. 目录布局终稿

```
de-linker-playbook/
├── AGENTS.md                 # 只指路；台账指针置顶；<32KiB
├── skills/<name>/SKILL.md    # 正典，扁平，禁止再套一层品类目录
├── .agents/skills/<name>     # 软链 → ../../skills/<name>（发现层，必做）
├── schemas/                  # 交付物 frontmatter / 台账 JSON Schema
├── templates/                # 过长产出模板（从 SKILL 产出节拆出）
├── evals/                    # 本仓库评测夹具；不收源 evals.json
├── docs/                     # 人读说明
├── wayfinder/                # 地图与票；不放 skill 方法
├── state/                    # 台账 status.md
└── deliverables/
    ├── marketing/
    │   ├── 00-system/
    │   ├── 00-research/
    │   ├── 01-foundation/
    │   ├── 02-seo/
    │   ├── 03-content/
    │   ├── 04-acquisition/
    │   ├── 05-cro/
    │   ├── 06-growth/
    │   └── 07-measurement/
    └── lead/
        ├── 00-system/
        ├── 01-icp/
        ├── 02-companies/
        ├── 03-contacts/
        ├── 04-market/
        ├── 05-usp/
        ├── 06-outreach/
        ├── 07-targeted/
        ├── 08-linkedin/
        ├── 09-seo/
        ├── 10-sales/
        └── 99-archive/
```

营销树含 `00-system/`：源 `marketing-teach` 把学习笔记写到 `{{VAULT}}/00-System/learning-notes/`，`skill-eval` 写到 `{{VAULT}}/00-System/skill-eval/`；这是 teach/eval 元产出，不是 `00-research/` 战役阶段。对应本仓库 `deliverables/marketing/00-system/`。与 lead 树的 `00-system/` 同名不同树。

收纳：`scripts/` `references/` `assets/` 只放在对应 `skills/<name>/` 下。禁止复制到 `.claude/skills/`、`.kimi/`、`.codex/`。无扫描器的 harness 靠 AGENTS.md 打开 `skills/<name>/SKILL.md`。

`{{VAULT}}` 替换：营销 `{{VAULT}}/02-SEO/seo-audit.md` → `deliverables/marketing/02-seo/seo-audit.md`（阶段目录小写）；`{{VAULT}}/00-System/learning-notes/` → `deliverables/marketing/00-system/`。获客 `{{VAULT}}/06-Outreach/cold-emails.md` → `deliverables/lead/06-outreach/cold-emails.md`。源 `{{VAULT}}/lead-generation/*.xlsx` 并入 `deliverables/lead/02-companies/` 或 `01-icp/` 对应文件，禁止保留 `deliverables/lead/lead-generation/`。Excel/CSV 同样只进上述树。

试点文件 `deliverables/value-proposition.md` 可保留到编排阶段表改写完成；其后 `marketing-copywriting` 改写到 `deliverables/marketing/03-content/`。

迁入白名单：`SKILL.md`、`references/**`、`scripts/**`、`assets/**`。黑名单：`AGENTS.md`、`evals.json`、`.DS_Store`、各 harness wrapper。

抽取后必须为每个 skill 建 `.agents/skills/<name>` 相对软链。不建 `.claude/skills/`。

---

## 8. 验收清单

在仓库根执行。任一条非零即失败。

1. **name 正则与目录一致**
   ```
   python3 - <<'PY'
   import re, pathlib, sys
   rx=re.compile(r'^(marketing|lead)-[a-z0-9]+(-[a-z0-9]+)*$')
   bad=[]
   for p in pathlib.Path('skills').glob('*/SKILL.md'):
       t=p.read_text(); n=re.search(r'^name:\s*(\S+)',t,re.M)
       if not n or n.group(1)!=p.parent.name or not rx.match(n.group(1)) or len(n.group(1))>64:
           bad.append(str(p))
   sys.exit(print('\n'.join(bad) or 'OK') or (1 if bad else 0))
   PY
   ```
2. **description 长度 300–700、无 `<>`**
   ```
   python3 - <<'PY'
   import re, pathlib, sys
   bad=[]
   for p in pathlib.Path('skills').glob('*/SKILL.md'):
       t=p.read_text(); m=re.match(r'^---\n(.*?)\n---',t,re.S)
       fm=m.group(1) if m else ''
       dm=re.search(r'^description:\s*>(.*?)(?=^[a-zA-Z0-9_-]+:|\Z)',fm,re.S|re.M)
       val=' '.join((dm.group(1) if dm else '').split())
       if not (300<=len(val)<=700) or '<' in val or '>' in val: bad.append(f'{p} {len(val)}')
   sys.exit(print('\n'.join(bad) or 'OK') or (1 if bad else 0))
   PY
   ```
3. **禁用 frontmatter 字段**
   ```
   rg -n '^(allowed-tools|disallowed-tools|model|effort|context|agent|hooks|paths|globs|disable-model-invocation|disableModelInvocation|user-invocable|when_to_use|whenToUse|arguments|argument-hint|type|icon|color|background|shell):' skills/*/SKILL.md
   ```
   期望：无匹配。
4. **harness 工具 ID / 变量**
   ```
   rg -n 'mcp__|\$ARGUMENTS|\$\{CLAUDE_SKILL_DIR\}|\$\{KIMI_SKILL_DIR\}|spawn_agent|context: fork' skills
   ```
   期望：无匹配。`dispatch a subagent, else do it inline` 必须在编排 skill 中出现：
   ```
   rg -n 'dispatch a subagent, else do it inline' skills/marketing-orchestrator/SKILL.md
   ```
5. **产品词**
   ```
   rg -i -n '不锈钢|屏风|佛山|Foshan|PVD|Linker|金达|Jinda|316L|广交会|Canton Fair|stainless steel|Made-in-China|Made in China|Marketing-Vault|LeadGen-Vault|Obsidian|\{\{VAULT\}\}|阿里巴巴|\bAlibaba\b|\bShopify\b' skills
   ```
   期望：无匹配。若命中在已标注例子块，人工确认后改写或删除，不得留无标注命中。
6. **例子标注**
   ```
   python3 - <<'PY'
   import pathlib, sys
   bad=[]
   for p in pathlib.Path('skills').glob('*/SKILL.md'):
       t=p.read_text()
       if ('## 例子' in t or '## Examples' in t) and '仅供理解，禁止引用到输出' not in t:
           bad.append(str(p))
   for p in pathlib.Path('skills').glob('*/references/examples.md'):
       if '仅供理解，禁止引用到输出' not in p.read_text(): bad.append(str(p))
   sys.exit(print('\n'.join(bad) or 'OK') or (1 if bad else 0))
   PY
   ```
7. **路径**
   ```
   rg -n '/Users/|/home/chesterjohn|Marketing-Vault|LeadGen-Vault|\$\{CLAUDE_SKILL_DIR\}' skills AGENTS.md state
   rg -n '~/Documents/' skills AGENTS.md state
   ```
   第一条期望无匹配。第二条每条路径必须以 `~/Documents/New` 开头。
8. **行数上限**
   ```
   wc -l skills/*/SKILL.md | awk '$1>=500{print}'
   ```
   期望：无 skill 行。`wc` 最后一行 total 忽略。
9. **扁平与软链**
   ```
   find skills -mindepth 3 -name SKILL.md
   # 期望空。然后每个 skills/<name> 都有 .agents/skills/<name> 软链：
   python3 - <<'PY'
   import pathlib, sys
   bad=[]
   for d in pathlib.Path('skills').iterdir():
       if not (d/'SKILL.md').exists(): continue
       link=pathlib.Path('.agents/skills')/d.name
       if not link.is_symlink() or link.resolve()!=d.resolve():
           bad.append(d.name)
   sys.exit(print('\n'.join(bad) or 'OK') or (1 if bad else 0))
   PY
   ```
10. **产出根**
    ```
    rg -n '\{\{VAULT\}\}|vault_path' skills
    ```
    期望：无匹配。方法 skill 的产出路径必须以 `deliverables/marketing/` 或 `deliverables/lead/` 开头。

### 冒烟（供 `acceptance-review-and-smoke` 直接用）

环境：新会话、cwd = 本仓库根、只靠 AGENTS.md + `.agents/skills/`。先探测五家 CLI（Kimi / Z Code / DeepSeek / OpenCode / Hermes）是否安装登录；缺的列给用户，不在抽取票内安装。

| # | 动作 | 通过标准 |
| --- | --- | --- |
| S1 | 提示：「做这个仓库设定的下一步。不要让我解释仓库。」 | 读 `state/status.md`；宣布 phase / 方法 skill / 产出路径；不询问 slash command |
| S2 | 推进到一个方法 skill 落地 | `deliverables/` 下非空新文件；内容能回溯 `~/Documents/New`；**不是** skill 例子原文 |
| S3 | 寒暄：「你好」 | 只复述 phase，不改文件、不跑管线 |
| S4 | 抽一个已迁入方法 skill（如 `marketing-content-strategy` 或 `marketing-site-and-schema`）对 New 里一个真实页面任务跑一遍 | 产物可执行；无不锈钢词；无 `mcp__` |
| S5 | 对照源文件抽查 20% skill | 方法步骤仍在；产品锁与 harness 字段已剥 |

子代理逐 skill review 四问：方法保真、无禁止词、无禁用字段、例子标注与前缀正确。

---

## 附录 A. lead-gen 43 个命名映射

重叠列供 overlap 票，本票不合并。

| 源 name | 目标 name | 近似 marketing |
| --- | --- | --- |
| buyer-psychology | lead-buyer-psychology | marketing-psychology |
| cold-email-gen | lead-cold-email-gen | marketing-email-outreach |
| company-research | lead-company-research | |
| competitor-analysis | lead-competitor-analysis | marketing-competitor-intelligence |
| contact-discovery | lead-contact-discovery | |
| data-validation | lead-data-validation | |
| distributor-research | lead-distributor-research | |
| email-sequence-strategy | lead-email-sequence-strategy | marketing-email-outreach |
| followup-sequence | lead-followup-sequence | marketing-email-outreach |
| icp-analysis | lead-icp-analysis | marketing-profile |
| lead-generation | lead-generation | marketing-orchestrator（编排，不合并） |
| lead-interview | lead-interview | |
| lead-magnet-gen | lead-magnet-gen | |
| lead-teach | lead-teach | marketing-teach |
| linkedin-authority | lead-linkedin-authority | marketing-social-content |
| linkedin-behind-scenes | lead-linkedin-behind-scenes | marketing-social-content |
| linkedin-buyer-concern | lead-linkedin-buyer-concern | marketing-social-content |
| linkedin-education | lead-linkedin-education | marketing-social-content |
| linkedin-expertise | lead-linkedin-expertise | marketing-social-content |
| linkedin-faq | lead-linkedin-faq | marketing-social-content |
| linkedin-market-challenge | lead-linkedin-market-challenge | marketing-social-content |
| linkedin-mythbust | lead-linkedin-mythbust | marketing-social-content |
| linkedin-pain-solution | lead-linkedin-pain-solution | marketing-social-content |
| linkedin-personal-story | lead-linkedin-personal-story | marketing-social-content |
| linkedin-topic-research | lead-linkedin-topic-research | marketing-social-content |
| market-analysis | lead-market-analysis | marketing-foundation |
| product-knowledge | lead-product-knowledge | marketing-product-profile |
| retailer-research | lead-retailer-research | |
| search-term-expansion | lead-search-term-expansion | |
| seo-content-edit | lead-seo-content-edit | marketing-seo-audit / marketing-content-strategy |
| seo-content-gen | lead-seo-content-gen | 同上 |
| seo-editorial-guidelines | lead-seo-editorial-guidelines | 同上 |
| seo-outline-gen | lead-seo-outline-gen | 同上 |
| service-delivery | lead-service-delivery | |
| service-first-contact | lead-service-first-contact | |
| service-first-order | lead-service-first-order | |
| service-objection | lead-service-objection | |
| service-quotation | lead-service-quotation | |
| service-retention | lead-service-retention | marketing-retention |
| targeted-outreach | lead-targeted-outreach | marketing-email-outreach |
| targeted-research | lead-targeted-research | |
| usp-extraction | lead-usp-extraction | marketing-positioning |
| warm-email-transform | lead-warm-email-transform | marketing-email-outreach |
