'''
Задача No49.
Решение в группах Создать телефонный справочник с возможностью импорта и
экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона -
данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной
записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной
'''
import os


def show_menu():
    os.system('clear')
    print("\nВыберите необходимое действие:\n"
          "1. Вывести справочник на экран\n"
          "2. Сохранить справочник в текстовом файле\n"
          "3. Найти абонента по фамилии\n"
          "4. Найти абонента по имени\n"
          "5. Завершить работу программы\n")
    choice = int(input('> '))
    return choice

def go_to_function(variant):
    while (variant != 5):
        if variant == 1:         # Вывести справочник на экран
            for line in read_from_txt(filename):
                print(*line, end='')
                pause()
        elif variant == 2:       # Сохранить справочник в текстовом файле
            write_to_txt(filename, abon_list)
            print('\nфайл сохранён !', end='')
            pause()
        elif variant == 3:       # Найти абонента по фамилии
            finder = input_finder('введите фамилию абонента')
            find_abonent(filename, finder)
            pause()              
        elif variant == 4:       # Найти абонента по имени
            finder = input_finder('введите имя абонента')
            find_abonent(filename, finder)
            pause()
        variant = show_menu()

def read_from_txt(filename):         # Чтение файла txt в список
    phone_list = [fields]
    with open(filename, 'r', encoding='utf-8') as file:
        # phone_list.append(fields)
        for line in file:
            phone_list.append(line.split(','))
    return phone_list

def write_to_txt(filename, phone_dict):        # Запись списка в файл txt
    with open(filename, 'w', encoding='utf-8') as file:
        for line in phone_dict:
            word = ''
            for w in line:
                word += str(w) + ','
            file.write(f'{word[:-1]}\n')

def input_finder(message):              # Запрос параметра для поиска
    answer = input(f'\n{message} > ').title()
    print('\n')
    return answer

def pause():
    input('\nнажмите Enter для продолжения...')

def find_abonent(filename, find_param):
    phone_list = read_from_txt(filename)
    find_list = []
    for line in phone_list:
        if find_param in line:
            find_list.append(line)
    if len(find_list) == 0: print('нет данных!')
    else: 
        find_list.insert(0, fields)
        for line in find_list:
            print(*line, end='')


filename = './my_stack/phone.txt'
fields = ["Фамилия", "Имя", "Отчество", "Телефон\n\n"]
abon_list = [
    ['Пушкин','Александр','Сергеевич',999],
    ['Есенин','Сергей','Александрович',123]
]
go_to_function(show_menu())

    