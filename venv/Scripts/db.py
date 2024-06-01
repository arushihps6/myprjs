import mysql.connector
from mysql.connector import Error

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',       # Replace with your database username
            password='admin',  # Replace with your database password
            database='db'      # Replace with your database name
        )
        if connection.is_connected():
            print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")
