Proyecto: Análisis Interactivo de Vehículos Usados

Descripción

Esta aplicación web, desarrollada con Streamlit, permite explorar y analizar un conjunto de datos de anuncios de venta de vehículos usados en EE.UU. Proporciona herramientas interactivas para visualizar los datos de manera intuitiva y obtener insights clave sobre las características de los vehículos en venta.

Funcionalidades

Visualización Interactiva:

 histograma de la columna "odometer" para analizar la distribución de las lecturas del odómetro en millas.

Generacion de gráfico de dispersión que relaciona el precio del vehículo con las lecturas del odómetro.

Interactividad:

La aplicación incluye botones que permiten al usuario generar las visualizaciones de forma dinámica.

Gráficos Avanzados:

Utiliza Plotly Express para generar gráficos interactivos y personalizables.

Tecnologías Utilizadas

Python: Lenguaje principal de programación.

Streamlit: Framework para construir aplicaciones web interactivas.

Pandas: Biblioteca para la manipulación y análisis de datos.

Plotly Express: Herramienta para la visualización de datos.

Cómo Ejecutar la Aplicación

Clona el repositorio en tu máquina local.

Asegúrate de tener instalado Python 3.8 o superior.

Instala las dependencias ejecutando:

pip install -r requirements.txt

Inicia la aplicación con:

streamlit run app.py

Abre la URL generada en tu navegador (https://aplicacionweb2.onrender.com)

Dataset

El conjunto de datos utilizado es vehicles_us.csv, el cual contiene información sobre:

Precio del vehículo.

Lectura del odómetro.

Otros detalles del anuncio.