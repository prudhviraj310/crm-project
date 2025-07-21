from .connection import create_connection

def insert_sample_data():
    conn = create_connection()
    if conn:
        cursor = conn.cursor()

        # Insert a user
        cursor.execute("""
            INSERT INTO users (name, email, password)
            VALUES (%s, %s, %s)
        """, ("Chinnu", "chinnu@example.com", "securepassword"))

        # Get inserted user ID
        user_id = cursor.lastrowid

        # Insert a lead
        cursor.execute("""
            INSERT INTO leads (name, email, phone, status, source, user_id)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, ("Prudhvi Raj", "prudhvi@example.com", "9876543210", "new", "website", user_id))

        lead_id = cursor.lastrowid

        # Insert a deal
        cursor.execute("""
            INSERT INTO deals (title, value, stage, lead_id, user_id)
            VALUES (%s, %s, %s, %s, %s)
        """, ("Website Project", 50000.00, "prospecting", lead_id, user_id))

        # Insert a task
        cursor.execute("""
            INSERT INTO tasks (title, description, due_date, status, lead_id, user_id)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, ("Follow-up call", "Call the client to discuss requirements", "2025-07-20", "pending", lead_id, user_id))

        conn.commit()
        conn.close()
        print("✅ Sample data inserted successfully.")
    else:
        print("❌ Failed to insert data: No database connection.")
