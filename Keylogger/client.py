import socket
from pickle import loads

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect(("192.168.178.22", 1250))
while True:
    try:
        s.connect((socket.gethostname(), 1251))
        break
    except ConnectionRefusedError:
        continue

while True:
    data = b''
    while True:
        data_stream = s.recv(1)
        if not data_stream:
            break
        data += data_stream
    data = loads(data)
    print(data_stream)



