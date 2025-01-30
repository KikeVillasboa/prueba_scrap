# Programa para leer un archivo txt, buscar cierta información y guardarla en otro archivo csv
# Autor: Cristhian Villasboa
# Fecha: 2025-01-01
# Versión: 1.0
# Python 3.9.5

import csv
import re

# Función para leer un archivo txt, buscar cierta información y guardarla en otro archivo csv
# El archivo txt debe tener el siguiente formato:
# Nombre, Edad, Correo
def scrap_txt(file_txt, file_csv):
    # Se abre el archivo txt en modo lectura
    with open(file_txt, 'r') as file:
        # Se lee el contenido del archivo
        content = file.read()
        # La expresión regular busca una o más palabras, seguidas de una coma, un espacio, un número, una coma, un espacio y una dirección de correo electrónico.
        data = re.findall(r'(\w+),(\d+),(\w+@\w+\.\w+)', content)
        # Se crea una lista para almacenar las tuplas que cumplen con la busqueda
        filter_data = []
        # Se imprime la lista de tuplas para comprobar que se encontraron los datos
        print('Datos encontrados:', data)
        # Recorrer la lista de tuplas
        for row in data:
            # Recorrer la tupla
            for value in row:
                # Preguntar si es el segundo elemento de la tupla
                if value == row[1]:
                    # Preguntar si es mayor de 24 y menor de 30
                    if int(value) > 24 and int(value) < 30:
                        # Se imprime la tupla
                        print(row)
                        # Almacenar las tuplas que cumplen con la busqueda en una nueva lista de tuplas
                        filter_data.append(row)

    print('Datos filtrados:', filter_data)

    # Se abre el archivo csv en modo escritura
    with open(file_csv, 'w', newline='') as file:
        # Se crea el objeto writer
        writer = csv.writer(file)
        # Se escriben los encabezados
        writer.writerow(['Nombre', 'Edad', 'Correo'])
        # Recorrer la lista de tuplas y escribir los datos en el archivo csv
        for row in filter_data:
            writer.writerow(row)
        # Se imprime un mensaje para indicar que los datos se guardaron correctamente
    print('Datos guardados en', file_csv)
    
# Se llama a la función scrap_txt
scrap_txt('datos.txt', 'data.csv')