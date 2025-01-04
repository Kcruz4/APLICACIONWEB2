# Usa una imagen base de Python 3
FROM python:3.11-slim

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y python3-venv

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el código fuente y el archivo requirements.txt al contenedor
COPY . /app

# Instalar las dependencias de Python desde el requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Comando para ejecutar la aplicación Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=$PORT"]
