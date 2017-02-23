# http://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

from random import randint

def estaDentroDe(num, lista):
    for i in lista:
        if (i == num):
            return True

a = []
b = []
res = []

for i in range(20): #GENERAR DOS LISTAS ALEATORIAS
    numa = randint(0,20)
    numb = randint(0,20)
    a.append(numa)
    b.append(numb)
#
a.sort()
b.sort()

for i in range(20): #RECORRER LAS DOS LISTAS EN BUSCA DE REPETICIONES
    repe = False
    for j in range(20):
        #repe = False
        if(a[i] == b[j]):
            if (not estaDentroDe(a[i],res)):
                res.append(a[i])
#
res.sort()

print (a)
print (b)
print (res)
