# -*-encoding:utf-8-*-

import urllib.request
import re
from bs4 import BeautifulSoup

class g1:
    def parse(html):
        soup = BeautifulSoup(html, "lxml")
        texto_cru = soup.find_all("p", class_=re.compile('^content-text__container'))
        texto = []
        title = soup.find('h1', attrs={'class', 'content-head__title'}).get_text()
        for txt in texto_cru:
            texto.append("\n")
            texto.append(txt.get_text())
        return ''.join(texto), title
