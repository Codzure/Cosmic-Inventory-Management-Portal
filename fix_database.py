import os
from dotenv import load_dotenv
import pymysql
from utils.security import get_db_password
import sys

# Load environment variables
load_dotenv()

# Get database connection parameters from environment variables
host = os.getenv('MYSQL_HOST')
user = os.getenv('MYSQL_USER')
db_password = get_db_password()
port = int(os.getenv('MYSQL_PORT'))
database = os.getenv('MYSQL_DATABASE', 'stocks')

print(f"Attempting to connect to MySQL to fix database schema:")
print(f"Host: {host}")
print(f"Port: {port}")
print(f"User: {user}")
print(f"Database: {database}")

try:
    # Connect to MySQL server
    connection = pymysql.connect(
        host=host,
        user=user,
        password=db_password,
        port=port,
        database=database
    )
    
    # Create a cursor
    with connection.cursor() as cursor:
        # Check if the item table exists
        cursor.execute("SHOW TABLES LIKE 'item'")
        table_exists = cursor.fetchone()
        
        if table_exists:
            # Check if user_id column exists in the item table
            cursor.execute("SHOW COLUMNS FROM item LIKE 'user_id'")
            user_id_exists = cursor.fetchone()
            
            if not user_id_exists:
                print("Adding user_id column to item table...")
                cursor.execute("ALTER TABLE item ADD COLUMN user_id INT NOT NULL")
                cursor.execute("ALTER TABLE item ADD CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE")
                print("user_id column added successfully!")
            else:
                print("user_id column already exists in item table.")
        else:
            print("Creating item table...")
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS item (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                description TEXT,
                price FLOAT NOT NULL,
                quantity INT DEFAULT 0,
                user_id INT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE
            )
            """)
            print("Table 'item' created successfully!")
        
        # Commit the changes
        connection.commit()
        print("Database schema fixed successfully!")
    
    # Close the connection
    connection.close()
    
except pymysql.MySQLError as e:
    print(f"Error: {e}")
    sys.exit(1)
