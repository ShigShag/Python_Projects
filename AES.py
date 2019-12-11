from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from tkinter.filedialog import askopenfilename
from sys import argv, exit


def main(argv):
    if "-help" in argv:
        print("-c\t\tcrypt\n-d\t\tdecypt\n-path []\tpath to file to crypt/decrypt | if not given will ask you to choose file\n-p\t\tcustom_password required for encryption and decryption\n-help\t\tshows this list")
        exit()

    if "-c" in argv and "-d" in argv:
        print("Only one argument of -c and -d expected\ntype -help to show list of commands")
        exit()

    if "-p" in argv:
        default_key, default_salt = keygen(argv[argv.index("-p") + 1])
        user_password = argv[argv.index("-p") + 1]
    else:
        print("ERROR: No password given")
        exit()

    if "-c" in argv:
        if "-path" in argv:
            path_to_file = argv[argv.index("-path") + 1]
        else:
            path_to_file = askopenfilename()
        try:
            encrypt(default_key, default_salt, path_to_file)
        except FileNotFoundError:
            print("EROOR: FILE NOT FOUND")
            exit()
        return False

    elif "-d" in argv:
        if "-path" in argv:
            path_to_file = argv[argv.index("-path") + 1]
        else:
            path_to_file = askopenfilename()
        try:
            decrypt(user_password, path_to_file)
        except FileNotFoundError:
            print("EROOR: FILE NOT FOUND")
            exit()
        return False
    else:
        print("-c or -d argument required\ntype -help to show list of commands")
        exit()


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
    return PBKDF2(user_password, salt, dkLen=32), salt


if __name__ == '__main__':
    while main(argv[1:]):
        pass


# Weiter machen mit programm generell