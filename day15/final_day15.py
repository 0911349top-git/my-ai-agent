import logging
import sys
from getpass import getpass
from gigachat import GigaChat
from pydantic import BaseModel, Field

# Настройка logging
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# Pydantic-модель данных вакансий
class S_Info(BaseModel):
    category: str = Field(description="Категория вакансий: IT, Производство, Строительство, Медицина")
    education: str = Field(description="Образование: высшее, колледж, школа")
    stage: int = Field(description="Стаж работы в годах")
    forma : str = Field(description="Формат занятости: полная, частичная, удаленная")


# Ввод данных
key = getpass("Введите ключ: ")
text = input("Введите текст: ")

# Проверка на пустой ввод
if not text.strip():
    logging.warning("Пользователь ввёл пустой текст или только пробелы. Запрос к API отменен.")
    print("Ошибка: Вы ввели пустой текст.")
    sys.exit() # Завершаем программу, API не вызывается

# Формирование запроса и обращение к API
prompt = f"Определи категорию вакансии, стаж работы, какое образование и форму занятости из текста: «{text}»"
logging.info(f"Начало запроса к API. Текст пользователя: {text}")

# переменная-счётчик перед try
success_requests = 0
try:
    with GigaChat(credentials=key, verify_ssl_certs=False, model="GigaChat-2") as client:
        completion, parsed = client.chat_parse(
            prompt,
            response_format=S_Info,
            strict=True
        )
        success_requests += 1
        
        # Успешный вывод для пользователя
        print("\n=== РЕЗУЛЬТАТ ===")
        print(f"Вакансия: {parsed.category}")
        print(f"Опыт: {parsed.stage}")
        print(f"Образование: {parsed.education}")
        print(f"Форма занятости: {parsed.forma}")
        print(f"Успешных запросов в этой сессии: {success_requests}")

        with open("result_14.txt", "a", encoding="utf-8") as file:
            file.write(f"Вакансия: {parsed.category}\n")
            file.write(f"Опыт работы: {parsed.stage}\n")
            file.write(f"Образование: {parsed.education}\n")
            file.write(f"Форма занятости: {parsed.forma}\n")

        
        # Логирование успеха
        logging.info(f"Запрос выполнен успешно. Категория: {parsed.category}, Стаж: {parsed.stage}")

except Exception as error:
    # Короткое сообщение для пользователя
    print("Не удалось получить ответ. Попробуйте позже.")
    
    # Техническая ошибка в лог
    logging.error(f"Ошибка при обращении к API: {error}", exc_info=True)