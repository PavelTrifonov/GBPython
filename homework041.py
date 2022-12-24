# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
def f_poly(k):
    # k=int(input("Введите степень многочлена: "))
    from random import randint as rd
    polynom=""
    while k!=0:
        koef=rd(-100,100)
        if len(polynom)==0:
            polynom+=str(koef)+"*x**"+str(k)
            k-=1
            continue
        if k==1:
            if koef!=0 and koef<0:
                polynom+=" - "+str(abs(koef))+"*x"
                k-=1
            elif koef!=0 and koef>0:
                polynom+=" + "+str(koef)+"*x"
                k-=1
            continue
        if koef!=0 and koef<0:
            polynom+=" - "+str(abs(koef))+"*x**"+str(k)
            k-=1
        elif koef!=0 and koef>0:
            polynom+=" + "+str(koef)+"*x**"+str(k)
            k-=1
        else:
            k-=1
    if koef!=0 and koef<0:
        polynom+=" - "+str(abs(koef))
    else:
        polynom+=" + "+str(koef)
    polynom+=" = 0 "
    print(polynom)
    return polynom
def write_file(k):
    data = open('fileHomeWork.txt', 'w')
    data.write(f_poly(k))
    data.write('\n')
    data.write(f_poly(k))
    data.close()
write_file(int(input("Введите степень многочлена: ")))
