import pandas as pd

data = {
    "Имя": ["Анна", "Иван", "Олег", "Виктор", "Ольга", "Артем", "Кира", "Кирилл"],
    "Группа" :["1ИИ-1", "1ИИ-2", "1ИИ-2", "1ИИ-1", "1ИИ-1", "1ИИ-1", "1ИИ-1", "1ИИ-1"],
    "Баллы": [85, 72, 91, 84, 100, 89, 95, 99],
    "Посещено занятий": [85, 72, 91, 84, 100, 98, 82, 96]
}

df = pd.DataFrame(data)

df["Баллы после бонуса"] = df["Баллы"] + 5

print(df)
print(df.shape)
print(df.columns)
print(df.head(3))
print(df.tail(2))
print(df["Баллы"].mean())
print(df["Баллы"].min())
print(df["Баллы"].max())
print(df["Посещено занятий"].sum())        
print(df[df["Баллы"] >= 80])
print(df[df["Группа"] == "1ИИ-1"])

result = df[(df["Баллы"] >= 60) & (df["Баллы"] <= 80)]
print(result)
print(df[["Имя", "Баллы"]])
print(df.loc[0])
print(df.iloc[1])

df["Всего занятий"] = 110
df["Процент посещаемости"] = df["Посещено занятий"] / df["Всего занятий"] * 100

print(df)

result_2 = df[(df["Баллы"] >= 70) & (df["Процент посещаемости"] >= 80)]
print(result_2)

average = df["Баллы"].mean()
result_3 = df[df["Баллы"] > average]

print(average)
print(result_3)