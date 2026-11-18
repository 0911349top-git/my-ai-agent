#from gigachat import GigaChat
#print("Библиотека gigachat доступна")

from getpass import getpass
from gigachat import GigaChat

# 1. Ввод ключа (символы не будут отображаться на экране)
credentials = getpass("Вставьте ключ авторизации: ")

prompt = input("Введите вопрос модели: ")
prompt = prompt + " Ответь не более чем в 5 предложениях."

# 2. Подключение
with GigaChat(credentials=credentials, verify_ssl_certs=False, model="GigaChat-2") as client:
    # 3. Отправка запроса
    #response = client.chat("Объясни простыми словами, что такое API, списком из 4 коротких пунктов.")
    response = client.chat.create(prompt)
     # 4. Вывод ответа (в SDK GigaChat путь к ответу: choices -> message -> content)
    print("=== ОТВЕТ МОДЕЛИ ===")
    print(response.messages[0].content[0].text)
