# http://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

from random import randint

while True:
    nint = 0
    numero = randint(1,9)
    print ("Estoy pensando en un número, cual es?")

    while True:
        nint += 1
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

    if (nint == 1):
        print ("Has acertado a la primera!")
    elif (nint == 3):
        print ("Has acertado al 3er intento")
    else:
        print ("Has acertado al {}º intento".format(nint))
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
