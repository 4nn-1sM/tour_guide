# utilizar una imagen de python
FROM python:3.9-slim
# Establecer el directorio de la app
WORKDIR /app

# Instalar dependencias del sistema necesarias para `cryptography`
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc libssl-dev libffi-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copiamos los archivos al directorio del contenedor
COPY app.py /app

# En el doc requirements tienen que aparecer todas las librerías que se necesiten para utilizar el código
# lo suyo, para no liarla es poner también las versiones que se necesitan de cada librería. 
# comprobar en terminal con pip freeze y escribir como aparece ahí (ej. numpy==1.23.5). 
#Si no lo indicamos, descargará la última versión
COPY home.html /app/
COPY requirements.txt /app/
COPY static /app/static/
RUN pip install --no-cache-dir -r requirements.txt
# Exponer el puerto en el que la aplicación está corriendo en el contenedor
EXPOSE 8000
# Comando para ejecutar la aplicación
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]