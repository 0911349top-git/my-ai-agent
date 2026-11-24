from getpass import getpass
from gigachat import GigaChat

key = getpass("Введите ключ: ")

prompt = f"""
Ты — помощник начинающего программиста.
Задача — объяснять сложные темы простыми словами.
Аудитория: студент, ко
Ответ дай в 2-5 предложениях.
Пиши простыми словами.
"""

with GigaChat(credentials=key, verify_ssl_certs=False, model="GigaChat-2") as client:
    response = client.chat.create(prompt)
    print(response.messages[0].content[0].text)