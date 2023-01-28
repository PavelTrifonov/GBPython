
def open_class():
        num_class=input('\nВведите номер класса или жмите "enter" для выхода и сохранения изменений: ')
        print("")
        return num_class

def show_subject(dict_class:dict):
    print("")
    for k in dict_class.keys():
        print(f"{k}")


def open_subject():
        subject=input('\nВыберите предмет или жмите "enter" для возврата: \n\n')
        return subject

def show_students(dict_class:dict,key_dict:str):
    for k,i in dict_class[key_dict].items():
        print(f"{k}:  {i}")

def open_student():
        student=input('\nВведите фамилию ученика, чтобы постпавить оценку или жмите "enter" для возврата: ')
        return student

def estimate():
    bal=input('\nПоставьте оценку или жмите "enter" для возврата: ')
    print("")
    return bal

def save_journal():
    print("\nЖурнал сохранен!!!\n")  

def Get_bal():
    change_bal=input("Какую оценку поставить: ")
    return change_bal

def new_bal(key1,key2,key3):
    print(key1[key2][key3])

def performance_student(name):
    print(f"\nУспеваемость ученика {name}: ")