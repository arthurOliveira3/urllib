import urllib.request
import time

def preco():
    pagina = urllib.request.urlopen("http://beans.itcarlow.ie/prices.html")
    texto  = pagina.read().decode("utf8")
    onde  =  texto.find(">$")
    inicio  = onde + 2
    fim  = inicio + 4
    preco  = texto[inicio:fim]
    preco = float(preco)
    return preco


def precoEspecial():
    pagina = urllib.request.urlopen("http://beans.itcarlow.ie/prices-loyalty.html")
    texto  = pagina.read().decode("utf8")
    onde  =  texto.find(">$")
    inicio  = onde + 2
    fim  = inicio + 4
    preco  = texto[inicio:fim]
    preco = float(preco)
    return preco

espera = 15
for n in range(10):
    if precoEspecial() < 4.70:
        preco = precoEspecial()
        print('Comprar! Preço: %5.2f' %preco)
        time.sleep(espera)
    else:
        preco = precoEspecial()
        print('Espere! Preço: %5.2f' %preco)
        time.sleep(espera)