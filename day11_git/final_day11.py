import pandas as pd

df = pd.read_csv("day_11_students.csv")

#print(df.head())

print(df.info())

result = df.groupby("Группа")["Баллы"].mean().reset_index()
sorted_df = result.sort_values("Баллы", ascending=False)

sorted_df.to_csv("day_11_mean.csv", encoding="utf-8")
print(sorted_df)