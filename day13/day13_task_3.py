from getpass import getpass
from gigachat import GigaChat

key = getpass("Введите ключ: ")

prompt = f"""
Ты — помощник начинающего программиста.
Задача — объяснять сложные темы простыми словами.
Аудитория: студент, которые начинают изучать Python и знает только базовый синтаксис (переменные, print, input, if).
Ограничения:
1. Отвечай кратко.
2. Если используешь незнакомый термин — сразу объясняй его.
3. Приводи только один простой пример кода.
"""

with GigaChat(credentials=key, verify_ssl_certs=False, model="GigaChat-2") as client:
    response = client.chat.create(prompt)
    print(response.messages[0].content[0].text)