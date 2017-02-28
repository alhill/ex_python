# http://www.practicepython.org/exercise/2014/04/25/12-list-ends.html

def principioFinal(lista):
    listares = [item for item in lista if (item == lista[0] or item == lista[len(lista)-1])]
    return listares

a = [5, 10, 15, 20, 25]
print(a)
print (principioFinal(a))
