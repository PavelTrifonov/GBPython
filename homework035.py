# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи
numb = int(input("Введите число: "))
F_list1 = [0, 1]
F_list2 = [1, 0]
i = 1
while i < numb:
    F_list1.append(F_list1[i]+F_list1[i-1])
    F_list2.insert(0, F_list2[1]-F_list2[0])
    i += 1
F_list2.pop(-1)
print(F_list2+F_list1)