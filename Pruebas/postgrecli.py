"""POSTGRE
Instalacion: Binary zip C:\Install\postgres-16
Inicialización:  
  C:\install\postgres-16\bin\initdb.exe -D C:\Install\postgres-16-data -U postgres -E UTF8
Arranque servidor:
  C:\install\postgres-16\bin\pg_ctl.exe -D C:\Install\postgres-16-data start
Estado servidor:
  C:\install\postgres-16\bin\pg_ctl.exe -D C:\Install\postgres-16-data status
Parada servidor:
    C:\install\postgres-16\bin\pg_ctl.exe -D C:\Install\postgres-16-data stop
.\pg_ctl.exe -D C:\Install\postgres-16-data start
-- nota: No tiene password en local, ni servcio creado como windows. Para crear un servicio:
  C:\install\postgres-16\bin\pg_ctl.exe register -N "PostgreSQL 16" -D C:\Install\postgres-16-data -U postgres -P <password> -w
  net start "PostgreSQL 16"
Conexion a BD:
    C:\install\postgres-16\bin\psql.exe -U postgres -d postgres -h localhost -p 5432

For python : pip install psycopg2-binary
"""

import psycopg2

conn = psycopg2.connect('dbname=pru user=postgres')
#conn = psycopg2.connect('dbname=example')

cursor = conn.cursor()

## Open a cursor to perform database operations
cur = conn.cursor()

## drop any existing todos table
cur.execute("DROP TABLE IF EXISTS todos;")

## (re)create the todos table
## (note: triple quotes allow multiline text in python)
cur.execute("""
  CREATE TABLE todos (
    id serial PRIMARY KEY,
    description VARCHAR NOT NULL
  );
""")

## commit, so it does the executions on the db and persists in the db
conn.commit()

cur.close()
conn.close()


