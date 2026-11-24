from getpass import getpass
from gigachat import GigaChat

key = getpass("Введите ключ: ")

# Формируем строгий промпт
prompt = """
Ты преподаватель Python для начинающих.
Объясни тему «словари».
Ответ дай в формате:
1. Определение.
2. Один пример кода.
3. Две типичные ошибки.
"""

with GigaChat(credentials=key, verify_ssl_certs=False, model="GigaChat-2") as client:
    response = client.chat.create(prompt)
    print("=== ОТВЕТ МОДЕЛИ ===")
    print(response.messages[0].content[0].text.strip())