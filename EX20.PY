# http://www.practicepython.org/exercise/2014/11/11/20-element-search.html
from random import randint

def cogeNum():
    while True:
        try:
            num = int(input("Escoge un número del 0 al 100: "))
            if 0<=num<=100:
                break
        except:
            pass
    return num
#

def estaDentroDe(num, lista):
    if num in lista:
        return True
    else:
        return False
#

a = set(randint(0, 100) for n in range(50))

num = cogeNum()
esta = estaDentroDe(num, a)
print(a)

if esta:
    print("{} está en la lista".format(num))
else:
    print("{} no está en la lista".format(num))
