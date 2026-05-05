# Plan de Acción ETL — TFG Detección Acústica

Este documento describe la fase de Extracción, Transformación y Carga (ETL) del proyecto. El objetivo es consolidar los datos de múltiples días de grabación y geolocalizar cada detección acústica.

## Contexto del Proyecto

Los datos se recogen diariamente y se organizan en carpetas `DD-MM-YYYY/` dentro de `data/raw/`.

| Archivo | Descripción |
| :--- | :--- |
| `*.gpx` | Trazas GPS del trayecto (lat, lon, time). |
| `predicciones_*.txt` | Detecciones del modelo: `microfono_id, t_start, t_end, class, confidence`. |
| `observaciones.txt` | Notas manuales del trayecto. |

## Estructura de Datos

```text
data/
  raw/                  # Datos brutos por día
    23-03-2026/
      ..._15_10_48.gpx
      predicciones_2026-03-23.txt
      observaciones.txt
  processed/            # Datos listos para análisis
    predictions.parquet      # Todas las predicciones unificadas
    tracks.parquet           # Todos los puntos GPS consolidados
    predictions_geo.parquet  # Predicciones con coordenadas (Join)
    observations.csv         # Observaciones consolidadas
```

---

## Fase 1: Carga y Consolidación de Predicciones

Se unifican los archivos de texto, aplicando limpiezas y correcciones horarias necesarias.

### Tareas:
- [x] Búsqueda recursiva de archivos `predicciones_*.txt`.
- [x] Gestión de errores en líneas mal formadas (`on_bad_lines='skip'`).
- [x] **Corrección Horaria**: Ajuste manual para días donde el dispositivo no tenía la hora sincronizada.
- [x] Normalización de zonas horarias (Local Europe/Madrid → UTC).
- [x] Cálculo de duración del evento y limpieza de duplicados.

```python
# Lógica principal de corrección y limpieza
TIME_CORRECTIONS = {"23-03-2026": -1} # Ejemplo: restar 1 hora

for day_corr, hours in TIME_CORRECTIONS.items():
    mask = pred["date"] == day_corr
    pred.loc[mask, "t_start"] = pd.to_datetime(pred.loc[mask, "t_start"]) + pd.Timedelta(hours=hours)
    pred.loc[mask, "t_end"] = pd.to_datetime(pred.loc[mask, "t_end"]) + pd.Timedelta(hours=hours)
```

---

## Fase 2: Carga de Trazas GPS

Extracción de coordenadas y marcas de tiempo de los archivos GPX.

### Tareas:
- [x] Parseo de archivos `.gpx` usando `gpxpy`.
- [x] Identificación de dirección (ida/vuelta) según la hora del archivo.
- [x] Consolidación en un único formato Parquet para mayor eficiencia.

---

## Fase 3: Validación de Sincronía Temporal

Paso crítico para asegurar que las predicciones y los GPS coinciden en el tiempo antes del join.

### Tareas:
- [x] Calcular el rango `[min, max]` de tiempo para GPS y Predicciones por día.
- [x] Verificar el solapamiento temporal (`overlap_min`).
- [x] Generar alertas para días sin coincidencia (posibles errores de fecha o desfase horario no corregido).

---

## Fase 4: Join Espacio-Temporal

Asignación de coordenadas a cada detección basándose en la proximidad temporal.

### Tareas:
- [x] Implementar búsqueda del punto GPS más cercano (`nearest_gps`).
- [x] Establecer un umbral máximo de tolerancia (ej. 4 segundos).
- [x] Generar el dataset final `predictions_geo.parquet`.

---

## Fase 5: Validación de Calidad del ETL

Control de calidad final sobre el proceso de unión.

### Métricas de control:
- **% de Geolocalización**: Ratio de eventos con coordenadas vs total de eventos.
- **Distribución por Micrófono**: Asegurar que ambos sensores (Frontal/Trasero) están representados.
- **Ventana de Join**: Comprobar que los eventos geolocalizados caen dentro de la ruta real.

---

## Dependencias

- `pandas`, `pyarrow`: Gestión de datos y formato Parquet.
- `gpxpy`: Lectura de archivos GPS.
- `pathlib`: Gestión de rutas de archivos.

## Resultados Esperados

1. **`predictions_geo.parquet`**: El archivo maestro para cualquier análisis posterior.
2. **Informe de Sincronía**: Tabla resumen de solapamientos por día.
3. **Log de Calidad**: Porcentaje de éxito del join y conteo por sensor.
