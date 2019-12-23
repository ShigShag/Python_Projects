import socket
from os import system


class Socket:

    established = False
    cmd_received = False

    def connect_to_server(self):
        try:
            self.active_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.active_socket.connect((socket.gethostname(), 50000))
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
        system(cmd)


connection = Socket()
while True:
    if not connection.established:
        connection.connect_to_server()
        continue
    while connection.receive_command():
        pass
