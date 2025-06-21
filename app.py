import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header('Análisis de Datos de Vehículos')

# Casillas de verificación para seleccionar gráficos
show_histogram = st.checkbox('Mostrar histograma')
show_scatter = st.checkbox('Mostrar gráfico de dispersión')

if show_histogram:  # Si se selecciona la casilla de histograma
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un histograma
    fig_hist = px.histogram(car_data, x="odometer")
    
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

if show_scatter:  # Si se selecciona la casilla de gráfico de dispersión
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Gráfico de Dispersión: Odometer vs Price")
    
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)
