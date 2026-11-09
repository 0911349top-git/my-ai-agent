from colorama import Fore, Style

first_name = input("Введите имя: ")
last_name = input("Введите фамилию: ")
group = input("Введите группу: ")

print(Fore.GREEN + "==КАРТОЧКА==")
print(Fore.CYAN + first_name)
print(Fore.CYAN + last_name)
print(Style.RESET_ALL + group)