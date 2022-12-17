# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11
while True:
    number=input("Введите число: ")
    if number=="":
        break
    sum_numbers=0
    if "," in number:
        number=number.split(",")
        for i in number[0]:
            sum_numbers+=int(i)
        for i in number[1]:
            sum_numbers+=int(i)
    elif "." in number:
        number=number.split(".")
        for i in number[0]:
            sum_numbers+=int(i)
        for i in number[1]:
            sum_numbers+=int(i)
    else:
        for i in number:
            sum_numbers+=int(i)
    print(sum_numbers)