# Задайте список из вещественных чисел. Напишите программу, которая
# найдёт разницу между максимальным и минимальным значением дробной
# части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
my_list = input("Введите числа через пробел: ").split()
print(list(float(i) for i in my_list), end=" => ")

# new_list = []
# for i in my_list:
#     l = i.split(".")
#     if len(l) > 1:
#         new_list.append(float("0."+l[1]))

new_list = list(float("0."+i[1]) for i in filter(lambda x: len(x)>1, map(lambda x: x.split("."), my_list)))
print(max(new_list)-min(new_list))