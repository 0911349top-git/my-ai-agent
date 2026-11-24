from getpass import getpass
from gigachat import GigaChat

key = getpass("Введите ключ: ")

# Формируем строгий промпт
prompt = """
Контекст: студент изучает Python третий день. 
Он знает print(), input(), переменные и if.

Задача: объясни, что такое списки в Python.

Ограничения:
- Не используй функции и классы.
- Не используй циклы.
- Не используй сложные термины без пояснения.
- Ответ не длиннее 8 строк.
- Приведи только один пример.
- Не добавляй вступление.
- Пиши простыми словами.
"""

with GigaChat(credentials=key, verify_ssl_certs=False, model="GigaChat-2") as client:
    response = client.chat.create(prompt)
    print("=== ОТВЕТ МОДЕЛИ ===")
    print(response.messages[0].content[0].text.strip())