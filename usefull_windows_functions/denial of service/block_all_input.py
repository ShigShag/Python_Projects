from ctypes import windll
from time import sleep

def block_input():
    windll.user32.BlockInput(True)
    while True:
        sleep(0.001)

if __name__ == '__main__':
    block_input()


# Needs to be run as admin
# STRG ALT ENTF can counter it