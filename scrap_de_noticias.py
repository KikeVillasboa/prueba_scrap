from bs4 import BeautifulSoup
import requests
import pandas as pd

# URL de la página a scrapear
url = "https://www.abc.com.py/"

# Realiza la petición GET
res = requests.get(url)

# Verifica si la petición fue exitosa
res.raise_for_status()

# Verifica el status_code de la respuesta
if res.status_code == 200:
    print("La petición fue exitosa")
    
    # Crea un objeto BeautifulSoup
    soup = BeautifulSoup(res.text, 'lxml')

    # Creamos una lista para almacenar los datos
    noticias = []

    # Encuentra los section en la página
    noticias = soup.find_all('section-content')

    # Convertir noticias en un objeto BeautifulSoup
    noticias = [BeautifulSoup(str(noticia), 'lxml') for noticia in noticias]

    # Recorre las noticias
    for noticia in noticias:

        # Validar si noticia es un objeto BeautifulSoup
        if not isinstance(noticia, BeautifulSoup):
            print("Noticia no es un objeto BeautifulSoup")
            continue
        
        # Encuentra el título de la noticia
        titulo = noticia.find('div', class_='article-title)')
        print(titulo)

    
    # Crea un DataFrame con los datos y lo guardamos en un archivo CSV
    df = pd.DataFrame(noticias)
    df.to_csv('noticias.csv', index=False)

    print("Datos guardados en noticias.csv")

else:
    print("La petición no fue exitosa")
    print("Status code:", res.status_code)

