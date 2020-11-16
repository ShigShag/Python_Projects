import socket
from os import system

def main():
    s_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_object.connect(("192.168.178.46", 5050))
    s_object.close()
    system("start explorer")

def main2():
    msg = "1"
    s_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_object.bind(("192.168.178.46", 5050))
    s_object.listen()
    connection, address = s_object.accept()
    print(f"Connected with {address}")
    s_object.close()

if __name__ == '__main__':
    main()
