from gigachat.models import ChatMessage

messages = [
    ChatMessage(
        role="system",
        content="Ты учебный помощник. Объясняй кратко и простыми словами."
    )
]
user_text = input("Вы: ")

messages.append(
    ChatMessage(
        role="user",
        content=user_text
    )
)