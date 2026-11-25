text = input("Введите текст : ")

try:
    with GigaChat(credentials=key) as client:
        response = client.chat.create("Привет")
        print(response.messages[0].content[0].text)
except Exception as error:
    print("Ошибка :", error)