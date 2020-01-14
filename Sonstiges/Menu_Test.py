import sys
from tkinter.filedialog import askopenfilename
def menu():
    user_input = input("1: Choose File (TXT files only)\n2: Manuel Input\n> ")
    if user_input == "1":
        file = askopenfilename()
        user_input = input("1: Crypt\n2: Decrypt\n> ")






menu()
