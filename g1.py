# -*-encoding:utf-8-*-

import urllib.request
import re
from bs4 import BeautifulSoup
class g1:
    def parse(html):
        sopa = BeautifulSoup(html, "lxml")
        texto_cru = sopa.find_all("p", class_=re.compile('^content-text__container'))
        texto = []
        for txt in texto_cru:
            texto.append("\n")
            texto.append(txt.get_text())
        return ''.join(texto)
