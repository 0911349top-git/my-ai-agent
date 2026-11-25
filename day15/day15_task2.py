text = input("Введите текст : ")

try:
    print("Пробуем выполнить действие")
    n = int(text)
except Exception as error:
    print("Ошибка :", error)