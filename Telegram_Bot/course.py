
from bs4 import BeautifulSoup
import urllib.request


req = urllib.request.urlopen('https://forklog.com/')
html = req.read()


soup = BeautifulSoup(html)
print = (soup)