# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом
# def pole():
#     global list_pole
#     list_pole = list(" . " for i in range(3))
#     list_pole = list(list_pole for i in range(3))
#     return list_pole


# pole()


# def print_pole():
#     for i in list_pole:
#         for j in i:
#             print(j, end="")
#         print("")


# print_pole()


# def step_in_pole():
#     x, y = input("В какую строчку и в какой столбец поставим Х?").split()
#     x = int(x)
#     y = int(y)
#     print(x, y)
#     list_pole[1][1]="x"
#     return list_pole

# list_pole[1][2]="o"
# step_in_pole()
# print_pole()
# print(list_pole)
import random
pole = {}
for i in range(1, 4):
    j = 1
    while j < 4:
        pole[str(i)+","+str(j)] = "  .  "
        j += 1


def print_pole():
    for k in pole:
        if int(k[-1]) != 3:
            print(pole[k], end="")
        else:
            print(pole[k])
            print("")


# print_pole()
list_x = []
list_o = []


def play1():
    global k_x, l_x, x_x
    k_x, l_x, x_x = 0, 0, 0
    my_step_x = 0
    while pole.get(my_step_x) != "  .  ":
        my_step_x = input("Через запятую введите сторку и колонку, куда поставить х: ")
    pole[my_step_x] = "  x  "
    print_pole()
    list_x.append(my_step_x)
    # print(list_x, len(list_x))
    for i in range(len(list_x)):
        if k_x == 2 or l_x == 2 or x_x == 2:
            break
        k_x = 0
        l_x = 0
        x_x = 0
        for j in range(len(list_x)):
            if i != j and list_x[i][2] == list_x[j][2]:
                k_x += 1
                # print(f"k_x={k_x}")
            if i != j and list_x[i][0] == list_x[j][0]:
                l_x += 1
                # print(f"l_x={l_x}")
            if i != j and list_x[i][0] == list_x[i][2] and list_x[j][0] == list_x[j][2]:
                x_x += 1
                # print(f"x_x={x_x}")
    return list_x, pole, k_x, l_x, x_x


def play2():
    global k_o, l_o, x_o
    k_o, l_o, x_o = 0, 0, 0
    my_step_o = 0
    while pole.get(my_step_o) != "  .  ":
        my_step_o = input("Через запятую введите сторку и колонку, куда поставить o: ")
    pole[my_step_o] = "  o  "
    print_pole()
    list_o.append(my_step_o)
    # print(list_o, len(list_o))
    for i in range(len(list_o)):
        if k_o == 2 or l_o == 2 or x_o == 2:
            break
        k_o = 0
        l_o = 0
        x_o = 0
        for j in range(len(list_o)):
            if i != j and list_o[i][2] == list_o[j][2]:
                k_o += 1
                # print(f"k_o={k_o}")
            if i != j and list_o[i][0] == list_o[j][0]:
                l_o += 1
                # print(f"l_o={l_o}")
            if i != j and list_o[i][0] == list_o[i][2] and list_o[j][0] == list_o[j][2]:
                x_o += 1
                # print(f"x_o={x_o}")
    return list_o, pole, k_o, l_o, x_x


def bot():
    global k_o, l_o, x_o
    k_o, l_o, x_o = 0, 0, 0
    my_step_o = 0
    count=0
    while pole.get(my_step_o) != "  .  " :
        my_step_o=random.choice(list(pole))
        # print(my_step_o)
        for i in list_x:
            if my_step_o[0]!=i[0] or my_step_o[2]!=i[2]:
                break
            elif my_step_o[0]==i[0] or my_step_o[2]==i[2]:
                break
            else:
                my_step_o=0
                # print("step")
                # count+=1
                break
    print("   ----------")
    pole[my_step_o] = "  o  "
    print_pole()
    list_o.append(my_step_o)
    # print(list_o, len(list_o))
    for i in range(len(list_o)):
        if k_o == 2 or l_o == 2 or x_o == 2:
            break
        k_o = 0
        l_o = 0
        x_o = 0
        for j in range(len(list_o)):
            if i != j and list_o[i][2] == list_o[j][2]:
                k_o += 1
                # print(f"k_o={k_o}")
            if i != j and list_o[i][0] == list_o[j][0]:
                l_o += 1
                # print(f"l_o={l_o}")
            if i != j and list_o[i][0] == list_o[i][2] and list_o[j][0] == list_o[j][2]:
                x_o += 1
                # print(f"x_o={x_o}")
    return list_o, pole, k_o, l_o, x_x

def step_play1():
    print_pole()
    while "  .  " in pole.values():
        play1()
        # print(f"l_x={l_x}  k_x={k_x} x_x={x_x}")
        if k_x == 2 or l_x == 2 or x_x == 2:
            print("Play1 you win!!!")
            break
        # play2()
        bot()
        # print(f"l_o={l_o}  k_o={k_o} x_o={x_o}")
        if k_o == 2 or l_o == 2 or x_o == 2:
            print("Play2 you win!!!")
            break
        if "  .  " not in pole.values():
            print("Ничья!!!)))")
# print(pole)
def step_play2():
    pole["2,2"]="  o  "
    list_o.append("2,2")
    print_pole()
    while "  .  " in pole.values():
        play1()
        # print(f"l_x={l_x}  k_x={k_x} x_x={x_x}")
        if k_x == 2 or l_x == 2 or x_x == 2:
            print("Play1 you win!!!")
            break
        # play2()
        bot()
        # print(f"l_o={l_o}  k_o={k_o} x_o={x_o}")
        if k_o == 2 or l_o == 2 or x_o == 2:
            print("Play2 you win!!!")
            break
        if "  .  " not in pole.values():
            print("Ничья!!!)))")
while True:
    print("Кидаем монетку)))")
    rnd=random.randint(0,2)
    if rnd==0:
        print("Ваш ход!")
        step_play1()
    else:
        print("Первым ходит копьютер!")
        step_play2()
    say=input("Продолжить- 1, закончить- 0:  ")
    if say=="1":
        continue
    else:
        break