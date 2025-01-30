from bs4 import BeautifulSoup
import requests

url = "https://www.nytimes.com/section/world"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

enlaces = soup.select('a')

for enlace in enlaces:
    print(enlace.get('href'))