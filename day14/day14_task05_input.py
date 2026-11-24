from getpass import getpass
from gigachat import GigaChat
from gigachat.models import ChatCompletionRequest, ChatMessage

key = getpass("Введите ключ: ")

# Список сообщений: пока только system
messages = [
    ChatMessage(
        role="system",
        content="Ты учебный помощник. Пиши простыми словами."
    )
]

# Получаем текст пользователя и добавляем его в messages
user_text = input("Вы: ")
messages.append(ChatMessage(role="user", content=user_text))

# Проверяем, что сообщений теперь два
print("Количество сообщений:", len(messages))

# Формируем запрос
request = ChatCompletionRequest(messages=messages)

# Отправляем запрос и выводим ответ
with GigaChat(credentials=key, verify_ssl_certs=False, model="GigaChat-2") as client:
    response = client.chat.create(request)
    answer = response.messages[0].content[0].text
    print("Бот:", answer)