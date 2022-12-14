# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой 
# находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
while True:
    x=input("Введите значение х: ")
    y=input("Введите значение y: ")
    if x=="" or y=="":
        break
    elif int(x)>0 and int(y)>0:
        print(f"x={x}; y={y} -> 1")
    elif int(x)>0 and int(y)<0:
        print(f"x={x}; y={y} -> 2")
    elif int(x)<0 and int(y)<0:
        print(f"x={x}; y={y} -> 3")
    else:
        print(f"x={x}; y={y} -> 4")