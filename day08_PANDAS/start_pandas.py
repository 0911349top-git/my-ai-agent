import pandas as pd

# print("Pandas подключена")
# print(pandas.__version__)

#6. Series — один столбец данных
scores = pd.Series([70, 80, 90, 65])
print(scores)

#8. Индексы Series
print(scores[0])
print(scores[2])

#9. Собственные индексы Series
scores = pd.Series(
    [70, 80, 90],
    index=["Иванов", "Петров", "Сидорова"]
)

print(scores["Петров"])

#10. Первый DataFrame
data = {
    "Имя": ["Анна", "Иван", "Олег"],
    "Баллы": [85, 72, 91]
}

df = pd.DataFrame(data)
print(df)

#14. shape у DataFrame
print(df.shape)

#15. columns — названия столбцов
print(df.columns)

#16. index — индексы строк
print(df.index)

#17. Выбор одного столбца
print(df["Баллы"])

#19. Выбор нескольких столбцов
print(df[["Имя", "Баллы"]])

#20. Добавим третий столбец
df["Группа"] = ["1ИИ-1", "1ИИ-1", "1ИИ-2"]
print(df)

#21. Столбец из одного значения
df["Курс"] = 1
print(df)

#22. Изменение столбца вычислением
df["Баллы"] = df["Баллы"] + 5
print(df)

#23. Создание нового вычисляемого столбца
df["Баллы после бонуса"] = df["Баллы"] + 10
print(df)

#24. Выбор строки через loc
print(df.loc[0])

#25. Выбор строки через iloc
print(df.iloc[1])

#26. Выбор конкретного значения через loc
print(df.loc[0, "Имя"])

#27. Выбор нескольких строк через iloc
print(df.iloc[0:2])

#28. Фильтрация строк по условию
result = df[df["Баллы"] >= 80]
print(result)

#30. Фильтрация по равенству
result = df[df["Группа"] == "1ИИ-1"]
print(result)

#31. Несколько условий
result = df[(df["Баллы"] >= 70) & (df["Баллы"] <= 90)]
print(result)

#32. Сумма столбца
print(df["Баллы"].sum())

#33. Среднее значение
print(df["Баллы"].mean())

#34. Минимум и максимум
print(df["Баллы"].min())
print(df["Баллы"].max())

#35. count() — количество непустых значений
print(df["Баллы"].count())

#36. head() — первые строки
print(df.head())
#`head()` показывает первые строки таблицы. По умолчанию — до пяти строк.
print(df.head(2))
#Так можно попросить показать только первые 2 строки.

#37. tail() — последние строки
print(df.tail(2))

#38. info() — краткая информация
df.info()

#39. dtypes — типы столбцов
print(df.dtypes)

#40. describe() — простая статистика
print(df.describe())