# Plan de Acción: Análisis y Visualización Espacial — TFG

Este plan detalla la fase de análisis de datos y generación de mapas, con el objetivo central de **demostrar la influencia de la ubicación geográfica en la presencia y tipo de distractores acústicos**.

## Objetivo de Investigación
Validar la hipótesis de que los eventos acústicos detectados no se distribuyen de manera uniforme, sino que presentan agrupamientos (clusters) vinculados a zonas específicas del trayecto (ej. intersecciones, zonas industriales, centros urbanos).

## Estructura de Salida
Los resultados se organizarán en los siguientes notebooks:
- `notebooks/02_analysis.ipynb`: Análisis estadístico y descriptivo.
- `notebooks/03_maps.ipynb`: Generación de mapas interactivos y visualización espacial.

---

## Fase 1: Análisis Estadístico y de Confianza

Antes del análisis espacial, se debe asegurar la calidad de las detecciones mediante el filtrado por confianza.

### Tareas:
- [x] **Análisis de Confianza por Clase**: Evaluar la distribución de confianza (boxplots) para cada clase para refinar los umbrales (thresholds).
- [x] **Metodología de Umbrales**: Cálculo y comparativa de umbrales sugeridos basados en la fórmula estadística `mean + 1*std`.
- [x] **Filtrado de Datos**: Aplicar los umbrales específicos por clase para eliminar falsos positivos.
- [x] **Estadística Descriptiva**:
    - Frecuencia de eventos por clase (Gráficos de barras).
    - Distribución temporal (¿Hay más ruido en ciertas horas o días?).
    - Comparativa entre sensores (Micrófono Frontal vs. Trasero).

---

## Fase 2: Análisis de Distribución Espacial

Demostrar la relación entre la posición (lat/lon) y las detecciones.

### Tareas:
- [x] **Mapeo de Puntos (Scatter Plot)**: Visualizar todos los eventos geolocalizados sobre el mapa de Valencia.
- [x] **Análisis de Densidad (Heatmaps)**:
    - Generar un mapa de calor general de "contaminación acústica".
    - Generar mapas de calor por clase (ej. ¿Dónde se concentran las sirenas?).
- [x] **Identificación de Hotspots**: Detectar zonas críticas con alta densidad de eventos utilizando algoritmos como KDE (Kernel Density Estimation).

---

## Fase 3: Análisis por Segmentos y Rutas

Dividir el trayecto para cuantificar la carga acústica por tramo.

### Tareas:
- [x] **Segmentación de Ruta**: Dividir el trayecto en tramos de 100m o 500m.
- [x] **Carga Acústica por Tramo**: Calcular el número de eventos o la intensidad media por segmento para identificar "tramos ruidosos".
- [ ] **Correlación con el Entorno**: (Opcional) Cruzar visualmente con puntos de interés (POIs) como hospitales, colegios o grandes avenidas.

---

## Fase 4: Demostración de Hipótesis

Cruzar los datos espaciales con las variables de interés.

### Tareas:
- [x] **Comparativa de Trayectos**: Comparar la distribución de eventos en trayectos de "ida" vs. "vuelta" en el mismo punto espacial.
- [x] **Validación con Observaciones**: Cruzar los eventos detectados automáticamente con las notas manuales (`observaciones.txt`) en los puntos geográficos señalados por el conductor.

---

## Entregables Esperados (Outputs)

| Archivo | Descripción |
| :--- | :--- |
| `class_distribution.png` | Gráfico de barras de frecuencias por clase filtrada. |
| `confidence_distribution.png` | Boxplot de confianza por clase. |
| `heatmap_total.html` | Mapa de calor interactivo de todos los distractores. |
| `mapa_clases_capas.html` | Mapa interactivo con capas activables por tipo de sonido. |
| `analisis_segmentos.png` | Gráfico de línea que muestra el nivel de ruido a lo largo de la ruta. |

## Dependencias
- `matplotlib`, `seaborn`: Visualización estadística.
- `folium`: Mapas interactivos (Leaflet).
- `scipy` / `sklearn`: (Si se requiere) para análisis de clusters o densidad.
