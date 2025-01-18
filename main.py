from manager.password_gen import generate_password
from manager.storage import save_password, get_passwords

def main():
    print("Password Manager")
    while True:
        print("\n1. Generate Password")
        print("2. Save Password")
        print("3. View Saved Passwords")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            length = int(input("Enter password length: "))
            password = generate_password(length)
            print(f"Generated Password: {password}")

        elif choice == "2":
            name = input("Enter service name: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            save_password(name, username, password)

        elif choice == "3":
            passwords = get_passwords()
            for item in passwords:
                print(f"Service: {item['service']}, Username: {item['username']}, Password: {item['password']}")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
