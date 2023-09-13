#
# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя  или фамилию, и Вы должны реализовать функционал для изменения
# и удаления данных

import os


def write_to_file(path1):
    tmp_line = input("Введите ФИО и телефон: ")
    with open('phones.txt', "a") as file1:
        file1.write(tmp_line + "\n")


def search_file(path1, search_input):
    with open('phones.txt', "r") as file1:
        lst_1 = file1.readlines()
        flag1 = False
        result = "\n"
        for line in lst_1:
            if search_input in line:
                result = result + line
                flag1 = True
        if not flag1:
            result = "Извините, такой записи нет\n"
    return result


def show_all(path1):
    with open('phones.txt', "r") as file1:
        return file1.read()


def update_record(path1, search_input):
    with open('phones.txt', "r") as file1:
        lst_1 = file1.readlines()
    with open('phones.txt', "w") as file2:
        updated = False
        for line in lst_1:
            if search_input in line:
                new_data = input("Введите новые ФИО и телефон для изменения: ")
                file2.write(new_data + "\n")
                updated = True
            else:
                file2.write(line)
        if not updated:
            print("Извините, такой записи нет")


def delete_record(path1, search_input):
    with open('phones.txt', "r") as file1:
        lst_1 = file1.readlines()
    with open('phones.txt', "w") as file2:
        deleted = False
        for line in lst_1:
            if search_input in line:
                deleted = True
            else:
                file2.write(line)
        if not deleted:
            print("Извините, такой записи нет")


while True:
    print("\nМеню:")
    print("1. Вывести весь файл")
    print("2. Записать новые данные в файл?")
    print("3. Найти конкретную запись в файле")
    print("4. Изменить данные")
    print("5. Удалить данные")
    print("6. Выйти из программы")

    choice = input("Выберите действие (1/2/3/4/5/6): ")

    if choice == '1':
        print(show_all('phones.txt'))
    elif choice == '2':
        write_to_file('phones.txt')
    elif choice == '3':
        search_input = input("Что ищем?: ")
        print(search_file('phones.txt', search_input))
    elif choice == '4':
        search_input = input("Введите ФИО или телефон для изменения: ")
        update_record('phones.txt', search_input)
    elif choice == '5':
        search_input = input("Введите ФИО или телефон для удаления: ")
        delete_record('phones.txt', search_input)
    elif choice == '6':
        break
    else:
        print("Неправильный ввод. Попробуйте снова.")