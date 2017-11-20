 # -*-encoding:utf-8-*-

import urllib.request
import re
from bs4 import BeautifulSoup

class terra:
    def parse(html):
        sopa = BeautifulSoup(html, "lxml")
        artigo = re.sub('<[/em]*>','', str(sopa.find('div', class_=re.compile('^articleData'))))
        div_artigo = BeautifulSoup(artigo, 'lxml')
        for div in div_artigo.find_all('div', {'class':re.compile('related.*')}):
            print("SEU REGEX TÁ CERTO")
            div.decompose()
        paragrafos = div_artigo.find_all('p')
        texto = []
        for paragrafo in paragrafos:
            #texto.append('\n')
            texto.append(paragrafo.get_text().replace('\n', '').replace('   ', ' ').replace('  ', ' '))
            texto.append('\n')
        return ''.join(texto)
