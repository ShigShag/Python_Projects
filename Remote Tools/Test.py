from pickle import dumps
from os import getcwd

print(getcwd())
path = r"C:\Users\leonw\PycharmProjects\Python_Projects\Remote Tools"
path2 = f"wasd{getcwd()}"
path = dumps(path)
path2 = dumps(path2)
print()