# http://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html

def crearVacia(num, tabla):
    for i in range(num):
        tabla.append(" ")
    return tabla

def crearCuadriculaCustom(filas, columnas, datos=[]):
    crearVacia(filas*columnas, datos)
    for i in range((filas*2)+1):
        if (i%2 == 0):
            for j in range(columnas):
                print (" ---", end="")
        else:
            for j in range(columnas):
                print ("| {} ".format(datos[int((i-1)/2)+j]), end="")
            print ("|", end="")
        print()

while True:
    salir = True
    try:
        filas = int(input("Introduce el número de filas: "))
    except ValueError:
        salir = False
    try:
        columnas = int(input("Introduce el número de columnas: "))
    except ValueError:
        salir = False
    if (filas <= 0 or columnas <= 0):
        print("Los números de filas y columnas tienen que ser positivos y distintos de 0")
        salir = False
    if salir:
        break

crearCuadriculaCustom(filas, columnas)
