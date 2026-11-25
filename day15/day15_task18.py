from getpass import getpass
from gigachat import GigaChat
from pydantic import BaseModel, Field

class TopicAnalysis(BaseModel):
    topic: str = Field(description="Категоря тем текста.")
    difficulty: int = Field(description="Сложность темы: низкая = 1, средняя = 2, высокая = 3.")
    summary: str = Field(description="Краткое описание темы (1 предложение)")


key = getpass("Введите ключ: ")
text = input("Введите сообщение : ")

prompt = f"Определи категорию темы и трудность: «{text}»"

with GigaChat(credentials=key, verify_ssl_certs=False, model="GigaChat-2") as client:
    completion, parsed = client.chat_parse(
        text,
        response_format=TopicAnalysis,
        strict=True
    )

print("Тема:", parsed.topic)
print("Сложность:", parsed.difficulty)
print("Содержание:", parsed.topic)