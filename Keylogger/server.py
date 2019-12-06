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
                data_rec = connection.connection.recv(2048)
                if not data_rec:
                    break
                data_rec = pickle.loads(data_rec)
                print(data_rec )
                print("\n\n")


#Wenn Server zu erst Startet received er NUR data wenn man key drückt
#Wenn Server nicht zu erst startet receivet er permanent data nach array
#Er wartet also nicht beim data_rec, sondern erhät permanent: b''