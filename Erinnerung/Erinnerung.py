import time
from win10toast import ToastNotifier

time.sleep(10)

path = r"G:\Python_Projects\Erinnerung\stats.txt"
toast = ToastNotifier()
duration = 5
with open(path, "r")as f:
    x = f.readlines()

for msg in x:
    toast.show_toast("NEW NOTIFICATION", msg, duration=duration)






