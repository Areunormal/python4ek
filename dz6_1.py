arraystrok = ["Privet", "Darova","Zdravstvui","Hi","Hello","Sup"]
baity=[]
def perevod():
    for i in range (0,len(arraystrok)-1):
        baity.append(bytes(arraystrok[i], encoding="utf-8"))
    print (baity)
perevod()