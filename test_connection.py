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
database = os.getenv('MYSQL_DATABASE')
port = int(os.getenv('MYSQL_PORT'))

print(f"Attempting to connect to MySQL database:")
print(f"Host: {host}")
print(f"Port: {port}")
print(f"User: {user}")
print(f"Database: {database}")

try:
    # Attempt to establish a connection
    connection = pymysql.connect(
        host=host,
        user=user,
        password="Malcolm.k",
        database=database,
        port=port
    )
    
    # If connection is successful
    print("\nConnection successful!")
    print("MySQL server info:", connection.get_server_info())
    
    # Test a simple query
    with connection.cursor() as cursor:
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        print(f"MySQL version: {version[0]}")
    
    # Close the connection
    connection.close()
    print("Connection closed.")
    
except pymysql.MySQLError as e:
    print(f"\nError connecting to MySQL: {e}")
    sys.exit(1)
