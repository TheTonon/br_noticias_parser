# -*-encoding:utf-8-*-

from bs4 import BeautifulSoup
import urllib.request
import re
def testing():
    noticia = urllib.request.urlopen("https://g1.globo.com/sao-paulo/noticia/doria-cria-nova-secretaria-para-acomodar-bruno-covas-apos-vice-prefeito-deixar-comando-da-zeladoria.ghtml")
    sopa = BeautifulSoup(noticia, "lxml")
    texto = sopa.find_all("p", class_=re.compile('^content-text__container'))
    for txt in texto:
        print (txt.get_text())

def get_html(url):
    return urllib.request.urlopen(url)

def parse_g1(g1_url):
    noticia_html = get_html(noticia_url)
    sopa = BeautifulSoup(noticia_html, "lxml")
    texto_cru = sopa.find_all("p", class_=re.compile('^content-text__container'))
    texto = ""
    for txt in texto_cru:
        texto.join("\n")
        texto.join(txt)
    return texto


