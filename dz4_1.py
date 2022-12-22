chisla=[]
while True:
    dobavit  = str(input("Dobavit' chislo?(+/-): "))
    if dobavit == "-":
        break
    elif dobavit =="+":
        try:
            chislo = float(input("Vvedi chislo dlya massiva: "))
            chisla.append(chislo)
        except ValueError:
            print("Error, vvedi chislo: ")
    else:
        print("Error, vvedi + ili -")

for i in range(len(chisla)-1):
    for j in range  (len(chisla)-i-1):
        if chisla[j] > chisla [j+1]:
            a = chisla[j]
            b = chisla[j+1]
            chisla[j] = b
            chisla[j+1] = a
        else:
            None 
print(chisla)
