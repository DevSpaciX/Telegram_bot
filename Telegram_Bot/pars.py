
import requests
from bs4 import BeautifulSoup as BS


r = requests.get('https://www.google.com/finance/quote/USD-UAH?hl=ru')
e = requests.get('https://www.google.com/finance/quote/EUR-UAH?hl=ru')
b = requests.get('https://www.google.com/finance/quote/BTC-USD?hl=ru')
l = requests.get('https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D0%B5%D0%B2/10-%D0%B4%D0%BD%D0%B5%D0%B9')
k = requests.get('https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BB%D1%8C%D0%B2%D0%BE%D0%B2/10-%D0%B4%D0%BD%D0%B5%D0%B9')
g = requests.get('https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%83%D0%BA%D1%80%D0%B0%D0%B8%D0%BD%D0%BA%D0%B0-303027377/10-%D0%B4%D0%BD%D0%B5%D0%B9')
html = BS(r.content,'html.parser')
html1 = BS(e.content,'html.parser')
html2 = BS(b.content,'html.parser')
html3 = BS(l.content,'html.parser')
html4 = BS(k.content,'html.parser')
html5 = BS(g.content,'html.parser')
usd = html.find('div', class_='P6K39c').get_text(strip=True)
eur = html1.find('div', class_='YMlKec fxKbKc').get_text(strip=True)
btc = html2.find('div', class_='YMlKec fxKbKc').get_text(strip=True)
kyiv = html3.find('div', class_='description').get_text(strip=True)
lviv = html4.find('div', class_='description').get_text(strip=True)
ukr = html5.find('div', class_='description').get_text(strip=True)



