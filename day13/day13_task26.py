from getpass import getpass
from gigachat import GigaChat
from gigachat.models import ChatCompletionRequest, ChatMessage, ChatModelOptions

key = getpass("Введите ключ: ")

request = ChatCompletionRequest(
    messages=[
        ChatMessage(
            role="user",
            content="Придумай 3 коротких названия для учебного IT-проекта."
        )
    ],
    model_options=ChatModelOptions(
        temperature=1.0,
        max_tokens=150,
        repetition_penalty=1.05
    )
)

with GigaChat(credentials=key, verify_ssl_certs=False, model="GigaChat-2") as client:
    response = client.chat.create(request)
    print(response.messages[0].content[0].text)