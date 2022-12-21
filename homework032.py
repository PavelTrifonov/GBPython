# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]
my_list = list(int(i) for i in input("Введите числа через пробел: ").split())
print(my_list)
s = len(my_list)
if s % 2 == 1:
    i = 0
    sum_list = []
    while i != (s-1)/2:
        sum_list.append(my_list[i]*my_list[s-1-i])
        i += 1
    sum_list.append((my_list[i])**2)
else:
    i = 0
    sum_list = []
    while i < s/2:
        sum_list.append(my_list[i]*my_list[s-1-i])
        i += 1
print(sum_list)
