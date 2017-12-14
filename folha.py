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
        try:
            title_tag = soup.find('h1', {'itemprop':'headline'})
            title = title_tag.get_text()
        except Exception as e:
            print(e)
            title = "Folha"
        for paragraph in paragraphs:
            final_text.append("\n")
            final_text.append(paragraph.get_text())
        return ''.join(final_text), title
