import socket
import threading
from time import sleep


class Person:

    def __init__(self, client_object, address):

        self.object = client_object
        self.address = address

    def get_object(self):
        return self.object

    def get_address(self):
        return self.address

# defines
CLIENT_OBJECT = 0
CLIENT_ADDRESS = 1
CLIENT_IP = 0
CLIENT_PORT = 1

IP = "192.168.178.22"
PORT = "5050"
ADDRESS = (IP, PORT)

# Stores person class objects
CLIENTS = []


def main():
    listening_thread = threading.Thread(target=listen)
    listening_thread.daemon = True
    listening_thread.start()

    while True:
        pass



def get_info(client_object):
    pass

def listen():
    while True:
        connection, address = SERVER.accept()
        person = Person(connection, address)
        CLIENTS.append(person)




SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind(ADDRESS)
main()




