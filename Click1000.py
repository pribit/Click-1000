import requests
from bs4 import BeautifulSoup

r = requests.get('http://click1000.training.hackerdom.ru/start')
for i in range(1000):
    soup = BeautifulSoup(r.content, 'html.parser')
    link = soup.find('a').get('href')
    r = requests.get('http://click1000.training.hackerdom.ru/' + link)
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())
