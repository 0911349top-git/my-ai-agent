from getpass import getpass
from gigachat import GigaChat

key = getpass("Введите ключ: ")

# Формируем промпт с контекстом и ограничением
prompt = """
Контекст: студент изучает Python третий день.
Он уже знает: print(), input(), переменные и if.

Задача: объясни, что такое списки в Python.

Ограничения:
- Не используй в объяснении функции.
- Не используй классы.
- Не показывай код с функциями или классами.
- Пиши простыми словами, как для новичка.
- Приведи 2–3 коротких примера только с переменными и списками.
"""

with GigaChat(credentials=key, verify_ssl_certs=False, model="GigaChat-2") as client:
    response = client.chat.create(prompt)
    print("=== ОТВЕТ МОДЕЛИ ===")
    print(response.messages[0].content[0].text.strip())