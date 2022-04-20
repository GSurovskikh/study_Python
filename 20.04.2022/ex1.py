import sqlite3
from pathlib import Path



WORK_DIR = Path(__file__).absolute().parent
DB_FILE_NAME = WORK_DIR / 'db.db'

#Подключение к БД
connection = sqlite3.connect(DB_FILE_NAME)
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Person (
    "person_id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "first_name" TEXT(100),
    "last_name" TEXT(100),
    "birth_date" TEXT(10)
    );
""")
cursor.execute("""
INSERT OR REPLACE 
    INTO Person(first_name,last_name,birth_date) VALUES
        ("Garry","Brown","2000-12-20"),
        ("Larry","Green","2004-10-30"),
        ("Harry","Black","2000-12-30");
""")

connection.commit() # Подтвердить отсылку запроса

people = [
    ("N1","L1","YYYY"),
    ("N12","L1","YYYY"),
    ("N13","L31","YYYY"),
    ("N2","L14","YYYY"),
]

cursor.executemany("""
INSERT OR REPLACE
    INTO Person(first_name,last_name,birth_date)
        VALUES(?,?,?);
    """,
    people
)
connection.commit()

#Запрос данных из БД
cursor.execute("""SELECT * FROM Person""")
data = cursor.fetchall()
for row in data:
    print(row)