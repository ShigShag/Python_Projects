from cryptography.fernet import Fernet
from tkinter import filedialog
import os


def main(origin_file, new_file_name, icon, extract_file):
    with open(origin_file, "rb")as file:
        origin_file_content = file.read()
    encrypted_text, key = encryption(origin_file_content)
    pseudo_text = """from os import startfile, remove, path
from cryptography.fernet import Fernet
def main(key, text_to_decrypt):
    file_name = "{}.exe"
    with open(file_name, "wb")as file:
        file.write(decryption(text_to_decrypt, key))
    startfile(file_name)
    
def decryption(text_to_decrypt, key):
    method = Fernet(key)
    decrypt_text = method.decrypt(text_to_decrypt)  
    return decrypt_text
key = {}
text_to_decrypt = {}
main(key, text_to_decrypt)
""".format(extract_file, key, encrypted_text)
    with open(new_file_name, "w")as n:
        n.write(pseudo_text)
    if icon is None:
        os.system(f"Pyinstaller -F -w {new_file_name}")
    else:
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
    name_of_extract_file = input("Name of extract file(without exe): ")
    icon_input = input("Custom Icon(.ico)(Y/N): ")
    if icon_input == "Y" or icon_input == "y":
        icon = filedialog.askopenfilename(filetypes=(("ico files", "*.ico"), ("all files", "*.*")))
    else:
        icon = None
    main(f, new_file_name, icon, name_of_extract_file)
