from bs4 import BeautifulSoup
import requests

url = "https://developer.mozilla.org/es/docs/Learn_web_development/Core/Structuring_content/HTML_table_basics" # URL de la página web
res = requests.get(url) # Realiza la petición GET
res.raise_for_status() # Si hay un error, se lanza una excepción
soup = BeautifulSoup(res.text, 'lxml') # Crea un objeto BeautifulSoup

tabla = soup.find('table') # Encuentra la primera tabla en la página

if tabla:
    for fila in tabla.find_all('tr'):
        for celda in fila.find_all('td'):
            print(celda.text.strip())
else:
    print("No se encontró ninguna tabla en la página.")
