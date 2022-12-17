# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для и получения случайного int
from random import randint as rd
myNumb_list = []
for i in range(rd(3, 10)):
    myNumb_list.append(rd(1, 100))
print(f"Рандомный список ---> {myNumb_list}")
myMix_list = []
len_list = len(myNumb_list)
i = 0
while i != len_list:
    lenList = len(myNumb_list)
    n = rd(0, lenList-1)
    myMix_list.append(myNumb_list[n])
    myNumb_list.remove(myNumb_list[n])
    i += 1
print(f"Миксованный список -> {myMix_list}")
