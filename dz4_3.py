"""Сравнение двух произвольных наборов чисел"""
import random
nabor1 =set()
nabor2 =set()
"""Задаются произвольные наборы"""
dlina=random.randint(1,20)
for i in range (dlina):
    nabor1.add(random.randint(1,100))
    nabor2.add(random.randint(1,100))
"""Вывод сравнений"""
print("2 randomnix nabora:", nabor1, nabor2)
print ("peresechenie naborov:",nabor1.intersection(nabor2))
print ("est v pervom nabore, no net vo vtorov:",nabor1.difference(nabor2))
print ("est vo vtorom nabore, no net v pervom:",nabor2.difference(nabor1))
print("est v pervom nabore ili vo vtorom, no ne v oba odnovremenno: ")
print (nabor1.symmetric_difference(nabor2))
