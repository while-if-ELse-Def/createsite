import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Параметры соединения
params = {
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": "5432"
}

# Создайте соединение
conn = psycopg2.connect(**params)

# Установите уровень изоляции для автокоммита
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Создайте курсор для выполнения SQL-запросов
cur = conn.cursor()

# Имя новой базы данных
dbname = "site"

# SQL-запрос для создания новой базы данных
create_db_query = f"CREATE DATABASE {dbname};"


# Выполните SQL-запрос

cur.execute(create_db_query)
# Закоммитить изменения
conn.commit()

# Закрыть курсор и соединение
cur.close()
conn.close()
# Создайте соединение
conn = psycopg2.connect(
    dbname=dbname,
    user="C",
    password="postgres",
    host="localhost",
    port="5432"
)

# Создайте курсор для выполнения SQL-запросов
cur = conn.cursor()

# SQL-запросы для создания таблиц
create_table_query1 = """
CREATE TABLE certs (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price NUMERIC(10,2) NOT NULL,
    description VARCHAR(1000) NULL,
    
);
"""

create_table_query2 = """
CREATE TABLE table2 (
    id SERIAL PRIMARY KEY,
    address VARCHAR(255) NOT NULL,
    phone VARCHAR(50) NOT NULL
);
"""

# Выполните SQL-запросы
cur.execute(create_table_query1)
cur.execute(create_table_query2)

# Закоммитить изменения
conn.commit()

# Закрыть курсор и соединение
cur.close()
conn.close()