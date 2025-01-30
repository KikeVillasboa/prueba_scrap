# Programa para leer un pdf, contar las palabras y guardarlas en un archivo csv
# Autor: Cristhian Villasboa
# Fecha: 2025-01-01
# Versión: 1.0
# Python 3.9.5
from PyPDF2 import PdfReader
import csv

def scrap_pdf(file_pdf, file_csv):
    with open(file_pdf, 'rb') as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)
        text = ""
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            page_text = page.extract_text()
            if page_text:
                text += page_text

    print('Número de páginas:', num_pages)
    
    # print('Texto extraído:', text) # Descomentar para ver el texto extraído

    words = text.split()
    word_count = len(words)
    print('Número de palabras:', word_count)

    with open(file_csv, 'w', newline='') as file:
        try:
            writer = csv.writer(file)
            writer.writerow(['Palabras encontradas en el pdf: {word_count}'.format(word_count=word_count)])
            
            # Contar palabras repetidas y mostrar la cantidad de veces que se repiten
            # Crear un diccionario para almacenar las palabras y sus conteos
            word_counts = {}
            for word in words:
                word = word.lower()
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1
            
            # Escribir las 10 palabras más comunes en el archivo csv
            writer.writerow(['Palabra', 'Cantidad'])
            for word, count in sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
                print(word, count)
                writer.writerow([word, count])
        except Exception as e:
            print('Error:', e)
            writer.writerow(['Error al procesar el archivo'])   
    
    print('Datos guardados en', file_csv)



scrap_pdf('ejemplo_pdf.pdf', 'data1.csv')
