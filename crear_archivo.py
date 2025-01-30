import webbrowser, requests

# Descargamos un pagina web y lo guardamos en un archivo
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()

archivo = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    archivo.write(chunk)
archivo.close()

webbrowser.open('RomeoAndJuliet.txt')