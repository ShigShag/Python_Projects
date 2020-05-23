import base64
import string
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from secrets import token_bytes, choice, SystemRandom
from os import path, listdir, chdir
from sys import argv, exit

class aes:

    @staticmethod
    def main():
        command = argv
        # If a command is given
        if len(command) > 1:

            # If help is requested
            if '-h' in command:
                aes.print_stuff(help=True)


            # If encrypt and password command is given
            elif '-e' in command and '-p' in command:
                try:
                    # Generate Key and Salt
                    key, salt = aes.generate_key(command[command.index('-p') + 1])

                    # If directory crypt returns -1 the given path has to be a file or invalid
                    if aes.crypt_directory(command[command.index('-e') + 1], key, salt, recursive_loop='-r' in command) == -1:
                        if aes.encrypt_file(command[command.index('-e') + 1], key, salt) == 1:
                            aes.print_stuff(success=True)
                        else:
                            aes.print_stuff(error=True)

                # If not enough arguments are given
                except IndexError:
                    aes.print_stuff(error=True)


            # If decrypt and password command is given
            elif '-d' in command and '-p' in command:
                try:

                    # If directory decrypt returns -1 the given path has to be a file or invalid
                    # Do recursive loop if -r is in command
                    if aes.decrypt_directory(command[command.index('-d') + 1], command[command.index('-p') + 1], recursive_loop='-r' in command) == -1:
                        if aes.decrypt_file(command[command.index('-d') + 1], command[command.index('-p') + 1]) == 1:
                            aes.print_stuff(success=True)
                        else:
                            aes.print_stuff(error=True)

                # If not enough arguments are given
                except IndexError:
                    aes.print_stuff(error=True)


            # If no valid argument was given
            else:
                aes.print_stuff(error=True)

            return 1


    @staticmethod
    def print_stuff(help=False, error=False, success=False):
        if help:
            print("𝓐𝓔𝓢 𝓒𝓡𝓨𝓟𝓣𝓔𝓡 𝓥𝓔𝓡𝓢𝓘𝓞𝓝 1.0\n\n"
                  "Syntax:\n"
                  "-e/-d 'path_to_file_or_directory' -p 'password' -r\n\n"
                  "-e = encrypt\n"
                  "-d = decrypt\n"
                  "-p = password\n"
                  "-r = recursive encryption for directories. Is ignored if file is given\n\n"
                  "General:\n"
                  "- Syntax is not important as long as all necessary commands are followed by arguments.\n"
                  "- AES uses cbc method provided by pythons 'encryption' library.\n"
                  "- The password used for encryption will not get stored and therefore needs to be remembered for decryption.\n"
                  "- To change salt settings, cycles etc change source code.\n")

        if error:
            print("Missing or wrong arguments. Type -h for help")

        if success:
            print("done")


    @staticmethod
    def crypt_directory(directory_path, key, salt, recursive_loop=False):
        # Check if directory exists
        if not path.isdir(directory_path):
            return -1

        # Change working directory
        chdir(directory_path)

        # Loop through files in directory
        for file in listdir(directory_path):

            # Not recursive
            if not recursive_loop:

                if not path.isfile(file):
                    continue

                aes.encrypt_file(file, key, salt)
                continue

            # Recursive
            if recursive_loop:
                # Change working directory
                chdir(directory_path)

                if path.isdir(file):
                    # Call the function again with the new directory
                    aes.crypt_directory(directory_path + "\\" + file, key, salt, recursive_loop=True)

                if not path.isfile(file):
                    continue

                aes.encrypt_file(file, key, salt)
                continue
        return 1

    @staticmethod
    def decrypt_directory(directory_path, user_password, recursive_loop=False):
        # Check if directory exists
        if not path.isdir(directory_path):
            return -1

        # Change working directory
        chdir(directory_path)

        # Loop through files in directory
        for file in listdir(directory_path):

            # Not recursive
            if not recursive_loop:

                if not path.isfile(file):
                    continue

                aes.decrypt_file(file, user_password)
                continue

            # Recursive
            if recursive_loop:
                # Change working directory
                chdir(directory_path)

                if path.isdir(file):
                    # Call the function again with the new directory
                    aes.decrypt_directory(directory_path + "\\" + file, user_password, recursive_loop=True)

                if not path.isfile(file):
                    continue

                aes.decrypt_file(file, user_password)
                continue
        return 1

    @staticmethod
    def generate_key(user_password):
        # Add salt to user_password
        user_password += aes.get_random_string()

        # Pepper the user password
        user_password += choice(['1', '2', '3'])

        salt = token_bytes(16)
        kdf = PBKDF2HMAC(algorithm=hashes.SHA3_256(), length=32, salt=salt, iterations=111355, backend=default_backend())
        key = base64.urlsafe_b64encode(kdf.derive(user_password.encode()))
        return key, salt

    @staticmethod
    def encrypt_file(file_path, key, key_salt):
        # Check if file exists
        if not path.isfile(file_path):
            return -1

        # Split the keygen salt
        head, tail = key_salt[:8], key_salt[8:]

        # Open and read, read, close file
        try:
            file = open(file_path, "rb")
        except PermissionError:
            print("Permission Error at: " + file_path)
            return -1

        try:
            data = file.read()
        finally:
            file.close()

        # Add the keygen salt and data to one string
        data = data

        # Encrypt data
        method = Fernet(key)
        data = method.encrypt(data)

        # Random salt to manipulate the encrypted data
        random_salt = token_bytes(36)
        r_head, r_middle, r_tail = random_salt[:12], random_salt[12:24], random_salt[24:]

        # Split encrypted data in half
        data_head, data_tail = data[:len(data) // 2], data[len(data) // 2:]

        # Add the random salt to the encrypted string to confuse
        token = r_head + head + data_head + tail + r_middle + data_tail + r_tail

        # Open, write, close file
        try:
            file = open(file_path, "wb")
        except PermissionError:
            print("Permission Error at: " + file_path)
            return -1

        try:
            file.write(token)
        finally:
            file.close()

        return 1

    @staticmethod
    def decrypt_file(file_path, user_password):
        # Check if file exists
        if not path.isfile(file_path):
            return -1

        # Open and read, read, close file
        try:
            file = open(file_path, "rb")
        except PermissionError:
            print("Permission Error at: " + file_path)
            return -1

        try:
            data = file.read()
        finally:
            file.close()

        # Filter out data by removing the salts
        half_data_size = (len(data) - 52) // 2

        # Get salt parts of key
        key_salt_head, key_salt_tail = data[12:20], data[20 + half_data_size: 28 + half_data_size]
        salt = key_salt_head + key_salt_tail

        # Get data
        data = data[20:20 + half_data_size] + data[40 + half_data_size:len(data) - 12]

        # Salt the user password
        user_password += str(aes.get_random_string())

        # Try to decrypt file for every pepper
        passed = False

        for pepper in ['1', '2', '3']:
            # Create kdf multiple times because a kdf instance can only be used once
            kdf = PBKDF2HMAC(algorithm=hashes.SHA3_256(), length=32, salt=salt, iterations=111355, backend=default_backend())

            # Create Key
            key = base64.urlsafe_b64encode(kdf.derive((user_password + pepper).encode()))
            method = Fernet(key)
            try:
                # Only break if decryption does not fail
                decrypted_data = method.decrypt(data)

                # This only gets executed if decryption is successful
                passed = True
                break
            except InvalidToken:
                continue

        if not passed:
            return -1

        # Open, write, close file
        try:
            file = open(file_path, "wb")
        except PermissionError:
            print("Permission Error at: " + file_path)
            return -1

        try:
            file.write(decrypted_data)
        finally:
            file.close()

        return 1

    @staticmethod
    def create_random_string_file(user_password=None, file_path="randomstring.txt", rewrite_file=True, size=1000000, encrypted=False):
        if rewrite_file:
            file = open(file_path, "w")
            file.close()

        # Create random string
        generator = SystemRandom()
        random_string = ""
        i = 0
        while i != size:
            n = generator.randrange(0, 10)
            random_string += str(n)
            i += 1

        if encrypted:
        # Create Key
            salt = token_bytes(16)
            kdf = PBKDF2HMAC(algorithm=hashes.SHA3_256(), length=32, salt=salt, iterations=111355, backend=default_backend())
            key = base64.urlsafe_b64encode(kdf.derive(user_password.encode()))

            # Create method
            method = Fernet(key)

            # Encrypt data
            random_string = method.encrypt(random_string.encode())

            # Add salt to Key salt to encrypted data
            data = salt[:8] + random_string + salt[8:]

            # Open, write, close file
            file = open(file_path, "wb")
            try:
                file.write(random_string)
            finally:
                file.close()

            return 1

        file = open(file_path, "w")
        try:
            file.write(random_string)
        finally:
            file.close()

        return 1
    @staticmethod
    def get_random_string(user_password=None, file_path="randomstring.txt", encrypted=False):
        # Check if File exists
        if not path.isfile(file_path):
            return -1

        if encrypted:
            # Open, read, close file
            file = open(file_path, "rb")
            try:
                data = file.read()
            finally:
                file.close()

            # Get Salt
            salt = data[:8] + data[len(data) - 8:]

            # Generate Key
            kdf = PBKDF2HMAC(algorithm=hashes.SHA3_256(), length=32, salt=salt, iterations=111355, backend=default_backend())
            key = base64.urlsafe_b64encode(kdf.derive(user_password.encode()))

            # Create method
            method = Fernet(key)

            # Try to decrypt data
            try:
                decrypted_data = method.decrypt(data[8:len(data) - 8])
            except InvalidToken:
                print("Wrong password")
                return -1

            return decrypted_data

        # Open, read, close file
        file = open(file_path, "r")
        try:
            data = file.read()
        finally:
            file.close()

        return data



if __name__ == '__main__':
    exit(aes.main())