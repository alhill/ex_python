# http://www.practicepython.org/exercise/2014/07/14/19-decode-a-web-page-two.html

from bs4 import BeautifulSoup
import requests

url = requests.get("http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture")

sopa = BeautifulSoup(url.text, "lxml")
titulo = sopa.find("h1")
subtitulo = titulo.find_next("span")
texto = sopa.find_all("p")

nombre = input("Introduce el nombre del archivo de salida: ")
with open(nombre, "w") as archivo:
    archivo.write(titulo.get_text() + "\n")
    archivo.write(subtitulo.get_text()  + "\n")
    for parrafo in texto:
        try:
            if int(parrafo.attrs["data-reactid"]) < 457:
                archivo.write (parrafo.get_text()  + "\n")
        except:
            pass
