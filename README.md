# Catálogo de Indicios Teuchitlán

Este proyecto presenta una galería interactiva de indicios descubiertos en el Rancho Izaguirre, basada en la información oficial de la Fiscalía de Jalisco.
> “El día de hoy nos encontramos en una búsqueda en un predio que según eso ya se había cateado, pero nos estamos encontrando varias fosas, hornos crematorios y la localización de varios huesos“, así inicia la narración de uno de los videos que grabaron, el 5 de marzo de 2025, integrantes del Colectivo Guerreros Buscadores de Jalisco al interior del Rancho Izaguirre, ubicado en la comunidad La Estanzuela del municipio de Teuchitlán, Jalisco. Lugar que antes y después del “cateo y aseguramiento” realizado por la Fiscalía del Estado de Jalisco, en septiembre de 2024, se presume fue utilizado como sitio de entrenamiento forzado y un lugar de exterminio.
>
> Darwin Franco, [Teuchitlán: cuando la necromaquina opera impunemente](https://www.zonadocs.mx/2025/03/12/teuchitlan-cuando-la-necromaquina-opera-impunemente/), 2025.

## URL del Sitio
Visita el catálogo desplegado en: [https://juanpablosolana.github.io/catalogoIndiciosTeuchitlan/](https://juanpablosolana.github.io/catalogoIndiciosTeuchitlan/)

## Inspiración
Este proyecto está inspirado en [abundis-rmn2/catalogoIndiciosTeuchitlan](https://github.com/abundis-rmn2/catalogoIndiciosTeuchitlan), un catálogo estático en HTML. Lo hemos ampliado con:
- Una interfaz dinámica en Astro con filtros para "Tipo de Indicio", "Color" y "Marca".
- Tipado seguro mediante TypeScript.
- Un diseño moderno y responsivo con CSS personalizado.
- Scripts en Python para procesar datos e imágenes.
- Despliegue automatizado en GitHub Pages.

## Fuente de Información
La información utilizada proviene de una fuente oficial de la Fiscalía de Jalisco:
- **URL:** [https://docs.google.com/spreadsheets/d/1K5gul4mUWEIWc7yhlIZlheJDkqH7thPv/htmlview#gid=2057625904](https://docs.google.com/spreadsheets/d/1K5gul4mUWEIWc7yhlIZlheJDkqH7thPv/htmlview#gid=2057625904)
- **Formato:** Exportada como archivo CSV (`complete_data.csv`) para su procesamiento.

## Proceso de Desarrollo

### 1. Obtención de la Base de Datos
- Se descargó el archivo CSV desde la hoja de Google Sheets mencionada.
- El archivo `complete_data.csv` contiene todos los datos originales y se encuentra en la raíz del repositorio.

### 2. Conversión de CSV a JSON
- **Script:** `csv-to-json.py`
- **Ubicación:** `/script/csv-to-json.py`
- **Función:** Convierte `complete_data.csv` en `output_with_paths.json`, estructurando los datos para su uso en el frontend.
- **Dependencias:** Python con `pandas`.

### 3. Descarga de Imágenes
- **Script:** `download_images.py`
- **Ubicación:** `/script/download_images.py`
- **Función:** Descarga las imágenes desde los enlaces en el campo `LINK FOTO` del CSV y las guarda en `public/imagenes_descargadas/` con nombres como `001_1A.jpg`.
- **Dependencias:** Python con `requests` y `os`.

### 4. Actualización del JSON con Rutas Locales
- **Script:** `update_json_with_paths.py`
- **Ubicación:** `/script/update_json_with_paths.py`
- **Función:** Actualiza `output_with_paths.json` añadiendo el campo `"RUTA IMAGEN"` con las rutas locales (ejemplo: `imagenes_descargadas/001_1A.jpg`).
- **Dependencias:** Python con `json`.

### 5. Desarrollo del Frontend
- **Framework:** Astro con TypeScript.
- **Estructura:**
  - `src/pages/index.astro`: Página principal con una tabla filtrable que carga datos desde `public/output_with_paths.json`.
  - `src/styles/styles.css`: Estilos personalizados para un diseño responsivo y moderno.
  - `src/types/indicio.ts`: Interfaz TypeScript para tipar los datos:
    ```typescript
    export interface Indicio {
      id: string;
      INDICIO: string;
      'TIPO DE INDICIO': string;
      COLOR: string;
      MARCA: string;
      TALLA: string;
      OBSERVACIONES: string;
      'LINK FOTO': string;
      'RUTA IMAGEN': string;
    }
    ```
- **Características:** Tabla con filtros dinámicos y visualización de imágenes locales.

### 6. Despliegue en GitHub Pages
- **Configuración:** `astro.config.mjs`:
  ```javascript
  import { defineConfig } from 'astro/config';

  export default defineConfig({
    site: 'https://juanpablosolana.github.io',
    base: '/catalogoIndiciosTeuchitlan',
    output: 'static',
  });