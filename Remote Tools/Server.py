import socket


class Socket:

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


connection = Socket()
while True:
    if not connection.established:
        connection.listen_to_for_client()
    print("Enter command:")
    user_input = input("> ")
    connection.send_command(user_input)

