from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from tkinter.filedialog import askopenfilename
from sys import exit

random_string = "mucj9058tu9q083ut09q53ut905uz8t07z5238790t5h23807t235th9235h8x95,mh589th82ht785fmc3jh2t"
x = 1


def main():
    print("[1] crypt File\n[2] decrypt File\n[3] exit")
    user_input = input("> ")
    if user_input == "1":
        print("Enter Path:")
        path = input("> ")
        if not check_file_exists(path):
            print("File not found, choose manually")
            path = askopenfilename()
            if not check_file_exists(path):
                print("File not found")
                return True
        print("Enter Password to encrypt")
        user_input = input("> ")
        default_key, default_salt = keygen(user_input)
        encrypt(default_key, default_salt, path)
        print("Encryption finished")
        return True

    elif user_input == "2":
        print("Enter Path:")
        path = input("> ")
        if not check_file_exists(path):
            print("File not found, choose manually")
            path = askopenfilename()
            if not check_file_exists(path):
                print("File not found")
                return True
        print("Enter Password to decrypt")
        user_input = input("> ")
        decrypt(user_input + random_string, path)
        print("decryption finished")
        return True

    elif user_input == "3":
        return False

    else:
        print("wrong command")
        return True


def check_file_exists(path):
    try:
        open(path, "rb")
        return True
    except (FileNotFoundError, PermissionError):
        return False


def encrypt(key, salt, path):
    with open(path, "rb")as f:
        msg = f.read()
    cipher = AES.new(key, AES.MODE_CBC)
    encrypted_message = cipher.encrypt(pad(msg, AES.block_size))
    with open(path, "wb")as f:
        f.write(salt)
        f.write(cipher.iv)
        f.write(encrypted_message)


def decrypt(user_password, path):
    with open(path, "rb")as f:
        salt = f.read(32)
        iv = f.read(16)
        ciphered_data = f.read()
    key = PBKDF2(user_password, salt, dkLen=32)
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    try:
        original_date = unpad(cipher.decrypt(ciphered_data), AES.block_size)
    except ValueError:
        print("ERROR")
        exit()
    with open(path, "wb")as f:
        f.write(original_date)


def keygen(user_password):
    salt = get_random_bytes(32)
    return PBKDF2(user_password + random_string, salt, dkLen=32), salt


while main():
    pass


