import socket
import threading
from time import sleep
from sys import exit


class Server:

    clients = []

    def __init__(self, ip, port, header):

        # Create and bind server to Address
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(("192.168.178.22", port))
        self.server.settimeout(None)

        # Header size for marking the length of messages
        self.HEADER = header

        # Disconnect message
        self.DISCONNECT_MESSAGE = "!DISCONNECT"

        # Ip and port to bind
        self.ip = ip
        self.port = port

        # List for client selection
        self.selection = []

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
        while True:
            cmd = input(">>> ")

            # If client list is requested
            if cmd == "list" or cmd == "client" or cmd == "clients":
                self.check_client()
                self.print_stuff(clients=True)
                self.print_stuff(selected_clients=True)

            elif "select" in cmd and cmd != "select":
                temp = cmd.split(" ")

                # If more than on argument was given
                if len(temp) > 1:

                    # Delete all old selections
                    del self.selection[:]

                    # check clients
                    self.check_client()

                    # Loop temp from index 1
                    for entry in temp[1:]:
                        try:

                            # If entry is an index of an existing client
                            if 0 <= int(entry) < len(self.clients) + 1:
                                self.selection.append(int(entry))

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
                    if len(self.selection) >= 1:

                        # check for clients
                        # TODO
                        # self.check_client()

                        # passed variable to check if a send failed
                        passed = False

                        for i in self.selection:
                            try:
                                passed = self.send(self.clients[i - 1][0], cmd[5:])
                                sleep(1)
                                msg = self.receive(self.clients[i - 1][0])

                                # If message was received print it
                                if msg:
                                    self.print_stuff(content=msg)

                                # If message was not received set passed to 0
                                else:
                                    passed = 0

                            # if client entry does not exists
                            except IndexError:
                                continue

                        # If a message send or receive was not successful check clients again
                        if not passed:
                            self.check_client()

                    # If no clients were selected
                    else:
                        self.print_stuff(selection_error=True)

                # If no arguments were given
                else:
                    self.print_stuff(syntax_error=True)

            elif cmd == "help":
                pass # TODO

            elif cmd == "exit":
                return


    def receive(self, client):
        # Try to receive a message from given index
        try:
            client.settimeout(15.0)
            size = client.recv(self.HEADER)
        # If it fails
        except(ConnectionAbortedError, ConnectionResetError, TimeoutError, socket.timeout):
            print(f"Timeout while receiving feedback from client: {client.getsockname()}")
            return 0

        try:
            msg = client.recv(int(size.decode()))
        except ValueError:
            print("Error received")
            return 0

        # self.print_stuff(msg.decode())
        if msg.decode:
            return msg.decode()

        return 0

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

    def send(self, client, msg):
        # Safe length of message
        msg_len = str(len(msg)).encode()

        # Add empty bytes to it until the header size is reached
        msg_len += b' ' * (self.HEADER - len(msg_len))

        try:
            # Send length of message
            client.send(msg_len)

            #send message
            client.send(msg.encode())

        # If sending fails
        except (ConnectionResetError, ConnectionAbortedError):
            return 0

        return 1

    def print_stuff(self,content=None, clients=False, selected_clients=False, shell=False, syntax_error=False, selection_error=False):
        # Custom print
        if content:
            print(content)

        # Print all clients if clients ara available
        elif clients and len(self.clients) > 0:
            i = 0
            print("INDEX\tHOSTNAME\t\t\t\t\t\t\tADDRESS\t\t\tPORT")
            for client in self.clients:
                print(f"[{i + 1}] \t{socket.gethostbyaddr(client[1][0])[0]}\t\t\t{client[1][0]}\t{client[1][1]}")
                i += 1

        elif selected_clients:
            if len(self.selection) > 0:
                print("Selected clients:")
                print(self.selection)
            else:
                print("No clients selected")

        elif shell:
            print("\n[SHELL STARTED]")

        elif syntax_error:
            print("Missing or wrong arguments. Type help for for information")

        elif selection_error:
            print("No clients selected")


s = Server("192.168.43.13", 5050, 64)
exit(s.main())
