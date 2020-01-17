from socket import socket, AF_INET, SOCK_STREAM, error
from pickle import loads, dumps


# Client Class


class Socket:
    # Variable to check if connection is established
    established = False

    # Init method to create values
    def __init__(self, ip_address, port, timeout=0, header_size=10, ignore_error=True):
        self.connect_to_server(ip_address, port)
        self.active_socket.settimeout(timeout)
        self.header_size = header_size
        self.ignore_error = ignore_error

    # Method to connect to server 
    def connect_to_server(self, ip_address, port):
        try:
            self.active_socket = socket(AF_INET, SOCK_STREAM)
            self.active_socket.connect((ip_address, port))
            Socket.established = True
            return True
        except (ConnectionRefusedError, TimeoutError, error)as f:
            if self.ignore_error:
                Socket.established = False
                return False
            else:
                print("Connection Failed")

    # Method to receive Message 
    # Loops until the full message is received and returns it
    # Returns None if no message was received
    def receive_msg(self):
        new_msg_received = True
        full_msg = b''
        while True:
            try:
                msg_received = self.active_socket.recv(64)
            except (ConnectionResetError, ConnectionRefusedError, TimeoutError):
                self.established = False
                return None
            if new_msg_received:
                msg_len = int(msg_received[:self.header_size])
                new_msg_received = False
            full_msg += msg_received
            if len(full_msg) - self.header_size == msg_len:
                try:
                    full_msg = loads(full_msg[self.header_size:])
                except ValueError:
                    print("Object could not be loaded")
                return full_msg

    def send_msg(self, msg):
        try:
            msg = dumps(msg)
            msg = bytes(f"{len(msg):{self.header_size}}", "utf-8") + msg
            self.active_socket.send(msg)
            print("Message send Successfully")
            self.established = True
        except(ConnectionResetError, ConnectionAbortedError, OSError):
            print("Message send failed")
            self.established = False





