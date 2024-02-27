import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Создайте соединение
conn = psycopg2.connect(
    dbname="site",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)

# Создайте курсор для выполнения SQL-запросов
cur = conn.cursor()
# SQL query to select data from the table
select_query = "SELECT id, name FROM certs;"

# Execute the query
cur.execute(select_query)

# Fetch all the rows
rows = cur.fetchall()
spa_id=0
holy_id=0
attra_id=0
for row in rows:
    id,name=row
    if name =="spa":
        spa_id=id
    if name== "holidays":
        holy_id=id
    if name == "attraction":
        attra_id=id


zapros2=F"""insert into sklad (cert_id, count)
values
({spa_id},400),
({holy_id},500),
({attra_id},600);
"""
cur.execute(zapros2)

conn.commit()

cur.close()
conn.close()