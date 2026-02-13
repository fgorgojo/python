# SAMPLE VERSION OF TODO APP
This app is written in Python with Flask and SQLAlchemy, as a part of the Udacity's Full Stack Web Developer Nanodegree program.

## A. Dependency
In order to run this app, the following dependencies must have been already installed:
1. Postgres. 
 * Start manually: `pg_ctl -D /usr/local/var/postgres start`
 * Stop manually: `pg_ctl -D /usr/local/var/postgres stop -s -m fast`
 
2. Flask

## B. Database 
The database relations `todos(id, description, complete, list_id)` and `todolists(id, name)` must have been already created in Postgres. We have assumed that the Postgres is running on default port 5432.

* `dropdb todoapp -p 5432 && createdb todoapp -p 5432` 
* Open the database prompt - `psql -p 5432`
* Connect to the database - `\c todoapp` 
* Displays the tables in the database `\dt` 
* Displays the schema of the 'todos' table `\d todos` 
* Displays the schema of the 'todolists' table `\d todolists` 

You can insert a few rows in both the tables. Insert first in the `todolists` relation. 


## C. Steps to Run the App: 
* `python3 -m venv env` set the virtual environment for Pyhton 
* `source env/bin/activate` activate the venv
* `python -m pip install -r requirements.txt` to install dependencies. For Mac users, if you face difficulty in installing the `psycopg2`, you may consider intalling the `sudo brew install libpq` before running the `requirement.txt`. 
* `python3 app.py` to run the app (http://127.0.0.1:5000/ or http://localhost:5000)
* `deactivate` de-activate the virtual environment


----- REORGANIZAR ESTO DI DA TIEMPO --------------
## Development 
- En el desarrollo con windows, la interaccion ORM se tiene que hacer con el contexto de la app:
Tanto en la ejecución normal como con la interactiva con python ó ipython
```
with app.app_context():
    db.createall()
    db.session.add(person)
```
En otro caso obtendríamos un error como este:
with app.app_context():

```
RuntimeError: Working outside of application context.

This typically means that you attempted to use functionality that needed
the current application. To solve this, set up an application context
with app.app_context(). See the documentation for more information.
```

- Esto evita un warning en Linux ( no ocurre en Windows ) 
```app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False ```

- Ejecutar desde la consola: Dentro del proyecto app de fullstack
("PS C:\Users\f.gorgojo.marugan\workspace\PYTHON\python\Udacity\fullstack\todoap")
```
$ cd todoapp
$ export FLASK_APP=app.py  PowerShell: $env:FLASK_APP = "app.py"
$ export FLASK_DEBUG=true  PowerShell: $env:FLASK_DEBUG = "true"
$ flask run
```
Ejecutando así funciona, pero no ejecuta la parte del main de app.py ( No se ejecuta directamete)

## BASE DE DATOS: PostGres-16
 - Instalada en local sin instalador de windows.
   Se instala la 16 porque consejo de chatGpt frente a la 18.
   ```$env:PATH = "C:\install\postgres-16\bin;" + $env:PATH ```
   
   El usuario es el genérico y no le ponemos password. 
   ```plsql -U 'postgres' ```
 
 - Se pueden crear , borrar e interactuar con las bases de datos de postgres:
```
(virtual) PS C:\Users\f.gorgojo.marugan\workspace\PYTHON\python> dropdb -U 'postgres' todoapp
dropdb: error: database removal failed: ERROR:  no existe la base de datos Â«todoappÂ»
(virtual) PS C:\Users\f.gorgojo.marugan\workspace\PYTHON\python> createdb -U 'postgres' todoapp
(virtual) PS C:\Users\f.gorgojo.marugan\workspace\PYTHON\python> 
```
 - Inicializacion de la base de datos ( solo al principio)
 ```C:\install\postgres-16\bin\initdb.exe -D C:\Install\postgres-16-data -U postgres -E UTF8```


 - Arranque de la base de datos
```C:\install\postgres-16\bin\pg_ctl.exe -D C:\Install\postgres-16-data start```

 - Estado de la base de datos
```C:\install\postgres-16\bin\pg_ctl.exe -D C:\Install\postgres-16-data status```

 - Parada de la base de datos
```C:\install\postgres-16\bin\pg_ctl.exe -D C:\Install\postgres-16-data stop```

# Procedimiento de migration 
## Inicializar base de datos
- Agregar ruta de ejecutables de postgres al PATH (en PowerShell) 
```$env:PATH = "C:\install\postgres-16\bin;" + $env:PATH```
up
 - Borrar y crear una base de datos
```
dropdb -U 'postgres' todoapp
createdb -U 'postgres' todoapp
```

## Procedimiento FLASK migration
 - Flask-Migrate (flask_migrate) is our migration manager for migrating SQLALchemy-based database changes:  ```pip install Flask-Migrate```
 - Flask-Script (flask_script) lets us run migration scripts we defined, from the terminal

 ## Steps to get migrations going
1. Initialize the migration repository structure for storing migrations
 - cd todoapp (ruta del proyecto); ```flask db init```
   Crea la estructura de migración **(migration)** dentro del proyecto.
2. Create a migration script (using Flask-Migrate)
 - La primera vez re-creamos o generamos base de datos nueva. **Manda el codigo**
 - El resto de las veces: ```flask db migrate```
3. (Manually) Run the migration script (using Flask-Script)
 - Ejecutamos con ```flask db upgrade``` , que ejecuta el método upgrade de la última versión
 - Caso de quere revertir los cambios, ejecutaríamos ```flask db downgrade```

 ## Steps using python interactive or ipython
 
 ### Creating a n:m relation 
 


