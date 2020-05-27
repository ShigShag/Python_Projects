import socket
from os import system

HEADER = 64
ADDR = socket.gethostbyname(socket.gethostname())
PORT = 5050
FORMAT = "utf-8"


class client:

    def __init__(self, ip, port, header):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect((ip, port))
        self.header = header

    def main(self):
        while True:
            self.receive()

    def receive(self):
        try:
            size = self.server.recv(self.header)
        except ConnectionRefusedError:
            return

        msg = self.server.recv(int(size.decode()))

        print(msg.decode())



s = client(ADDR, PORT, 64)
s.main()