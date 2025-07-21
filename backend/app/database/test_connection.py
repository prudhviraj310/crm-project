import mysql.connector

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="yourpassword",  # << this is the problem
            database="your_db_name"
        )
        print("✅ Connected to MySQL database")
        return connection
    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")
        return None

