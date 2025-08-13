import sqlite3

DB_NAME = "students.db"

def create_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn
