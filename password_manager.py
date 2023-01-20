import hashlib
import getpass

# Dictionary to store username and hashed password
password_db = {}

def create_account():
    # Prompt user for a new username and password
    username = input("Enter a new username: ")
    password = getpass.getpass("Enter a new password: ")

    # Hash the password using sha256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Add the new account to the password database
    password_db[username] = hashed_password

def login():
    # Prompt user for their username and password
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    # Check if the username exists in the password database
    if username in password_db:
        # Hash the entered password and compare it to the stored hashed password
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if password_db[username] == hashed_password:
            print("Access granted.")
        else:
            print("Incorrect password.")
    else:
        print("Username not found.")

# Main menu
while True:
    print("1. Create a new account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Invalid choice.")
