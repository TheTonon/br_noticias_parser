# -*-encoding:utf-8-*-

import urllib.request
import re
from bs4 import BeautifulSoup

class uol:
    def parse(html):
        soup = BeautifulSoup(html, "lxml")
        #div_texto = sopa.find("div", id_=re.compile('^texto'))
        div_texto = soup.find('div', attrs={'id':'texto'})
        paragrafos = div_texto.find_all("p")
        texto = []
        title = soup.find('h1', attrs={'class':re.compile('pg-color[0-9]+')}).get_text()
        for paragrafo in paragrafos:
            texto.append("\n")
            texto.append(paragrafo.get_text())
        return ''.join(texto), title

