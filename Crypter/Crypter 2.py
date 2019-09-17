import RSAModule
from tkinter.filedialog import askopenfilename
n, d, e = RSAModule.rsa_module()


def menu(i, c):
    if i == "1":
        f = askopenfilename()
        print("1: simple crypt\n2: simple decrypt\n3: rsa encrypt(only small text)\n4: rsa decrypt(only small text)")
        i = input("> ")
        if i == "1":
            with open(f, "r")as file:
                read = file.read()
            while simple_crypt(read, "", c)is False:
                pass
            with open(f, "w")as file:
                file.write(simple_crypt(read, "", c))
                print("success")
            menu(input("> "), "n8")
        elif i == "2":
            with open(f, "r")as file:
                read = file.read()
            if simple_decrypt(read, "", c)is False:
                print("Unknown sequence")
            else:
                with open(f, "w")as file:
                    file.write(simple_decrypt(read, "", c))
                    print("success")
            menu(input("> "), "n8")
        elif i == "3":
            with open(f, "r")as file:
                read = file.read()
                while rsa_encrypt(read, "")is False:
                    pass
                if rsa_encrypt(read, "") == 1:
                    print("Text to long")
                else:
                    with open(f, "w")as file:
                        file.write(rsa_encrypt(read, ""))
                        print("success")
            menu(input("> "), "n8")
        elif i == "4":
            with open(f, "r")as file:
                read = file.read()
            if rsa_decrypt(read, "")is False:
                print("Value Error")
            else:
                with open(f, "w")as file:
                    file.write(rsa_decrypt(read, ""))
                    print("success")
            menu(input(">"), "n8")
    elif i == "2":
        f = input("Enter your text here: ")
        print("1: simple crypt\n2: simple decrypt\n3: rsa encrypt(only small text)\n4: rsa decrypt(only small text)")
        i = input("> ")
        if i == "1":
            while simple_crypt(f, "", c) is False:
                pass
            print(simple_crypt(f, "", c))
            menu(input("> "), "n8")
        elif i == "2":
            if simple_decrypt(f, "", c)is False:
                print("Unknown sequence")
            else:
                print(simple_decrypt(f, "", c))
            menu(input("> "), "n8")
        elif i == "3":
            while rsa_encrypt(f, "") is False:
                pass
            if rsa_encrypt(f, "") == 1:
                print("Text to long")
            else:
                print(rsa_encrypt(f, ""))
            menu(input("> "), "n8")
        elif i == "4":
            if rsa_decrypt(f, "") is False:
                print("Value Error")
            else:
                print(rsa_decrypt(f, ""))
            menu(input("> "), "n8")
        else:
            print("command not found")
            menu(input("> "), "n8")
    else:
        print("command not found")
        menu(input("> "), "n8")


def hashes():
    with open("Lists.TXT", "r")as f:
        file = f.read()
    o = ["\n", "\t"]
    for i in file:
        o.append(i)
    return o


def simple_crypt(text, new_text, hash):
    try:
        for t in text:
            t = index.index(t)
            for h in hash:
                h = index.index(h)
                if h + t >= len(index):
                    new_text += index[(h + t) - len(index)]
                else:
                    new_text += index[h + t]
        return new_text
    except ValueError:
        new_hash(t)
        return False


def simple_decrypt(text, new_text, hash):
    try:
        text = text[0:len(text):len(hash)]
        for t in text:
            new_text += index[index.index(t) - index.index(hash[0])]
        return new_text
    except ValueError:
        new_hash(t)
        return False


def rsa_encrypt(text, k):
    try:
        for i in text:
            k += str(index.index(i) + 100)
        k = int(k)
        if k >= n:
            return 1
        else:
            return str(pow(int(k), e, n))
    except ValueError:
        new_hash(i)
        return False


def rsa_decrypt(k, new_text):
    try:
        t = 0
        k = str(pow(int(k), d, n))
        while t != len(k):
            x = int(k[0 + t:3 + t])
            for i in index:
                if index.index(i) == x - 100:
                    new_text += index[x - 100]
                    t += 3
                    break
        return new_text
    except ValueError:
        return False


def new_hash(i):
    index.append(i)
    with open("Lists.TXT", "a")as file:
        file.write(i)


index = hashes()
code = "n8"
print("1: Choose File\n2: Manually input")
menu(input("> "), code)