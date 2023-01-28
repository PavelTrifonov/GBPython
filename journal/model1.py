path=""
journal={}
def open_journal(numb:str):
    global path
    global journal
    path=f"journal\{numb}.txt"
    with open(path, 'r',encoding="UTF-8") as file:
        input = file.readlines()
        for i in input:
            predm = i[:i.index(':')]
            chlds = {j.split(':')[0]: j.split(':')[1].strip().split(',')
                     for j in i[i.index(':')+1:].split(';')}
            journal[predm] = chlds
    return journal
def append_bal(key1,key2,key3,el):
    var=key1[key2][key3]
    var.append(el)
    return var
def save_journal(numb:str):
    global path
    global journal
    path=f"journal\{numb}.txt"
    with open(path,"w",encoding="UTF-8") as file:
        for k,v in journal.items():
            var=list(i+":"+",".join(j) for i,j in v.items())
            var=";".join(var)
            file.write("".join(f"{k}:{var}\n"))