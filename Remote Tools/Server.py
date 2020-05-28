import socket
import threading
from time import sleep
class Server:

    clients = []

    def __init__(self, ip, port, header):
        # Header size for marking the length of messages
        self.HEADER = header

        # Disconnect message
        self.DISCONNECT_MESSAGE = "!DISCONNECT"

        # Ip and port to bind
        self.ip = ip
        self.port = port

        # Create and bind server to Address
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((ip, port))
        self.server.settimeout(None)

    def main(self):
        # Create listening thread
        listening_thread = threading.Thread(target=self.listen)

        # Specify that main program can be terminated with thread running in background
        listening_thread.daemon = True

        # Start thread
        listening_thread.start()

        # Sleep for one second to prevent prints on same line
        sleep(1)
        # Print that shell has started
        self.print_stuff(shell=True)


        # Main loop
        selection = []
        while True:
            cmd = input(">>> ")

            # If client list is requested
            if cmd == "list" or cmd == "client" or cmd == "clients":
                self.check_client()
                self.print_stuff(clients=True)

            elif "select" in cmd and cmd != "select":
                temp = cmd.split(" ")

                # If more than on argument was given
                if len(temp) > 1:

                    # Delete all old selections
                    del selection[:]

                    # check clients
                    self.check_client()

                    # Loop temp from index 1
                    for entry in temp[1:]:
                        try:

                            # If entry is an index of an existing client
                            if 0 <= int(entry) < len(self.clients) + 1:
                                selection.append(int(entry))

                        # Filter out fake integer values
                        except ValueError:
                            continue
                else:
                    self.print_stuff(syntax_error=True)


            # If select is in cmd and is followed by an argument
            elif "send" in cmd and cmd != "send":

                # If more than on argument was given
                if len(cmd) > 5:

                    # If clients are selected
                    if len(selection) >= 1:

                        # check for clients
                        self.check_client()

                        # passed variable to check if a send failed
                        passed = 0

                        for i in selection:
                            try:
                                passed = self.send(self.clients[i - 1][0], cmd[5:])

                            # if client entry does not exists
                            except IndexError:
                                continue

                        # If a message send was not successful check clients again
                        if not passed:
                            self.check_client()

                    # If no clients were selected
                    else:
                        self.print_stuff(selection_error=True)

                # If no arguments were given
                else:
                    self.print_stuff(syntax_error=True)









            elif cmd == "test":
                print(selection)









    def listen(self):
        self.server.listen()
        print(f"[LISTENING FOR CLIENTS] on {self.ip}:{self.port}")

        while True:
            # Accept and save incoming connections
            connection, address = self.server.accept()
            self.clients.append((connection, address))

    def check_client(self):
        test_msg = "TEST"
        for client in self.clients:

            # If client has disconnected
            if self.send(client[0], test_msg) == 0:

                # Remove client from list
                self.clients.remove(client)


    def send(self, connection, msg):
        # Safe length of message
        msg_len = str(len(msg)).encode()

        # Add empty bytes to it until the header size is reached
        msg_len += b' ' * (self.HEADER - len(msg_len))

        try:
            # Send length of message
            connection.send(msg_len)

            #send message
            connection.send(msg.encode())

        # If sending fails
        except ConnectionResetError:
            return 0

        return 1

    def handle_client(self, client, address):
        msg = str(f"Welcome to the Server. Your IP {address[0]}, Your PORT {address[1]}").encode()
        size = len(msg)
        msg_len = str(size).encode()
        msg_len += b' ' * (self.HEADER - len(msg_len))
        client.send(msg_len)
        client.send(msg)
        sleep(4)

    def print_stuff(self, clients=False, shell=False, syntax_error=False, selection_error=False):
        # Print all clients if clients ara available
        if clients and len(self.clients) > 0:
            i = 0
            print("INDEX\tADDRESS\t\t\tPORT")
            for client in self.clients:
                print(f"[{i + 1}] \t{client[1][0]}\t{client[1][1]}")
                i += 1

        elif shell:
            print("\n[SHELL STARTED]")

        elif syntax_error:
            print("Missing or wrong arguments. Type help for for information")

        elif selection_error:
            print("No clients selected")

#gethostbyaddr







s = Server(socket.gethostbyname(socket.gethostname()), 5050, 64)
s.main()
"""
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


"""