import requests
from bs4 import BeautifulSoup

respons = requests.get("https://www.ceneo.pl/71299209#tab=reviews")

page_dom = BeautifulSoup(respons.text, "html.parser")

print(page_dom.prettify())