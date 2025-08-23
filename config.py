# config.py
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host='localhost',
        user='libra_user',
        password='libra_pass',
        database='libratrack_db'
    )
