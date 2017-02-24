# http://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

from random import randint

while True:
    numero = randint(1,9)
    print ("Estoy pensando en un número, cual es?")

    while True:
        while True:
            try:
                intento = int(input("Inserta un número entre el 1 y el 9: "))
                break
            except ValueError:
                pass
            #
        #

        if (numero == intento):
            print ("Has acertado!!")
            break
        elif (numero > intento):
            print ("Demasiado bajo...")
        else:
            print ("Demasiado alto...")
    #

    while True:
        op = input("Quieres volver a jugar? (s, n): ").lower()
        if (op == "s" or op == "y"):
            salir = False
            break
        elif (op == "n"):
            salir = True
            break
        else:
            pass
    #

    if (salir == True):
        break

#
