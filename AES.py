from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from tkinter.filedialog import askopenfilename
from sys import argv

d_key = b'\xfc\x9d\xcd\xe8%\xd5\xebkV\\I\xf8\xb1w]\xf5@\x98\x82!vW\x17\xad\x17\x82\x02p\xacl\xa9\x1f'
d_salt = b"\xf0\x10\xfbg\xee\xc5?\x19\xed\x0c'f>\xc3\xe2a\xe1\xe4\x19(\xcb\x0cs*q\x9fN\xbb8\xdb\xc2H"


def main(argv, default_key, default_salt):
    if "-help" in argv:
        print(
            "-c\t\tcrypt\n-d\t\tdecypt\n-key []\t\tkey to crypt/decrypt\n-path []\tpath to file to crypt/decrypt | if not given will ask you to choose file\n-p\t\tcustom_password used for encryption and decryption\n-help\t\tshows this list")
        quit()

    if "-c" in argv and "-d" in argv:
        print("Only one argument of -c and -d expected\ntype -help to show list of commands")
        quit()

    if "-p" in argv:
        default_key, default_salt = keygen(argv.index("-p") + 1)
        print(default_key, default_salt)

    if "-c" in argv:
        if "-path" in argv:
            path_to_file = argv[argv.index("-path") + 1]
        else:
            path_to_file = askopenfilename()
        try:
            encrypt(default_key, default_salt, path_to_file)
        except FileNotFoundError:
            quit()
        return False
    elif "-d" in argv:
        if "-path" in argv:
            path_to_file = argv[argv.index("-path") + 1]
        else:
            path_to_file = askopenfilename()

        decrypt(default_key, default_salt, path_to_file)
        return False
    else:
        print("-c or -d argument required\ntype -help to show list of commands")
        quit()


def encrypt(key, salt, path):
    with open(path, "rb")as f:
        msg = f.read()
    cipher = AES.new(key, AES.MODE_CBC)
    encrypted_message = cipher.encrypt(pad(msg, AES.block_size))
    with open(path, "wb")as f:
        f.write(salt)       #CHECK
        f.write(cipher.iv)
        f.write(encrypted_message)


def decrypt(key, salt, path):
    with open(path, "rb")as f:
        salt = f.read(32)
        iv = f.read(16)
        ciphered_data = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    original_date = unpad(cipher.decrypt(ciphered_data), AES.block_size)
    with open(path, "wb")as f:
        f.write(original_date)


def keygen(user_password):
    salt = b':2}\xd7\xe7\xd4n\x1d\tH#y\xc0V|\x93\x17\x92\xa9AqC\x96\x1f\xa4j\x18\xf9+^\xde$'
    return PBKDF2(user_password, salt, dkLen=32), salt


if __name__ == '__main__':
    while main(argv[1:], d_key, d_salt):
        pass

# Custom Salt in die Datei schreiben
# Weiter machen mit programm generell
