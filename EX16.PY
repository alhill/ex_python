# http://www.practicepython.org/exercise/2014/05/28/16-password-generator.html

from random import randint

def cogeNum():
    while True:
        try:
            num = int(input("Número de caracteres de la contraseña a generar: "))
            while True:
                if num < 8:
                    op = input("Para ser segura, la contraseña debería ser de al menos 8 caracteres, seguro que desea continuar? (s,n): ").lower()
                    if (op == "s" or op == "y"):
                        break
                    elif op == "n":
                        num = int(input("Número de caracteres de la contraseña a generar: "))
                    else:
                        pass
                else:
                    break
            #
            break
        except ValueError:
            print ("Valor incorrecto, introduzca un número entero")
    #
    return num
#

def generaContra(num):
    mayus = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    minus = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    simbo = ["|", "@", "#", "~", "€", "¬", "{", "!", "}", "<", "$", "%", "&", "/", "(", ")", "=", ",", "º", "¡", "_", ";", ">", "^", "¿", "?"]
    caracteres = [mayus, minus, simbo, range(0,10)]

    pw = []
    for n in range(num):
        tipo = randint(0,3)
        if tipo == 3:
            caracter = randint(0,9)
        else:
            caracter = randint(0,25)
        pw.append(str(caracteres[tipo][caracter]))
    return "".join(pw)
#

print ("Generador de contraseñas")
num = cogeNum()
contra = generaContra(num)
print (contra)
