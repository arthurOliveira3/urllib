import urllib.request
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def preco():
    pagina = urllib.request.urlopen("http://beans.itcarlow.ie/prices.html")
    texto  = pagina.read().decode("utf8")
    onde  =  texto.find(">$")
    inicio  = onde + 2
    fim  = inicio + 4
    preco  = texto[inicio:fim]
    preco = float(preco)
    return preco


def preco_especial():
    pagina = urllib.request.urlopen("http://beans.itcarlow.ie/prices-loyalty.html")
    texto  = pagina.read().decode("utf8")
    onde  =  texto.find(">$")
    inicio  = onde + 2
    fim  = inicio + 4
    preco  = texto[inicio:fim]
    preco = float(preco)
    return preco


def envia_email(preco):
    email_google = ''
    senha_google = 'dxxzbjgcgewbvpwr'

    remetente = email_google
    destinatario = 'INSIRA O EMAIL DO DESTINATARIO'

    mensagem = MIMEMultipart()
    mensagem['Subject'] = 'Compre o café'
    mensagem['From'] = remetente
    mensagem['To'] = destinatario
    body = f"Você deve comprar o café IMEDIATAMENTE o preço atual é de: {preco}"
    mensagem.attach(MIMEText(body, 'html'))

    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(email_google, senha_google)
        smtp_server.sendmail(remetente, destinatario, str(mensagem))
        smtp_server.close()
        print ("E-mail enviado com sucesso!!")
    except Exception as ex:
        print ("Algo deu errado...",ex)


def main():    
    espera = 15
    for n in range(10):
        if preco_especial() < 4.7:
            preco = preco_especial()
            print(f'Comprar! Preço: {preco}')
            preco = str(preco)
            envia_email(preco)
            time.sleep(espera)
        else:
            preco = preco_especial()
            print(f'Espere! Preço: {preco}')
            time.sleep(espera)

   
main()