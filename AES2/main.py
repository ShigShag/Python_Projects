import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from secrets import token_bytes


# backend = default_backend()

class Encrypt:

    pepper = 0

    def main(self):
        key, salt = self.generate_key(b"Hello")
        self.encrypt_file("test.txt", key)
        input("> ")
        self.decrypt("test.txt", key)

    def generate_key(self, user_password):
        salt = token_bytes(16)
        kdf = PBKDF2HMAC(algorithm=hashes.SHA3_256(), length=32, salt=salt, iterations=100000, backend=default_backend())
        key = base64.urlsafe_b64encode(kdf.derive(user_password))
        return key, salt


    def store_salt(self, salt):
        pass

    def encrypt_file(self, file_name, key):
        method = Fernet(key)

        try:
            file = open(file_name, "rb")
        except NameError:
            return -1

        try:
            data = file.read()
        finally:
            file.close()

        token = method.encrypt(data)

        try:
            file = open(file_name, "wb")
        except NameError:
            return -1

        try:
            file.write(token)
        finally:
            file.close()

        return 1



    def decrypt(self, file_name, key):
        method = Fernet(key)

        try:
            file = open(file_name, "rb")
        except NameError:
            return -1

        try:
            data = file.read()
        finally:
            file.close()

        token = method.decrypt(data)

        try:
            file = open(file_name, "wb")
        except NameError:
            return -1

        try:
            file.write(token)
        finally:
            file.close()

        return 1


if __name__ == "__main__":
    x = Encrypt()
    x.main()
