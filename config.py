import os

DATABASE_USER = os.getenv("DB_USER", default="root")
DATABASE_PASSWORD = os.getenv("DB_PASSWORD", default="qwerty123")
DATABASE_HOST = "localhost"
DATABASE_NAME = os.getenv("DB_NAME", default="car_db")

# Ссылка на базу данных
MYSQL_URL = f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}"

CSV_FILE_NAME = "mashina_kg.csv"


