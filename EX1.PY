#http://www.practicepython.org/exercise/2014/01/29/01-character-input.html

import time

seguir = True
tener = "Tendrás"

while seguir:
    while True:
        try:
            edad = int(input("Cual es tu edad? "))
        except:
            print ("Introduce un número entero")
            continue
        if (edad>100):
            print ("Dudo que tengas más de 100 años")
            continue
        if (edad==100):
            tener = "Tienes"
            break
        else:
            break
    #

    year = int(time.strftime("%Y"))
    year100 = year + (100 - edad)
    print ("{} 100 años en {}".format(tener, year100))
    sn = " "

    while True:
        flag = input("\nDesea continuar?{}".format(sn))
        if (flag == 'y' or flag == 'Y' or flag == 's' or flag == 'S'):
            seguir = True
            break
        elif (flag == 'n' or flag == 'N'):
            seguir = False
            break
        else:
            sn = " (s, n) "
#
