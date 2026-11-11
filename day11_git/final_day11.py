import pandas as pd

df = pd.read_csv("day_11_students.csv")

print(df.head())

print(df.info())

print(df)

result = df.groupby("Группа")["Баллы"].mean().reset_index()
sorted_df = result.sort_values("Баллы", ascending=False)
print(sorted_df)