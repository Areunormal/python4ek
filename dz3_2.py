x = 0
y = 0
shag = 0
i = 1
print("Твои кординаты (0,0)")
while (i!=0):
    print("Введите сторону")
    print("право, лево, низ, верх или стоп, чтобы остановить программу: ")
    side = str(input())
    if (side == "право"):
        try:
            shag = float(input("Введи расстояние шага: "))
        except ValueError:
            print("Error, введи число")
            shag = 0
        if (shag < 0):
            print("Шаг не может быть отрицательным")
            shag = float(input("Введи расстояние шага: "))
        x+=shag
        print(f"Твои координаты сейчас = {x,y}")
    elif (side =="лево"):
        try:
            shag = float(input("Введи расстояние шага: "))
        except ValueError:
            print("Error, введи число")
            shag = 0
        if (shag < 0):
            print("Шаг не может быть отрицательным")
            shag = float(input("Введи расстояние шага: "))
        x-=shag
        print(f"Твои координаты сейчас -{x,y}")
    elif (side =="низ"):
        try:
            shag = float(input("Введи расстояние шага: "))
        except ValueError:
            print("Error, введи число")
            shag = 0
        if (shag < 0):
            print("Шаг не может быть отрицательным")
            shag = float(input("Введи расстояние шага: "))
        y-=shag
        print(f"Твои координаты сейчас -{x,y}")
    elif (side == "верх"):
        try:
            shag = float(input("Введи расстояние шага: "))
        except ValueError:
            print("Error, введи число")
            shag = 0
        if (shag < 0):
            print("Шаг не может быть отрицательным")
            shag = float(input("Введи расстояние шага: "))
        y+=shag
        print(f"Твои координаты сейчас -{x,y}")
    elif (side == "стоп"):
        i=0
    else:
        print("Введи сторону, как было указано ранее")