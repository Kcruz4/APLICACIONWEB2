import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')  # Asegúrate de que el archivo esté en el mismo directorio

# Encabezado de la aplicación
st.header("Análisis de Vehículos.")

# Botón para construir el histograma
hist_button = st.button('Construir Histograma')

if hist_button:  # Al hacer clic en el botón
    # Mensaje al usuario
    st.write('Creación de un histograma para la columna "odometer"')
    # Crear un histograma
    fig = px.histogram(car_data, x="odometer", title="Histograma del Odómetro (en millas)")
    # Mostrar el gráfico en la app
    st.plotly_chart(fig, use_container_width=True)

# Botón para construir el gráfico de dispersión
scatter_button = st.button('Construir Gráfico de Dispersión')

if scatter_button:  # Al hacer clic en el botón
    # Mensaje al usuario
    st.write('Creación de un gráfico de dispersión con las columnas "price" y "odometer"')
    # Crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price", title="Precio vs Odómetro",
                     labels={"odometer": "Odómetro (millas)", "price": "Precio ($)"})
    # Mostrar el gráfico en la app
    st.plotly_chart(fig, use_container_width=True)


# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')

