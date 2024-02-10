import psycopg2

# Создайте соединение
conn = psycopg2.connect(
    dbname="your_database",
    user="your_username",
    password="your_password",
    host="localhost",
    port="5432"
)

# Создайте курсор для выполнения SQL-запросов
cur = conn.cursor()

# SQL-запросы для создания таблиц
create_table_query1 = """
CREATE TABLE table1 (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
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