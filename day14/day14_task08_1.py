from getpass import getpass
from gigachat import GigaChat
from gigachat.models import ChatCompletionRequest, ChatMessage

key = getpass("Введите ключ: ")

# 1. Начало диалога: system-сообщение
messages = [
    ChatMessage(
        role="system",
        content="Ты учебный помощник. Пиши простыми словами."
    )
]

# 2. Первый вопрос пользователя
user_text_1 = input("Вы: ")
messages.append(ChatMessage(role="user", content=user_text_1))

# 3. Отправляем запрос и получаем ответ
request = ChatCompletionRequest(messages=messages)

with GigaChat(credentials=key, verify_ssl_certs=False, model="GigaChat-2") as client:
    response = client.chat.create(request)
    answer = response.messages[0].content[0].text
    print("Бот:", answer)

# 4. Добавляем ответ бота обратно в историю!
messages.append(ChatMessage(role="assistant", content=answer))

# 5. Проверяем, что история выросла
print("\n--- История диалога ---")
for i, msg in enumerate(messages, 1):
    print(f"{i}. [{msg.role}] {msg.content[:50]}...")
print(f"Всего сообщений в истории: {len(messages)}")