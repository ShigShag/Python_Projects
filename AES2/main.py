import base64
import string
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from secrets import token_bytes, choice
from os import path


# backend = default_backend()

class Encrypt:

    def main(self):
        key, salt = self.generate_key()
        self.encrypt_file("test.txt", key, salt)

    def generate_key(self):
        print("Enter password")
        user_password = input("> ")
        # Pepper the user password
        user_password += choice(string.ascii_letters + string.digits)
        salt = token_bytes(16)
        kdf = PBKDF2HMAC(algorithm=hashes.SHA3_256(), length=32, salt=salt, iterations=111355, backend=default_backend())
        key = base64.urlsafe_b64encode(kdf.derive(user_password.encode()))
        return key, salt

    def check_key(self, salt):
        print("Enter password")
        user_password = input("> ")
        kdf = PBKDF2HMAC(algorithm=hashes.SHA3_256(), length=32, salt=salt, iterations=111355, backend=default_backend())

        passed = True
        for pepper in string.ascii_letters + string.digits:
            kdf.verify((user_password + pepper).encode(), )


    def encrypt_file(self, file_path, key, key_salt):
        # Check if file exists
        if not path.isfile(file_path):
            return -1

        # Split the keygen salt
        head, tail = key_salt[:8], key_salt[8:]

        # Open and read, read, close file
        file = open(file_path, "rb")

        try:
            data = file.read()
        finally:
            file.close()

        # Add the keygen salt and data to one string
        data = head + data + tail

        # Encrypt data
        method = Fernet(key)
        data = method.encrypt(data)

        # Random salt to manipulate the encrypted data
        random_salt = token_bytes(36)
        r_head, r_middle, r_tail = random_salt[:12], random_salt[12:24], random_salt[24:]

        # Split encrypted data in half
        data_head, data_tail = data[:len(data) // 2], data[len(data) // 2:]

        # Add the random salt to the encrypted string to confuse
        token = r_head + data_head + r_middle + data_tail + r_tail

        # Open, write, close file
        file = open(file_path, "wb")

        try:
            file.write(token)
        finally:
            file.close()

        return 1

    def decrypt_file(self, file_path):
        # Check if file exists
        if not path.isfile(file_path):
            return -1

        # Open and read, read, close file
        file = open(file_path, "rb")

        try:
            data = file.read()
        finally:
            file.close()

        # Filter out data by removing the salts
        half_data_size = (len(data) - 36) // 2
        data = data[12:12 + half_data_size] + data[24 + half_data_size:len(data) - 12]

        # Get salt parts of key
        key_salt_head, key_salt_tail = data[:8], data[len(data) - 8:]
        key_salt = key_salt_head + key_salt_tail






if __name__ == "__main__":
    x = Encrypt()
    x.main()
