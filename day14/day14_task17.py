from getpass import getpass
from gigachat import GigaChat
from gigachat.models import ChatCompletionRequest, ChatMessage

key = getpass("Введите ключ: ")

# 1. Системное сообщение (сохраняется навсегда)
system_message = ChatMessage(
    role="system",
    content="Ты учебный помощник. Пиши простыми словами и запоминай контекст диалога."
)
messages = [system_message]

with GigaChat(
    credentials=key,
    verify_ssl_certs=False,
    model="GigaChat-2",
    max_retries=3,
    timeout=60.0
) as client:

    # 2. Вывод списка доступных команд перед циклом
    print("Доступные команды:")
    print("  выход     — завершить программу")
    print("  очистить  — сбросить историю диалога (system сохраняется)")
    print("  Введите текст (Вы) — отправить вопрос модели")

    while True:
        user_text = input("\nВы: ")
        command = user_text.lower().strip()

        if command == "выход":
            print("Диалог завершён.")
            break

        if command == "очистить":
            messages = [system_message]
            print("История очищена. Системное сообщение сохранено.")
            print(f"Количество сообщений: {len(messages)}")
            continue

        messages.append(ChatMessage(role="user", content=user_text))
        request = ChatCompletionRequest(messages=messages)
        response = client.chat.create(request)
        answer = response.messages[0].content[0].text

        print("Бот:", answer)
        messages.append(ChatMessage(role="assistant", content=answer))

        if len(messages) > 7:
            messages = messages[:1] + messages[-6:]
            print(f"[История обрезана до {len(messages)} сообщений]")