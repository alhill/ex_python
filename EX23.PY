# http://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html

with open("EX23_DATA1", "r") as arch1:
    lista1 = [int(dato) for dato in arch1]

with open("EX23_DATA2", "r") as arch2:
    lista2 = [int(dato) for dato in arch2]

# concordancias = [a for a in lista1 for b in lista2 if a == b]

concordancias = [a for a in lista1 if a in lista2]
print(concordancias)
