"""Ejemplos de uso de cursores con la DBAPI psycopg2"""
import psycopg2

connection = psycopg2.connect('dbname=pru user=postgres')

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS table2;')

cursor.execute('''
  CREATE TABLE table2 (
    id INTEGER PRIMARY KEY,
    completed BOOLEAN NOT NULL DEFAULT False
  );
''')

cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (1, True))

SQL = 'INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);'

data = {
  'id': 2,
  'completed': False
}
cursor.execute(SQL, data)

#cursores son iterables
cursor.execute('SELECT * from table2;')
result = cursor.fetchall()
print(result)

cursor.execute("INSERT INTO table2 (id, completed) VALUES (%s,%s);", (3,True))

cursor.execute('SELECT * from table2;')

result2 = cursor.fetchone()
print('fetchone ' , result2)

result = cursor.fetchmany(2)
print('fetchmany ' , result)

result3 = cursor.fetchone()
print('fetchone ' , result3)

connection.commit()

connection.close()
cursor.close()