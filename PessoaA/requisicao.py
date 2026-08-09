import requests
from bs4 import BeautifulSoup

# Implementação teste de uma requisição e raspagem de dados
pagina = requests.get("https://quotes.toscrape.com/")
dados_pagina = BeautifulSoup(pagina.text, 'html.parser')

textos = dados_pagina.find_all("span", class_="text")

for span in textos:
    print(span.text)