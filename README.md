# Car Sales Dashboard

Esta es una aplicación web interactiva desarrollada con Streamlit que permite explorar visualmente un conjunto de datos de anuncios de vehículos en EE.UU.

## Funcionalidad

- Muestra un **histograma** de la columna `odometer` (kilometraje).
- Muestra un **gráfico de dispersión** entre `odometer` y `price`.
- Ambos gráficos se pueden activar mediante **casillas de verificación interactivas**.
- Utiliza `pandas` para el análisis de datos y `plotly.express` para las visualizaciones.

## Tecnologías utilizadas

- Python
- Streamlit
- Pandas
- Plotly Express

## Cómo ejecutarlo

1. Clona este repositorio
2. Activa el entorno virtual
3. Ejecuta:

```bash
streamlit run app.py