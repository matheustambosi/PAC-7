import requests
from bs4 import BeautifulSoup

# faz a requisição da página web
page = requests.get("https://www.vivareal.com.br/venda/santa-catarina/joinville/apartamento_residencial")

# analisa a página com o BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

items = soup.find_all(class_='property-card__container')

# extrai o título, preço e endereço de cada item e imprime na tela
for item in items:
    title = item.find(class_='property-card__title').get_text().strip()
    price = item.find(class_='property-card__price').get_text().strip()
    address = item.find(class_='property-card__address').get_text().strip()
    print(f"Nome: {title}\nPreço: {price}\nEndereço: {address}\n")