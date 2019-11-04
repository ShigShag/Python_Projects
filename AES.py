from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from tkinter.filedialog import askopenfilename
from sys import argv
key = b'\xfc\x9d\xcd\xe8%\xd5\xebkV\\I\xf8\xb1w]\xf5@\x98\x82!vW\x17\xad\x17\x82\x02p\xacl\xa9\x1f'


def main(argv, default_key):
    if "-help" in argv:
        print("-c\t\tcrypt\n-d\t\tdecypt\n-key []\t\tkey to crypt/decrypt\n-path []\tpath to file to crypt/decrypt | if not given will ask you to choose file\n-help\t\tshows this list")
        quit()
    if "-c" in argv and "-d" in argv:
        print("Only one argument of -c and -d expected\ntype -help to show list of commands")
        quit()
    if "-c" in argv:
        if "-path" in argv:
            path_to_file = argv[argv.index("-path") + 1]
        else:
            path_to_file = askopenfilename()
        if "-key" in argv:
            key_to_crypt = argv[argv.index("-key") + 1]
            if type(key_to_crypt) != bytes:
                key_to_crypt = b'\xfc\x9d\xcd\xe8%\xd5\xebkV\\I\xf8\xb1w]\xf5@\x98\x82!vW\x17\xad\x17\x82\x02p\xacl\xa9\x1f'    #Programm akzepiert nicht eingegebenen Schlüssel, sondern nur den der Hinterlegt ist
        else:
            key_to_crypt = default_key
        encrypt(key_to_crypt, path_to_file)
        return False
    elif "-d" in argv:
        if "-path" in argv:
            path_to_file = argv[argv.index("-path") + 1]
        else:
            path_to_file = askopenfilename()
        if "-key" in argv:
            key_to_crypt = argv[argv.index("-key") + 1]
            if type(key_to_crypt) != bytes:
                key_to_crypt = bytes(key_to_crypt)
        else:
            key_to_crypt = default_key
        decrypt(key_to_crypt, path_to_file)
        return False
    else:
        print("-c or -d argument required\ntype -help to show list of commands")
        quit()


def encrypt(key, path):
    with open(path, "rb")as f:
        msg = f.read()
    cipher = AES.new(key, AES.MODE_CBC)
    encrypted_message = cipher.encrypt(pad(msg, AES.block_size))
    with open(path, "wb")as f:
        f.write(cipher.iv)
        f.write(encrypted_message)


def decrypt(key, path):
    with open(path, "rb")as f:
        iv = f.read(16)
        ciphered_data = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    original_date = unpad(cipher.decrypt(ciphered_data), AES.block_size)
    with open(path, "wb")as f:
        f.write(original_date)


if __name__ == '__main__':
    while main(argv[1:], key):
        pass
