from socket import socket, AF_INET, SOCK_STREAM, timeout
from pickle import loads, dumps


class Socket:

    # Variable to check if connection is established
    established = False

    # Create Socket Object and bind to Address
    def __init__(self, ip_address, port, header_size=10, ignore_errors=True):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.bind((ip_address, port))
        # Max size in bytes of objects to send
        self.header_size = header_size
        # If True raises error else ignores them
        self.ignore_errors = ignore_errors

    # Listen for client
    def listen_for_client(self):
        try:
            self.socket.listen()
            self.connection, self.address = self.socket.accept()
            self.established = True
            print(f"Connection established with {self.address}")
        except timeout:
            self.established = False
            if self.ignore_errors:
                print("Connection could not be established")
            else:
                raise timeout

    # Send Python object
    def send_msg(self, msg):
        msg = dumps(msg)
        msg = bytes(f"{len(msg):{self.header_size}}", "utf-8") + msg
        try:
            self.connection.send(msg)
            self.established = True
        except ConnectionResetError:
            self.established = False
            if self.ignore_errors:
                print(f"Lost Connection to {self.address}")
                print("Message could not be sended")
            else:
                raise ConnectionResetError

    def receive_message(self, receive_bytes_amount=64):
        full_msg = b''
        new_msg = True
        while True:
            try:
                msg_rec = self.connection.recv(receive_bytes_amount)
            except (ConnectionAbortedError, ConnectionResetError, TimeoutError)as error:
                self.established = False
                if self.ignore_errors:
                    print(f"Lost connection to {self.address}")
                    return None
                else:
                    raise error
            if new_msg:
                msg_len = int(msg_rec[:self.header_size])
                new_msg = False
            full_msg += msg_rec
            if len(full_msg) - self.header_size == msg_len:
                try:
                    full_msg = loads(full_msg[self.header_size:])
                except TypeError:
                    if self.ignore_errors:
                        print("Message could not be deciphered")
                        return None
                    else:
                        raise TypeError
                return full_msg
