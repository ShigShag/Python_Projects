from win32api import SetCursorPos
from time import sleep

def disable_mouse():
    pos = (1000, 5000)
    while True:
        SetCursorPos(pos)
        sleep(0.001)

if __name__ == '__main__':
    disable_mouse()