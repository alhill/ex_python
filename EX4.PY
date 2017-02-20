# http://www.practicepython.org/exercise/2014/02/26/04-divisors.html

print ("Divisores")
print ("-------------------------")
cadena = "Inserte el número que desea"

while True:
    try:
        dividendo = int(input("{} analizar: ".format(cadena)))
        break
    except ValueError:
        cadena = "Inserte un número válido a"
    #
#

divisores = []
for i in range(dividendo-2):
    divisor = dividendo - i - 1
    if (dividendo % divisor == 0):
        divisores.append(divisor)
    #
#

if (len(divisores)==0):
    print ("{} es un número primo.".format(dividendo))
else:
    print ("Los divisores de {} son: ".format(dividendo))
    for i in range(len(divisores)-1):
        print ("{}, ".format(divisores[i]), end="")
    print ("{}.".format(divisores[len(divisores)-1]))
    #
#
