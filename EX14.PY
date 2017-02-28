# http://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html

from random import randint

def lista_loop(a):
    sinrepe = []
    for i in a:
        if i not in sinrepe:
            sinrepe.append(i)
    return sinrepe
#

def lista_set(a):
    return set(a)

a = [randint(1,20) for i in range(20)]

print (a)
print (lista_set(a))
print (lista_loop(a))
