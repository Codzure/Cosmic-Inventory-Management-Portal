import os
from dotenv import load_dotenv
import pymysql
import sys

# Load environment variables
load_dotenv()

# Get database connection parameters from environment variables
host = os.getenv('MYSQL_HOST')
user = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_PASSWORD')
port = int(os.getenv('MYSQL_PORT'))

print(f"Attempting to connect to MySQL to create database:")
print(f"Host: {host}")
print(f"Port: {port}")
print(f"User: {user}")

try:
    # Connect to MySQL server without specifying a database
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        port=port
    )
    
    # Create a cursor
    with connection.cursor() as cursor:
        # Create the 'stocks' database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS stocks")
        print("Database 'stocks' created or already exists")
        
        # Use the 'stocks' database
        cursor.execute("USE stocks")
        
        # Create the 'user' table if it doesn't exist
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS user (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL UNIQUE,
            email VARCHAR(100) NOT NULL UNIQUE,
            password_hash VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        print("Table 'user' created or already exists")
        
        # Create the 'item' table if it doesn't exist
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
        print("Table 'item' created or already exists")
    
    # Commit the changes
    connection.commit()
    print("Database setup completed successfully!")
    
    # Close the connection
    connection.close()
    
except pymysql.MySQLError as e:
    print(f"Error: {e}")
    sys.exit(1)
