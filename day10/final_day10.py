import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students_missing.csv")

print(df.head(1))
print(df.info())


result_1 = df[df["Группа"] == "1ИИ-1"]
result_2 = df[df["Группа"] == "1ИИ-2"]
print(result_1, result_2)
print(df["Баллы"].agg(["mean", "min", "max", "count"]))

result = df.groupby("Группа")["Баллы"].mean().reset_index()
sorted_df = result.sort_values("Баллы", ascending=False)
print(sorted_df)

sorted_df.to_csv("group_summary.csv",index=False, encoding="utf-8")

plt.bar(sorted_df["Группа"], sorted_df["Баллы"])
plt.title("Средний балл по группам")
plt.xlabel("Группа")
plt.ylabel("Средний балл")
plt.grid()
plt.tight_layout()
plt.savefig("chart.png")
plt.show()