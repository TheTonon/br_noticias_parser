 # -*-encoding:utf-8-*-

import urllib.request
import re
from bs4 import BeautifulSoup

class terra:
    def parse(html):
        sopa = BeautifulSoup(html, "lxml")
        div_artigo = sopa.find("div", class_=re.compile('^articleData'))
        paragrafos = div_artigo.find_all('p')
        texto = []
        for paragrafo in paragrafos:
            texto.append('\n')
            texto.append(paragrafo.get_text())
        return ''.join(texto)
