Single-database configuration for Flask.
pip install Flask-Migrate
pip install flask_alchemy
# Pasos Migration 

## Inicializar base de datos
- Agregar ruta de ejecutables de postgres al PATH (en PowerShell) 
$env:PATH = "C:\install\postgres-16\bin;" + $env:PATH

 - Borrar y crear una base de datos
dropdb -U 'postgres' todoapp
createdb -U 'postgres' todoapp

## Procedimiento FLASK migration
 - Flask-Migrate (flask_migrate) is our migration manager for migrating SQLALchemy-based database changes:  ```pip install Flask-Migrate```
 - Flask-Script (flask_script) lets us run migration scripts we defined, from the terminal

 ## Steps to get migrations going
1. Initialize the migration repository structure for storing migrations
 - cd todoapp (ruta del proyecto); ```flask db init```
   Crea la estructura de migración dentro del proyecto 
1. Create a migration script (using Flask-Migrate)
1. (Manually) Run the migration script (using Flask-Script)

