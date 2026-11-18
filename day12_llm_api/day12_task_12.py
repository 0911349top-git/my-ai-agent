from getpass import getpass
from gigachat import GigaChat

# 1. Ввод ключа (символы не будут отображаться на экране)
credentials = getpass("Вставьте ключ авторизации: ")

phrase = "Студент Виктор, группа 1ИИ-11, набрал 90 баллов."

prompt = (
    f"Извлеки из текста имя студента, название группы и балл. "
    f"Выведи результат строго тремя отдельными строками в формате:\n"
    f"Имя: [имя]\nГруппа: [группа]\nБалл: [балл]\n"
    f"Текст: «{phrase}»"
)

# 2. Подключение
with GigaChat(credentials=credentials, verify_ssl_certs=False, model="GigaChat-2") as client:
    # 3. Отправка запроса
    #response = client.chat("Объясни простыми словами, что такое API, списком из 4 коротких пунктов.")
    response = client.chat.create(prompt)
     # 4. Вывод ответа (в SDK GigaChat путь к ответу: choices -> message -> content)
    print("=== ОТВЕТ МОДЕЛИ ===")
    print(response.messages[0].content[0].text)