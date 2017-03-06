# http://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html

import requests
from bs4 import BeautifulSoup

req = requests.get("http://www.eldiario.es/")
sopa = BeautifulSoup(req.text, "lxml")

titus = sopa.find_all('', { 'class': 'headline' })
for titu in titus:
    for elem in titu:
        try:
            if (elem.a):
                print(elem.a.attrs['title'])
            elif(elem):
                print(elem.attrs['title'])
        except:
            pass

titusopi = sopa.find_all('a', { 'class': 'headline' })
for b in titusopi:
    print (b.string.strip())
