import streamlit as st
import pandas as pd
import plotly_express as px

# Cargamos el conjunto de datos de vehículos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.header('Dashboard de Análisis de Vehículos')

# Crear instrucciones para el usuario
st.write('Selecciona qué visualizaciones deseas mostrar:')

# ----- HISTOGRAMA -----
show_histogram = st.checkbox('Mostrar Histograma de Odómetro')

if show_histogram:
    st.write('### Distribución del kilometraje')
    # Crear histograma basado en la columna 'odometer'
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# ----- SCATTER PLOT -----
show_scatter = st.checkbox('Mostrar Gráfico de Dispersión (Precio vs. Odómetro)')

if show_scatter:
    st.write('### Relación entre Precio y Kilometraje')
    # Crear scatter plot comparando 'odometer' y 'price'
    fig_scatter = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig_scatter, use_container_width=True)