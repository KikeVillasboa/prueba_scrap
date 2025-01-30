from bs4 import BeautifulSoup
import requests

#url = "https://www.nytimes.com/"
url = "https://www.nytimes.com/section/world"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

title = soup.select('title')
print(title[0].getText())