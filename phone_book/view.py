def main_menu():
    command=["Показать все контакты",
            "Открыть файл",
            "Сохранить файл",
            "Новый контакт",
            "Изменить контакт",
            "Удалить контакт",
            "Найти контакт",
            "Выйти из программы"]
    print("Список возможных действий с телефонной книгой: ")
    for i in range(len(command)):
        print(f"\t{i+1}.{command[i]}")
    user_input=int(input("\nВведите номер действия: "))
    return user_input

def show_contakts(phone_book:list):
    if len(phone_book)>0:
        for i in phone_book:
            print(f"{i[0]} {i[1]} ({i[2]})")
    else:
        print("\n\tТелефонная книга пуста!!!\n")

def load_book():
    print("\nТелефонная книга загружена!!!\n")

def save_book():
    print("\nТелефонная книга сохранена!!!\n")  

def new_contakt():
    name=input("Введите имя и фамилию контакта: ")
    number=input("Введите номер контакта: ")
    comment=input("Введите коментарий: ")
    return name, number, comment
def add_contact(name):
    print(f"\nКонтакт {name} добавлен!!!\n") 

def find_contakt():
    search=input("Введите что будем искать: ")
    return search

def delete_cont():
    del_contact=input("Введите какой контакт удалить: ")
    return del_contact

def del_from_book(name):
    print(f"\nКонтакт {name} удален из книги!!!\n") 

def change_contakt():
    change_name=input("Введите какой контакт изменить: ")
    return change_name