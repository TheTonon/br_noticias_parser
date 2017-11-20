# -*-encoding:utf-8-*-

import urllib.request
import re
from bs4 import BeautifulSoup

class r7:
    def parse(html):
        sopa = BeautifulSoup(html, "lxml")
        artigo = sopa.find("article")
        texto_cru = artigo.find_all("p")
        texto = []
        for txt in texto_cru:
            texto.append("\n")
            texto.append(txt.get_text())
        return ''.join(get_texto)

