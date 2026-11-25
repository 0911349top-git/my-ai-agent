from getpass import getpass
from gigachat import GigaChat
from pydantic import BaseModel, Field

class S_Info(BaseModel):
    category: str = Field(description="Категоря вакансий: IT, Производство, Строительство, Медицина ")
    stage: int = Field(description="Стаж работы")

key = getpass("Введите ключ: ")
text = input("Введите сообщение для поиска вакансии: ")

prompt = f"Определи категорию вакансии и стаж работы: «{text}»"

with GigaChat(credentials=key, verify_ssl_certs=False, model="GigaChat-2") as client:
    completion, parsed = client.chat_parse(
        prompt,
        response_format=S_Info,
        strict=True
    )

print("Вакансия:", parsed.category)
print("Опыт:", parsed.stage)