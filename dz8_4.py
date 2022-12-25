from time import ctime
import timeit
import time
def decorator1(func): 
    def dec_log():
        x = open("log.txt","w")
        x.write(f"Programm starts at {ctime()}")
        func()
        x.write(f", Programm ends at {ctime()}")
    return(dec_log())
def decorator2(func):
    def dec_time():
        vremya1 = time.time()
        func()
        vremya2 = time.time()
        print(f"Programm needs {vremya2-vremya1} seconds to end")
    return dec_time()
def decorator3(func):
    def dec_vremya_isp():
        func()
        print("Did it? Go rest for a while now")
        time.sleep(10)
    return dec_vremya_isp()
def func():
    print("WASSSUUUUUUP")
    print("Ooohh, sry dude, it was rly loud")
    print("Bye :D")
    return True