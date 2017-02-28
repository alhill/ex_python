# http://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html

def reverse(cadena):
    lista_cad = cadena.split()
    lista_rev = [ lista_cad[len(lista_cad) - a - 1] for a in range(len(lista_cad)) ]
    return " ".join(lista_rev)
#

cadena = input ("Introduce una cadena, preferiblemente compuesta por varias palabras: ")
cadena_rev = reverse(cadena)
print (cadena_rev)
