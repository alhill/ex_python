# http://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html
from random import randint

a = [randint(1,20) for i in range(20)]
b = [randint(1,20) for i in range(20)]

lista = set([elem_a for elem_a in a if elem_a in b]) #LIST COMPREHENSION & SETS
listab = set(a) & set(b) #ONLY SETS
listac_dup = [elem_a for elem_a in a if elem_a in b] #LIST COMPREHENSION & FOR/IF
listac = []
for elem in listac_dup:
    if elem not in listac:
        listac.append(elem)

print (a)
print (b)
print (lista)
print (listab)
print (listac)
