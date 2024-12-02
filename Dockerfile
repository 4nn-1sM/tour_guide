# utilizar una imagen de python
FROM python:3.12.6
# Establecer el directorio de la app
WORKDIR /app

# Copiamos los archivos al directorio del contenedor
COPY app.py /app

# En el doc requirements tienen que aparecer todas las librerías que se necesiten para utilizar el código
# lo suyo, para no liarla es poner también las versiones que se necesitan de cada librería. 
# comprobar en terminal con pip freeze y escribir como aparece ahí (ej. numpy==1.23.5). 
#Si no lo indicamos, descargará la última versión
COPY . /app/
RUN pip install --no-cache-dir -r requirements.txt
# Exponer el puerto en el que la aplicación está corriendo en el contenedor
EXPOSE 8000
# Comando para ejecutar la aplicación
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]