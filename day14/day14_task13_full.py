from getpass import getpass
from gigachat import GigaChat
from gigachat.models import ChatCompletionRequest, ChatMessage

key = getpass("Введите ключ: ")

# 1. Начало диалога: system-сообщение
messages = [
    ChatMessage(
        role="system",
        content="Ты учебный помощник. Пиши простыми словами и запоминай контекст диалога."
    )
]

with GigaChat(
    credentials=key,
    verify_ssl_certs=False,
    model="GigaChat-2",
    max_retries=3,
    timeout=60.0
) as client:

    # 2. Бесконечный цикл диалога
    while True:
        user_text = input("\nВы (или 'выход' для завершения): ")

        # 3. Проверка на выход
        if user_text.lower().strip() == "выход":
            print("Диалог завершён.")
            break

        # 4. Добавляем user-сообщение в историю
        messages.append(ChatMessage(role="user", content=user_text))

        # 5. Отправляем запрос и получаем ответ
        request = ChatCompletionRequest(messages=messages)
        response = client.chat.create(request)
        answer = response.messages[0].content[0].text

        # 6. Выводим ответ
        print("Бот:", answer)

        # 7. Добавляем assistant-сообщение в историю
        messages.append(ChatMessage(role="assistant", content=answer))