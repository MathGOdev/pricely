import cloudscraper
import json
from datetime import date
import re
from bs4 import BeautifulSoup

# Extração do texto brito usando seletores HTML combinados
URL = "https://www.amazon.com.br/Notebook-Aspire-AG15-71P-76Z8-Intel-gera%C3%A7%C3%A3o/dp/B0B8Z8B75C"
try:
    scraper = cloudscraper.create_scraper()
    pagina = scraper.get(URL)

    if pagina.status_code == 200:
        dados_pagina = BeautifulSoup(pagina.text, 'html.parser')
 
    textos = dados_pagina.find_all("div", class_="a-section a-spacing-none aok-align-center aok-relative")

    if not textos:
        raise ValueError("Não foi possível encontrar o preço. Layout alterado.")
    
    for tag in textos:
        preco_bruto = tag.find("span", class_="a-price aok-align-center reinventPricePriceToPayMargin priceToPay apex-pricetopay-value").text

    # Limpeza do valor e conversão para float
    substituicoes = {
        'R': '',
        '$': '',
        '.': '',
        ',': '.'
    }

    preco_limpo = float(re.sub(r'[R\$.,]', lambda m: substituicoes[m.group(0)], preco_bruto))
    data_atual = str(date.today())

    dados = {
        "produto": "Notebook Acer Aspire 15 Go",
        "preco": preco_limpo,
        "data_coleta" : data_atual
    }

    with open("dados.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

except ValueError as e:
    print(f'Falha na raspagem de dados: {e}')
except Exception as e:
    print(f'Falha ao buscar a URL: {e}')
