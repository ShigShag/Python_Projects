import socket
from pickle import loads


class Socket:

    header = 10
    established = False

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((socket.gethostname(), 50000))
        self.listen_to_for_client()

    def listen_to_for_client(self):
        try:
            print("Listening...")
            self.socket.listen(1)
            self.connection, self.address = self.socket.accept()
            self.established = True
            print(f"Connection established with {self.address}")
        except socket.timeout:
            self.established = False

    def send_command(self, command):
        command = str(command)
        self.connection.send(command.encode())
        self.receive_command_output()

    def receive_command_output(self):
        full_msg = b''
        new_msg = True
        while True:
            msg_rec = self.connection.recv(64)
            if new_msg:
                msg_len = int(msg_rec[:self.header])
                new_msg = False
            full_msg += msg_rec
            if len(full_msg) - self.header == msg_len:
                full_msg = loads(full_msg[self.header:])
                print(full_msg)
                return True


connection = Socket()
while True:
    if not connection.established:
        connection.listen_to_for_client()
    print("Enter command:")
    user_input = input("> ")
    connection.send_command(user_input)

