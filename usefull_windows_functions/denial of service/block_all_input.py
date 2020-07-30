from ctypes import windll

def main():
    while True:
        windll.user32.BlockInput(True)

if __name__ == '__main__':
    main()


# Needs to be run as admin
# STRG ALT T can counter it