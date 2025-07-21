import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

load_dotenv()  # ✅ This loads variables from .env

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print(f"✅ Connected to MySQL Server version {db_Info}")
            return connection

    except Error as e:
        print(f"❌ Error while connecting to MySQL: {e}")

    return connection
