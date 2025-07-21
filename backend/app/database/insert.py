# insert.py
from app.database.connection import create_connection

def insert_user(name, email, phone):
    try:
        conn = create_connection()
        cursor = conn.cursor()

        query = "INSERT INTO users (name, email, phone) VALUES (%s, %s, %s)"
        values = (name, email, phone)

        cursor.execute(query, values)
        conn.commit()

        print("✅ User inserted successfully.")

    except Exception as e:
        print("❌ Error inserting user:", e)

    finally:
        cursor.close()
        conn.close()

# Example insert
if __name__ == "__main__":
    insert_user("Prudhvi Raj", "prudhvi@example.com", "9949872039")
