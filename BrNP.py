# -*-encoding:utf-8-*-
import sys
sys.path.append('br_noticias_parser/')
import requests
import urllib.request
import re
from g1 import g1
from r7 import r7
from terra import terra
from uol import uol
from folha import folha
from elpais import elpais
from exame import exame

lista_sites = ["folha.uol.com.br",
               "g1.globo.com",
               "r7.com",
               "uol.com.br",
               "terra.com.br",
               "brasil.elpais.com",
               "exame.abril.com.br"]

parsers = [folha.parse,
           g1.parse,
           r7.parse,
           uol.parse,
           terra.parse,
           elpais.parse,
           exame.parse]

def is_url(url):
    if url.startswith("http://") or url.startswith("https://"):
        return True
    else:
        if url.startswith("http:/"):
            new_url = str(url).replace('http:/', 'http://')
        if url.startswith("https:/"):
            new_url = str(url).replace('https:/', 'https://')
        return False

def get_noticia(url):
    site_counter = 0
    html = get_html(url)
    for site in lista_sites:
        busca = re.compile("{0}".format(site))
        if busca.search(url):
            content, title = parsers[site_counter](html)
            return content, site, title
        else:
            site_counter = site_counter + 1
    return None 

def get_html(url):
    if is_url(url):
        r = requests.get(url)
        return r.text
    else:
        return "url invalida"
