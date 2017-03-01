# http://www.practicepython.org/exercise/2014/05/28/16-password-generator.html

from random import randint
import string

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

def generaContraNum(num, grupo):
    caracteres = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]
    pw = []
    for n in range(num):
        tipo = randint(0, grupo)
        caracter = randint(0,len(caracteres[tipo])-1)
        pw.append(str(caracteres[tipo][caracter]))
    return "".join(pw)
#

def cogeCmplx():
    print("\n1 - Dos palabras, CamelCase\n2 - 8 caracteres, mayúsculas y minúsculas\n3 - 10 caracteres, mayúsculas, minúsculas y cifras\n4 - 15 caracteres, mayúsculas, minúsculas, cifras y símbolos\n")
    while True:
        try:
            op = int(input("Escoge la complejidad de la contraseña (1-4): "))
            if 0<op<5:
                break
            else:
                print ("Introduce valores entre 1 y 4")
        except ValueError:
            print ("Introduce valores entre 1 y 4")
    return op
#

def contraPalabras():
    listado = open("EX16_WORDLIST", "r", encoding='utf-8', errors="ignore")
    #print("{} {}".format(aleat1, aleat2))
    contra = ""
    npal = 0
    aleat1 = randint(0,80383)
    aleat2 = randint(0,80383)
    for i, linea in enumerate(listado):
        if i == aleat1:
            #print("{} {}".format(i, linea))
            linea = linea.rstrip("\n")
            contra += linea.capitalize()
        elif i == aleat2:
            #print("{} {}".format(i, linea))
            linea = linea.rstrip("\n")
            contra += linea.capitalize()
            #
        #
    #

    return contra
    #
#

def generaContraCmplx(cmplx):
    caracteres = [string.ascii_lowercase, string.ascii_uppercase, string.punctuation, string.digits]
    pw = []
    for n in range(num):
        tipo = randint(0,3)
        caracter = randint(0,len(caracteres[tipo])-1)
        pw.append(str(caracteres[tipo][caracter]))
    return "".join(pw)
#

print ("Generador de contraseñas")
while True:
    try:
        opc = input("1 - Generar por nivel de complejidad\n2 - Generar por número de caracteres\n")
        if (opc == "1" or opc == "2"):
            break
        else:
            print("Escoja una opción correcta")
    except ValueError:
        print("Escoja una opción correcta")
#

if opc == "1":
    cmplx = cogeCmplx()
    if cmplx == 1:
        contra = contraPalabras()
        contra1 = contraPalabras()
        contra2 = contraPalabras()
    elif cmplx == 2:
        contra = generaContraNum(8, 1)
        contra1 = generaContraNum(8, 1)
        contra2 = generaContraNum(8, 1)
    elif cmplx == 3:
        contra = generaContraNum(10, 2)
        contra1 = generaContraNum(10, 2)
        contra2 = generaContraNum(10, 2)
    elif cmplx == 4:
        contra = generaContraNum(15, 3)
        contra1 = generaContraNum(15, 3)
        contra2 = generaContraNum(15, 3)
    #contra = generaContraCmplx(cmplx)
elif opc == "2":
    num = cogeNum()
    contra = generaContraNum(num, 3)
    contra1 = generaContraNum(num, 3)
    contra2 = generaContraNum(num, 3)
#

print (contra)
print (contra1)
print (contra2)
