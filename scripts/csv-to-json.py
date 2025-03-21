import csv
import json

# Nombre del archivo CSV de entrada y el JSON de salida
csv_file = 'input.csv'  # Cambia esto si tu archivo tiene otro nombre
json_file = 'output.json'  # Nombre del archivo JSON que se creará

# Lista para almacenar los datos
data = []

# Leer el archivo CSV
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
            print(f"\nFila {row_count}: {row}")
            # Crear un diccionario con los encabezados esperados
            entry = {
                "id": row[0].strip(),
                "INDICIO": row[1].strip(),
                "TIPO DE INDICIO": row[2].strip(),
                "COLOR": row[3].strip(),
                "MARCA": row[4].strip(),
                "TALLA": row[5].strip(),
                "OBSERVACIONES": row[6].strip(),
                "LINK FOTO": row[7].strip()
            }
            print(f"Convertido a JSON: {json.dumps(entry, ensure_ascii=False, indent=4)}")
            data.append(entry)
        else:
            print(f"Fila ignorada (incompleta o vacía): {row}")

# Escribir los datos en un archivo JSON
print(f"\nGuardando {len(data)} entradas en el archivo JSON: {json_file}")
with open(json_file, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print(f"Conversión completada. El archivo JSON se guardó como {json_file}")
