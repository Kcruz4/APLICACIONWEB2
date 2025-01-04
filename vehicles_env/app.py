import streamlit as st # type: ignore
import pandas as pd # type: ignore
import plotly.express as px # type: ignore

# Leer el archivo CSV en un DataFrame
car_data = pd.read_csv('vehicles_us.csv')