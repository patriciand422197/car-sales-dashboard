import streamlit as st
import pandas as pd
import plotly.express as px

# Leer el dataset
car_data = pd.read_csv('vehicles_us.csv')

# Título y encabezado
st.title('Análisis de ventas de vehículos en EE.UU.')
st.header('Cuadro de mandos interactivo')

# Casilla para mostrar histograma
build_histogram = st.checkbox('Mostrar histograma de odómetro')

if build_histogram:
    st.write('Construyendo histograma de odómetro...')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Casilla para mostrar gráfico de dispersión
build_scatter = st.checkbox(
    'Mostrar gráfico de dispersión (odómetro vs precio)')

if build_scatter:
    st.write('Construyendo gráfico de dispersión...')
    fig2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)
