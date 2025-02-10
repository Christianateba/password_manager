import sqlite3
from cryptography.fernet import Fernet
import os

class PasswordStorage:
    def __init__(self, db_name="passwords.db", key_file="key.key"):
        self.db_name = db_name
        self.key_file = key_file
        self.key = self.load_or_generate_key()
        self.cipher = Fernet(self.key)
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def load_or_generate_key(self):
        if os.path.exists(self.key_file):
            with open(self.key_file, "rb") as key_file:
                return key_file.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, "wb") as key_file:
                key_file.write(key)
            return key

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS passwords (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                service TEXT UNIQUE,
                encrypted_password TEXT
            )
        """
        )
        self.conn.commit()

    def add_password(self, service, password):
        encrypted_password = self.cipher.encrypt(password.encode()).decode()
        self.cursor.execute("REPLACE INTO passwords (service, encrypted_password) VALUES (?, ?)", (service, encrypted_password))
        self.conn.commit()

    def get_password(self, service):
        self.cursor.execute("SELECT encrypted_password FROM passwords WHERE service = ?", (service,))
        result = self.cursor.fetchone()
        if result:
            return self.cipher.decrypt(result[0].encode()).decode()
        return None

    def close_connection(self):
        self.conn.close()

if __name__ == "__main__":
    storage = PasswordStorage()
    storage.add_password("example.com", "mypassword123")
    print("Retrieved password:", storage.get_password("example.com"))
