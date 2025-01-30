# Programa para analizar una pagiga web y extraer información
# de ella. En este caso se extraen los enlaces de la página
# web del portal de noticias abc.com.py
# Autor: Cristhian Villasboa
# Fecha: 2025/01/01
# Versión: 1.0
# Python Version: 3.9.5
# Descripción: Este programa se encarga de extraer los enlaces
# de la página web del portal de noticias abc.com.py y los
# guarda primero en un dataframe y luego en un archivo csv.

# Importar librerías
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Definir la URL de la página web
url = 'https://www.abc.com.py/'

# Realizar la petición a la página web
response = requests.get(url)

# Verificar que la petición fue exitosa
if response.status_code == 200:
    # Parsear el contenido de la página web
    soup = BeautifulSoup(response.content, 'html.parser')
    # Extraer los enlaces de la página web
    links = soup.find_all('a')
    # Crear un dataframe para almacenar los enlaces
    df = pd.DataFrame(columns=['Enlace'])
    # Recorrer los enlaces y guardarlos en el dataframe
    for link in links:
        df = df._append({'Enlace': link.get('href')}, ignore_index=True)
    # Guardar los enlaces en un archivo csv
    df.to_csv('links.csv', index=False)
else:
    print('Error al realizar la petición a la página web')

# Fin del programa
