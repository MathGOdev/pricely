import cloudscraper
from bs4 import BeautifulSoup


URL = "https://www.amazon.com.br/Notebook-Aspire-AG15-71P-76Z8-Intel-gera%C3%A7%C3%A3o/dp/B0B8Z8B75C"
scraper = cloudscraper.create_scraper()
pagina = scraper.get(URL)

dados_pagina = BeautifulSoup(pagina.text, 'html.parser')

textos = dados_pagina.find_all("div", class_="a-section a-spacing-none aok-align-center aok-relative")

for tag in textos:
    preco_real = tag.find("span", class_="a-price-whole").text
    preco_centavos = tag.find("span", class_="a-price-fraction").text

   
print(preco_real)
print(preco_centavos)