# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios
COPY requirements.txt .

# Instala las dependencias
RUN pip install -r requirements.txt

# Copia el código de la aplicación
COPY app.py .

# Expone el puerto en el que correrá el servicio
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
