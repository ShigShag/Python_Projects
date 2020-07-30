from ctypes import windll
from sys import argv

def uac_request():
    windll.shell32.ShellExecuteW(None, "runas", argv[0], "", None, 1)

def force_uac_request():
    while windll.shell32.ShellExecuteW(None, "runas", argv[0], "", None, 1) != 42:
        pass

if __name__ == '__main__':
    # uac_request()
    # force_uac_request()
    pass