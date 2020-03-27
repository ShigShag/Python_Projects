from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from tkinter.filedialog import askopenfilename
from os import path
from sys import exit


class Settings:
    # Variables 
    cycles = 10
    string_path = r"G:\Python_Projects\Constants\String.txt"
    
    @staticmethod
    def change_settings():
        user_input = ""
        while user_input != "3" and user_input != "exit":
            print("[1] Change cycles for hardcore encryption\n"
                  "[2] Change password\n"
                  "[3] Exit settings")
            user_input = input("> ")

            if user_input == "1":
                value_input = input("> ")
                Settings.cycles = int(value_input)

            if user_input == "2":
                print("Enter old password")
                Settings.change_password(input("> "))

    @staticmethod
    def change_password(old_password):
        if decrypt(old_password, Settings.string_path):
            print("Enter new password")
            new_password = input("> ")

            salt = get_random_bytes(32)
            new_key = PBKDF2(new_password, salt, dkLen=32)
            if encrypt(new_key, salt, Settings.string_path):
                print("Password changed")
                return True
            else:
                return False
        else:
            return False


def main():
    print("[1] Crypt file\n"
          "[2] Decrypt file\n"
          "\n"
          "[3] Hardcore encrypt file\n"
          "[4] Hardcore decrypt file\n"
          "\n"
          "[5] Settings\n"
          "[6] Exit")

    user_input = input("> ")

    # Encrypt

    if user_input == "1":
        print("Enter Path:")
        file_path = input("> ")
        file_path = file_path.replace('"', '')
        if not path.exists(file_path):
            print("File not found, choose manually")
            file_path = askopenfilename()
            if not path.exists(file_path):
                print("File not found")
                return True
        print("Enter password to encrypt")
        user_input = input("> ")
        default_key, default_salt = keygen(user_input)
        if encrypt(default_key, default_salt, file_path):
            print("Encryption finished")
        else:
            print("Encryption failed")
        return True

    # Decrypt

    elif user_input == "2":
        print("Enter Path:")
        file_path = input("> ")
        file_path = file_path.replace('"', '')
        if not path.exists(file_path):
            print("File not found, choose manually")
            file_path = askopenfilename()
            if not path.exists(file_path):
                print("File not found")
                return True
        print("Enter password to decrypt")
        user_input = input("> ")
        if decrypt(user_input + random_string, file_path):
            print("decryption finished")
        else:
            print("decryption failed")
        return True

    # Hardcore encrypt

    elif user_input == "3":
        letter_counter = 0
        word_cycle_counter = 0
        print("Enter Path:")
        file_path = input("> ")
        file_path = file_path.replace('"', '')
        if not path.exists(file_path):
            print("File not found, choose manually")
            file_path = askopenfilename()
            if not path.exists(file_path):
                print("File not found")
                return True
        print("Enter password to encrypt")
        user_input = input("> ")
        while word_cycle_counter < Settings.cycles:
            try:
                default_key, default_salt = keygen(user_input[letter_counter])
                if not encrypt(default_key, default_salt, file_path):
                    print("Encryption failed")
                    return True
                letter_counter += 1
            except IndexError:
                word_cycle_counter += 1
                letter_counter = 0
                continue
        print("Encryption finished")
        return True

    # Hardcore decrypt

    elif user_input == "4":
        word_cycle_counter = 0
        print("Enter Path:")
        file_path = input("> ")
        file_path = file_path.replace('"', '')
        if not path.exists(file_path):
            print("File not found, choose manually")
            file_path = askopenfilename()
            if not path.exists(file_path):
                print("File not found")
                return True
        print("Enter password to decrypt")
        user_input = input("> ")
        letter_counter = len(user_input) - 1
        while word_cycle_counter < Settings.cycles:
            if letter_counter >= 0:
                if not decrypt(user_input[letter_counter] + random_string, file_path):
                    print("Decryption failed")
                    return True
                letter_counter -= 1
            else:
                word_cycle_counter += 1
                letter_counter = len(user_input) - 1
        print("Decryption finished")
        return True

    # Settings

    elif user_input == "5":
        Settings.change_settings()
        return True

    # Exit application

    elif user_input == "6" or user_input == "exit":
        return False

    else:
        print("wrong command")
        return True


def encrypt(key, salt, file_path):
    try:
        with open(file_path, "rb")as f:
            msg = f.read()
        cipher = AES.new(key, AES.MODE_CBC)
        encrypted_message = cipher.encrypt(pad(msg, AES.block_size))
        with open(file_path, "wb")as f:
            f.write(salt)
            f.write(cipher.iv)
            f.write(encrypted_message)
        return True
    except PermissionError:
        print("Access Denied")
        return False


def decrypt(user_password, file_path, only_return_content=False, only_return_bool=False):
    # Open and read file
    try:
        with open(file_path, "rb")as f:
            salt = f.read(32)
            iv = f.read(16)
            ciphered_data = f.read()
        key = PBKDF2(user_password, salt, dkLen=32)
    except PermissionError:
        print("Access Denied")
        return False

    # Create new cipher
    try:
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    except ValueError:
        print("Data was not encrypted")
        return False

    # Unpad ciphered data
    try:
        original_date = unpad(cipher.decrypt(ciphered_data), AES.block_size)
    except ValueError:
        print("Wrong Password")
        return False

    # Return statements
    if not only_return_content and not only_return_bool:
        with open(file_path, "wb")as f:
            f.write(original_date)
        return True
    elif only_return_content:
        return str(original_date)
    elif only_return_bool:
        return True


def keygen(user_password):
    salt = get_random_bytes(32)
    return PBKDF2(user_password + random_string, salt, dkLen=32), salt


def get_string(user_password):
    string = decrypt(user_password, Settings.string_path, only_return_content=True)
    if not string:
        return False
    else:
        return string


random_string = ""
print("Enter Password")
while not random_string:
    input_user = input("> ")
    if input_user == "exit":
        exit()

    random_string = get_string(input_user)


while main():
    pass



