import psutil
from sys import argv, exit
from time import sleep
from os import startfile

def main():
    # argv[1] = Filename    argv[2] = full path
    if not argv[1] or not argv[2]:
        exit()

    while True:
        if not process_active(argv[1]):
            try:
                startfile(argv[2])
            except (FileNotFoundError, PermissionError):
                pass
        sleep(1)

def process_active(name):
    for process in psutil.process_iter():
        try:
            if name.lower() in process.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return False

if __name__ == '__main__':
    main()