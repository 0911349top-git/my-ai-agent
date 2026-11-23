name = input('Введите имя:')
family = input('Введите фамилию:')
age = int(input('Введите возраст:'))
rost = int(input('Введите рост:'))
tech = input('Введите любимую IT-технологию:')

full_name = name + ' ' + family
print('=' * 30)
print('количество символов в полном имени', len(name) + len(family))
print('Возраст через 5 лет будет:', (age + 5))
print(name[0])
print('=' * 30)