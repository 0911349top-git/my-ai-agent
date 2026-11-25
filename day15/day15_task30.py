from getpass import getpass
from gigachat import GigaChat
from pydantic import BaseModel, Field

# 1. Создаём ПЕРВУЮ модель (для вакансий)
class JobInfo(BaseModel):
    category: str = Field(description="Категория вакансии")
    stage: int = Field(description="Стаж работы в годах")

# 2. Создаём ВТОРУЮ модель (для студентов)
class Comp_Info(BaseModel):
    name: str = Field(description="Название организации")
    sphere: str = Field(description="Специализация деятельности")
   
key = getpass("Введите ключ: ")

# 3. Спрашиваем у пользователя режим работы
print("Выберите режим:")
print("1. Анализ вакансии")
print("2. Анализ компании")
mode = input("Введите номер режима (1 или 2): ")

# 4. В зависимости от режима выбираем модель и формируем промпт
if mode == "1":
    selected_model = JobInfo
    prompt_text = "Извлеки категорию вакансии и стаж работы из текста: "
elif mode == "2":
    selected_model = Comp_Info
    prompt_text = "Извлеки название компании, её сферу деятельности из текста: "
else:
    print("Неверный режим. Завершение программы.")
    exit()

text = input("Введите текст: ")
prompt = f"{prompt_text} «{text}»"

# 5. Отправляем запрос, подставляя выбранную модель
with GigaChat(credentials=key, verify_ssl_certs=False, model="GigaChat-2") as client:
    try:
        # В response_format передаётся та переменная, которая была выбрана выше
        completion, parsed = client.chat_parse(
            prompt,
            response_format=selected_model, # подстановка модели
            strict=True
        )
        
        print("\n=== РЕЗУЛЬТАТ ===")
        # 6. Выводим данные (поля зависят от выбранной модели)
        if mode == "1":
            print(f"Вакансия: {parsed.category}")
            print(f"Стаж: {parsed.stage}")
        elif mode == "2":
            print(f"Компания: {parsed.name}")
            print(f"Сфера деятельности: {parsed.sphere}")
        

    except Exception as error:
        print("Не удалось получить ответ.")
        print(f"Техническая ошибка: {error}")