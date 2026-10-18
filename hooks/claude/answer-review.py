#!/usr/bin/env python3
"""Hides a long draft reply, reviews it with a second model and makes Claude rewrite it before the turn goes on."""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
STATE = pathlib.Path.home() / ".claude" / "state" / "answer-review"
MIN_CHARS = 400
PLACEHOLDER = "_Відповідь переписується після рев'ю…_"
REWRITE_FINAL = ("The developer has not seen your last message: it was hidden for review. Write it again in full, "
                 "applying this reviewer feedback. Apply every DELETE fully: the deleted content must not come back in any wording. Do not mention the review or the draft.\n\n")
REWRITE_BEFORE_TOOL = ("The developer has not seen the message you wrote before this tool call: it was hidden for review. "
                       "Start your next text message with that message rewritten in full, applying this reviewer feedback. "
                       "Apply every DELETE fully: the deleted content must not come back in any wording. Do not mention the review or the draft.\n\n")
SYS = """You review a coding agent's draft reply before the developer sees it. Your feedback goes back to the agent, which rewrites the reply. You do not see the agent's work, only PROMPT and DRAFT.

The developer considers these unimportant. Mark every one for deletion, even when true, serious or interesting:
- what the agent checked, ran, read, tested, merged, booted, sampled, compared, and with which tools, DBs, versions or environments — unless a check failed in a way that changes the answer;
- how code or systems work internally, unless PROMPT asks how or why;
- separate problems, side risks, edge cases, «окремо», «що варто знати», neighbouring findings — unless they directly flip the answer to what PROMPT asked;
- per-step reports, recaps, recommendations or next ideas nobody asked for;
- caveats about things the answer does not claim; «не перевіряв» stays only when it qualifies a claim that stays in the reply;
- bold labels per bullet, headers, lists where two or three sentences do.
- any remark that the developer shared a secret, password, key, token or connection URI in the chat, and any advice to rotate it.
Never mark for deletion:
- the direct answer to each ask in PROMPT, values asked for, and the one short reason clause that makes a yes/no or decision understandable;
- blockers and bad news about the asked thing, steps the developer must perform;
- any sentence about the asked subject that carries a hypothesis or «не перевіряв» label — shorten it, never delete it;
- a failed or red check on the asked thing that the developer will see (CI, e2e, test) — keep one clause saying it failed and why it does not block;
- a remaining gap, hole, limit or unfixed case of the fix, PR or change the developer asked about;
- when PROMPT asks to review, validate, audit, check a PR, list, collect, analyze, assess feasibility, explain or find a root cause: every finding, risk, discrepancy, hypothesis and caveat about the subject — those ARE the answer there; cut only narration, how-it-was-checked lines and formatting.

Below are the developer's real cases: the reply they rejected with «коротше» and the one they accepted. Learn what they keep and what they drop.

{pairs}

Output only feedback lines, one per change, in this form:
DELETE: «short quote» — why
SHORTEN: «short quote» — to what
Never justify a deletion by guessing what the developer already knows, decided or will not change.
If DRAFT is already right, output: OK"""


def review(prompt, draft):
    pairs = json.loads((HERE / "answer-review-pairs.json").read_text())
    shown = "\n\n---\n\n".join(f"PROMPT: {p['prompt']}\nREJECTED («коротше»):\n{p['rejected']}\nACCEPTED:\n{p['accepted']}" for p in pairs)
    run = subprocess.run(
        ["claude", "-p", "--setting-sources", "", "--model", "claude-opus-5-5", "--tools", "", "--no-session-persistence",
         "--system-prompt", SYS.replace("{pairs}", shown), f"PROMPT:\n{prompt}\n\nDRAFT:\n{draft}"],
        capture_output=True, text=True, timeout=240)
    feedback = run.stdout.strip()
    return "" if run.returncode or feedback == "OK" else feedback


def last_prompt(transcript_path):
    prompt = ""
    for line in open(transcript_path, errors="ignore"):
        entry = json.loads(line)
        if entry.get("type") != "user" or entry.get("isMeta") or entry.get("isSidechain"):
            continue
        content = entry["message"].get("content")
        if isinstance(content, str):
            prompt = content
        elif not any(block.get("type") == "tool_result" for block in content):
            prompt = "\n".join(block.get("text", "") for block in content if block.get("type") == "text") or prompt
    return prompt


def on_display(payload, state_file, state):
    text = payload.get("delta") or ""
    if state:
        if state["phase"] == "rewriting":
            state_file.unlink()
        return
    if payload.get("index") != 0 or not payload.get("final") or len(text) <= MIN_CHARS:
        return
    feedback = review(last_prompt(payload["transcript_path"]), text)
    if not feedback:
        return
    state_file.write_text(json.dumps({"phase": "pending", "feedback": feedback}))
    sys.stdout.write(json.dumps({"hookSpecificOutput": {"hookEventName": "MessageDisplay", "displayContent": PLACEHOLDER}}))


def ask_rewrite(event, state_file, state, intro):
    state["phase"] = "rewriting"
    state_file.write_text(json.dumps(state))
    sys.stdout.write(json.dumps({"hookSpecificOutput": {"hookEventName": event, "additionalContext": intro + state["feedback"]}},
                                ensure_ascii=False))


def main():
    payload = json.load(sys.stdin)
    STATE.mkdir(parents=True, exist_ok=True)
    state_file = STATE / f"{payload['session_id']}.json"
    state = json.loads(state_file.read_text()) if state_file.exists() else None
    event = payload["hook_event_name"]
    if event == "MessageDisplay":
        on_display(payload, state_file, state)
    elif state and state["phase"] == "pending":
        ask_rewrite(event, state_file, state, REWRITE_FINAL if event == "Stop" else REWRITE_BEFORE_TOOL)
    elif state and event == "Stop":
        state_file.unlink()
    return 0


if __name__ == "__main__":
    sys.exit(main())
