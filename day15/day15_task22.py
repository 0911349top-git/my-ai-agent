import logging
import sys
from getpass import getpass
from gigachat import GigaChat
from pydantic import BaseModel, Field

# 1. Настройка logging
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# 2. Модель данных
class S_Info(BaseModel):
    category: str = Field(description="Категория вакансий: IT, Производство, Строительство, Медицина")
    stage: int = Field(description="Стаж работы в годах")

# 3. Ввод данных
key = getpass("Введите ключ: ")
text = input("Введите текст: ")

# 4. Проверка на пустой ввод
if not text.strip():
    logging.warning("Пользователь ввёл пустой текст или только пробелы. Запрос к API отменен.")
    print("Ошибка: Вы ввели пустой текст.")
    sys.exit() # Завершаем программу, API не вызывается

# 5. Формирование запроса и обращение к API
prompt = f"Определи категорию вакансии и стаж работы из текста: «{text}»"
logging.info(f"Начало запроса к API. Текст пользователя: {text}")

try:
    with GigaChat(credentials=key, verify_ssl_certs=False, model="GigaChat-2") as client:
        completion, parsed = client.chat_parse(
            prompt,
            response_format=S_Info,
            strict=True
        )
        
        # Успешный вывод для пользователя
        print("\n=== РЕЗУЛЬТАТ ===")
        print(f"Вакансия: {parsed.category}")
        print(f"Опыт: {parsed.stage}")
        
        # Логирование успеха
        logging.info(f"Запрос выполнен успешно. Категория: {parsed.category}, Стаж: {parsed.stage}")

except Exception as error:
    # Короткое сообщение для пользователя
    print("Не удалось получить ответ. Попробуйте позже.")
    
    # Техническая ошибка в лог
    logging.error(f"Ошибка при обращении к API: {error}", exc_info=True)