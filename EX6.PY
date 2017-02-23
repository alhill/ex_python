# http://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

palabra = input ("Introduce una palabra: ")

sinespacioslista = []
for letra in palabra:
    letra = letra.lower()
    if (letra == "á" or letra == "à" or letra == "ä" or letra == "â"):
        letra = "a"
    if (letra == "é" or letra == "è" or letra == "ë" or letra == "ê"):
        letra = "e"
    if (letra == "í" or letra == "ì" or letra == "ï" or letra == "î"):
        letra = "i"
    if (letra == "ó" or letra == "ò" or letra == "ö" or letra == "ô"):
        letra = "o"
    if (letra == "ú" or letra == "ù" or letra == "ü" or letra == "û"):
        letra = "u"
    if (letra != " " and letra != "," and letra != "." and letra != ":" and letra != ";"):
        sinespacioslista.append(letra)
#

print (sinespacioslista)

flag = True
for i in range(len(sinespacioslista)-1):
    print ("{} con {}".format(sinespacioslista[i], sinespacioslista[-(i+1)]))
    if (sinespacioslista[i] != sinespacioslista[-(i+1)]):
        flag = False
        break
#

if flag == True:
    print ("La cadena \"{}\" es un palíndromo".format(palabra))
else:
    print ("La cadena \"{}\" no es un palíndromo".format(palabra))
