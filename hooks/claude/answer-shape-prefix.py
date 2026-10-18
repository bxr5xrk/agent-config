#!/usr/bin/env python3
"""UserPromptSubmit hook: a prompt prefix sets the answer shape before the answer is written."""
import json
import re
import sys

PREFIX = re.compile(r"^\s*(так/ні|рішення|аудит)\s*:", re.IGNORECASE)

SHAPES = {
    "так/ні": "Питання так/ні. Перший рядок — вердикт як факт. Далі максимум 2 рядки, тільки те, що змінює мій наступний крок. Без заголовків, жирних розділів, file:line, переліку перевірок.",
    "рішення": "Питання про рішення. Перший рядок — рішення. Далі максимум 3 рядки: блокер або ризик, якщо є. Без заголовків, жирних розділів, file:line, переліку перевірок.",
    "аудит": "Повний аудит: усі знахідки, з file:line.",
}


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0
    match = PREFIX.match(payload.get("prompt") or "")
    if not match:
        return 0
    context = SHAPES[match.group(1).lower()]
    sys.stdout.write(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": context}}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
