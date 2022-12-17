# Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран,
# а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06
while True:
    n = input("Введите число: ")
    if n == "":
        break
    my_list = []
    n = int(n)
    for i in range(1, n+1):
        my_list.append(round((1+1/i)**i, 2))
    sum_numbers = 0
    for i in my_list:
        sum_numbers += i
    print(f"Для n={n} -> {my_list}")
    print(f"Сумма {sum_numbers}")
