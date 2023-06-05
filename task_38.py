# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной.
# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.
 
def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv('phonebook.csv')
    while (choice !=8):
        if choice == 1:
            show_phonebook(phone_book)
        elif choice == 2:
            name = input('Введите Фамилию: ').lower()
            print(find_by_name(phone_book, name))
        elif choice == 3:
            number = input('Введите номер: ')
            print(find_by_number(phone_book, number))
        elif choice == 4:
            user_data = get_new_user()
            add_user(phone_book, user_data)
            write_csv('phonebook.csv', phone_book)
        elif choice == 5:
            delete_user(phone_book)
        elif choice == 6:
            write_txt('phon.txt', phone_book)
        elif choice == 7: 
            print('До свидания!') 
            return
        choice = show_menu()

def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Удалить абонениа из справочника\n"
          "6. Сохранить справочник в текстовом формате\n"
          "7. Закончить работу")
    choice = int(input())
    return choice

def read_csv(phone_book):
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(phone_book, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data

def show_phonebook(phone_book):
    for dic in phone_book:
            for key,value in dic.items():
                print (key, value,end= ', ')
            print()

def find_by_name(phone_book, name):
    flag = False
    for dic in phone_book:
        for key,value in dic.items():
            if value.lower() == name:
                flag = True
                print(dic)
    if flag == False:
                    print('Такого абонента не существует')

def find_by_number(phone_book, number):
    flag = False
    for dic in phone_book:
        for key,value in dic.items():
            if value.lower() == number:
                flag = True
                print(dic)
    if flag == False:
                    print('Такого абонента не существует')

def get_new_user():
     user_data = []
     user_data.append(input('Введите фамилию: '))
     user_data.append(input('Введите имя: '))
     user_data.append(input('Введите телефон: '))
     user_data.append(input('Введите описание: '))
     return user_data

def add_user(phone_book, user_data):                                    
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    record = dict(zip(fields, user_data))
    phone_book.append(record)

def write_csv(filename, data):
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                      s += v + ','
            fout.write(f'{s[:-1]}\n')

def delete_user(phone_book):
    show_phonebook(phone_book)
    r = input('Введите фамилию абонента, которого нужно удалить: ')
    flag = False
    for dic in phone_book:
        for key,value in dic.items():
            if value.lower() == r.lower():
                phone_book.remove(dic)
                return(phone_book)
    if flag == False:
        print('Такого абонента не существует') 
    write_csv(phone_book, r)
        
def write_txt(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')
    print('Данные сохранены')

work_with_phonebook()
               

        




    