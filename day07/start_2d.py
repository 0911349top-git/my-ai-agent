import numpy as np

numbers = np.array([10, 20, 30, 40])
print(numbers)
print(numbers.shape)
print(numbers.ndim)

data = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(data)
print(data.ndim)
print(data.shape)
print(data.size)

print(data[0, 0])
print(data[1, 2])

print(data[0])
print(data[:, 1])

data[0, 1] = 999
print(data)

data[1] = [1, 2, 3]
print(data)

# 13. Срез строк
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(data[0:2])

# 14. Срез строк и столбцов одновременно
print(data[0:2, 1:3])

# 15. Арифметика со всей таблицей
data = np.array([[1, 2], [3, 4]])
print(data + 10)
print(data * 2)
# Операция выполняется для каждого элемента.

# 16. Сумма, среднее, минимум и максимум
data = np.array([[10, 20], [30, 40]])
print(np.sum(data))
print(np.mean(data))
print(np.min(data))
print(np.max(data))
# Эти функции работают сразу по всей таблице.

# 18. axis=0 — по столбцам
data = np.array([[10, 20, 30], [40, 50, 60]])
print(np.sum(data, axis=0))
# Результат:
# [50 70 90]

# 19. axis=1 — по строкам
print(np.sum(data, axis=1))
# Результат:
# [ 60 150]

# 20. Среднее по строкам и столбцам
print(np.mean(data, axis=1))
print(np.mean(data, axis=0))

# 21. np.arange() + reshape()
numbers = np.arange(1, 13)
print(numbers)

table = numbers.reshape(3, 4)
print(table)
# Получается таблица 3 × 4.

# 23. Нули и единицы двумерной формы
print(np.zeros((2, 3)))
print(np.ones((3, 2)))

# 24. Сравнение двумерного массива с числом
scores = np.array([[45, 67, 82], [91, 53, 74]])
print(scores >= 60)
# Результат — таблица True/False той же формы.

# 25. Фильтрация
passed = scores[scores >= 60]
print(passed)
# После фильтрации получится одномерный массив только из подходящих значений