from getpass import getpass
from gigachat import GigaChat
from gigachat.models import ChatCompletionRequest, ChatMessage

key = getpass("Введите ключ: ")

request = ChatCompletionRequest(
    messages=[
        ChatMessage(
            role="system",
            content="Ты помощник начинающего студента. Объясняй кратко и простыми словами."
        ),
        ChatMessage(
            role="user",
            content="Объясни, что такое список в Python."
        )
    ]
)


with GigaChat(credentials=key, verify_ssl_certs=False, model="GigaChat-2") as client:
    response = client.chat.create(request)
    print(response.messages[0].content[0].text)