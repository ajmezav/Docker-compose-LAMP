## Reto MELI
## Johan Estevan Berrio Estrada

### API

Se desarrolla una API en lenguaje Python y haciendo uso del framework Django. Dicha API tiene 7 endpoints (5 solicitados en el reto y 2 más) y es subida a un dockerfile.

A tráves de Django se pueden generar unas tablas de permisos, usuarios y grupos; unas tablas que asocian los usuarios con los permisos y grupos, y otras tablas que albergan información sobre logs, migraciones y datos de inicio de sección. La API se conecta a una base de datos MYSQL denominada django_api, en esta base de datos se almacenan los permisos que se van creando a tráves del endpoint de creación de permisos, en la tabla auth_permission; se almacenan tambíen los usuarios a tráves de un endpoint de creación de usuarios, en la tabla auth_user; y finalmente, la tabla auth_user_user_permissions almacena la relación entre los usuarios y los permisos.


![diagrama-arquitectura](https://user-images.githubusercontent.com/61033029/162891360-b2b615cf-a5d0-44fb-8114-1fca1c3b8277.jpg)


### Endpoint de creación de permisos: 
http://127.0.0.1:8000/api/permissions/create

Este Endpoint se configura para crear permisos en la base de datos.
Se hace uso de un JSON para ingresar los atributos del permiso a crear.
![image](https://user-images.githubusercontent.com/61033029/162867652-a39e16f8-d01b-47e5-8061-d0a90f6b787e.png)





### Endpoint de actualización de permisos:
http://127.0.0.1:8000/api/permissions/update/43

Este Endpoint permite actualizar un permiso, cambiando su nombre y/ código. El número 43 es simplemente un id de la tabla de permisos que representa un permiso.Puede ser cualquiera.


![image](https://user-images.githubusercontent.com/61033029/162868858-0eeb7bb0-bbc6-4b1d-90de-e2cb333ea34c.png)




### Endpoint de visualización de permisos:
http://127.0.0.1:8000/api/permissions/

Este Endpoint permite visualizar la lista de permisos almacenada en la base de datos
![image](https://user-images.githubusercontent.com/61033029/162870252-1f046979-0873-496b-963b-7ba2336fc782.png)




### Endpoint de asignación de permisos a usuarios:
http://127.0.0.1:8000/api/users/update/15

Este Endpoint está configurado para que se asignen permisos a un usuario. En la URL el número 15 es el id de la tabla de usuarios que representa un usuario único.
Se hace uso de un JSON para enviar los valores de la columna de permisos que se desean asignar y el valor de la columna de usuario al que se le desea asignar el permiso.

![image](https://user-images.githubusercontent.com/61033029/162871840-f2b198af-a496-4d91-88b1-4411f3b18030.png)





### Endpoint de eliminación de permisos a un usuario:
http://127.0.0.1:8000/api/users/remove/8

Este Endpoint permite eliminar un permiso asociado a un usuario. En la URL el número 8 es el id de la tabla de usuarios que representa un usuario único.
![image](https://user-images.githubusercontent.com/61033029/162872620-2ab2b9cf-95b2-4baf-8464-3b04780b9649.png)




### Endpoint de creación de usuarios:
http://127.0.0.1:8000/api/users/create/

Este Endpoint está configurado para crear usuarios en la base de datos.
![image](https://user-images.githubusercontent.com/61033029/162873596-eeff4820-97a2-4645-a126-1c1fca929a03.png)




### Endpoint de visualización de usuarios:
http://127.0.0.1:8000/api/users/

A través de ete Endpoint se puede visualizar la lista de usuarios almacenada en la base de datos.
![image](https://user-images.githubusercontent.com/61033029/162874751-24cd84af-3e6b-49ce-87f7-6a885a77a5e9.png)


### Base de Datos

Se crea una base de datos haciendo uso de Mysql y de las credenciales que son User: root y Password: 'meli.2022'. En esta base de datos se encontraran varias tablas generadas a tráves de la migración que se hace con Django, y dichas tablas pueden ser modificadas desde los Enpoint de creación y actualización. Entre estas tablas se encuentran: auth_permission, auth_user y auth_user_user_permission; que son las tablas que se usan para la creación de la API.

![image](https://user-images.githubusercontent.com/61033029/162876235-d79b86da-37fc-4b7f-800e-33a6243f074a.png)

#### Asignación de varios permisos a un usuario y un permiso asignado a varios usuarios

![image](https://user-images.githubusercontent.com/61033029/162886630-5ba537c4-515e-454b-8052-dde29a61a331.png)


Las tablas auth_group, auth_group_permissions, auth_user_groups, django_admin_log, django_content_type, django_migrations y django_session son irrelevantes y no se usan dentro del reto. Las tablas api_permission y api_user fueron creadas a partir de modelos creados en models.py, pero se decidieron no utilizar ya que no se hallaron formas "fáciles y eficientes" de asignar los permisos a los usuarios, por lo que se usan las tablas auth_permission y auth_user generadas con django.

### Pruebas unitarias

Se realizan pruebas unitarias triviales haciendo uso de Pytest, ya que este framework de python permite la escalabilidad del proyecto y con un simple comando se puede observar con algo de detalle si nuestra aplicación tiene errores, alertas o fallas.


### Paso a Paso para la creación de la API

1. Creación de carpeta donde se almacenará el proyecto, denominada API_REST. 
2. Ubicación de la carpeta del proyecto creada dentro del editor de código (Visual studio Code, en mi caso)
3. Apertura de terminal en editor de código o consola de comandos de elección.
4. Creación y activación de entorno virtual (opcional), comandos: virtualenv -p python3 env  |  .\env\Scripts\activate 
5. Instalación del framework django, comando: pip install Django == x.y.z (donde x.y.z es el número de la versión, que en este caso es 3.2.4)
6. Creación del proyecto en django, comando: django-admin startproject nombredelproyecto (que en este caso nombre del proyecto es Challenge_IAM)
7. Acceso al proyecto, comando: cd .\proyecto\ (donde proyecto en este caso es Challenge_IAM)
8. Creación de la carpeta que contiene las aplicaciones, comando: django-admin startapp nombre de la app (donde nombre de la app es api en este caso)
9. Configuración de los parámetros para la conección con la base de datos Mysql. Esto se realiza dentro del archivo settings.py en la sección DATABASES
10. Instalación del cliente mysql para la comunicación con la base de datos, comando: pip install mysqlclient pymysql
11. Confirmación de la conección con la base de datos, comando: python manage.py migrations
12. Creación de superusuario para poder acceder al panel de administración, comando: python manage.py createsuperuser. Se ingresan las credenciales de usuario y contraseña.
13. Migración del modelo a la base de datos, comando: python manage.py makemigrations
14. Confirmación la migración, comando: python manage.py migrations
15. Ejecución del servidor, comando: python manage.py runserver
16. Acceso al localhost en http://127.0.0.1:8000


### Creación de los contenedores por separado

Parado en la ruta de Docker donde estan los archivos:
Para construir la imagen de la api:
docker build -f Dockerfile-api -t api-meli:0.1 .

Para construir la imagen de la db:
docker build -f Dockerfile-bd -t bd-meli:0.1 .


### Uso de la API desde Docker-Compose

Para correr el Docker-Compose se hace uso del comando: docker-compose up-d

![image](https://user-images.githubusercontent.com/61033029/163100763-9ac425b3-a0cc-4650-9e13-08a1b7e75fbf.png)

En la barra de direcciones del navegador se ingresan las URL especificadas en los Endpoints para hacer uso de la API.





