from shutil import rmtree
from os import getenv
rmtree(getenv("Temp"), ignore_errors=True)

