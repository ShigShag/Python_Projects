from os import getenv, listdir, remove, chdir
chdir(getenv("Temp"))
for file in listdir(getenv("Temp")):
    try:
        remove(file)
    except PermissionError:
        continue
