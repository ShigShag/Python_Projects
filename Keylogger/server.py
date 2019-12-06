import socket
import pickle


class Socket:

    def __init__(self):
        socket.timeout(5)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((socket.gethostname(), 50000))
        print("Listening...")
        try:
            self.socket.listen(1)
            self.connection, self.address = self.socket.accept()
            Global.connection_established = True
        except socket.timeout:
            Global.connection_established = False


class Global:
    connection_established = False


connection = Socket()
print(f"Conncted to {connection.address}")
while True:
    while True:
        if Global.connection_established:
            while Global.connection_established:
                try:
                    data_rec = connection.connection.recv(2048)
                except ConnectionResetError:
                    print(f"Lost Connection to {connection.address}")
                    Global.connection_established = False
                    break
                if not data_rec:
                    break
                data_rec = pickle.loads(data_rec)
                print(data_rec)

#Neu listen wenn client Verbindung unterbochen hat
