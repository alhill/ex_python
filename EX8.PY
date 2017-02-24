# http://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
from random import randint

puntj = puntia = 0
print ("Al primero que gane tres!")

while True:
    while puntj<3 and puntia<3:
        jugador = "inicial"
        while (jugador != "piedra" and jugador != "papel" and jugador != "tijeras" and jugador != "tijera"):
            jugador = input("Un, dos, tres, piedra, papel o tijera! ").lower()
            if (jugador == "piedra"):
                j = 1
                break
            elif (jugador == "papel"):
                j = 2
                break
            elif (jugador == "tijera" or jugador == "tijeras"):
                j = 3
                break
        #

        ia = randint(1,3)
        if (ia == 1):
            iastr = "piedra"
        elif (ia == 2):
            iastr = "papel"
        elif (ia == 3):
            iastr = "tijera"
        else:
            print ("Error inesperado")

        # print("Jugador: {}, IA: {}".format(j, ia))

        if (j == ia):
            print ("Los dos hemos sacado {}, empate!".format(jugador))
        if ((j == 1 and ia == 2) or (j == 2 and ia == 3) or (j == 3 and ia == 1)):
            print ("Yo saqué {}, gané!".format(iastr))
            puntia += 1
        if ((j == 2 and ia == 1) or (j == 3 and ia == 2) or (j == 1 and ia == 3)):
            print ("Yo saqué {}, ganaste...".format(iastr))
            puntj += 1

        if (puntia<3 and puntj<3):
            if (puntia>puntj):
                print("Gano {} a {}!".format(puntia, puntj))
            elif (puntia<puntj):
                print("Vas ganando {} a {}!".format(puntj, puntia))
            else:
                print("Estamos empatados a {}".format(puntia))
        elif(puntia == 3):
            print("He ganado!!")
        elif(puntj == 3):
            print("Has ganado...")
    #

    while True:
        op = input("Otra partida? (s,n): ").lower()
        if (op=="s" or op == "n" or op == "y"):
            break

    if (op == "n"):
        break
    else:
        puntj = 0
        puntia = 0
#
