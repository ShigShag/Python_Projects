import os
import shutil
import sys


icon_path = r"F:\Python_Projects\Constants\icon.ico"
try:
    name = sys.argv[1]
except IndexError:
    sys.exit(1)

pure_name = name.split('.')[0]
exe_name = name.split('.')[0] + ".exe"
w_set = False
try:
    w_set = (sys.argv[2] == '-w' or sys.argv[2] == 'w' or sys.argv[2] == 'hide')
except IndexError:
    pass

if w_set:
    os.system(f"pyinstaller -i {icon_path} --onefile -w {name}")
else:
    os.system(f"pyinstaller -i {icon_path} --onefile {name}")
try:
    shutil.rmtree("__pycache__")
except (shutil.Error, FileNotFoundError):
    pass
shutil.rmtree("build")
os.remove(f"{pure_name}.spec")
directory = os.getcwd()
os.chdir("dist")
if os.path.exists(directory + "\\" + exe_name):
    os.remove(directory + "\\" + exe_name)
shutil.move(exe_name, directory)
os.chdir(directory)
shutil.rmtree("dist")