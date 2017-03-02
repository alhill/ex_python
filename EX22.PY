# http://www.practicepython.org/exercise/2014/12/06/22-read-from-file.html

try:
    f = open("EX22_DATALIST", "r")
except:
    print ("Error en la carga del archivo de datos")

categorias = {}
for linea in f:
    cat = linea.split("/")[2]
    if cat not in categorias:
        categorias[cat] = 1
    else:
        categorias[cat] += 1
#

for a in categorias:
    print("{} -> {}".format(a, categorias[a]))
