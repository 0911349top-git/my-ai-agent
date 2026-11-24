from getpass import getpass
from gigachat import GigaChat

key = getpass("Введите ключ GigaChat API: ")

with GigaChat(credentials=key, verify_ssl_certs=False, model="GigaChat-2") as client:
    response = client.chat.create("Объясни, что такое API, простыми словами.")
    print(response.messages[0].content[0].text)