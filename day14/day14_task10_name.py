from getpass import getpass
from gigachat import GigaChat
from gigachat.models import ChatCompletionRequest, ChatMessage

key = getpass("Введите ключ: ")

# 1. Начало диалога: system-сообщение
messages = [
    ChatMessage(
        role="system",
        content="Ты учебный помощник. Пиши простыми словами и запоминай информацию, которую сообщает пользователь."
    )
]

# 2. Сообщаем модели своё имя
my_name = input("Ваше имя: ")
messages.append(ChatMessage(role="user", content=f"Меня зовут {my_name}."))

# 3. Отправляем запрос, получаем ответ и сохраняем его в историю
request = ChatCompletionRequest(messages=messages)

with GigaChat(
    credentials=key,
    verify_ssl_certs=False,
    model="GigaChat-2",
    max_retries=3,
    timeout=60.0
) as client:
    response = client.chat.create(request)
    answer_1 = response.messages[0].content[0].text
    print("\nБот:", answer_1)

    # Сохраняем ответ бота в историю (role="assistant")
    messages.append(ChatMessage(role="assistant", content=answer_1))

    # 4. Задаём отдельный вопрос: «Как меня зовут?»
    messages.append(ChatMessage(role="user", content="Как меня зовут?"))

    # 5. Отправляем второй запрос (с полной историей)
    request_2 = ChatCompletionRequest(messages=messages)
    response_2 = client.chat.create(request_2)
    answer_2 = response_2.messages[0].content[0].text
    print("\nБот:", answer_2)

    # 6. Для наглядности выводим историю
    print("\n--- История диалога ---")
    for i, msg in enumerate(messages, 1):
        print(f"{i}. [{msg.role}] {msg.content}")