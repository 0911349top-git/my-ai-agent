from getpass import getpass
from gigachat import GigaChat

# 1. Ввод ключа (символы не будут отображаться на экране)
credentials = getpass("Вставьте ключ авторизации: ")

# 2. Создаём переменную с разговорной фразой
casual_phrase = "Полушай, я тут подумал, может, замутим что-нибудь по проекту на следующей неделе?"


prompt = (
    f"Перепиши следующую фразу в нейтральном деловом стиле. "
    f"Сохрани смысл, убери разговорные выражения и сленг. "
    f"Выведи только переработанный текст, без пояснений:\n\n"
    f"«{casual_phrase}»"
)


with GigaChat(credentials=credentials, verify_ssl_certs=False, model="GigaChat-2") as client:
    response = client.chat.create(prompt)

    # Вывод ответа
    print("=== ИСХОДНАЯ ФРАЗА ===")
    print(casual_phrase)

    print("\n=== ДЕЛОВОЙ ВАРИАНТ ===")
    print(response.messages[0].content[0].text.strip())