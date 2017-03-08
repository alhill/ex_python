# http://www.practicepython.org/exercise/2014/07/14/19-decode-a-web-page-two.html

from bs4 import BeautifulSoup
import requests

url = requests.get("http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture")

sopa = BeautifulSoup(url.text, "lxml")
titulo = sopa.find("h1")
subtitulo = titulo.find_next("span")
texto = sopa.find_all("p")
print(titulo.get_text())
print(subtitulo.get_text())
for parrafo in texto:
    try:
        if int(parrafo.attrs["data-reactid"]) < 457:
            print (parrafo.get_text())
    except:
        pass
