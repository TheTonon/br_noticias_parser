# -*-encoding:utf-8-*-

import urllib.request
import re
from bs4 import BeautifulSoup

class uol:
    def parse(html):
        sopa = BeautifulSoup(html, "lxml")
        artigo = sopa.find("article")
        div_texto = sopa.find("div", id_=re.compile('^texto'))
        paragrafos = div_texto.find_all("p")
        texto = []
        for paragrafo in paragrafos:
            texto.append("\n")
            texto.append(paragrafo.get_text())
        return ''.join(texto)

