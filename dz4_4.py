import random
nazv_shmotok =["Раж Амбу(доспех)","Величие Азири(доспех)","Прибежище Ирения(доспех)","Колючий панцирь(доспех)","Разбитая корона(шлем)","Венец Титуса(шлем)","Треуголка Могиллана(шлем)","Золотой колпак(шлем)","Башмаки сумерек(обувь)","Скороходы(обувь)","Лапы Львиного глаза(обувь)","Тихоходы Немого ветра(обувь)","Амулет с ониксом(Бижутерия)","Амулет с лазуритом(Бижутерия)","Кольцо с опалом(Бижутерия)","Радужное кольцо(Бижутерия)","Сеятель гибели(двуручный меч)","Затмение Соляриса(жезл)","Стрелы рока(лук)","Кровопускатель(кинжал)"]
inventar=[]
sila = int(input("Введи параметр силы твоего персонажа:"))
print(f"Ваш переносимый вес равен {sila*5} кг")
dost_ves= sila*5
ves=0
flag=1
print("-Фух, ну и сложный босс конечно был, все хилки истратил\n-Да ладно тебе, оно того стоило, собирай дроп, да валим отсюда")
while (flag !=0):
    if len(inventar)==0:
        print("Ваш инвентарь сейчас пуст")
    dost_ves=dost_ves-ves    
    ves = random.randint(1,10)
    vesh=(nazv_shmotok[random.randint(0,19)],f"{ves} kg")
    print(f"{vesh[0]}-{vesh[1]}")
    if (dost_ves>=ves):
        sogl=str(input("Хотите взять данную вещь?(+/-):"))
        if (sogl =="+"):
            inventar.append(vesh)
        elif(sogl=="-"):
            None
        else:
            print("Все действия кроме ввода +/- являются несанкцинонированными , ввиду чего вы  были забанены на данном сервере, удачи)")
            break
        sogl2=str(input("Открыть инвентарь?(+/-):"))
        if (sogl2 =="+"):
            for i in range(len(inventar)):
                print(f"{i+1} ячейка -", inventar[i-1][0],inventar[i-1][1])
        elif(sogl2=="-"):
            None
        else:
            print("Все действия кроме ввода +/- являются несанкцинонированными , ввиду чего вы  были забанены на данном сервере, удачи)")
            break
        sogl3=str(input("Хотите выкинуть какую-то вещь?(+/-):"))
        if (sogl3=="+"):
            a=int(input("Введи номер ячейки, в которой лежит эта вещь:"))
            inventar.pop(a-1)
        elif(sogl3=="-"):
            None
        else:
            print("Все действия кроме ввода +/- являются несанкцинонированными , ввиду чего вы  были забанены на данном сервере, удачи)")
            break
        sogl4=str(input("Налутался, валим?(+/-):"))
        if (sogl4=="+"):
            flag = 0
            print("Ваш спутник открыл портал и перенес вас в ближайжую деревню")
        elif(sogl4=="-"):
            None
        else:
            print("Все действия кроме ввода +/- являются несанкцинонированными , ввиду чего вы  были забанены на данном сервере, удачи)")
            break
    else:
        print("Если вы возьмете эту вещь, то не сможете идти, будет превышен максимальный вес")
        sogl2=str(input("Открыть инвентарь?(+/-):"))
        if (sogl2 =="+"):
            for i in range(len(inventar)):
                print(f"{i+1} ячейка -", inventar[i-1][0],inventar[i-1][1])
        elif(sogl2=="-"):
            None
        else:
            print("Все действия кроме ввода +/- являются несанкцинонированными , ввиду чего вы  были забанены на данном сервере, удачи)")
            break
        sogl3=str(input("Хотите выкинуть какую-то вещь?(+/-):"))
        if (sogl3=="+"):
            a=int(input("Введи номер ячейки, в которой лежит эта вещь:"))
            inventar.pop(a-1)
        elif(sogl3=="-"):
            None
        else:
            print("Все действия кроме ввода +/- являются несанкцинонированными , ввиду чего вы  были забанены на данном сервере, удачи)")
            break
        sogl4=str(input("-Налутался, валим?(+/-):"))
        if (sogl4=="+"):
            flag = 0
            print("Ваш спутник открыл портал и перенес вас в ближайжую деревню")
        elif(sogl4=="-"):
            None
        else:
            print("Все действия кроме ввода +/- являются несанкцинонированными , ввиду чего вы были забанены на данном сервере, удачи)")
            break


