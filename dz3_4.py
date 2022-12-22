import math as m
i =  0
while (i != 1):
    print("Введи коэффициенты a,b,c в твоем уравнении(через пробел): ")
    try:
        a,b,c=map(float,input().split())
    except ValueError:
        print("Error, коэффициенты должны быть числами")
    else:
        i = 1
discr = (b**2-(4*a*c))
print("Дискриминант равен = ",discr)
while (i!=0):
    try:
        koren = m.sqrt(discr)
    except ValueError:
        print("Корней нет")
        break
    x1 = float((-b + koren)/(2*a))
    x2 = float((-b - koren)/(2*a))
    if (discr > 0):
        print("x1 = ",x1)
        print("x2 = ",x2)
        i = 0
    elif (discr == 0):
        print("x = ",x1)
        i = 0
    else:
        None