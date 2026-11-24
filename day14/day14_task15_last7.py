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

    while True:
        user_text = input("\nВы (или 'выход' для завершения): ")

        if user_text.lower().strip() == "выход":
            print("Диалог завершён.")
            break

        # Добавляем user-сообщение
        messages.append(ChatMessage(role="user", content=user_text))

        # Отправляем запрос и получаем ответ
        request = ChatCompletionRequest(messages=messages)
        response = client.chat.create(request)
        answer = response.messages[0].content[0].text

        print("Бот:", answer)

        # Добавляем assistant-сообщение
        messages.append(ChatMessage(role="assistant", content=answer))

        # Ограничиваем историю: system + последние 6 сообщений
        if len(messages) > 7:
            # messages[0] — system, messages[-6:] — последние 6
            messages = messages[:1] + messages[-6:]
            print(f"[История обрезана до {len(messages)} сообщений]")