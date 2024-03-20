# Guía Instalación Servidor web Linux

## Objetivos

1. Instalar un stack en linux de backend, frontend y base de datos
2. Reconocer los comandos necesarios para ejecutar labores de administración en un servidor

## Pre-requisitos

1. Ubuntu (22.04 o superior)
2. Git
   Instalación:

   ```shell
   sudo apt-get update
   sudo apt-get install git
   ```

3. Python
   Instalación:

   ```shell
   sudo add-apt-repository ppa:fkrull/deadsnakes
   sudo apt-get update
   sudo apt-get install python3.6
   ```

4. Virtual env

   Genera un espacio de trabajo con una versión de python en específico

   ```python
   pip intall virtualenv
   ```

5. Node

   Instalación

   ```shell
   sudo apt-get update
   sudo apt-get install nodejs
   ```

6. PostgreSQL

   Motor de base de datos:

   ```shell
   sudo apt-get update
   sudo apt-get install postgresql postgresql-contrib
   ```

7. Instalar libreria cliente para python

   Necesitamos un conector para el motor de base de datos llamado psycopg2

   ```python
   pip install psycopg2-binary
   ```

## Instalación del proyecto

1. Se recomienda el uso de entornos virtuales por proyecto (con la finalidad de tener ambientes independientes)

   ```shell
   py -m venv virtual_env
   ```

   De esta forma puede ejecutarse desde el IDE el intérprete en específico de la aplicación.
   Si se esta usando VSCode se recomienda la instalación del plugin python

2. Instalar django

   ```shell
   pip install django
   ```

   Comprobamos si esta instalado con el comando ```django-admin --version```

3. Crear el proyecto:

   Con el comando ```django-admin startproject app_compensar .``` creamos el proyecto principal

4. Correr el proyecto:

   Con ```python3 manage.py runserver``` se correra el proyecto de forma local en el puerto 8000

5. Crear una aplicación:

   En el contexto de django un proyecto puede tener diversas aplicaciones, para nuestro ejemplo crearemos nuestra aplicación ```students```
   Con el comando ```python3 manage.py startapp students``` creamos la aplicación, sin embargo nuestro proyecto ```app_compensar``` aún no conoce esta aplicación

6. Agregar la aplicación ```students``` al proyecto ```app_compensar```

   En nuestra carpeta ```app_compensar``` tenemos un archivo llamado ```settings.py``` lo abriremos y dentro del objeto ```INSTALLED_APPS``` agregaremos nuestra aplicación ```students```, quedará algo similar a esto:

   ```python
   INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'students' # our app
    ]
   ```

7. Ejecutar migraciones

   Las migraciones se utilizan para modificar el esquema de la base de datos. Esto puede implicar agregar o eliminar tablas, modificar columnas o índices, o realizar otros cambios estructurales, son muy usadas en el ámbito laboral pues permiten llevar un registro de los cambios realizados a un sistema de base de datos.

   ```python
   python3 manage.py migrate
   ```

   *Nota: Por defecto se usa como almacenamiento sqlite3*

8. Django permite renderizar html (para servir contenido estático), sin embargo como vamos a separar responsabilidades el backend solo servira un REST API que será consumido por nuestro front.

   Por esta razón debemos instalar un toolkit llamado django-rest framework, se instala así:

   ```python
   pip install djangorestframework
   ```

9. Solucionar problemas de cabeceras CORS

   Uno de los principales problemas en la comunicación entre back y front son los problemas de CORS, para evitar esto instalaremos una librería que se encargue del manejo de las cabeceras HTTP:

   ```python
   pip install django-cors-headers
   ```

10. Agregaremos las dependecias en nuestro archivo settings.py de nuestro proyecto app_compensar

    ```python
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders', # solution for cors
    'rest_framework', # rest_framework
    'students' # our app
    ]
    ```

    También debemos en la sección de middleware agregar la librería:

    ```python
    MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', # solution for CORS
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
    ```

    Finalmente debemos crear una lista blanca (white list) para aceptar peticiones de servidores conocidos, al final del archivo settings.py agregamos:

    ```python
    CORS_ALLOWED_ORIGINS = [
      'http://localhost:8080'
    ]
    ```

11. Instalar Django Rest Swagger

    Es importante documentar nuestra API, por ello usaremos esta herramienta

    ```python
    pip install drf-yasg
    ```

## Iniciando el desarrollo nuestra aplicación

1. Modelo

   El modelo es aquel que interactua con la base de datos, es la representación de nuestra entidad, en este caso nuestro students

   En el archivo models.py crearemos el modelo student (por convención en singular)

   ```python
   class Student(models.Model):
    name = models.CharField(max_length=200)
    identification = models.CharField(max_length=30)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   ```

   Una vez hecho en la terminal podemos ejecutar la migración:

   ```python
   python3 manage.py makemigrations students
   ```

   Esto creará la migración dentro de ```students/migrations```un archivo nuevo llamado ```0001_initial.py``` donde estará el contenido de los datos a crear

   Ahora si ejecutamos la migración

   ```python
   python3 manage.py migrate students
   ```

   Se creó en la base de datos (por defecto sqlite3)

2. Crear un super usuario para el panel de administración

   Django cuenta con un panel de administración donde puedo interactuar con los modelos creados, para ello vamos primero a crear un super usuario:

   ```python
   python3 manage.py createsuperuser
   ```

   Esto nos pedira un usuario, correo, clave y repetir clave. Una vez creados podemos ejecutar el servidor

   ```python
   python3 manage.py runserver
   ```

   Ahora entramos a ```http://localhost:8000/admin```con el usuario y clave creado

3. Registrar el modelo en el admin.py de nuestra app students:

   ```python
   from .models import Student
   
   admin.site.register(Student)
   ```

   Con esto ya podremos interactuar con nuestro modelo en el admin de django
