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

zapros="""insert into certs (name, price, description, photo)
values 
('spa', 400, 'Расслабиться в спа', 'serd1.jpg'),
('holidays', 6000, 'поездка на природу','serd2.jpg'),
('attraction', 300,'Поездка в парк развлечений', 'serd3.jpg');
"""
cur.execute(zapros)
# Закоммитить изменения
conn.commit()

cur.close()
conn.close()


