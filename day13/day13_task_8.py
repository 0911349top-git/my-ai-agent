from getpass import getpass
from gigachat import GigaChat
from gigachat.models import ChatCompletionRequest, ChatMessage, ChatModelOptions

key = getpass("Введите ключ: ")

topic = input("Введите тему: ")

request = ChatCompletionRequest(
    messages=[
        ChatMessage(
            role="system",
            content="Объясни простыми словами. Ответ не длиннее 6 строк"
        ),
        ChatMessage(
            role="user",
            content=topic
        )
    ],
    model_options=ChatModelOptions(
        temperature=0.2,
        max_tokens=150,
        repetition_penalty=1.05
    )
)

with GigaChat(credentials=key, verify_ssl_certs=False, model="GigaChat-2") as client:
    response = client.chat.create(request)
    print(response.messages[0].content[0].text)