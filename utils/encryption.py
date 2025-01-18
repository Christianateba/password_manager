from cryptography.fernet import Fernet # type: ignore

KEY_FILE = "key.key"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)

def load_key():
    if not os.path.exists(KEY_FILE):
        generate_key()
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()

def encrypt_message(message):
    key = load_key()
    fernet = Fernet(key)
    return fernet.encrypt(message.encode()).decode()

def decrypt_message(encrypted_message):
    key = load_key()
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_message.encode()).decode()
