import cmath as cm
i = 0
while (i != 1):
    try:
        a,b,c=map(complex,input("Введи коэффициенты a,b,c в твоем уравнении(через пробел): ").split())
    except ValueError:
        print("Error, коэффициенты должны быть числами")
    else:
        i = 1
discr = (b.real**2-(4*a.real*c.real))
print("Дискриминант равен = ",discr)
koren = complex(cm.sqrt(discr))
x1 = complex((-b + koren)/(2*a))
x2 = complex((-b - koren)/(2*a))
if ( discr > 0):
    print("x1 = ", x1.real)
    print("x2 = ", x2.real)
elif (discr == 0):
    print("x = ", x1.real)
else:
    print("x1 = ", x1)
    print("x2 = ", x2)

