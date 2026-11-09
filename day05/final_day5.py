names = ["Иванов", "Петров", 'Сидоров', 'Королева', 'Яшин']
scores = [78, 55, 98, 87, 59]

total = 0
m = 0
for i in range(len(scores)):
    if scores[i] > m:
        m = scores[i]
with open("group_report.txt", "w", encoding="utf-8") as file:
    for i in range(len(names)):
        total += scores[i]
        if scores[i] >= 60 :
            # print(names[i] + '-' +  str(scores[i]) + '- зачёт')
            file.write(names[i] + ' - ' +  str(scores[i]) + ' - зачёт\n')
        else:
            # print(names[i] + '-' +  str(scores[i]) + '- незачёт')
            file.write(names[i] + ' - ' +  str(scores[i]) + ' - незачёт\n')

    file.write(str(total) + '\n')
    file.write(str(m) + '\n')

with open("group_report.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

name_new = input('Введите фамилию : ')
ball_new = int(input('Введите балл : '))
names.append(name_new)
scores.append(ball_new)

with open("group_report.txt", "a", encoding="utf-8") as file:
    if ball_new >= 60:
        file.write(name_new + ' - ' + str(ball_new) +  " - зачёт\n")
    else:
        file.write(name_new + ' - ' + str(ball_new) +  " - незачёт\n")