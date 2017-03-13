# http://www.practicepython.org/exercise/2015/11/01/25-guessing-game-two.html

while True:
    try:
        numero = int(input("Elige un número del 1 al 100: "))
        if 1 <= numero <= 100:
            break
    except ValueError:
        pass

anterior = -1
numero = 50
maxi = 101
mini = 1
intentos = 0
trampa = False

while True:

    intentos += 1
    es = input("¿Es el número {}? (s, n) ".format(numero)).lower()

    if es != "s" and es != "y":
        if (mini == maxi) or (anterior == numero):
            print ("Has hecho trampa!")
            trampa = True
            break
        while True:
            print ("max={} min={}".format(maxi, mini))
            direccion = input("¿Tu número es mayor o menor que el mío? ").lower()
            if direccion == "mayor":
                numdir = 1
                break
            elif direccion == "menor":
                numdir = -1
                break
            else:
                pass

        if numdir == 1:
            mini = numero
        elif numdir == -1:
            maxi = numero
        else:
            print("error")
        anterior = numero
        numero = int((maxi + mini)/2)

    else:
        break

if numero == 1:
    s = ""
else:
    s = "s"

if not trampa:
    print ("Era el {}, lo he acertado en {} intento{}".format(numero, intentos, s))
