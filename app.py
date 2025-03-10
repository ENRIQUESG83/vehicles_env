import streamlit as st
import pandas as pd
import plotly.express as px

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Agregar un encabezado
st.header("Análisis de Vehículos Usados")
# Botones para crear gráficos
#hist_button = st.button('Construir histograma')
#scatter_button = st.button('Construir gráfico de dispersión')

hist_checkbox = st.checkbox('Construir histograma')
scatter_checkbox = st.checkbox('Construir gráfico de dispersión')

if hist_checkbox:  # al hacer clic en histograma
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if scatter_checkbox:  # al hacer clic en gráfico de dispersión
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price", title="Gráfico de dispersión de venta de coches")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig,use_container_width=True)



