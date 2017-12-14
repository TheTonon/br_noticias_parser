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
        try:
            title = soup.find('title').get_text()
        except Exception as e:
            print(e)
        for paragrafo in paragrafos:
            texto.append("\n")
            texto.append(paragrafo.get_text())
        return ''.join(texto), title

