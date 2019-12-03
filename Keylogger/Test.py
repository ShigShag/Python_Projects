import socket
socket.setdefaulttimeout(2)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen()
client_socket, address = s.accept()
