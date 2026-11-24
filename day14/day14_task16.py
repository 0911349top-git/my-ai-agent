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

    while True:
        user_text = input("\nВы (команды: 'выход', 'очистить'): ")
        command = user_text.lower().strip()

        # 2. Команда «выход» — завершение программы
        if command == "выход":
            print("Диалог завершён.")
            break

        # 3. Команда «очистить» — сброс истории, system остаётся
        if command == "очистить":
            messages = [system_message]
            print("Диалог удален. system сохранен.")
            print(f"Количество сообщений: {len(messages)}")
            continue  # переходим к следующей итерации, API не вызываем

        # 4. Обычный вопрос — добавляем в историю
        messages.append(ChatMessage(role="user", content=user_text))

        # 5. Запрос к API
        request = ChatCompletionRequest(messages=messages)
        response = client.chat.create(request)
        answer = response.messages[0].content[0].text

        print("Бот:", answer)

        # 6. Сохраняем ответ бота
        messages.append(ChatMessage(role="assistant", content=answer))

        # 7. Ограничиваем историю: system + последние 6
        if len(messages) > 7:
            messages = messages[:1] + messages[-6:]
            print(f"[История обрезана до {len(messages)} сообщений]")