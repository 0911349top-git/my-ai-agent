age = int(input("Введите возраст : "))

if age >= 16 :
    sogl = input("Введите есть ли согласие на участие (`да`/`нет`) : ")
    if sogl == 'да':
        name = input("Введите имя участника : ")
        kurs = int(input("Введите курс : "))
        ball = int(input("Введите набранный тестовый балл от 0 до 100 : "))
        if ball >= 90 and ball <= 100:
            print(kurs)
            print(ball)
            print(sogl)
            print("Высокий результат")
        elif ball >= 70:
            print(kurs)
            print(ball)
            print(sogl)
            print("Хороший результат")
        elif ball >= 50:
            print(kurs)
            print(ball)
            print(sogl)
            print("Допустимый результат")
    else:
            print(kurs)
            print(ball)
            print(sogl)
            print("Результат недостаточен")
    else:
        print('Нет согласия на участие')
else:
    print('Возраст не подходит')
