#!/usr/bin/env python3
"""Stop hook: log answer-shape violations. Never blocks — a block cannot retract
the message already on screen, it only appends a second copy."""
import datetime
import json
import os
import re
import sys

BANNED_PHRASES = [
    "let me ", "great question", "чудове питання", "ти маєш рацію",
    "зараз перевірю", "зараз подивлюсь", "швидко гляну", "спершу гляну",
    "ось що я знайшов", "тести проходять", "лінт чистий", "tests pass",
    "перевірив живим", "підтвердив живим", "не здогад", "перевірено живим",
    "звідки взяв", "джерела:", "evidence:", "relevant paths",
    "не перевіряв рендер", "не клікав", "не відкривав лінк",
]

LABEL_BEFORE_URL = re.compile(
    r"^\s*(ось\s+лінк|лінк|посилання|прямий\s+лінк|пряме\s+посилання)\b[^\n]{0,80}:\s*$",
    re.IGNORECASE | re.MULTILINE,
)

PROVENANCE = re.compile(
    r"(\.ci/|\.github/|\.helm/|\.env[\w.]*)[^\s`]*:\d+|\b\w+\.(ya?ml|sh|json):\d+",
    re.IGNORECASE,
)

CLOSING_OFFER = re.compile(
    r"(хочеш|можу|готовий|скажи, якщо|дай знати|want me to|should i|let me know)"
    r"\b[^\n]*\?\s*$",
    re.IGNORECASE,
)

HYPOTHESIS_MARKERS = ("гіпотеза", "припущен", "hypothes", "не перевірен", "не перевіряв")
HEDGE = re.compile(
    r"\b(схоже, що|напевно|мабуть|ймовірно|мало би|likely|probably)\b", re.IGNORECASE
)

SHORT_PREFIX = re.compile(r"^\s*(так/ні|рішення)\s*:", re.IGNORECASE)
SHORTER = re.compile(r"^\s*коротше\b", re.IGNORECASE)
SECTION = re.compile(r"^\s*(#{1,6}\s|\*\*[^*\n]+\*\*\s*$)", re.MULTILINE)
SHORT_MAX_CHARS = 400

QUOTED = re.compile(r"`[^`]*`|«[^»]*»|\"[^\"]*\"|“[^”]*”")


def prose_only(text):
    out, in_fence = [], False
    for line in text.split("\n"):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence:
            out.append(QUOTED.sub(" ", line))
    return "\n".join(out)


def last_assistant_text(path):
    text = None
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue
            if entry.get("type") != "assistant":
                continue
            content = (entry.get("message") or {}).get("content")
            if not isinstance(content, list):
                continue
            chunks = [c.get("text", "") for c in content if c.get("type") == "text"]
            joined = "\n".join(x for x in chunks if x.strip())
            if joined.strip():
                text = joined
    return text


def last_user_prompt(path):
    prompt = None
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue
            if entry.get("type") != "user" or entry.get("isMeta"):
                continue
            content = (entry.get("message") or {}).get("content")
            if isinstance(content, str):
                prompt = content
            elif isinstance(content, list):
                chunks = [c.get("text", "") for c in content if c.get("type") == "text"]
                if chunks:
                    prompt = "\n".join(chunks)
    return prompt


def check_shape(prompt, text):
    out = []
    if SHORTER.match(prompt):
        out.append("скарга «коротше» на попередню відповідь")
    if SHORT_PREFIX.match(prompt) and (len(text) > SHORT_MAX_CHARS or SECTION.search(text)):
        out.append(f"довга відповідь на так/ні чи рішення: {len(text)} символів")
    return out


def check(text):
    prose = prose_only(text)
    lower = prose.lower()
    out = []

    hits = [p.strip() for p in BANNED_PHRASES if p in lower]
    if hits:
        out.append("заборонені фрази: " + ", ".join(hits))
    if LABEL_BEFORE_URL.search(prose):
        out.append("лейбл-рядок перед лінком")
    if PROVENANCE.search(prose):
        out.append("атрибуція джерел")
    if CLOSING_OFFER.search(prose.rstrip()):
        out.append("фінальна пропозиція прозою замість AskUserQuestion")
    if HEDGE.search(prose) and not any(m in lower for m in HYPOTHESIS_MARKERS):
        out.append("здогад без мітки гіпотези")
    return out


LOG = os.path.expanduser("~/.claude/answer-shape.log")


def log(msg):
    try:
        stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(LOG, "a", encoding="utf-8") as fh:
            fh.write(f"{stamp} {msg}\n")
    except OSError:
        pass


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0
    if payload.get("stop_hook_active"):
        return 0
    path = payload.get("transcript_path")
    if not path:
        return 0
    try:
        text = last_assistant_text(path)
    except OSError:
        return 0
    if not text:
        return 0
    violations = check(text)
    prompt = last_user_prompt(path)
    if prompt:
        violations += check_shape(prompt, text)
    log("passed" if not violations else "violations: " + "; ".join(violations))
    return 0


if __name__ == "__main__":
    sys.exit(main())
