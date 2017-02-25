# http://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html

def pideNumero():
    while True:
        try:
            num = int(input("Inserta un número: "))
            return num
        except ValueError:
            pass
#

def esDivisor(dividendo, divisor):
    if (dividendo % divisor == 0):
        return True
#


num = pideNumero()

primo = True
for i in range(num-2):
    if esDivisor(num, i+2):
        primo = False
        break

if primo and num > 0:
    print("{} es primo".format(num))
else:
    print("{} no es primo".format(num))
