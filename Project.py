import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

# Function to generate and write a new encryption key to a file
def write_key():
    key1 = Fernet.generate_key()
    with open('key.key', 'wb') as kf:
        kf.write(key1)

# Function to load the encryption key from a file
def load_key():
    with open('key.key', 'rb') as file:
        key2 = file.read()
    return key2

# Function to derive a Fernet key from the master password and the loaded key
def derive_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

# Get the master password from the user
master_pass = input("What is the master password: ")

# Load the encryption key (salt) and derive the Fernet key
salt = load_key()
key = derive_key(master_pass, salt)

# Initialize the Fernet encryption object
fer = Fernet(key)

# Function to view decrypted passwords
def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            plt, name, passw = data.split("|")
            b = passw.encode()
            decrypted_data = fer.decrypt(b)
            print("Platform :", plt, "| user :", name, "| password :", decrypted_data.decode())

# Function to add a new password
def add():
    plt = input("Enter the Platform: ")
    name = input("Account name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        data = pwd.encode()
        encrypted_data = fer.encrypt(data)
        f.write(plt + "|" + name + "|" + encrypted_data.decode() + "\n")
        print("New Login details successfully added!")

# Main loop to interact with the user and validate whether the master_password matches with brecw
while master_pass == "brecw":
    mode = input("Would you like to add a new password or view existing ones (view, add) and press q to quit ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue
else:
    print("Incorrect Password")
    quit
