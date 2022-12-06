import urllib.request

pagina = urllib.request.urlopen("https://www.gutenberg.org/files/11/11-0.txt")
texto  = pagina.read().decode("utf8")
print(texto[0:1000])