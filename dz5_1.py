parol=str(input("Введите пароль: "))
def passwd(parol):
    """Proverka parolya
    
    Na dlinu, nalichie cifr i nalichie slova password
    
    """
    kolvo = 0
    flag = 0
    if len(parol)<6:
        flag+=1
    for i in parol:
        if i=="0" or i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9":
            kolvo +=1
    if kolvo == 0 or kolvo == len(parol):
        flag+=1
    if "password" in parol.lower():
        flag+=1
    if flag>0:
        return False
    else:
        return True
if passwd(parol)==False:
    print("Ваш пароль не подходит")
else:
    print("Ваш пароль подходит")