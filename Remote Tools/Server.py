import socket
import threading
import pickle

class Server:

    def __init__(self, ip, port):
        # Header size for marking the length of messages
        self.HEADER = 64

        # Disconnect message
        self.DISCONNECT_MESSAGE = "!DISCONNECT"

        # Ip and port to bind
        self.ip = ip
        self.port = port

        # Create and bind server to Address
        self.sever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((ip, port))

    def Start(self):
        print(f"[LISTENING FOR CLIENTS] on {self.ip}")

        # Main Loop
        while True:
            # Accept incoming connections
            connection, address = self.sever.accept()

            # Create new thread and start it
            thread = threading.Thread(target=self.handle_client, args=(connection, address))
            thread.start()

            print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

    def handle_client(self, connection, address):
        print(f"[NEW CONNECTION] {address}")
        connected = True

        while connected:




def handle_client(conn, addr):
    print("NEW CONNECTION{} connected".format(addr))

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {IP}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("Starting Server")
start()


