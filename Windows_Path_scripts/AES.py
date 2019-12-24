from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from tkinter.filedialog import askopenfilename
from sys import exit
from os import path


random_string = """mucj9058tu9q083ut09q53ut905uz8t07z52387904ztn4zc09g4z907gcn708942zg045zg0ßm04mx70g79ß2j9, 
87uß92u54ß9g08u5ß420guß054328ug9ßc54ug90743z5g90c 
ß9x4h9gh9nß45hg9ß543hmg9043hcgß943h9ß07h0m4chmg90ß452hg9ßc0m54h9g70ßh3459ßghß45zmß92zg98, hx9h90h9g0h490gh027hß9x 
ßj23opigjfopig45346465ru978jz2098z9r708z0978zy8zr078z7z30792zrn07z98r7z8972z8972zr987z83497rz8934tr43th943ht9c34htn3ztc3
87t446gh3iofzi3hi3f934f9039fz34nfz3489fz983zc3891zf8913z897fcz891zcj87f1z8fz1c8jfz143fcz1fz1zf14zfjc1t5h23807t235th9235h
8x95,mh589th82ht785fmc3jh2t """


def main():
    print("[1] crypt File\n[2] decrypt File\n[3] exit")
    user_input = input("> ")
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
        print("Enter Password to encrypt")
        user_input = input("> ")
        default_key, default_salt = keygen(user_input)
        encrypt(default_key, default_salt, file_path)
        print("Encryption finished")
        return True

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
        print("Enter Password to decrypt")
        user_input = input("> ")
        decrypt(user_input + random_string, file_path)
        print("decryption finished")
        return True

    elif user_input == "3":
        return False

    else:
        print("wrong command")
        return True


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
        print("Wrong Password")
        exit()
    with open(path, "wb")as f:
        f.write(original_date)


def keygen(user_password):
    salt = get_random_bytes(32)
    return PBKDF2(user_password + random_string, salt, dkLen=32), salt


while main():
    pass

