import time
import os
import sys
import subprocess
subprocess.Popen([r"F:\Python_Projects\test.exe", sys.argv[0], os.path.realpath(sys.argv[0])], shell=True)
input("Press Enter to exit")