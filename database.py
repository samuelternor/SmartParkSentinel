
import sqlite3

DATABASE_NAME = "smartpark.db"


def create_database():
    with sqlite3.connect(DATABASE_NAME) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS vehicles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                plate TEXT NOT NULL,
                hours_parked INTEGER NOT NULL,
                status TEXT NOT NULL
            )
        """)


def add_vehicle(plate, hours_parked, status):
    with sqlite3.connect(DATABASE_NAME) as connection:
        cursor = connection.execute(
            "INSERT INTO vehicles (plate, hours_parked, status) VALUES (?, ?, ?)",
            (plate, hours_parked, status)
        )
        return cursor.lastrowid


def get_vehicles():
    with sqlite3.connect(DATABASE_NAME) as connection:
        cursor = connection.execute(
            "SELECT id, plate, hours_parked, status FROM vehicles ORDER BY id"
        )
        return cursor.fetchall()
