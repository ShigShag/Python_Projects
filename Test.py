import psutil
import os

for proc in psutil.process_iter(['pid', 'name', 'username']):
    print(proc.name())
    p = psutil.Process(proc.pid)
    print(p.exe())

print(psutil.pid_exists(9532))