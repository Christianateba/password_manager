import os
import json

FILE_PATH = "passwords.json"

def save_password(service, username, password):
    data = get_passwords()
    data.append({"service": service, "username": username, "password": password})
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)

def get_passwords():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as file:
        return json.load(file)
