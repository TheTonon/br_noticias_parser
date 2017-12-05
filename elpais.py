# -*-encoding:utf-8-*-

import requests
import re
from bs4 import BeautifulSoup

class elpais:
    def parse(html):
        soup = BeautifulSoup(html, "lxml")
        try:
            intro = soup.find('div', attrs={'id':'articulo-introduccion'})
            intro_paragraph = intro.find_all("p")
        except:
            pass
        try:
            content = soup.find('div', attrs={'id':'articulo_contenedor'})
            content_paragraphs = content.find_all("p")
        except:
            pass
        text = []
        if content_paragraphs:
            for paragraph in content_paragraphs:
                text.append('\t' + paragraph.get_text())
                text.append('\n')
        if intro_paragraph:
            for paragraph in intro_paragraph:
                text.append('\t' + paragraph.get_text())
                text.append('\n')
        return ''.join(text)

    def get_article(url):
        response = requests.get(url)
        article = elpais.parse(response.text)
        print(article)
        return article
