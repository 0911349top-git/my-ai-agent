from getpass import getpass
from gigachat import GigaChat
from pydantic import BaseModel, Field

class StudentInfo(BaseModel):
    name: str = Field(description="ФИО Студента")
    group: str = Field(description="Группа")
    score: int = Field(description="Оценка")

key = getpass("Введите ключ: ")
prompt = "Определи данные: Студент Артем Серов из группы 1ИИ-1 получил 5 по экзамену."

with GigaChat(credentials=key, verify_ssl_certs=False, model="GigaChat-2") as client:
    completion, parsed = client.chat_parse(
        prompt,
        response_format=StudentInfo,
        strict=True
    )

print("Студент:", parsed.name)
print("Группа:", parsed.group)
print("Оценка:", parsed.score)