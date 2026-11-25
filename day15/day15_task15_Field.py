from pydantic import BaseModel, Field

class Book(BaseModel):
    title: str = Field(description="Название книги")
    author: str = Field(description="ФИО Автора")
    year: int = Field(description="Год издания")

result = Book(title="Онегин", author="Пушкин", year="2000")
print(result)
print(result.title)
print(result.author)
print(result.year)