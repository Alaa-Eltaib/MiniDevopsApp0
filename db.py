import mysql.connector
import time

def get_connection():
    return mysql.connector.connect(
        host="db",
        user="root",
        password="root",
        database="mydb"
    )


def wait_for_db():
    while True:
        try:
            conn = get_connection()
            conn.close()
            break
        except:
            print("Waiting for database...")
            time.sleep(2)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            email VARCHAR(255)
        )
    """)
    conn.commit()
    conn.close()