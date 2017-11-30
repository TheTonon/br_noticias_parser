# -*-encoding:utf-8-*-

import requests
import re
from bs4 import BeautifulSoup

class elpais:
    def parse(html):
        soup = BeautifulSoup(html, "lxml")
        intro = soup.find('div', attrs={'id':'articulo-introduccion'})
        intro_paragraph = intro.find_all("p")
        content = soup.find('div', attrs={'id':'articulo_contenedor'})
        content_paragraphs = content.find_all("p")
        text = []
        for paragraph in content_paragraphs:
            text.append(paragraph.get_text())
            text.append('\n')
        for paragraph in intro_paragraph:
            text.append(paragraph.get_text())
            text.append('\n')
        return ''.join(text)

    def get_article(url):
        response = requests.get(url)
        article = elpais.parse(response.text)
        print(article)
        return article
