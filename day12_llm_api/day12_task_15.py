from getpass import getpass
from gigachat import GigaChat


credentials = getpass("Вставьте ключ авторизации: ")

text = input("Введите вопрос модели: ")

# Формируем запрос
prompt = text + " Ответь не более чем в 5 предложениях."

# 3. Отправляем запрос модели
with GigaChat(credentials=credentials, verify_ssl_certs=False, model="GigaChat-2") as client:
    response = client.chat.create(prompt)
    answer = response.messages[0].content[0].text.strip()

# 4. Сохраняем в файл: вопрос, «Ответ:», ответ модели
with open("answer.txt", "w", encoding="utf-8") as file:
    file.write(text + "\n")
    file.write("Ответ:\n")
    file.write(answer + "\n")

print(answer)
print("Результат сохранён в файл answer.txt")