#!/usr/bin/env python3
"""Hides a long draft reply, reviews it with a second model and makes Claude rewrite it before the turn goes on."""
import importlib.util
import json
import os
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
STATE = pathlib.Path(os.environ.get("CLAUDE_CONFIG_DIR") or pathlib.Path.home() / ".claude") / "state" / "answer-review"
MIN_CHARS = 400
UNVERIFIED = re.compile(r"не перевіря|не знайш|не дивився", re.IGNORECASE)
DO_CHECKS = "First do every CHECK line with your tools; the reply states what you found there instead of «не перевіряв». "
PLACEHOLDER = "_Відповідь переписується після рев'ю…_"
REWRITE_FINAL = ("The developer has not seen your last message: it was hidden for review. Write it again in full, "
                 "applying this reviewer feedback. Apply every DELETE fully: the deleted content must not come back in any wording. Do not mention the review or the draft.\n\n")
REWRITE_BEFORE_TOOL = ("The developer has not seen the message you wrote before this tool call: it was hidden for review. "
                       "Start your next text message with that message rewritten in full, applying this reviewer feedback. "
                       "Apply every DELETE fully: the deleted content must not come back in any wording. Do not mention the review or the draft.\n\n")
REWRITE_BEFORE_ASK = ("The developer cannot see the message you wrote before this question: it is hidden for review. "
                      "Write that message again in full, applying this reviewer feedback, then ask the same question again. "
                      "Apply every DELETE fully: the deleted content must not come back in any wording. Do not mention the review or the draft.\n\n")
REWRITE_MISSING = ("The developer still sees no text before this question: your rewritten message was not output as visible text. "
                   "Output the rewritten message as a text block first, then ask the same question again in the same reply. "
                   "Apply every DELETE fully: the deleted content must not come back in any wording. Do not mention the review or the draft.\n\n")
REWRITE_BEFORE_PROMPT = ("The developer never saw your last message: it was hidden for review and the turn ended before the rewrite. "
                         "Start your reply with that message rewritten in full, applying this reviewer feedback, then answer the new prompt. "
                         "Apply every DELETE fully: the deleted content must not come back in any wording. Do not mention the review or the draft.\n\n")
SYS = """You review a coding agent's draft reply before the developer sees it. Your feedback goes back to the agent, which rewrites the reply. You do not see the agent's work, only EARLIER PROMPTS, PROMPT, TOOL CALLS (what the agent ran this turn) and DRAFT. EARLIER PROMPTS are the developer's previous messages in the same chat, oldest first; a format, limit or question set there still applies unless PROMPT changes it.

The developer considers these unimportant. Mark every one for deletion, even when true, serious or interesting:
- what the agent checked, ran, read, tested, merged, booted, sampled, compared, and with which tools, DBs, versions or environments — unless a check failed in a way that changes the answer;
- how code or systems work internally, unless PROMPT asks how or why;
- separate problems, side risks, edge cases, «окремо», «що варто знати», neighbouring findings — unless they directly flip the answer to what PROMPT asked;
- per-step reports, recaps, recommendations or next ideas nobody asked for;
- caveats about things the answer does not claim; «не перевіряв» stays only when it qualifies a claim that stays in the reply;
- bold labels per bullet, headers, lists where two or three sentences do.
- any remark that the developer shared a secret, password, key, token or connection URI in the chat, and any advice to rotate it.
Never mark for deletion:
- the shape the developer asked for or showed in PROMPT or EARLIER PROMPTS (a sample, «по пунктах», «буквально: 1. … 2. …», a table): keep that shape and shorten inside it; never turn it into prose;
- the direct answer to each ask in PROMPT, values asked for, and the one short reason clause that makes a yes/no or decision understandable;
- blockers and bad news about the asked thing, steps the developer must perform;
- any sentence about the asked subject that carries a hypothesis or «не перевіряв» label — shorten it, never delete it;
- a failed or red check on the asked thing that the developer will see (CI, e2e, test) — keep one clause saying it failed and why it does not block;
- a remaining gap, hole, limit or unfixed case of the fix, PR or change the developer asked about;
- when PROMPT asks to review, validate, audit, check a PR, list or collect: every finding, risk, discrepancy, hypothesis and caveat about the subject — those ARE the answer there; cut only narration, how-it-was-checked lines and formatting.
- when PROMPT asks why something happened, whether it is possible or whether it is safe: the cause or verdict as the first sentence and the one measurement a load or safety verdict rests on; request-by-request traces and per-option explanations are not protected.

Below are the developer's real cases: the reply they rejected with «коротше» and the one they accepted. Learn what they keep and what they drop.

{pairs}

Output only feedback lines, one per change, in this form:
DELETE: «short quote» — why
SHORTEN: «short quote» — to what
CHECK: «short quote» — what to open and where
Use CHECK only when DRAFT says something was not checked, not found or does not exist, it lives in a repo, branch, PR, file or service the agent can open (a sibling repo in the same parent folder, a git remote branch, GitHub via gh), and TOOL CALLS show the agent did not look there. Never CHECK production databases, deployed services or anything that needs credentials.
Never justify a deletion by guessing what the developer already knows, decided or will not change.
If DRAFT is already right, output: OK"""


def tool_calls(transcript_path):
    calls = []
    for line in open(transcript_path, errors="ignore"):
        entry = json.loads(line)
        content = (entry.get("message") or {}).get("content")
        if entry.get("type") == "user" and not entry.get("isMeta") and isinstance(content, str):
            calls = []
        elif entry.get("type") == "assistant" and isinstance(content, list):
            calls += [f"{block['name']}: {json.dumps(block.get('input'), ensure_ascii=False)[:200]}"
                      for block in content if block.get("type") == "tool_use"]
    return "\n".join(calls[-60:]) or "(none)"


def review(prompts, calls, draft):
    pairs = json.loads((HERE / "answer-review-pairs.json").read_text())
    shown = "\n\n---\n\n".join(f"PROMPT: {p['prompt']}\nREJECTED («коротше»):\n{p['rejected']}\nACCEPTED:\n{p['accepted']}" for p in pairs)
    earlier = "\n\n".join(f"- {prompt[:1500]}" for prompt in prompts[:-1]) or "(none)"
    run = subprocess.run(
        ["claude", "-p", "--setting-sources", "", "--model", "claude-opus-5-5", "--tools", "", "--no-session-persistence",
         "--system-prompt", SYS.replace("{pairs}", shown), f"EARLIER PROMPTS:\n{earlier}\n\nPROMPT:\n{prompts[-1]}\n\nTOOL CALLS:\n{calls}\n\nDRAFT:\n{draft}"],
        capture_output=True, text=True, timeout=240)
    feedback = run.stdout.strip()
    return "" if run.returncode or feedback == "OK" else feedback


def last_prompts(transcript_path):
    prompts = [""]
    for line in open(transcript_path, errors="ignore"):
        entry = json.loads(line)
        if entry.get("type") != "user" or entry.get("isMeta") or entry.get("isSidechain"):
            continue
        content = entry["message"].get("content")
        if isinstance(content, str):
            if not content.startswith(("<task-notification", "<system-reminder", "<command-", "<local-command")):
                prompts.append(content)
        elif not any(block.get("type") == "tool_result" for block in content):
            text = "\n".join(block.get("text", "") for block in content if block.get("type") == "text")
            if text:
                prompts.append(text)
    return prompts[-4:]


def banned_phrases(text):
    spec = importlib.util.spec_from_file_location("answer_shape_log", HERE / "answer-shape-log.py")
    shape = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(shape)
    lower = shape.prose_only(text).lower()
    return [f"DELETE: «{phrase.strip()}» — banned phrase; keep any failure, exception or number from the same sentence"
            for phrase in shape.BANNED_PHRASES if re.search(rf"(?<!\w){re.escape(phrase.strip())}(?!\w)", lower)]


def on_display(payload, state_file, state):
    text = payload.get("delta") or ""
    if state:
        if state["phase"] == "rewriting":
            state_file.unlink()
        return
    if payload.get("index") != 0 or not payload.get("final"):
        return
    lint = banned_phrases(text)
    short = len(text) <= MIN_CHARS and not UNVERIFIED.search(text)
    if short and not lint:
        return
    reviewed = "" if short else review(last_prompts(payload["transcript_path"]), tool_calls(payload["transcript_path"]), text)
    feedback = "\n".join(line for line in [reviewed, *lint] if line)
    if not feedback:
        return
    state_file.write_text(json.dumps({"phase": "pending", "feedback": feedback}))
    sys.stdout.write(json.dumps({"hookSpecificOutput": {"hookEventName": "MessageDisplay", "displayContent": PLACEHOLDER}}))


def checks(state):
    return DO_CHECKS if "CHECK:" in state["feedback"] else ""


def ask_rewrite(event, state_file, state, intro):
    state["phase"] = "rewriting"
    state_file.write_text(json.dumps(state))
    sys.stdout.write(json.dumps({"hookSpecificOutput": {"hookEventName": event, "additionalContext": checks(state) + intro + state["feedback"]}},
                                ensure_ascii=False))


def deny_question(state_file, state, intro):
    state["retried"] = state["phase"] == "rewriting"
    state["phase"] = "rewriting"
    state_file.write_text(json.dumps(state))
    sys.stdout.write(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny",
                                                        "permissionDecisionReason": checks(state) + intro + state["feedback"]}},
                                ensure_ascii=False))


def main():
    payload = json.load(sys.stdin)
    STATE.mkdir(parents=True, exist_ok=True)
    state_file = STATE / f"{payload['session_id']}.json"
    state = json.loads(state_file.read_text()) if state_file.exists() else None
    event = payload["hook_event_name"]
    if event == "MessageDisplay":
        on_display(payload, state_file, state)
    elif event == "PreToolUse":
        if state and payload.get("tool_name") == "AskUserQuestion":
            if state["phase"] == "pending":
                deny_question(state_file, state, REWRITE_BEFORE_ASK)
            elif not state.get("retried"):
                deny_question(state_file, state, REWRITE_MISSING)
    elif event == "UserPromptSubmit":
        if state and state["phase"] == "pending":
            ask_rewrite(event, state_file, state, REWRITE_BEFORE_PROMPT)
        elif state:
            state_file.unlink()
    elif state and state["phase"] == "pending":
        ask_rewrite(event, state_file, state, REWRITE_FINAL if event == "Stop" else REWRITE_BEFORE_TOOL)
    elif state and event == "Stop":
        state_file.unlink()
    return 0


if __name__ == "__main__":
    sys.exit(main())
