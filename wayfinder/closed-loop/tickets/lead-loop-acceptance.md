---
wayfinder: task
status: open
assignee: Codex 会话 2026-10-20
step: 7
blocked_by: [lead-loop-orchestrator, mailbox-pullback, activation-list-intake, l3-pullback]
---

# 获客线闭环验收

## Question

（HITL）用真实动作走一遍获客线：从激活名单里一家已调研的公司出发 → 产出外展信 → 操作者手动从 chester@ 发出 → 口述 → AI 在已发送里查证并写执行登记 → 送达 / 回复回流底表与看板 → 操作者说「下一步获客」→ AI 引用这条数据给出一个动作（有回复 / 无回复 / 退信各自合理）。

- 失败的环节当轮修，修不了的切新票并在本图登记。
- 证据存 vault；公开仓库只记「通过 / 不通过 + 环节」。

## 完成标准

- 一封真实发信能沿链追到底表、看板与 AI 下一步，且下一步可回溯到规则。

## 获客编排交接（「获客编排改循环」关票时写入，2026-10-15）

- **「下一步获客」**：按 `skills/lead-generation/SKILL.md` 走。脚本是 `uv run scripts/next_step.py --line 获客`，会话里先用 `--format json`，再按第 11 节说给操作者。
  - 冷启动下，只有 P1、P2 插队（真人回复 M-01 到 M-03 是 P1；永久退信 M-05、到期的下一封 M-11 是 P2）。P3–P5 让位给阶段工作，只顺带报告。
  - 验收要看三种情况：有回复 → M-01/M-02/M-03（P1）；无回复 → M-11（到期，P2）或 M-12、M-13（P5，只记账）；退信 → M-05（P2）或 M-06（P5）。
- **基线**：2026-10-15 16:31 在真实底表上，获客线 0 条登记、0 条邮件反馈、0 条询盘。输出是「今天没有要动的」，并列出在等的三样（原文见「获客编排改循环」Resolution）。验收时这三条应该变成引用具体登记编号、事件日期的动作。
- **登记那一环**：发信后按 `skills/marketing-execution-log/SKILL.md` 登记，必须带 `--line 获客`、`--company`、`--sequence S-公司名`、`--nth`。最好再带 `--planned` 和 `--next-date`，不带的话无回复时只会落到 M-13，只记账。编号写进获客台账的 `current_action_log`。
- **台账**：每轮都要回写 `feedback_read_at`、`current_action`、`current_action_log`。验收时可以对一下，营销台账没有被改。
- **询盘**：没归因的询盘两条线都会报告。只有填了「归因登记编号」、并且指向获客登记的，才只出现在获客线。

## 审稿交接（「操作者审稿」关票时写入，2026-10-15）

- 「产出外展信」这一步要走审稿（`docs/feedback-rules.md` 第 10 节）：初稿过证据闸 → 给操作者看 → 按意见改到操作者说「可以了」（`operator_ok`）→ 操作者从 chester@ 手动发出。审稿至少一轮，记录留在交付物里。
- 操作者在邮箱里发前又改过的，登记时把实际发出的版本同步回交付物，否则邮箱回流在「已发送」里对上的和交付物不是同一份字。
- 有回复时，回信（M-01–M-03）同样先审稿再发。

## 不代发（用户 2026-10-15 写入）

- 验收时确认：这一轮对外文字全部由操作者亲手发出，AI 没有代发、代发布或在任何工具里建活动 / 排期；交付物的 `send_status` / `publish_status` 为 `copy_only`，发没发以执行登记为准。`python3 evals/validate_project.py` 会拦 skill 里的代发口子。

## 激活名单交接（「激活名单入口」关票时写入，2026-10-15）

- **从哪家出发**：名单里已调研的是 `L-0002`，调研文件在 vault `deliverables/lead/02-companies/activation/L-0002.md`，`approved`，结论 `可接触`。
  - 查名单原行：`uv run scripts/activation_list.py show --id L-0002`。
  - 再要别家：`uv run scripts/activation_list.py progress` 给下一家，下一家是 L-0021（priority 1）。
- **公司名写法**：执行登记的 `--company` 和 `--sequence S-公司名`，都照名单 CSV 的 `company_name` 原文，和调研文件的标题、表行一致。官网或 Creditreform 上的其他写法只记在调研文件里，不用。
- **外展前还缺什么**：依赖图里 `lead-cold-email-gen -> [lead-icp-analysis, lead-usp-extraction]` 没改，而获客台账还在 phase 0，这两份都没有。所以写外展信之前，二选一：
  - 先把 phase 1 的 ICP、phase 4 的竞品分析、phase 5 的 USP 做到 `approved`；
  - 或者操作者明确同意跳过，记进获客台账「豁免」表。
- **联系人**：`lead-contact-discovery/list -> [lead-company-research/list]`，从名单取，`data_source` 指回名单行。名单里约 1612 行是免费邮箱（gmx、gmail、web.de 等），照录，在采集报告里列出。L-0002 的调研结论里写了接触前要知道的两点（细节在 vault 调研文件「结论」节）：它现在经一家电气批发商拿材料和方案支持；它用哪家的逆变器或储能〔未证实〕。
- **隐私**：名单有约 8 千人的姓名、邮箱、电话，只在私有 vault。验收证据里写编号，不写人名或邮箱。

## 进展（2026-10-20）

- 用户要求把验收改成“真实案例 + 销售判断力带教”，不在未学习时直接代做全部判断。学习状态在 vault `deliverables/lead/00-system/learning-state.md`，六项量表在同目录 `sales-judgment-rubric.md`。
- 本轮完成第一单元 `lead-buyer-psychology` 的 Stage 1 教学，并以交互式白板重新交付：vault `deliverables/lead/00-system/lead-academy-canvas.html`，可用 `uv run scripts/lead_academy.py` 打开。操作者拖动角色、画依赖箭头、把证据便签放区域，再把最小帮助接到关系线上。每一步都有可见的概念带与“你的画布说明了什么”即时反馈；最后回放关系图和三条判断规则。当前停在 Stage 2，等待操作者提交画布数据；未读取操作者答案前不得开始 Stage 3 系统独立稿。Markdown 讲义只作内部母稿，不要求操作者阅读。
- 操作者已提交第一单元画布 JSON，原文保存为 vault `deliverables/lead/00-system/my-work-lead-buyer-psychology.md`。系统独立稿在 `lead-buyer-psychology-system-output.md`，对比与 4/6 反馈在 `lead-buyer-psychology-comparison.md`。Apify 四条查询成功；两条并发查询因 16 GB 内存上限失败后按顺序用 2 GB 重跑成功，incumbent 页被 403/500 挡住后换查询与 Playwright 修复成功。
- 当前进入 Stage 4 的操作者笔记环节。用户 2026-10-20 明确否决画布式学习，要求退回第一版 HTML，并改用直接对话教学；`lead_academy.py` 已切回 `deliverables/lead/00-system/lead-academy.html`，白板与单独复盘页删除。后续只保留 HTML 参考，实际教学用一次一问的对话。必须等操作者自己写出复盘笔记后才算第一单元完成，不能代写。
- 用户要求所有外部搜索、验证、竞品与规则研究先把 Apify 修到可用。Token 已放仓外 mode-600 配置，`apify/rag-web-browser` 已实际跑通：run `ptP9nMbm8mjguEQbA`，dataset `7Mn2BNZky2iuYk6hv`，状态 `SUCCEEDED`；规则正典为 `docs/apify.md`。
- **进展（2026-10-21）**：第一学习单元 `lead-buyer-psychology` 的四块操作者笔记已完成，`learning-state` 记为 1 个单元完成；量表仍为 4/6。下一学习单元为 `lead-icp-analysis`，从 Stage 1 开始。教学完成没有改变获客台账 `phase`，验收票继续 open。
- **进展（2026-10-21，续）**：`lead-icp-analysis` Stage 1 教学稿已完成，进入 Stage 2 操作者练习。候选起点只用产品上下文已明确的安装商、EPC、经销商，L-0002 仅作单公司局部证据。获客台账仍为 phase 0。
- **进展（2026-10-21，社会倾听）**：按“先宽后窄、全球可用”完成 Reddit、LinkedIn、Facebook、Instagram、TikTok 第一轮安装商/下游公开内容扫描。研究记录在 vault `deliverables/lead/00-system/research/installer-social-listening-2026-10-21.md`；DIY/业主标为“客户的客户”，不混入直接 ICP。没有把“晚到/装错”定成安装商痛点。获客台账仍为 phase 0。
- **进展（2026-10-21，Facebook 登录态复用）**：操作者在 Chrome `Default` 登录一次后，`c_user` / `xs` 已于 12:41 更新。`opencli facebook whoami` 读回 `logged_in: true`，`opencli facebook search "solar installer Germany"` 与 `facebook-safe search` 均成功；旧 `Profile 2` 和 yt-dlp 导出仍无效。`facebook-safe` 已改为按 Chrome profile 最近访问时间选择 cookie，并在使用前探测登录态，后续直接复用同一浏览器会话，不再要求逐次登录。细节见 vault `deliverables/lead/00-system/research/toolchain-update-audit-2026-10-21.md`。
- **进展（2026-10-21，OpenCLI 补证与全链路）**：OpenCLI 已作为 Apify 之后的公开社媒补充路径写入 `docs/social-research-opencli.md`，并由根 `AGENTS.md`、共享标准、获客编排、搜索协议、ICP skill 和教学参考共同引用。研究范围改为完整链路：上游制造商/供应商、渠道、EPC/安装商、下游客户、规则闸门都要看；供应商观察、渠道语言和下游压力只作邻近证据，只有直接采购角色进入主 ICP。第二轮完成 41 次 OpenCLI 只读调用，覆盖 LinkedIn、Facebook、TikTok、Instagram、Reddit、YouTube、X 和 Bluesky；另用 7 次 X 专用 Apify 调用取得 270 条搜索/回复记录，证明 X 批量研究应走 Apify、OpenCLI 只做补充。证据、角色分级与缺口在 vault `deliverables/lead/00-system/research/opencli-full-chain-pass2-2026-10-21.md`。
- **进展（2026-10-21，获客知识库）**：新增私有知识库 `deliverables/lead/00-system/knowledge/knowledge-base.json`、HTML 审计台 `knowledge-base.html` 和维护脚本 `scripts/lead_kb.py`。当前收录 10 份资料、28 条 active 证据、3 个问题、9 条反馈。Agent 每轮先运行 `brief` 从 active 证据选题；每题登记 `option_evidence`、`analysis_chain`、`evidence_gaps` 和知识快照；`add-feedback` 可关联受影响证据，`update-evidence` 保留修订历史，`archive-evidence` 让旧结论退出默认检索。脚本强制解析到 `/Users/chesterjohn/Documents/de-linker-vault`，逐份校验原始文档存在，`trace-question` 可展开完整分析链和来源；知识库通过语义校验和 JSON Schema，HTML 桌面与移动端无错误。
