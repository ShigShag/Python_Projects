import threading
import time



def listen():
    print("Hello")
def h():
    listening_thread = threading.Thread(target=listen)
    listening_thread.daemon = True
    return listening_thread

a = h()

a.start()
print(a.getName())
time.sleep(3)
