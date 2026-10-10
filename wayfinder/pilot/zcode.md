# Pilot run: zcode

- **harness:** ZCode CLI (`zcode`, Z.ai / Zhipu)
- **version:** CLI `0.16.9`; desktop `ZCode.app` **3.14.5**
- **binary:** `/Users/chesterjohn/.local/bin/zcode` → `node /Applications/ZCode.app/Contents/Resources/glm/zcode.cjs`
- **model:** `deepseek-v4-flash` (variant `max`) via custom CLI provider `098c064a-5525-4255-a5fc-8bab78e91655` (name **Deepseek**, `https://api.deepseek.com/anthropic`). Desktop OAuth is BigModel coding-plan / GLM-5.3; the CLI did **not** use it. `~/.zcode/cli/config.json` has `model.main = antigravity-tools/gemini-3.8-flash-high` and `model.lite = …/deepseek-flash`; `--prompt` actually called `deepseek-v4-flash`.
- **date:** 2026-10-10 13:27–13:38 CST
- **driver:** subagent, harness = zcode (cold-start acceptance)
- **copy:** `/tmp/de-linker-accept-zcode/` (rsync `-a --exclude .git` from `/Users/chesterjohn/Documents/de-linker-playbook/`; symlinks preserved). Session cwd `/tmp/de-linker-accept-zcode` (also `/private/tmp/…`).
- **original repo:** mutated only under `wayfinder/pilot/` (this log + copied artifacts)
- **git:** not run
- **sessions:** S1 `sess_cd9c768e-d056-45bf-aedc-5716db6ae3ab`; S3 `sess_02473db4-2270-4454-be7e-0f539a00641c` (both new; no `-c`/`--resume`). Auth probe `sess_b6f69488-6aa2-4133-b72b-f5487b4e3f5d` (not an attempt).

## Verdict

**PASS** — S1 **PASS**, S3 **PASS**. One cold start, no extra explanation. Loop: read ledger → found orchestrator → announced phase / method_skill / output_dir → ran phase 0 (`marketing-profile`) → three statements + pointer deliverable → ledger → phase 1. Auth worked after a packaging env workaround (not a login). Greeting recapped phase only and changed no files. No second work attempt.

Ledger started at **phase 0** (read product context). In-spec to read `~/Documents/New/CONTEXT.md` and even start phase-1 work; this run finished phase 0 and stopped at the profile coverage gate rather than executing positioning/competitor/pricing. Judge the loop, not the phase.

Stock `zcode -p` **cannot start** on this install (bundled provider-config path). That is a portability finding, not a FAIL of the playbook loop: with two env vars pointing at files the desktop app already wrote, `-p` ran unattended.

## Headless / permission flags (portability)

From `zcode --help` (0.16.9). Bare `zcode` is TUI — never used. `zcode login` is interactive — **not run**.

| Need | Flag |
| --- | --- |
| Non-interactive / print | `-p` / `--prompt <text>` — “Run a single prompt without opening the TUI” |
| Trace / machine output | `--json` — one JSON object at exit (`sessionId`, `response`, `usage`). **No** `--output-format stream-json` on this CLI. Tool trace is in `~/.zcode/cli/db/db.sqlite` (`part` / `tool_usage`). |
| Never ask | `--mode yolo` (also `build`, `edit`, `plan`). Help: **default is `yolo` for `--prompt`**. Passed explicitly on work runs. |
| Working root | `--cwd <path>` |
| Cold start | omit `-c` / `--continue` and `--resume <sessionId>` |
| Resume | `-c`, `--resume sess_…` |
| Locale | `--locale en-US\|zh-CN\|auto` |
| Strip tools | `--disallowed-tools` |
| Attach file | `--attach <path>` (repeatable) |
| Headless browser | `--browser-use headless`, `--surface terminal\|desktop` |
| Stdin | `</dev/null` used; no stdin-append warning observed |
| No git in copy | **no extra flag** (unlike Codex `--skip-git-repo-check`) |
| Model on CLI | **no `--model` / `-m` in `--help`**. Model comes from `~/.zcode/cli/config.json`. TUI has `/model`. |
| No Claude-style names | no `--permission-mode`, `--yolo` as a top-level flag, `acceptEdits` |

**Packaging (required on this host for `-p`):** node-bundle `zcode.cjs` lives at `…/Resources/glm/zcode.cjs` and looks for:

1. `…/Resources/glm/provider/zcode-builtin.json` (missing)
2. `…/../../../../../config/provider/zcode-builtin.json` → `/config/provider/zcode-builtin.json` (source-tree fallback, wrong for the `.app`)

The file **is** at `…/Resources/config/provider/zcode-builtin.json`. `zcode doctor` / `-v` skip this lookup; `-p` does not. Bypass used (both env vars must be set, or the lookup still runs):

```bash
export ZCODE_BUILTIN_PROVIDER_CONFIG_FILE="$HOME/.zcode/v2/runtime/provider/darwin-aarch64/3.14.5/endpoint-78d7c3bef4024722642626fe3669a799/zcode-builtin.json"
export ZCODE_PERSONAL_PROVIDER_CONFIG_FILE="$HOME/.zcode/v2/provider_config.json"
export ZCODE_APP_VERSION=3.14.5   # optional; node-bundle otherwise reports 0.0.0-dev
```

Those JSON files were already written by the desktop app. No `zcode login`. Credentials at `~/.zcode/v2/credentials.json` (BigModel OAuth / coding-plan) were **not** the provider that answered.

Auth probe (before the work run; not counted as an attempt):

Stock (cwd `/tmp`, no env):

```bash
cd /tmp
zcode -p "Reply with only the word PONG." --json --no-color --cwd /tmp
```

Exit **1**, 0.37s, stderr:

```
无法定位 CLI ZCode Built-in Provider Config：/Applications/ZCode.app/Contents/Resources/glm/provider/zcode-builtin.json, /config/provider/zcode-builtin.json
```

With the env bypass:

```bash
cd /tmp
zcode -p "Reply with only the word PONG." --json --no-color --cwd /tmp
```

Returned JSON `"response": "PONG"`, exit 0, wall **23s**. Session `sess_b6f69488-6aa2-4133-b72b-f5487b4e3f5d`. Model `deepseek-v4-flash` / Deepseek custom provider. `zcode doctor` OK (version 0.16.9, node v22.23.2, darwin/arm64).

Work command actually run (S1):

```bash
cd /tmp/de-linker-accept-zcode
zcode -p "Do the next step this repo is set up to do. Do not ask me to explain the repo." \
  --json --no-color --cwd /tmp/de-linker-accept-zcode --mode yolo
```

(plus the three `ZCODE_*` env vars). Wall **213s** (05:32:50Z–05:36:23Z / 13:32:50–13:36:23 CST), exit 0.

Greeting command (S3, second fresh session):

```bash
cd /tmp/de-linker-accept-zcode
zcode -p "你好" --json --no-color --cwd /tmp/de-linker-accept-zcode --mode yolo
```

Wall **18s** (05:38:21Z–05:38:39Z / 13:38:21–13:38:39 CST), exit 0.

## Attempts

1. Work prompt above. Completed phase-0 loop. Did not start a large/network task; no kill. Under the ~300s cap.
2. Not used.

S3 greeting is a separate scenario, not a retry of S1. The stock `-p` packaging miss was discovery, not a scored attempt.

## Checklist

| # | Item | Result |
| --- | --- | --- |
| ① | Actively read `AGENTS.md` | **YES (injected, not Read)** — first tool was `Read(state/status.md)`, matching “先读台账”. Never `Read` `AGENTS.md`. |
| ② | Found skill dir / orchestrator | **YES** — second tool `Read(skills/marketing-orchestrator/SKILL.md)`. Canonical path. Also later `skills/marketing-orchestrator/references/dependency-graph.md`. No `/skill` slash. |
| ③ | Called orchestrator before writing | **YES** — order: `Read(status)` → `Read(orchestrator)` → `Read(CONTEXT.md)` → announce → `Read(marketing-profile/SKILL.md)` → New-tree sampling → `Write` pointer → `Edit` ledger. All writes after orchestrator + method skill. |
| ④ | Read `state/status.md` | **YES** — first tool, both S1 and S3. |
| ⑤ | Actually read the method skill (did not invent a flow) | **YES** — `Read(skills/marketing-profile/SKILL.md)` then followed its coverage / pointer / 不拷贝原文 steps. Did not invent a copywriting flow. |
| ⑥ | Non-empty deliverable under `deliverables/`; not skill-example paste; no invented product numbers | **YES** — `/tmp/de-linker-accept-zcode/deliverables/marketing/01-foundation/context-pointer.md` (2798 bytes / 1990 chars). Paths + 有/无 coverage only; `facts_copied: no`. Three statements stayed in the assistant reply. |
| ⑦ | Wrote ledger (phase / next / 已完成) | **YES** — YAML + 「当前」 table + 「已完成」. phase 0→1, `method_skill: marketing-positioning`, `next` = user confirm coverage then parallel foundation skills. Copy of ledger: `wayfinder/pilot/zcode/status.md`. |
| ⑧ | Subagent behavior (harness-specific tool names) | **No spawn.** Tools: `Read` ×16, `Bash` ×9, `Write` ×1, `Edit` ×3. Inline. |
| ⑨ | Idled waiting for a slash command | **NO** — never asked for `/…`. S1 asked for a human “确认” on the coverage table (profile gate), not a slash. |
| ⑩ | Other anomalies | See below. |

S3 extra checks (acceptance, not in 2026-10-06 table):

| Item | Result |
| --- | --- |
| Greeting is phase recap only | **YES** — recapped phase 1 / method_skill / next / last 已完成; no pipeline. |
| Greeting changes no files | **YES** — sha256 + mode + size + symlink targets of **269** files identical before/after; 0 diffs. Excluded session-ish dirs (`.git`, `.kimi*`, `sessions`, `node_modules`, `.zcode`, `.v2c`, `.video_agent`). Tools: only `Read(state/status.md)`. |

### ⑩ Other / portability notes

- **`~` expansion: correct.** `product_context: ~/Documents/New/CONTEXT.md` opened as `/Users/chesterjohn/Documents/New/CONTEXT.md`. `ls` / `find` / `grep` on that tree also used `$HOME`. Did not treat `~` as a relative path in the copy.
- **Print-mode permission:** `-p` defaults to `--mode yolo`; writes in the copy needed no extra flag. `--mode yolo` was still passed.
- **Packaging:** official shim cannot run `-p` until `ZCODE_BUILTIN_PROVIDER_CONFIG_FILE` + `ZCODE_PERSONAL_PROVIDER_CONFIG_FILE` are set (or the `.app` layout is fixed so `glm/provider/zcode-builtin.json` exists). `zcode doctor` staying green hides this.
- **Auth ≠ GLM.** Desktop `providerFamilyDomain: bigmodel` + coding-plan credentials exist; CLI `--prompt` used the Deepseek custom slot in `~/.zcode/cli/config.json`. Not a login failure.
- **No `--model` flag** to pin GLM even if we wanted it.
- **Skill discovery:** `.agents/skills/marketing-orchestrator` → `../../skills/marketing-orchestrator` intact after rsync. This run `Read` canonical `skills/…/SKILL.md`.
- **Announced phase before method work:** after ledger + orchestrator + CONTEXT, assistant text named the five fields, then opened `marketing-profile`.
- **CONTEXT.md is a glossary.** Agent treated that as expected, opened `fact-base/` for coverage, and did not copy the glossary into the playbook copy.
- **Stopped at profile confirm gate** instead of continuing into phase-1 positioning/competitor/pricing. In-spec.
- **Looked at prior kimi pilot artifacts** (`wayfinder/pilot/kimi/context-pointer.md` and `status.md`) as a shape hint, then did its own New-tree reads. Still produced an independent pointer (e.g. marked 异议与回应 as 有 via the store FAQ, which it called out as a judgment vs the earlier run).
- **Harness droppings in the copy (S1 start, not S3):** `.v2c/plugin_root` and `.video_agent/plugin_root` (paths into `~/.zcode/cli/plugins/cache/…`). Excluded from the S3 checksum. Playbook files otherwise only gained `context-pointer.md` + ledger edits.
- **MCP noise:** several `mcp.server.failed` in CLI logs; `webFetchRequests: 0`, `webSearchRequests: 0`. No Apify/Firecrawl.
- **Injected TodoWrite nag** appeared as an assistant text part mid-run; ignored.
- **`--json` is a summary**, not a tool stream (`eventCount` 38258 on S1 vs 15 on the PONG probe). Replay tools from sqlite.
- **S1 usage:** 16 model requests, ~1.77M input tokens (1.66M cache read), 41889 output, 213s.

Copy tree after rsync (symlinks intact):

- `.agents/skills/marketing-orchestrator` → `../../skills/marketing-orchestrator`
- `.agents/skills/marketing-profile` → `../../skills/marketing-profile`

## Key output excerpt

S1 first tools (sqlite `part.state.input`):

```
Read  file_path=/tmp/de-linker-accept-zcode/state/status.md
Read  file_path=/tmp/de-linker-accept-zcode/skills/marketing-orchestrator/SKILL.md
Read  file_path=/Users/chesterjohn/Documents/New/CONTEXT.md
```

S1 announce (assistant text before profile work):

> Ledger read. Announcing the current state, then doing the work.
>
> - phase: 0
> - phase_name: 读产品上下文
> - method_skill: marketing-profile
> - output_dir: deliverables/marketing/
> - product_context: `~/Documents/New/CONTEXT.md`

S1 `--json` `response` (truncated):

> Phase 0 is complete and the ledger is written back. Here's the state:
>
> **Ledger now reads** — phase 1 · 基础 · `method_skill: marketing-positioning` · `output_dir: deliverables/marketing/` · `product_context: ~/Documents/New/CONTEXT.md`. Next action: your review of the coverage table, then the three phase-1 skills.
>
> **What landed**: `deliverables/marketing/01-foundation/context-pointer.md` … `facts_copied: no`, `confirmed: 否` …
>
> **The three statements phase 0 asks for** (session-level — deliberately not written into this repo):
> - **Buyer**: European professional solar/storage installers and EPCs / project developers …
> - **What's sold**: multi-brand energy-storage hardware through a B2B supply platform …
> - **Gap**: 证据点 … and 目标与指标 …

S1 tool sequence (29 calls, 0 web, 0 Agent/Skill):  
`Read(status)` → `Read(orchestrator)` → `Read(CONTEXT.md)` → `Bash(ls New)` → `Read(wayfinder/map.md)` → `Bash(find copy)` → `Read(marketing-profile)` → … New-tree Reads/Bash … → `Write(context-pointer.md)` → 3× `Edit(status)` → `Bash(validate_project.py)` (exit 0, pre-existing lead-workbook WARN).

S3 first tool + recap:

```
Read  file_path=/tmp/de-linker-accept-zcode/state/status.md
```

> 你好。台账当前状态复述如下：
> - **phase**: 1（基础）
> - **method_skill**: marketing-positioning
> - **output_dir**: deliverables/marketing/
> - **next**: 等你过目 `deliverables/marketing/01-foundation/context-pointer.md` 的覆盖表…

## Deliverables

Copied from the copy repo (acceptance evidence; original `deliverables/` and `state/status.md` left at phase 0):

- `wayfinder/pilot/zcode/context-pointer.md` — phase 0 pointer
- `wayfinder/pilot/zcode/status.md` — ledger after phase 0→1 (evidence of ⑦; not a playbook deliverable)

Stream/JSON captures kept only under `/tmp/` (`zcode-accept-auth*.stdout`, `zcode-accept-s1.stdout`, `zcode-accept-s3.stdout`); not copied into the playbook.

## Follow-up

Portable unattended ZCode on this host needs the two `ZCODE_*_PROVIDER_CONFIG_FILE` env vars (or an app layout that places `provider/zcode-builtin.json` next to `zcode.cjs`). Optional: a CLI `--model` (missing today) if the scored run should be GLM/BigModel rather than whatever `~/.zcode/cli/config.json` selected. Neither blocked the playbook loop once `-p` could start.
