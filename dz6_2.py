molekuli = open("input.txt")
array = molekuli.readlines()
kolvoC = int(array[0])
kolvoH = int(array[1])
kolvoO = int(array[2])
kolvomolekul=0
while kolvoC >=2 and kolvoH >=6 and kolvoO >=1:
    kolvoC -=2
    kolvoH-=6
    kolvoO-=1
    kolvomolekul+=1
kolvospirta=open("output.txt","w")
kolvospirta.write(str(kolvomolekul))
kolvospirta.close()
molekuli.close()
