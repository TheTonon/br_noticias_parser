# -*-encoding:utf-8-*-

import requests
import re
from bs4 import BeautifulSoup

class exame:
    def parse(html):
        soup = BeautifulSoup(html, "lxml")
        section = soup.find('section', attrs={'class':'article-content'})
        content = section.find_all('p')
        text = []
        title = soup.find('h1', attrs={'class':'article-title'}).get_text()
        for paragraph in content:
            text.append(paragraph.get_text())
            text.append('\n')
        return ''.join(text), title

    def get_article(url):
        response = requests.get(url)
        article = exame.parse(response.text)
        print(article)
        return article
