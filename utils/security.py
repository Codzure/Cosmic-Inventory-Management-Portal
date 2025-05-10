import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv, set_key
import base64

def generate_key():
    """Generate a key and save it to a file"""
    key = Fernet.generate_key()
    with open(os.path.join(os.path.dirname(__file__), 'secret.key'), 'wb') as key_file:
        key_file.write(key)
    return key

def load_key():
    """Load the key from the secret.key file or generate if it doesn't exist"""
    key_path = os.path.join(os.path.dirname(__file__), 'secret.key')
    if not os.path.exists(key_path):
        return generate_key()
    with open(key_path, 'rb') as key_file:
        return key_file.read()

def encrypt_value(value):
    """Encrypt a value using the key"""
    if not value:
        return None
    
    key = load_key()
    encoded_value = value.encode()
    f = Fernet(key)
    encrypted_value = f.encrypt(encoded_value)
    # Convert to base64 string for storage in .env
    return base64.b64encode(encrypted_value).decode()

def decrypt_value(encrypted_value):
    """Decrypt a value using the key"""
    if not encrypted_value:
        return None
    
    try:
        key = load_key()
        f = Fernet(key)
        # Convert from base64 string
        decoded_value = base64.b64decode(encrypted_value.encode())
        decrypted_value = f.decrypt(decoded_value)
        return decrypted_value.decode()
    except Exception as e:
        print(f"Error decrypting value: {e}")
        return None

def encrypt_env_password():
    """Encrypt the MySQL password in the .env file"""
    load_dotenv()
    
    # Get the current password
    password = os.getenv('MYSQL_PASSWORD')
    if not password:
        print("No password found in .env file")
        return
    
    # Check if it's already encrypted (starts with 'ENC:')
    if password.startswith('ENC:'):
        print("Password is already encrypted")
        return
    
    # Encrypt the password
    encrypted_password = encrypt_value(password)
    
    # Update the .env file with the encrypted password
    env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
    set_key(env_path, 'MYSQL_PASSWORD', f"ENC:{encrypted_password}")
    
    print("Password encrypted successfully")

def get_db_password():
    """Get the decrypted database password"""
    load_dotenv()
    
    password = os.getenv('MYSQL_PASSWORD')
    if not password:
        return None
    
    # If the password is encrypted (starts with 'ENC:')
    if password.startswith('ENC:'):
        return decrypt_value(password[4:])  # Remove 'ENC:' prefix
    
    # If the password is not encrypted
    return password

if __name__ == "__main__":
    # If run directly, encrypt the password in the .env file
    encrypt_env_password()
