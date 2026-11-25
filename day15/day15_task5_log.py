import logging
from getpass import getpass
from gigachat import GigaChat
from gigachat.models import ChatCompletionRequest, ChatMessage

# 1. Первая настройка logging
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

logging.info(f"Программа запущена в app.log")