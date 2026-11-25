import logging
from getpass import getpass
from gigachat import GigaChat
from gigachat.models import ChatCompletionRequest, ChatMessage

# 1. Настройка logging (исправлено слово format)
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# 2. Ввод ключа и текста
key = getpass("Введите ключ: ")
text = input("Введите текст: ")

# Логируем ввод (исправлена проверка на пустую строку)
if not text.strip():
    logging.warning("Пользователь ввёл пустой текст или только пробелы")
else:
    logging.info(f"Получен пользовательский запрос: {text}")

# 3. Обращение к API с логированием результата
try:
    with GigaChat(credentials=key, verify_ssl_certs=False, model="GigaChat-2") as client:
        response = client.chat.create(text)
        answer = response.messages[0].content[0].text
        
        print("Бот:", answer)
        logging.info(f"Запрос к API выполнен успешно. Ответ: {answer}")

except Exception as error:
    # Логируем ошибку (упрощена строка форматирования)
    logging.error(f"Ошибка API: {error}", exc_info=True)
    print("Не удалось получить ответ.")