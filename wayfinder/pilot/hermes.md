# Pilot run: hermes

- **harness:** Hermes Agent CLI (`hermes`)
- **version:** `Hermes Agent v0.21.6+387.gdce1e9b (2026.9.24) · stable · local dce1e9b37581`
- **binary:** `/Users/chesterjohn/.local/bin/hermes` (install `/Users/chesterjohn/.hermes/hermes-agent`, method git)
- **model (config default):** `grok-4.6` / provider `xai-oauth`
- **model (scored work / S3):** `k3-256k` / provider `kimi-coding` (`-m` + `--provider`; default xAI hit HTTP 402 mid-matrix)
- **date:** 2026-10-10 13:27–14:01 CST
- **driver:** subagent, harness = hermes
- **copy:** `/tmp/de-linker-accept-hermes/` (rsync `-a --exclude .git` from `/Users/chesterjohn/Documents/de-linker-playbook/`; symlinks preserved). Scored run: process cwd + `TERMINAL_CWD` + isolated `HERMES_HOME=/tmp/hermes-accept-home` (config `terminal.cwd` = copy; `.env`/`auth.json` symlinked). Runtime prompt CWD = `/tmp/de-linker-accept-hermes`.
- **original repo:** mutated only under `wayfinder/pilot/` (this log + `wayfinder/pilot/hermes/` copies)
- **git:** not run against the copy (copy has no `.git`; Hermes did not refuse)
- **sessions:** auth `20261010_132730_72883d`; S1 att.1 `20261010_132807_4daac1`; att.2 `20261010_133938_4f5c37`; att.3 killed `20261010_135229_0d46f2`; att.4 false-kill `20261010_135632_5186fb`; **scored S1** `20261010_135750_8d1210`; first S3 (host home) `20261010_134546_f374af`; **scored S3** `20261010_140037_7b5fc3`. Fresh sessions (no `--resume` / `-c`).

## Verdict

**PASS** (S1 **PASS**, S3 **PASS**) after an invocation-layer CWD fix. Attempts 1–3 are history: `--in` / process `cd` / `TERMINAL_CWD` / `--ignore-user-config` still left the runtime CWD at `$HOME` because `apply_terminal_config_to_env(override=True)` writes `config.yaml` `terminal.cwd: /Users/chesterjohn` over the env. Isolated `HERMES_HOME` with `terminal.cwd` = copy is what actually rooted the agent.

Scored S1 (attempt 5): first tool `read_file state/status.md` (copy-relative), then `skills/marketing-orchestrator/SKILL.md`, announced phase 0 / `marketing-profile` / `deliverables/marketing/`, expanded `~/Documents/New/CONTEXT.md`, followed `marketing-profile`, wrote a pointer (not CONTEXT 原文), rewrote the copy ledger to `phase: 1` / `method_skill: marketing-positioning` / `output_dir: deliverables/marketing/01-foundation/`, stopped. No slash. No writes to the original playbook or `Documents/de-linker`. Wall **122s**.

Scored S3: fresh session, prompt `你好`, read `state/status.md`, recapped **phase 1**, checksum of the copy **identical**. Mild extra “有什么想做的？”.

Judge the loop, not the phase. 0→1 with three statements is in-spec. Original `state/status.md` left at phase 0 (`29261b27…`).

## Headless / permission flags (portability)

From `hermes --help` / `hermes chat --help` (v0.21.6):

| Need | Flag |
| --- | --- |
| Non-interactive / batch | Top-level `hermes -z/--oneshot PROMPT` — “print ONLY the final response”; tools/memory/rules/`AGENTS.md` in CWD load as normal; **approvals auto-bypassed**. Or `hermes chat -q QUERY` with `--oneshot` / `-Q` / non-TTY (answers and exits). |
| Trace tool use | `hermes chat -q … --format stream-json` (JSONL events: `system`/`tool_use`/`tool_result`/`text`/`result`; implies `--quiet`; not with `--tui`). `-z` has **no** tool trace. |
| Never hang on dangerous-command prompts | `--yolo` (chat). `-z` already auto-bypasses approvals. |
| Never hang on hook prompts | `--accept-hooks` (or `HERMES_ACCEPT_HOOKS=1`) |
| Wall-clock cap | `chat --run-budget SECONDS` (80% wrap-up notice). Used `300` for S1, `120` for S3. |
| Working root | **`--in DIR` is global** (chdir + session identity). **Not enough on this host.** `tools.terminal_tool._ensure_terminal_env_bridged` → `apply_terminal_config_to_env(override=True)` copies `config.yaml` `terminal.cwd` onto `TERMINAL_CWD`, which `resolve_agent_cwd()` prefers over process cwd. `--ignore-user-config` skips `load_cli_config()` but **not** this bridge. Fix that worked: isolated `HERMES_HOME` whose `config.yaml` has `terminal.cwd: /tmp/de-linker-accept-hermes`, plus `TERMINAL_CWD` and `cd` to the copy. |
| Cold start | omit `--resume`/`-r` and `--continue`/`-c` |
| Resume | `-r SESSION` / `--resume latest`; `-c [name]`; `--no-restore-cwd` |
| Isolate from `~/.hermes/config.yaml` | `--ignore-user-config` (`.env` credentials still load). Does **not** skip `SOUL.md` / memory / `USER.md`. |
| Skip AGENTS.md + SOUL + memory | `--ignore-rules` — **not used** (would also drop the copy’s `AGENTS.md`) |
| Model / provider | `-m MODEL --provider PROVIDER` (also `HERMES_INFERENCE_MODEL`) |
| Usage JSON | `--usage-file PATH` with `-z` only |
| Stdin | `</dev/null` used. `hermes send` is messaging, not an agent loop. |
| No git in copy | **no extra flag** |
| No Claude-style names | no `--permission-mode`, `acceptEdits`, `--dangerously-skip-permissions`. Closest: `--yolo` + `-z`. |

User `~/.hermes/config.yaml`: `model.default: grok-4.6`, `model.provider: xai-oauth`, `terminal.cwd: /Users/chesterjohn`, `agent.reasoning_effort: high`, `memory_enabled: true`, plugin `stop-that-shit` enabled, fallback `kimi-coding/k3-256k` then `deepseek/deepseek-v4-flash`. Gateway was running. `SOUL.md` identity is “persistent personal agent / not a coding copilot”.

`hermes -z` is the scripted oneshot; **scored runs used `chat -q --oneshot --format stream-json`** so tools could be judged.

## Auth probe (not counted as an attempt)

Default model (cwd `/tmp`, `--in /tmp`):

```bash
cd /tmp
hermes chat -q "Reply with only the word PONG." \
  --oneshot --format stream-json --in /tmp --source tool --accept-hooks \
  </dev/null
```

Exit 0, ~16.01s. Init model `grok-4.6`. Text `PONG`. Session `20261010_132730_72883d`. `hermes doctor` OK before the matrix. `hermes auth list`: xai-oauth `device_code`, kimi-coding, deepseek, minimax-cn, copilot.

`--ignore-user-config` without `-m` (not a work attempt):

```bash
hermes --in /tmp --ignore-user-config --yolo chat -q "Reply with only the word PONG." \
  --oneshot --format stream-json --accept-hooks </dev/null
```

Exit 1, ~22.5s. HTTP **402** xAI `personal-team-blocked:spending-limit` on `grok-4.6`.

Stored-provider retry (the model used for S1 attempt 2 / S3):

```bash
hermes --in /tmp --ignore-user-config --yolo -m k3-256k --provider kimi-coding \
  chat -q "Reply with only the word PONG." \
  --oneshot --format stream-json --accept-hooks </dev/null
```

Exit 0, ~19.49s. Text `PONG`. Init model `k3-256k`.

## Headless commands actually run

S1 attempt 1 (user config, `--in` on `chat`):

```bash
cd /tmp/de-linker-accept-hermes
hermes chat -q "Do the next step this repo is set up to do. Do not ask me to explain the repo." \
  --oneshot --format stream-json --yolo --accept-hooks --run-budget 300 \
  --in /tmp/de-linker-accept-hermes --source cli \
  </dev/null
```

Wall **345.82s** (05:28:05Z–05:33:51Z), exit 0. Session `20261010_132807_4daac1`. Export: `cwd /private/tmp/de-linker-accept-hermes`, billed `k3-256k` / `kimi-coding` (init JSON still said `grok-4.6`; fallback after xAI). `duration_ms: 342080`. `--run-budget 300` wrap-up fired.

S1 attempt 2 (scored flags retry; stdin closed):

```bash
cd /tmp/de-linker-accept-hermes
hermes --in /tmp/de-linker-accept-hermes --ignore-user-config --yolo --accept-hooks \
  -m k3-256k --provider kimi-coding \
  chat -q "Do the next step this repo is set up to do. Do not ask me to explain the repo." \
  --oneshot --format stream-json --run-budget 300 \
  </dev/null
```

Wall **291.16s** (05:39:32Z–05:44:23Z), exit 0. Session `20261010_133938_4f5c37`. Tokens input 22260 / output 6086 / cache_read 316928. Still no playbook tools.

S3 first try (host `HERMES_HOME`, not scored — SOUL recap):

```bash
cd /tmp/de-linker-accept-hermes
hermes --in /tmp/de-linker-accept-hermes --ignore-user-config --yolo --accept-hooks \
  -m k3-256k --provider kimi-coding \
  chat -q "你好" --oneshot --format stream-json --run-budget 120 \
  </dev/null
```

Wall **21.64s**, session `20261010_134546_f374af`, 0 tools, SOUL “学前阶段”.

S1 attempt 3 (killed): `cd` + `TERMINAL_CWD=/tmp/de-linker-accept-hermes` + `--ignore-user-config`. Runtime prompt CWD still `$HOME`. First tool `search_files path=/Users/chesterjohn pattern=*stop-that-shit*`. Watchdog SIGTERM. Session `20261010_135229_0d46f2`, wall ~29s.

S1 attempt 4 (false kill): isolated `HERMES_HOME=/tmp/hermes-accept-home` (config `terminal.cwd` = copy; `.env`/`auth.json` symlinks). First tools were copy-relative `state/status.md` + orchestrator + CONTEXT.md; watchdog wrongly treated `ls ~/Documents/New` as a home probe. Session `20261010_135632_5186fb`.

S1 attempt 5 (**scored**):

```bash
cd /tmp/de-linker-accept-hermes
export HERMES_HOME=/tmp/hermes-accept-home
export TERMINAL_CWD=/tmp/de-linker-accept-hermes
hermes --yolo --accept-hooks -m k3-256k --provider kimi-coding \
  chat -q "Do the next step this repo is set up to do. Do not ask me to explain the repo." \
  --oneshot --format stream-json --run-budget 300 \
  </dev/null
```

Wall **122.47s** (05:57:48Z–05:59:50Z), exit 0. Session `20261010_135750_8d1210`. `duration_ms: 119740`. Tokens input 18193 / output 4701 / cache_read 177687. Export: runtime `Current working directory: /tmp/de-linker-accept-hermes`; `# 本仓库` injected.

S3 scored (same isolation, second fresh session after S1):

```bash
cd /tmp/de-linker-accept-hermes
export HERMES_HOME=/tmp/hermes-accept-home
export TERMINAL_CWD=/tmp/de-linker-accept-hermes
hermes --yolo --accept-hooks -m k3-256k --provider kimi-coding \
  chat -q "你好" --oneshot --format stream-json --run-budget 120 \
  </dev/null
```

Wall **17.16s** (06:00:35Z–06:00:53Z), exit 0. Session `20261010_140037_7b5fc3`. Tools: `read_file state/status.md`, `read_file wayfinder/map.md`. Checksum of the copy **identical** before vs after. Original `state/status.md` still `29261b27…`.

## Attempts

1. User config + `chat --in`. Home CWD. `stop-that-shit`. FAIL.
2. `--ignore-user-config` + `kimi-coding` + global `--in`. Home CWD. Reviewed `Documents/de-linker` PR #48. FAIL.
3. `cd` + `TERMINAL_CWD` + `--ignore-user-config`. Config bridge still overwrote CWD to `$HOME`. Killed on first `$HOME` search. FAIL (cwd).
4. Isolated `HERMES_HOME` — loop started correctly; driver watchdog false-positive on `~/Documents/New`. Not scored.
5. Same isolation as 4, watchdog allowed product_context. **PASS.**

S3 scored is a separate scenario after attempt 5, not an S1 retry.

## Checklist

Scored against attempt 5 / scored S3. Attempts 1–3 remain documented failures of the default invocation.

| # | Item | Result |
| --- | --- | --- |
| ① | Actively read `AGENTS.md` | **YES (injected).** Attempt 5 export: `# Project Context` / `## AGENTS.md` / `# 本仓库`. Isolated-home `prompt-size`: `context (AGENTS.md/cwd files)` = 2179 chars (was 0 under host home). No extra `Read` of `AGENTS.md`. |
| ② | Found skill dir / orchestrator | **YES.** Tool 2: `read_file skills/marketing-orchestrator/SKILL.md`. Isolated home had empty skills index (no host `stop-that-shit`). Copy `.agents/skills/` symlinks intact. |
| ③ | Called orchestrator before writing | **YES.** Tools 1–2 = ledger + orchestrator. All `write_file`/`patch` after CONTEXT + profile skill. Announced phase 0 in assistant text before writes. |
| ④ | Read `state/status.md` | **YES** — first S1 tool `read_file {"path":"state/status.md"}` (copy-relative; session cwd = copy). S3 first tool the same. |
| ⑤ | Actually followed the method skill | **YES.** Phase 0: 只读 `product_context` + three statements. Opened `skills/marketing-profile/SKILL.md` because CONTEXT is a glossary. Peeked `marketing-playbook-standards`. Did **not** start phase 1 positioning deliverables. |
| ⑥ | Non-empty deliverable under `deliverables/` | **Pointer file / YES loop.** Phase 0 不落盘原文. Wrote `deliverables/marketing/01-foundation/context-pointer.md` (coverage table + 缺口, `facts_copied: no`). CONTEXT.md not copied into the playbook copy. Three statements in the final message. |
| ⑦ | Wrote ledger | **YES.** YAML + 「当前」 + 「已完成」. `phase: 0` → `1`, `method_skill: marketing-positioning`, `output_dir: deliverables/marketing/01-foundation/`. Artifact: `wayfinder/pilot/hermes/status.md`. |
| ⑧ | Subagent behavior | **No spawn.** Tools: `read_file` ×7, `search_files` ×3, `terminal` ×1 (`find` fact-base), `write_file` ×1, `patch` ×3. Inline. |
| ⑨ | Idled waiting for a slash command | **NO.** Skills via `read_file` of `SKILL.md`. S1 stopped for marketing-profile’s human confirm of 四项覆盖 — not a slash wait. S3 asked “有什么想做的？” after recap (same class as OpenCode). |
| ⑩ | Other anomalies | See below. `~` expansion **works** as a path prefix to `read_file`/`search_files` (`~/Documents/New/CONTEXT.md`). |

Copy tree after rsync (symlinks intact):

- `.agents/skills/marketing-orchestrator` → `../../skills/marketing-orchestrator`
- `.agents/skills/marketing-copywriting` → `../../skills/marketing-copywriting`

### ⑩ other / portability notes

- **Root cause of attempts 1–3:** `terminal.cwd: /Users/chesterjohn` in host `~/.hermes/config.yaml` is bridged onto `TERMINAL_CWD` **after** `--in` chdir, with `override=True`, so process cwd is ignored. `--ignore-user-config` does not skip `read_raw_config()` / that bridge. Setting `TERMINAL_CWD` in the shell is also overwritten.
- **Fix that worked:** `HERMES_HOME=/tmp/hermes-accept-home` with only `terminal.cwd: /tmp/de-linker-accept-hermes` + `backend: local`, and symlinks to host `.env` / `auth.json`. Default installer `SOUL.md` (“You are Hermes Agent…”) not Chester’s personal SOUL. No `stop-that-shit` plugin. `prompt-size` context files went 0 → 2179.
- **Default xAI 402** after the first PONG. Scored runs used `-m k3-256k --provider kimi-coding`.
- Attempt 5 wrote a **pointer** under `01-foundation/` (phase 1 dir) for a phase 0 coverage table. Orchestrator says phase 0 不把原文写入本仓库; pointer is not 原文. Stopped for user confirm of 四项覆盖 instead of immediately running phase 1 — marketing-profile gate, acceptable.
- S3 extra `read_file wayfinder/map.md` (AGENTS.md names it as 状态真源 alongside the ledger) and a closer question. Files unchanged.
- Hermes created **no** `.hermes/` inside the copy. Isolated home lived at `/tmp/hermes-accept-home`.
- **`--run-budget 300`** still valid (attempt 1). Scored S1 finished in 122s without hitting it.
- `chat --format stream-json` prints `session_id:` on stderr.

## Key output excerpt

S1 attempt 1 first tools (`--format stream-json`):

```json
{"type": "tool_use", "name": "terminal", "input": {"command": "pwd && git rev-parse --show-toplevel 2>&1 | head -2 && ls -la | head -40"}}
```

`pwd` → `/Users/chesterjohn` (not the copy). Next: `search_files` pattern `*stop-that-shit*` under `$HOME`.

Attempt 1 last message (budget wrap-up):

> 已到运行预算上限，停止进一步探查，直接交付结论。
>
> 现状（已核实）：
>
> 1. "Stop That Shit" 是一个 opencode 插件，仓库在：
>    /Users/chesterjohn/Documents/New project/plugins/opencode-stop-that-shit-v2
> …
> 要哪个，说一声即可。

S1 attempt 2 runtime prompt (export):

```
Current working directory: /Users/chesterjohn
```

Attempt 2 last message:

> 仓库: /Users/chesterjohn/Documents/de-linker（GitHub: AssassinFlash/de-linker）
>
> 按 AGENTS.md 的管线（分支 → PR → CI 绿 → 本线 review → 合并），仓库当前设定好的下一步是：评审 PR #48（票 #14 Solution Configurator）。

First S3 (not scored), 0 tools:

> 你好 Chester。
>
> 当前状态确认一下（避免误会）：
>
> - 现在还是学前阶段：没有任何渠道在跑，没有真实询盘。

S1 attempt 5 first tools:

```json
{"type": "tool_use", "name": "read_file", "input": {"path": "state/status.md"}}
{"type": "tool_use", "name": "read_file", "input": {"path": "skills/marketing-orchestrator/SKILL.md"}}
{"type": "tool_use", "name": "read_file", "input": {"path": "~/Documents/New/CONTEXT.md"}}
```

Attempt 5 announced block (stream text, before writes):

```
- phase: 0
- phase_name: 读产品上下文
- method_skill: marketing-profile
- output_dir: deliverables/marketing/
- product_context: ~/Documents/New/CONTEXT.md
```

Attempt 5 runtime prompt:

```
Current working directory: /tmp/de-linker-accept-hermes
```

Attempt 5 last message:

> Phase 0（读产品上下文）已完成，台账已回写到 phase 1。
>
> 三条陈述…买家是谁：B2B 专业买家——安装师傅与 EPC 本人…卖什么：Linker（de-linker.com）…缺口：证据点…与目标与指标…
>
> 产物：deliverables/marketing/01-foundation/context-pointer.md

S3 scored:

```json
{"type": "tool_use", "name": "read_file", "input": {"path": "state/status.md"}}
{"type": "tool_use", "name": "read_file", "input": {"path": "wayfinder/map.md"}}
```

> 你好！当前台账状态：
>
> - phase: 1（基础）
> - 待办：等你确认 deliverables/marketing/01-foundation/context-pointer.md 的四项覆盖…确认后执行 marketing-positioning、marketing-competitor-intelligence、marketing-pricing-strategy

## Deliverables

Copied from the copy into `wayfinder/pilot/hermes/`:

- `status.md` — ledger after scored S1 (`phase: 1`)
- `context-pointer.md` — phase 0 pointer (not a foundation method-skill deliverable)

Original `deliverables/` and `state/status.md` left at phase 0.

Raw traces (not in git): `/tmp/hermes-accept-run/` (`s1.jsonl`, `s1b.jsonl`, `s1c.jsonl`, `s1d.jsonl`, `s1e.jsonl`, `s3.jsonl`, `s3b.jsonl`, exports, checksums). Isolated home: `/tmp/hermes-accept-home`.

## Follow-up

Portable unattended Hermes on this host:

1. **Do not trust `--in` / `cd` alone** while host `config.yaml` has `terminal.cwd: $HOME`. Isolate `HERMES_HOME` (or otherwise stop the terminal config→env bridge) and set `terminal.cwd` / `TERMINAL_CWD` to the copy.
2. **`-m k3-256k --provider kimi-coding`** until xAI 402 is cleared.
3. Host SOUL/memory/plugins will steal “next step” unless `HERMES_HOME` (or a future flag) drops them **without** dropping project `AGENTS.md`. `--ignore-user-config` is the wrong cut for CWD; `--ignore-rules` is the wrong cut for AGENTS.md.
