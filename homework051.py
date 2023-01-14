# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет. Играют
# два игрока делая ход друг после друга. Первый ход определяется
# жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'
from random import randint as ri
numb = ri(100, 200)
print(numb)
first_move = ri(0, 2)
if first_move == 0:
    numb1 = int(input("Вы взяли конфет: "))
    numb -= numb1
    print(f"На столе осталось {numb} конфет!")
if numb % 28 != 0:
    bot = numb % 28-1
else:
    bot = 27
numb = numb-bot
print(f"Бот взял {bot} конфет)))")
print(f"На столе осталось {numb} конфет!")
while numb > 28:
    numb1 = int(input("Вы взяли конфет: "))
    numb -= numb1
    print(f"На столе осталось {numb} конфет!")
    if numb <= 28:
        print("Увы, конфеты достались не вам(((")
        break
    if numb//28 > 2:
        if numb % 28 != 0:
            bot = abs(numb % 28)
        else:
            bot = 27
    else:
        if numb % 28 != 0:
            if numb%28 == 1:
                bot = 28
            else:
                bot = ri(1, 29)
                print(f"Бот взял {bot} конфет)))")
                print(f"На столе осталось {numb-bot} конфет!")
                print("Поздравляем, все конфеты достаются вам!!!")
                break
            if numb-bot == 1:
                print(f"На столе осталось {numb-bot} конфет!")
                print("Поздравляем, все конфеты достаются вам!!!")
                break
        else:
            bot = 27

    print(f"Бот взял {bot} конфет)))")
    numb = numb-bot
    print(f"На столе осталось {numb} конфет!")
    # print(numb1,bot)
