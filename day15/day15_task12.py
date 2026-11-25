from pydantic import BaseModel

class Book(BaseModel):
    title: str
    author: str
    year: int

result = Book(title="Онегин", author="Пушкин", year="2000")
print(result)
print(result.title)
print(result.author)
print(result.year)