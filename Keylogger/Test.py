import pickle
import socket
char = []
for int in range(0, 99):
    char.append(str(int))
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    try:
        my_socket.connect((socket.gethostname(), 50000))
        break
    except ConnectionRefusedError:
        pass

while True:
    my_socket.send(pickle.dumps(char))
    input("Press Enter")#+r234ekjihnublfdsgg
