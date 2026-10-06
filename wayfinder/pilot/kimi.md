# Pilot run: kimi

- **harness:** Kimi Code CLI (`kimi`)
- **version:** 2.1.1
- **binary:** `/Users/chesterjohn/.local/bin/kimi` → `kimi-xai` wrapper → `/Users/chesterjohn/.kimi-code/bin/kimi`
- **model:** `kimi-code/k3` (config `default_model`; session `thinkingEffort: high`)
- **date:** 2026-10-06 13:18–13:20 CST
- **driver:** subagent, harness = kimi
- **copy:** `/tmp/de-linker-pilot-kimi/` (rsync `-a --exclude .git` from `/Users/chesterjohn/Documents/de-linker-playbook/`; symlinks preserved). Session cwd resolved to `/private/tmp/de-linker-pilot-kimi`.
- **original repo:** mutated only under `wayfinder/pilot/` (this log + copied artifacts)
- **git:** not run
- **session:** `session_74d42ead-f8aa-45d8-9d5e-e4c88bbb16ca` (new; no `-c`/`-S`)

## Verdict

**PASS** — one cold start, no extra explanation, completed the thin-slice loop: found orchestrator → read ledger → phase 0 (read `product_context`, three statements, ledger → phase 1) → actually read `marketing-copywriting/SKILL.md` → wrote `deliverables/value-proposition.md` → ledger → phase 2 / `next: stop`. Auth worked. No second attempt.

Orchestrator text says do phases until the deliverable lands, so running 0 then 1 in one shot is in-spec (not a “big task”). No network tools.

## Headless / permission flags (portability)

From `kimi --help` (2.1.1) plus a nested `kimi -p --help` that itself started print-mode (treat `--help` as the prompt — do not do that):

| Need | Flag |
| --- | --- |
| Non-interactive / print | `-p` / `--prompt <prompt>` — “Run one prompt non-interactively and print the response.” |
| Trace tool use | `--output-format stream-json` (choices: `text`, `stream-json`; only with `-p`) |
| Ask-when-needed | `-y` / `--yolo` |
| Never ask | `--auto` |
| Resume | `-S` / `--session [id]`, `-c` / `--continue`. Print-mode footer also prints undocumented `kimi -r session_<uuid>` |
| Skills override | `--skills-dir <dir>` (repeatable; *replaces* auto-discovered dirs) |
| Extra workspace | `--add-dir <dir>` |

**Do not combine `-p` with `--yolo` / `--auto` / `--plan`.** Print mode already runs under auto permissions. Observed `permission.set_mode`: `yolo` (from `~/.kimi-code/config.toml` `default_permission_mode = "yolo"`) then `auto` (print-mode override). Writes in the copy needed no extra flag.

Auth probe (before the work run; not counted as an attempt):

```bash
cd /tmp && kimi -p "Reply with only the word PONG." --output-format text
```

Returned `PONG`, exit 0, `kimi doctor` OK.

Work command actually run:

```bash
cd /tmp/de-linker-pilot-kimi
kimi -p "Do the next step this repo is set up to do. Do not ask me to explain the repo." \
  --output-format stream-json
```

Wall ~95s (05:18:56Z–05:20:31Z), exit 0.

## Attempts

1. Work prompt above. Completed. Did not start a large/network task; no kill.
2. Not used.

## Checklist

| # | Item | Result |
| --- | --- | --- |
| ① | Actively read `AGENTS.md` | **YES (injected, not Read)** — harness stuffed both `~/.kimi-code/AGENTS.md` and `/private/tmp/de-linker-pilot-kimi/AGENTS.md` into the system prompt (`agentsMdPaths`). Agent never `Read` the file; first think cites “The repo AGENTS.md says: read state/status.md first…”. |
| ② | Found skill dir / orchestrator | **YES** — Project skills listed via `.agents/skills/` symlink paths. First batch called `Skill(marketing-orchestrator)`. User-scope `linker-copywriting` was also listed; not used. |
| ③ | Called orchestrator before writing | **YES** — first tools: `Read(state/status.md)` + `Skill(marketing-orchestrator)` in parallel. All `Edit`/`Write` came after. Used the `Skill` tool (inline load) rather than `Read` of `skills/marketing-orchestrator/SKILL.md`. |
| ④ | Read `state/status.md` | **YES** — first `Read`. |
| ⑤ | Actually read `marketing-copywriting/SKILL.md` (did not invent a flow) | **YES** — `Read(skills/marketing-copywriting/SKILL.md)` after phase-0 ledger write, before drafting. Followed that template. |
| ⑥ | Non-empty deliverable under `deliverables/`; not skill-example paste; no invented product numbers | **YES** — `/tmp/de-linker-pilot-kimi/deliverables/value-proposition.md` (584 bytes). Forbidden example sentences absent. “224 SKU” only in the ledger (from CONTEXT.md), not invented into the draft. Draft uses “要规格、要方案”, no trial/signup. |
| ⑦ | Wrote ledger (phase / next / 已完成) | **YES** — YAML + 「当前」 table + 「已完成」. phase 0→1 (with three statements) then 1→2, `next: stop`. Copy of ledger: `wayfinder/pilot/kimi/status.md`. |
| ⑧ | Subagent behavior (harness-specific tool names) | **No spawn.** Tools used: `Skill`, `Read`, `Edit`, `Write`. `Agent` / `AgentSwarm` available (`subagents: coder, explore, plan`) but unused — inline, matching orchestrator “else do it inline”. |
| ⑨ | Idled waiting for a slash command | **NO** — never asked for `/…`. Skills via `Skill` tool + listing, not slash. |
| ⑩ | Other anomalies | See below. |

### ⑩ Other / portability notes

- **`~` expansion: correct.** `product_context: ~/Documents/New/CONTEXT.md` was opened as `/Users/chesterjohn/Documents/New/CONTEXT.md`. Did not treat `~` as a relative path.
- **Print-mode permission:** `yolo` then `auto`; `-p` is enough to write.
- **PATH `kimi` is not the stock binary** — it is `kimi-xai` (injects xAI OAuth `NODE_OPTIONS` require, then spawns `~/.kimi-code/bin/kimi`). Version still 2.1.1.
- **Skill discovery:** `.agents/skills/*` symlinks showed up as **Project** skills. Canonical `skills/` was also in the cwd listing.
- **word_count mismatch:** draft claims `word_count: 85`; non-whitespace length of the 草稿 body is 107 (skill cap is 混排 ≤100 字). Quality nit; not a loop miss. No skill-example paste.
- **Did not announce phase to the user before acting** (orchestrator checklist “当众宣布”); print-mode went straight to tools, then announced after phase 0 in an assistant content part.
- **CONTEXT.md is a glossary**, not a product one-pager. Agent stated that as the gap (no specs/prices/certs) and did not copy the glossary into the playbook copy.
- **No web / Apify / Firecrawl** despite global `~/.kimi-code/AGENTS.md` pushing Apify for research.

Copy tree after rsync (symlinks intact):

- `.agents/skills/marketing-orchestrator` → `../../skills/marketing-orchestrator`
- `.agents/skills/marketing-copywriting` → `../../skills/marketing-copywriting`

## Key output excerpt

First tool batch (stream-json):

```json
{"role":"assistant","tool_calls":[
  {"function":{"name":"Read","arguments":"{\"path\":\"state/status.md\"}"}},
  {"function":{"name":"Skill","arguments":"{\"skill\":\"marketing-orchestrator\",\"args\":\"next step\"}"}}
]}
```

`~` expansion:

```json
{"function":{"name":"Read","arguments":"{\"path\":\"/Users/chesterjohn/Documents/New/CONTEXT.md\"}"}}
```

Final assistant (truncated):

> 试点全部跑完，台账停在 **phase 2（试点完成，`next: stop`）**。
> **产物** `deliverables/value-proposition.md`
> Phase 2 的规则是「报告产物路径后停止，不发明下一阶段」，所以到这里停。

Tool sequence (11 calls, 0 web, 0 Agent):  
`Read(status)` → `Skill(orchestrator)` → `Read(CONTEXT.md)` → 3× `Edit(status)` (phase 1) → `Read(marketing-copywriting/SKILL.md)` → `Write(value-proposition.md)` → 3× `Edit(status)` (phase 2 / stop).

## Deliverables

Copied from the copy repo:

- `wayfinder/pilot/kimi/value-proposition.md` — phase 1 draft
- `wayfinder/pilot/kimi/status.md` — ledger after phase 2 (evidence of ⑦; not a playbook deliverable)

Original `deliverables/` and `state/status.md` left at phase 0.

## Follow-up

None required for this harness. Optional: tighten copywriting skill word-count check if the matrix starts scoring draft quality, not just the loop.
