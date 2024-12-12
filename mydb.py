import psycopg2
from psycopg2 import sql

# Подключение к PostgreSQL
try:
    connection = psycopg2.connect(
        host="localhost",
        user="postgres",   # Укажите имя пользователя PostgreSQL
        password="1111"    # Укажите ваш пароль
    )

    connection.autocommit = True  # Для выполнения команды CREATE DATABASE без транзакции

    # Создание курсора
    cursor = connection.cursor()

    # Создание базы данных
    cursor.execute(sql.SQL("CREATE DATABASE elderco"))

    print("All Done!")

except psycopg2.Error as e:
    print(f"Error: {e}")
finally:
    # Закрытие соединения
    if connection:
        cursor.close()
        connection.close()
