languages = ["Python", "Java", "C++"]

print(languages)
print(len(languages))

languages[1] = "JavaScript"
print(languages)

print(languages[0])
print(languages[1])
print(languages[2])

scores = [75, 82, 90, 68]
print(scores)
print(scores[0])

data = ["Анна", 18, 4.7, True]
print(data)

languages = ["Python", "Java"]
languages.append("C++")
print(languages)

languages = ["Python", "C++"]
languages.insert(1, "Java")
print(languages)

languages = ["Python", "Java", "C++"]
# languages.remove("Java") # удаление по значению
languages.pop(1) # vудаление по индексу
print(languages)

languages = ["Python", "Java", "C++"]

print("Python" in languages)
print("Go" in languages)

answer = input("Введите язык: ")

if answer in languages:
    print("Такой язык есть в списке")
else:
    print("Такого языка нет в списке")