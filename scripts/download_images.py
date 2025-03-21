import csv
import requests
import os

# Nombre del archivo CSV y carpeta de destino
csv_file = 'input.csv'  # Cambia esto si tu archivo tiene otro nombre
output_folder = 'imagenes_descargadas'  # Carpeta donde se guardarán las imágenes

# Crear la carpeta si no existe
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Función para convertir enlace de Google Drive a enlace de descarga directa
def get_direct_download_url(drive_url):
    try:
        # Extraer el ID del archivo desde la URL
        if "drive.google.com/file/d/" in drive_url:
            file_id = drive_url.split('/d/')[1].split('/')[0]
        elif "drive.google.com/open?id=" in drive_url:
            file_id = drive_url.split('id=')[1].split('&')[0]
        else:
            raise ValueError("Formato de URL no reconocido")
        return f"https://drive.google.com/uc?export=download&id={file_id}"
    except Exception as e:
        print(f"Error al procesar URL {drive_url}: {e}")
        return None

# Leer el CSV y descargar las imágenes
print(f"Abriendo el archivo CSV: {csv_file}")
with open(csv_file, 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    headers = next(csv_reader)  # Saltar la fila de encabezados
    print("Encabezados:", headers)
    
    row_count = 0
    for row in csv_reader:
        if row and len(row) >= 8:  # Asegurarse de que la fila tenga al menos 8 columnas
            row_count += 1
            id_value = row[0].strip()  # Columna 'id'
            indicio = row[1].strip()   # Columna 'INDICIO'
            drive_url = row[7].strip() # Columna 'LINK FOTO'
            
            print(f"\nProcesando fila {row_count} (id: {id_value}, INDICIO: {indicio})")
            print(f"URL original: {drive_url}")
            
            if drive_url:
                download_url = get_direct_download_url(drive_url)
                if download_url:
                    print(f"URL de descarga: {download_url}")
                    try:
                        # Descargar la imagen
                        response = requests.get(download_url, timeout=10)
                        if response.status_code == 200:
                            # Usar 'id' y 'INDICIO' para nombrar el archivo
                            file_name = f"{id_value}_{indicio}.jpg"  # Asume formato .jpg, ajusta si es necesario
                            file_path = os.path.join(output_folder, file_name)
                            with open(file_path, 'wb') as img_file:
                                img_file.write(response.content)
                            print(f"Imagen guardada como: {file_path}")
                        else:
                            print(f"Error al descargar: Código {response.status_code}")
                    except requests.RequestException as e:
                        print(f"Error en la descarga: {e}")
                else:
                    print("No se pudo generar URL de descarga")
            else:
                print("URL vacía, saltando...")
        else:
            print(f"Fila ignorada (incompleta o vacía): {row}")

print(f"\nDescarga completada. Imágenes guardadas en: {output_folder}")
