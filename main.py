# -*-encoding:utf-8-*-
import urllib.request
import re
from g1 import g1
from r7 import r7

lista_sites = ["g1.globo.com", 'r7.com', "uol.com.br", "terra.com.br", "brasil247.com.br"]

def testing():
    noticia = urllib.request.urlopen("https://g1.globo.com/sao-paulo/noticia/doria-cria-nova-secretaria-para-acomodar-bruno-covas-apos-vice-prefeito-deixar-comando-da-zeladoria.ghtml")
    sopa = BeautifulSoup(noticia, "lxml")
    texto = sopa.find_all("p", class_=re.compile('^content-text__container'))
    for txt in texto:
        print (txt.get_text())

def is_url(url):
    if url.startswith("http://") or url.startswith("https://"):
        return True
    else:
        return False

def get_site_name(url):
    contador_site_atual = 0
    for site in lista_sites:
        print ("{0}".format(site))
        busca = re.compile("{0}".format(site))
        if busca.search(url):
            print ("fechou")
            if contador_site_atual == 0:
                html = get_html(url)
                return (g1.parse(html))
            if contador_site_atual == 1:
                html = get_html(url)
                return (r7.parse(html))
            break
        else:
            contador_site_atual = contador_site_atual + 1
            print ("Xabu")

def get_html(url):
    if is_url(url):
        return urllib.request.urlopen(url)
    else:
        return "url invalida"

def parse_g1(noticia_url):
    noticia_html = get_html(noticia_url)
    sopa = BeautifulSoup(noticia_html, "lxml")
    texto_cru = sopa.find_all("p", class_=re.compile('^content-text__container'))
    texto = ""
    for txt in texto_cru:
        print (txt.get_text())
        texto.join("\n")
        texto.join(txt.get_text())
    return texto

def parse_r7(noticia_url):
    noticia_html = get_html(noticia_url)
    sopa = BeautifulSoup(noticia_html, "lxml")
    artigo = sopa.find("article")
    texto_cru = artigo.find_all("p")
    texto = ""
    for txt in texto_cru:
        print (txt.get_text())
        texto.join("\n")
        texto.join(txt.get_text())
    return texto

print(g1.__dict__)
print(get_site_name("https://g1.globo.com/sao-paulo/noticia/radares-de-aeroportos-nao-detectam-drones-segundo-aeronautica.ghtml"))
