from getpass import getpass
from gigachat import GigaChat
from gigachat.models import ChatCompletionRequest, ChatMessage

key = getpass("Введите ключ: ")

# 1. Список с одним system-сообщением
messages = [
    ChatMessage(
        role="system",
        content="Ты учебный помощник. Пиши простыми словами."
    )
]

# 2. Первое сообщение пользователя
user_text_1 = input("Вы (сообщение 1): ")
messages.append(ChatMessage(role="user", content=user_text_1))

# 3. Второе сообщение пользователя
user_text_2 = input("Вы (сообщение 2): ")
messages.append(ChatMessage(role="user", content=user_text_2))

# 4. Проверяем количество сообщений
print("Количество сообщений в списке:", len(messages))  # будет 3

# 5. Формируем запрос и отправляем
request = ChatCompletionRequest(messages=messages)

for message in messages:
    print(message.role)

with GigaChat(credentials=key, verify_ssl_certs=False, model="GigaChat-2") as client:
    response = client.chat.create(request)
    answer = response.messages[0].content[0].text
    print("Бот:", answer)