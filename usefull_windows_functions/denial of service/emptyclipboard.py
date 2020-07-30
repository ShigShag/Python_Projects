from win32clipboard import OpenClipboard, EmptyClipboard, CloseClipboard
from time import sleep
from sys import exit

def main():
    OpenClipboard()
    try:
        while True:
                EmptyClipboard()
                sleep(1)
    finally:
        CloseClipboard()

if __name__ == '__main__':
    exit(main())