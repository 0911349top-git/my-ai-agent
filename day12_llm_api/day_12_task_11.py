from getpass import getpass
from gigachat import GigaChat

# 1. Ввод ключа (символы не будут отображаться на экране)
credentials = getpass("Вставьте ключ авторизации: ")

long_text = (
    "Python — это популярный язык программирования. "
    "Он широко используется для веб-разработки, анализа данных, искусственного интеллекта и автоматизации. "
    "Его главное преимущество — простой и понятный синтаксис, который легко освоить новичкам. "
    "Кроме того, для Python написано огромное количество полезных библиотек, что ускоряет разработку."
)

prompt = f"Сократи следующий текст до 2 предложений, сохранив основной смысл:\n\n{long_text}"

# 2. Подключение
with GigaChat(credentials=credentials, verify_ssl_certs=False, model="GigaChat-2") as client:
    # 3. Отправка запроса
    #response = client.chat("Объясни простыми словами, что такое API, списком из 4 коротких пунктов.")
    response = client.chat.create(prompt)
     # 4. Вывод ответа (в SDK GigaChat путь к ответу: choices -> message -> content)
    print("=== ОТВЕТ МОДЕЛИ ===")
    print(response.messages[0].content[0].text)