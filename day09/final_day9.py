import pandas as pd

df = pd.read_csv("students_missing.csv")

print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())

print(df.isna().sum())
df["Баллы"] = df["Баллы"].fillna(0) # Отсутствующие баллы заменяются на 0
#df["Посещено"] = df["Посещено"].fillna(0) # Отсутствующие баллы заменяются на 0
#df["Группа"] = df["Группа"].fillna("Неизвестно") # не указана
clean_df = df.dropna() #Удаляются строки, где есть хотя бы один пропуск (Посещено = 1)

clean_df["Процент посещаемости"] = clean_df["Посещено"] / 20 * 100

result_b = clean_df[clean_df["Баллы"] >= 60]
print(result_b)
result_g = clean_df[clean_df["Группа"] == "1ИИ-1"]
print(result_g)

sorted_df = clean_df.sort_values("Баллы", ascending=False) #Сортировка по убыванию
print(sorted_df)
sort_df = clean_df.sort_values(["Группа", "Баллы"], ascending=[True, False]) #Сначала строки сортируются по группе, затем внутри группы — по баллам по убыванию
print(sort_df)

print(clean_df["Баллы"].mean())
print(clean_df["Баллы"].min())
print(clean_df["Баллы"].max())

clean_df = clean_df.reset_index(drop=True) #Сброс индекса

clean_df.to_csv("final_result_day9.csv",index=False, encoding="utf-8")

print(clean_df)