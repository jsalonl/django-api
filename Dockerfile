# Utiliza la imagen oficial de Python como base
FROM python:3.9

# Define variables de entorno para Python en modo no interactivo y para la codificación UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Configura el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt /app/

# Instala las dependencias del proyecto
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copia el resto del código fuente al contenedor
COPY . /app/

# Comando para ejecutar las migraciones de Django, correr los tests y levantar el servidor
CMD python manage.py migrate && coverage run manage.py test && python manage.py runserver 0.0.0.0:8000
