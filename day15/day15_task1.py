text = input("Введите текст : ")

try:
    print("Пробуем выполнить действие")
    n = int(text)
except Exception:
    print("Произошла ошибка")

