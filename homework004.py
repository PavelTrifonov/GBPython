# Напишите программу, которая по заданному номеру четверти, показывает диапазон 
# возможных координат точек в этой четверти (x и y).
while True:
    n=input("Введите номер четверти: ")
    if n=="" :
        break
    elif int(n)==1:
        print(f"n={n} -> x>0; y>0")
    elif int(n)==2:
        print(f"n={n} -> x>0; y<0")
    elif int(n)==3:
        print(f"n={n} -> x<0; y<0")
    elif int(n)==4:
        print(f"n={n} -> x<0; y>0")   
    else:
        print("Введите число от 1 до 4 включительно!!!")