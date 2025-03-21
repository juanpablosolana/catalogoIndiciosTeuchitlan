import csv
import json
import os

# Nombre del archivo CSV, carpeta de imágenes y archivo JSON de salida
csv_file = 'input.csv'  # Cambia esto si tu archivo tiene otro nombre
output_folder = 'imagenes_descargadas'  # Carpeta donde están las imágenes
json_file = 'output_with_paths.json'  # Nombre del nuevo archivo JSON

# Lista para almacenar los datos
data = []

# Leer el archivo CSV y construir el JSON
print(f"Abriendo el archivo CSV: {csv_file}")
with open(csv_file, 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    
    # Leer la fila de encabezados
    headers = next(csv_reader)
    print("Encabezados encontrados:", headers)
    
    # Procesar las filas de datos
    print("\nProcesando filas de datos:")
    row_count = 0
    for row in csv_reader:
        if row and len(row) >= 8:  # Asegurarse de que la fila tenga al menos 8 columnas
            row_count += 1
            id_value = row[0].strip()  # Columna 'id'
            indicio = row[1].strip()   # Columna 'INDICIO'
            
            # Crear el nombre del archivo de la imagen basado en el formato usado al descargar
            file_name = f"{id_value}_{indicio}.jpg"  # Ajusta la extensión si usaste otra
            file_path = os.path.join(output_folder, file_name)
            
            # Verificar si la imagen existe en la carpeta
            if os.path.exists(file_path):
                image_path = file_path  # Ruta absoluta
                # O usa ruta relativa si prefieres: image_path = os.path.join(output_folder, file_name)
            else:
                image_path = ""  # Si no existe, deja el campo vacío
                print(f"Advertencia: No se encontró la imagen {file_path} para la fila {row_count}")
            
            print(f"\nFila {row_count}: id={id_value}, INDICIO={indicio}")
            # Crear un diccionario con los datos originales más la ruta de la imagen
            entry = {
                "id": id_value,
                "INDICIO": indicio,
                "TIPO DE INDICIO": row[2].strip(),
                "COLOR": row[3].strip(),
                "MARCA": row[4].strip(),
                "TALLA": row[5].strip(),
                "OBSERVACIONES": row[6].strip(),
                "LINK FOTO": row[7].strip(),
                "RUTA IMAGEN": image_path
            }
            print(f"Entrada JSON: {json.dumps(entry, ensure_ascii=False, indent=4)}")
            data.append(entry)
        else:
            print(f"Fila ignorada (incompleta o vacía): {row}")

# Escribir los datos en un archivo JSON
print(f"\nGuardando {len(data)} entradas en el archivo JSON: {json_file}")
with open(json_file, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print(f"Conversión completada. El archivo JSON se guardó como {json_file}")
