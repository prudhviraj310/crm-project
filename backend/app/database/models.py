from .connection import create_connection

def create_tables():
    conn = create_connection()
    if conn:
        cursor = conn.cursor()

        # Users
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            email VARCHAR(255),
            password VARCHAR(255)
        );
        """)

        # Leads
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS leads (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            email VARCHAR(255),
            phone VARCHAR(20),
            status VARCHAR(50),
            source VARCHAR(100),
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            user_id INT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
        """)

        # Deals
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS deals (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255),
            value DECIMAL(10, 2),
            stage VARCHAR(50),
            lead_id INT,
            user_id INT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (lead_id) REFERENCES leads(id),
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
        """)

        # Tasks
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255),
            description TEXT,
            due_date DATE,
            status VARCHAR(50),
            lead_id INT,
            user_id INT,
            FOREIGN KEY (lead_id) REFERENCES leads(id),
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
        """)

        conn.commit()
        conn.close()
        print("✅ All tables created successfully.")
    else:
        print("❌ Failed to create tables: No database connection.")
