from getpass import getpass
from gigachat import GigaChat
from gigachat.models import ChatCompletionRequest, ChatMessage

key = getpass("Введите ключ: ")

# Системное сообщение — роль помощника Python-разработчика
system_message = ChatMessage(
    role="system",
    content=(
        "Ты помощник по GIT. "
        "Объясняй простыми словами, приводи короткие примеры кода. "
        "Обьясняй значение команд. "
        "Отвечай коротко."
    )
)
messages = [system_message]

with GigaChat(
    credentials=key,
    verify_ssl_certs=False,
    model="GigaChat-2",
    max_retries=3,
    timeout=60.0
) as client:

    print("Доступные команды:")
    print("  выход     — завершить программу")
    print("  очистить  — сбросить историю диалога (system сохраняется)")
    print("  любой текст — отправить вопрос модели")

    while True:
        user_text = input("\nВы: ")
        command = user_text.lower().strip()

        # Команда выхода
        if command == "выход":
            print("Диалог завершён.")
            break

        # Команда очистки истории
        if command == "очистить":
            messages = [system_message]
            print("История очищена. Системное сообщение сохранено.")
            print(f"Количество сообщений: {len(messages)}")
            continue

        # Обычный вопрос — добавляем в историю
        messages.append(ChatMessage(role="user", content=user_text))

        # Отправляем запрос к модели
        request = ChatCompletionRequest(messages=messages)
        response = client.chat.create(request)
        answer = response.messages[0].content[0].text

        print("Бот:", answer)

        # Сохраняем ответ бота в историю
        messages.append(ChatMessage(role="assistant", content=answer))

        # Ограничиваем историю: system + последние 6 сообщений
        if len(messages) > 7:
            messages = messages[:1] + messages[-6:]
            print(f"[История обрезана до {len(messages)} сообщений]")