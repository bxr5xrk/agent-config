#!/usr/bin/env python3
"""UserPromptSubmit hook: a prompt prefix sets the answer shape before the answer is written."""
import json
import re
import sys

SECRETS = "Never remark that I shared a secret, key, password, token or URI in the chat, never advise rotating it."

EXPLAIN = (
    "Текст для тестувальника чи продакту: що було не так → як було → як зараз, звичайними словами, без назв функцій, полів, подій і file:line. "
    "Неоднозначний термін — уточни систему: наша БД чи Google. "
    "Питаю статус довгої задачі — один рядок: відсоток, помилки чи переривання, ETA за Варшавою від поточного часу (прогрес стоїть — так і скажи); якщо раніше вже називав ETA і вона змінилась — скажи це. "
    "Команда для БД, яку я запускаю сам, — синтаксис Compass `db[\"coll\"].…` одним рядком. "
    "Потреби фронту не входять у блокери чи готовність бекенду."
)

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
    context = SECRETS + " " + EXPLAIN + (" " + SHAPES[match.group(1).lower()] if match else "")
    sys.stdout.write(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": context}}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
