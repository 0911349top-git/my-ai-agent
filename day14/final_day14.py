from getpass import getpass
from gigachat import GigaChat
from gigachat.models import ChatCompletionRequest, ChatMessage

key = getpass("Введите ключ: ")

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
        print(f"[История сообщений = {len(messages)} ]")
        messages.append(ChatMessage(role="assistant", content=answer))

        # Сохраняем пару «Вы / Бот» в файл
        with open("chat_history.txt", "a", encoding="utf-8") as file:
            file.write(f"Вы: {user_text}\n")
            file.write(f"Бот: {answer}\n")
            file.write("-" * 40 + "\n")

        if len(messages) > 7:
            messages = messages[:1] + messages[-6:]
            print(f"[История обрезана до {len(messages)} сообщений]")