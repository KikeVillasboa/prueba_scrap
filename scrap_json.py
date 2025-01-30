# Programa para leer un archivo json, buscar cierta información y guardarla en otro archivo csv
# Autor: Cristhian Villasboa
# Fecha: 2025-01-01
# Versión: 1.0
# Python 3.9.5
import csv
import json

# Función para leer un archivo json, buscar las personas que viven en Paraguay, preguntar por el argumento edad y guardar en un archivo csv si la persona es mayor de edad
def scrap_json(file_json, file_csv, age):
    # Se abre el archivo json en modo lectura
    with open(file_json, 'r') as file:
        # Se carga el contenido del archivo json en la variable data
        data = json.load(file)
        # Se imprime el contenido del archivo json
        print('Datos encontrados:', data)
        # Se crea una lista para almacenar las personas que cumplen con la busqueda
        filter_data = []
        # Recorrer la lista de diccionarios
        for person in data:
            # Preguntar si la persona vive en Paraguay
            if person['pais'] == 'Paraguay':
                # Preguntar si la persona es mayor de edad
                if person['edad'] >= age:
                    # Se imprime la persona
                    print(person)
                    # Almacenar las personas que cumplen con la busqueda en una nueva lista de diccionarios
                    filter_data.append(person)

    print('Datos filtrados:', filter_data)

    # Se abre el archivo csv en modo escritura
    with open(file_csv, 'w', newline='') as file:
        # Se crea el objeto writer
        writer = csv.writer(file)
        # Se escriben los encabezados
        writer.writerow(['Nombre', 'Edad', 'Pais'])
        # Recorrer la lista de diccionarios y escribir los datos en el archivo csv
        for person in filter_data:
            writer.writerow([person['nombre'], person['edad'], person['pais']])
        # Se imprime un mensaje para indicar que los datos se guardaron correctamente

    print('Datos guardados en', file_csv)

# Se llama a la función scrap_json
scrap_json('personas.json', 'data2.csv', 18)
