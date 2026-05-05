# TFG — Análisis Espacial de Distractores Acústicos en la Conducción

Este proyecto se centra en el análisis de la distribución espacial de eventos acústicos (distractores) detectados mediante sensores DAS (Distributed Acoustic Sensing) en trayectos urbanos e interurbanos. El objetivo principal es correlacionar las detecciones automáticas con la ubicación geográfica (GPX) para identificar puntos críticos de ruido y validar patrones espaciales.

## 🚀 Características Principales

- **Procesamiento de Señal (ETL)**: Pipeline completo para la limpieza, sincronización y estructuración de datos provenientes de sensores acústicos y GPS.
- **Detección y Clasificación**: Filtrado estadístico de eventos basado en umbrales de confianza por clase.
- **Visualización Espacial Interactiva**: Generación de mapas de calor y mapas de puntos por capas utilizando Folium.
- **Análisis de Segmentos**: División de rutas en tramos de 100m para cuantificar la carga acústica y velocidad media.
- **Análisis Multitemporal**: Comparativa interactiva de eventos y movilidad entre diferentes sesiones y fechas.

## 📁 Estructura del Proyecto

```text
Proyecto/
├── data/
│   ├── raw/              # Datos originales (GPX, archivos de audio/DAS)
│   └── processed/        # CSVs limpios y bases de datos SQLite
├── notebooks/
│   ├── 01_etl.ipynb      # Extracción, Transformación y Carga de datos
│   ├── 02_analysis.ipynb # Análisis estadístico, filtrado y descriptivo
│   └── 03_maps.ipynb     # Visualización espacial e interactiva (Folium)
├── outputs/
│   ├── figures/          # Gráficos de distribución, boxplots, etc. (Ignorado)
│   └── maps/             # Mapas interactivos en formato .html (Ignorado)
├── requirements.txt      # Dependencias del proyecto
└── README.md
```

## 🛠️ Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/jogarmo9/Proyecto-TFG.git
   cd Proyecto-TFG
   ```
2. Instalar las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```
3. (Opcional) Crear carpetas locales ignoradas si no existen:
   ```bash
   mkdir outputs
   ```

## 📈 Flujo de Trabajo

1. **ETL (`01_etl.ipynb`)**: Procesa los archivos GPX y sincroniza las marcas de tiempo con las detecciones acústicas.
2. **Análisis (`02_analysis.ipynb`)**: Evalúa la calidad de los datos, establece umbrales de confianza (mean + 1*std) y filtra falsos positivos.
3. **Mapas (`03_maps.ipynb`)**: Genera visualizaciones espaciales. Incluye:
    - Mapas de calor generales.
    - Mapas segmentados por intensidad de ruido.
    - Dashboard multitemporal para comparar fechas.

## 📊 Resultados Esperados

- Identificación de **hotspots** de contaminación acústica en Valencia.
- Validación de la consistencia de las detecciones DAS en comparación con observaciones manuales.
- Análisis de la relación entre la velocidad del vehículo y la frecuencia de eventos detectados.

---
*Este proyecto forma parte de un Trabajo de Fin de Grado (TFG).*
