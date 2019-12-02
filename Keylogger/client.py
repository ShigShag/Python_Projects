import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.178.22", 1236))

while True:
    msgr = ''
    new_msg = True
    while True:
        msg = s.recv(16)
        print(msg.decode())

