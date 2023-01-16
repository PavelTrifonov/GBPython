# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc
text1="aaaaabbbccccsfgg"
data = open('file.txt', 'w')
data.writelines(text1) 
data.close()

text2=[]
while len(text1)+1>1:
    if len(text1)==1:
        text2.append(str(1)+text1[0])
        text1=""
        break
    for i in range(1,len(text1)):
        if text1[i]!=text1[i-1]:
            text2.append(str(i)+text1[i-1])
            text1=text1[i:]
            break
        if i+1==len(text1):
            text2.append(str(len(text1))+text1[i-1])
            text1=""
            break
text2="".join(text2)
print(text2)
data = open('file.txt', 'w')
data.writelines(text2) 
data = open('file.txt', 'r')
text3 = str(data.read())
text1=[]
while len(text3)+1>1:
    for i in range(len(text3)):
        if text3[i].isdigit():
            continue
        else:
            text1.append(int(text3[:i])*text3[i])
            text3=text3[i+1:]
            break
text1="".join(text1)
data = open('newfile.txt', 'w')
data.writelines(text1) 
data.close()
print(text1)
print(text3)