import random
nazv_shmotok =["Раж Амбу(доспех)","Величие Азири(доспех)",
               "Прибежище Ирения(доспех)","Колючий панцирь(доспех)",
               "Разбитая корона(шлем)","Венец Титуса(шлем)",
               "Треуголка Могиллана(шлем)",
               "Золотой колпак(шлем)","Башмаки сумерек(обувь)",
               "Скороходы(обувь)","Лапы Львиного глаза(обувь)",
               "Тихоходы Немого ветра(обувь)","Амулет с ониксом(Бижутерия)",
               "Амулет с лазуритом(Бижутерия)","Кольцо с опалом(Бижутерия)",
               "Радужное кольцо(Бижутерия)","Сеятель гибели(двуручный меч)",
               "Затмение Соляриса(жезл)","Стрелы рока(лук)",
               "Кровопускатель(кинжал)"]
inventar=[]
flagminus1=0
while flagminus1==0:
    try:
        sila = int(input("Введи параметр силы твоего персонажа:"))
        flagminus1=1
    except ValueError:
        print("Введи число")
print(f"Ваш переносимый вес равен {sila*5} кг")
dost_ves= sila*5
maxves=sila*5
ves=0
flag=1
flag2=0
flag3=0
flag5=0
b=0
print("-Фух, ну и сложный босс конечно был, все хилки истратил")
print("-Да ладно тебе, оно того стоило, собирай дроп, да валим отсюда")
while (flag !=0):
    if len(inventar)==0:
        print("Ваш инвентарь сейчас пуст")
    print("Что делаем?(лутать, посмотреть инвентарь, выкинуть вещь, уйти): ")
    sogl=str(input())
    if (sogl =="лутать"):
        flag2 = 0
        while flag2 == 0:    
            ves = random.randint(1,10)
            vesh=(nazv_shmotok[random.randint(0,19)],ves )
            print(f"{vesh[0]}-{vesh[1]}")
            if (ves>maxves):
                print("Шмотка слишком тяжелая, не потянешь")
                sogl2="-"
            else:
                sogl2 =str(input("Берешь шмотку?(+/-/хватит):"))
            if (sogl2 =="+" and dost_ves>=ves):
                    inventar.append(vesh)
                    dost_ves=dost_ves-ves
            elif (sogl2 =="+" and dost_ves<ves):
                print("Не хватает места")
                print(sila*5,"- твой переносимый вес" )
                sogl4=str(input("Хочешь выкинуть что-нибудь?(+/-): "))
                flag3=0
                if sogl4=="+":
                    while flag3==0:
                        for i in range(len(inventar)):
                            print(f"{i+1} ячейка -", inventar[i-1][0],inventar[i-1][1], "кг")
                        print("Введи номер ячейки, в которой лежит эта вещь(назад, чтобы отменить):")    
                        sogl3=str(input())
                        try:
                            b = int(sogl3)
                            dost_ves+= inventar[b-1][1]
                            inventar.pop(b-1)
                        except ValueError:
                            if sogl3=="назад":
                                flag3+=1
                            else:
                                print("Введи назад, чтобы вернуться или номер ячейки, чтобы выкинуть шмотку")
                        except IndexError:
                            print("Больше нечего удалять")
                        if  dost_ves>=ves:
                            sogl5=str(input("Места хватает, хочешь забрать шмотку?:(+/-):"))
                            if (sogl5 =="+"):
                                inventar.append(vesh)
                                flag3+=1
                            elif(sogl5=="-"):
                                flag3+=1
                            else:
                                print("Научись читать!")

            elif(sogl2=="-"):
                None
            elif(sogl2=="хватит"):
                flag2+=1
            else:
                print("Все действия кроме ввода +/-/хватит являются несанкцинонированными")
                break        
    elif (sogl =="посмотреть инвентарь"):
        for i in range(len(inventar)):
            print(f"{i+1} ячейка -", inventar[i-1][0],inventar[i-1][1],"кг")
    elif (sogl=="выкинуть вещь"):
        flag5=0
        while flag5==0:
            for i in range(len(inventar)):
                print(f"{i+1} ячейка -", inventar[i-1][0],inventar[i-1][1],"кг")
            print("Введи номер ячейки, в которой лежит эта вещь(назад, отменить):")
            sogl3=str(input())
            try:
                b = int(sogl3)
                inventar.pop(b-1)
            except ValueError:
                if sogl3=="назад":
                    flag5+=1
                else:
                    print("Введи назад, чтобы вернуться или номер ячейки, чтобы выкинуть шмотку")
            except IndexError:
                print("Нечего выкидывать")
                flag5+=1
    elif (sogl=="уйти"):
        flag = 0
        print("Ваш спутник открыл портал и перенес вас в ближайжую деревню")
    else:
        print("Админ разочарован тем, что ты не умеешь читать, ты забанен")
        break



