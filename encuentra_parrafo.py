from bs4 import BeautifulSoup
import requests

url = "https://www.nytimes.com/section/world"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

parrafo = soup.find('p')
print(parrafo.getText())

