from getpass import getpass
from gigachat import GigaChat
from gigachat.models import ChatCompletionRequest, ChatMessage

key = getpass("Введите ключ: ")

messages = [
    ChatMessage(
        role="system",
        content="Ты учебный помощник. Пиши простыми словами."
    )
]

user_text = input("Вы: ")
messages.append(ChatMessage(role="user", content=user_text))

request = ChatCompletionRequest(messages=messages)

# Добавлены verify_ssl_certs=False и model="GigaChat-2"
with GigaChat(credentials=key, verify_ssl_certs=False, model="GigaChat-2") as client:
    response = client.chat.create(request)
    answer = response.messages[0].content[0].text
    print("Бот:", answer)