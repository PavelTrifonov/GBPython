# B. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
data = open('fileHomeWork.txt', 'r')

polynom = str(data.read())
data.close()
polynom1, polynom2 = polynom.split("\n")
polynom1 = polynom1.replace(" = 0 ", "").replace(
    " - ", " -").replace(" + ", " ").split(" ")
polynom2 = polynom2.replace(" = 0 ", "").replace(
    " - ", " -").replace(" + ", " ").split(" ")
print(polynom1)
print(polynom2)


def poly_dict(polynoms):
    polynoms_dict = {}
    for i in polynoms:
        p = 0
        if "**" in i:
            p = i.replace("-x*", "-1*x*").replace("*x", "x").replace("x**", " ").split(" ")
            if p[0]=="":
                polynoms_dict[int(p[1])] = 1
            else:
                polynoms_dict[int(p[1])] = int(p[0])
        if i.endswith("x"):
            p = i.replace("-x*", "-1*x*").replace("*x", "x").replace("x", " 1").split(" ")
            if p[0]=="":
                polynoms_dict[int(p[1])] = 1
            elif p[0]=="-":
                polynoms_dict[int(p[1])] = -1
            else:
                polynoms_dict[int(p[1])] = int(p[0])
        if "x" not in i:
            polynoms_dict[0] = int(i)
    print(polynoms_dict)
    return polynoms_dict
# poly_dict(polynom1)
# poly_dict(polynom2)
def sum_polynoms(p1, p2):
    keys = set()
    for i in p1:
        keys.add(int(i))
    for i in p2:
        keys.add(int(i))
    keys=list(keys)
    keys=sorted(keys)[::-1]
    print(keys)
    new_p={}
    for key in keys:
        if p1.get(key,0)+p2.get(key,0)==0:
            del key
        else:
            new_p[key] = p1.get(key,0)+p2.get(key,0)
    print(new_p)
    return new_p


string_polynoms = sum_polynoms(poly_dict(polynom1), poly_dict(polynom2))
S_P = ""
for key, value in string_polynoms.items():
    if  key>1:
        S_P += "+" + str(value)+"*"+"x**"+str(key)
    elif  key==1:
        S_P += "+" + str(value)+"*"+"x"
    else:
        S_P += "+" + str(value)
S_P += "=0"
S_P=S_P.replace("+1*x","+x").replace("- 1*x","-x").replace("+-"," - ").replace("+"," + ").replace("="," = ")
S_P=S_P[:3].replace(" + ","").replace(" - ","-")+S_P[3:]

# print(S_P)
data = open('fileHomeWork.txt', 'a')
data.write('\n')
data.write('Summa=')
data.write('\n')
data.write(S_P)
data.close()