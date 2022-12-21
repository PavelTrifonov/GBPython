# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10
numb = int(input("Введите число: "))
binary = ""
while numb != 0:
    binary += str(numb % 2)
    numb = int((numb-numb % 2)/2)
print(f"{numb} -> {binary[::-1]}")
