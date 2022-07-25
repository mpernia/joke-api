# joke-api
FastAPI demo

## Descripción
API Rest desarrollada con el framework [**FastAPI**](https://fastapi.tiangolo.com/) como parte de la 
[prueba técnica](public/Reto_python-jun22.pdf)

### Estructura del proyecto
Paquetes:
* **config**: configuración global del proyecto
* **models**: definición de los modelos para la persistencia de los datos
* **repositories**: repositorios para la gestón de los modelos
* **routes**: rutas del proyecto
* **schemas**: esquemas de los recursos de la API
* **services**: servicios para la lógica del negocio
    

## Instalación
Ejecuta el siguiente comando en la terminal:

```shell
$ pip install -r requirements.txt
```

<blockquote>
El comando anterior debe ejecutarse en el directorio dónde se encuentra el archivo requirements.txt.
</blockquote>

## Configuración

Ejecute el siguiente comando para hacer una copia del fichero de configuración:
```shell
cp .env.example .env
```


### Base de Datos

En el proyecto puede utilizar las siguientes bases de datos:
* MySQL
* SQLite
* PosgreSql
* MongoDB


Edite el fichero ``.env`` sustituya el valor del parámetro ``DB_CONNECTION`` por el que corresponda según la siguiente relación:
* **MySQL** -> _mysql_
* **SQLite** -> _sqlite_
* **PosgreSql** -> _pgsql_
* **MongoDB** -> _mongodb_

Modifique los valores para la conexión a la base de datos:
* DB_HOST
* DB_USER
* DB_PASSWORD
* DB_NAME


## Ejecución

Luego de instalados las dependencias y definida la configuraciópn de conexión a la base de datos, desde el directorio raíz del proyecto ejecute el comando:

```shell
python3 ./main.py
```

