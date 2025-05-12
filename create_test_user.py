import os
from dotenv import load_dotenv
import pymysql
from utils.security import hash_password, get_db_password
import sys

# Load environment variables
load_dotenv()

# Get database connection parameters from environment variables
host = os.getenv('MYSQL_HOST')
user = os.getenv('MYSQL_USER')
db_password = get_db_password()
port = int(os.getenv('MYSQL_PORT'))
database = os.getenv('MYSQL_DATABASE', 'stocks')

# Test user credentials
test_username = "admin"
test_email = "admin@example.com"
test_password = "password123"  # This will be hashed before storing

print(f"Attempting to connect to MySQL to create test user:")
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
        # Check if user already exists
        cursor.execute("SELECT id FROM user WHERE username = %s OR email = %s", (test_username, test_email))
        existing_user = cursor.fetchone()
        
        if existing_user:
            print(f"User '{test_username}' already exists.")
        else:
            # Hash the password
            hashed_password = hash_password(test_password)
            
            # Insert the test user
            cursor.execute(
                "INSERT INTO user (username, email, password_hash) VALUES (%s, %s, %s)",
                (test_username, test_email, hashed_password)
            )
            
            # Commit the changes
            connection.commit()
            print(f"Test user '{test_username}' created successfully!")
            print(f"Username: {test_username}")
            print(f"Password: {test_password}")
    
    # Close the connection
    connection.close()
    
except pymysql.MySQLError as e:
    print(f"Error: {e}")
    sys.exit(1)
