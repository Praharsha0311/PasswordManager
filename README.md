# Project Description
The Password Manager is a secure application designed to store and manage user passwords efficiently. Utilizing robust encryption techniques, this application ensures that users' sensitive information remains protected from unauthorized access. 
# Features
1. **Encryption**:
    - Uses strong encryption to keep your passwords safe.
    - Passwords are encrypted before storing and decrypted when you need them.

2. **Master Password**:
    - A master password protects access to your stored passwords.
    - The master password is combined with an encryption key to secure your data.

3. **Store and Retrieve Passwords**:
    - You can add new passwords by entering the platform, account name, and password.
    - View your stored passwords in a readable format.

4. **Easy to Use**:
    - Simple command-line interface.
    - Choose to add new passwords or view existing ones.

## Technical Details

- **Language**: Python
- **Libraries**: `cryptography` for encryption
- **Files**:
  - `key.key`: Stores the encryption key.
  - `passwords.txt`: Stores the encrypted passwords.

## How It Works

1. **Generate Encryption Key**:
    - Run a function to generate and save an encryption key.

2. **Load Encryption Key**:
    - Read the encryption key from the file.

3. **Derive Fernet Key**:
    - Combine the master password and encryption key to create a secure key.

4. **Encrypt and Decrypt Passwords**:
    - Encrypt passwords before saving and decrypt them when viewing.

## Acknowledgments

- Thanks to the `cryptography` library for encryption tools.
