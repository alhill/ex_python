# http://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html

from random import randint

if __name__=="__main__":
    cifra0 = str(randint(0,9))
    cifra1 = str(randint(0,9))
    cifra2 = str(randint(0,9))
    cifra3 = str(randint(0,9))
    numero = cifra0 + cifra1 + cifra2 + cifra3

    num = 0

    while True:
        num += 1
        while True:
            try:
                intento = input("Introduce cuatro cifras del 0 al 9 (p.ej: 0123): ")
                acert = 0
                descolocado = 0
                if ((len(intento) == 4 and int(intento)) or intento=="0000"):
                    break
            except ValueError:
                pass

        for i in range(4):
            if intento[i] in numero:
                if intento[i] == numero[i]:
                    acert += 1
                else:
                    descolocado += 1

        if (acert == 4):
            break
        else:
            if (acert == 1):
                s = ""
            else:
                s = "s"
            print ("Hay {} cifra{} en su sitio y {} fuera de su sitio".format(acert, s, descolocado))
    #

    if (num == 1):
        s = ""
    else:
        s = "s"

    print ("Has acertado! El numero era el {} y lo has acertado en {} intento{}".format(numero, num, s))
