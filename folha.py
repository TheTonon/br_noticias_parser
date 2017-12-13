# -*-encoding:utf-8-*-

import urllib.request
import re
from bs4 import BeautifulSoup

class folha:
    def parse(html):
        soup = BeautifulSoup(html, "lxml")
        article = soup.find('article',{'id':'news'})
        content = article.find('div',{'class':'content'})
        paragraphs = content.find_all('p')
        final_text = []
        title = soup.find('h1', atrrs={'itemprop':'headline'}).get_text()
        for paragraph in paragraphs:
            final_text.append("\n")
            final_text.append(paragraph.get_text())
        return ''.join(final_text), title
