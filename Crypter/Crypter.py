import RSAModule


def rsa_encrypt(text):
    new = ""
    for i in text:
        i = str(hash_liste.index(i) + 100)
        new += i
    new = str(pow(int(new), e, n))
    with open("Test.TXT", "w") as f:
        f.write(new)


def rsa_decrypt(code):
    with open("Test.TXT", "r")as text:
        sypher_text = text.read()
    decrypt = str(pow(int(sypher_text), d, n))
    decryption(decrypt, code)


def user_input():
    try:
        x = int(input("> "))
    except ValueError:
        print("ERROR")
        print("1: crypt\n2: decrypt")
        user_input()
    if x != 1 and x != 2:
        print("ERROR")
        print("1: crypt\n2: decrypt")
        user_input()
    elif x == 1:
        encryption(code)
        print("encryption successful")
        user_input()
    elif x == 2:
        rsa_decrypt(code)
        print("decryption successful")
        user_input()


def hash_list():
    x = open("Lists.TXT", "r")
    content = x.readline()
    check_list = ["\n"]
    for i in content:
        check_list.append(i)
    x.close
    return check_list


def encryption(code):
    f = open("Test.TXT", "r")
    content = list(f.read())
    f.close()
    for i in content:
        if i not in hash_liste:
                hash_liste.append(i)
                with open("Test.TXT", "a") as List:
                    List.write(i)
    for code in code:
        crypted = ""
        for i in content:
            i = hash_liste.index(i)
            for code_item in code:
                code_item = hash_liste.index(code_item)
                if code_item + i >= len(hash_liste):
                    result = (code_item + i) - len(hash_liste)
                else:
                    result = code_item + i
                crypted += hash_liste[result]
                content = crypted
    rsa_encrypt(crypted)


def decryption(decrypted_numbers, code):
    t = 0
    decrypted = ""
    while t != len(decrypted_numbers):
        digits = int(decrypted_numbers[0 + t:3 + t])
        for item in hash_liste:
            if hash_liste.index(item) == digits - 100:
                decrypted += item
                t += 3
                break
    code.reverse()
    for code in code:
        content = ""
        ci = hash_liste.index(code[0])
        decrypted = decrypted[0:len(decrypted):len(code)]
        for i in decrypted:
            i = hash_liste.index(i)
            result = i - ci
            content += hash_liste[result]
            decrypted = content
    with open("Test.TXT", "w")as file:
        file.write(decrypted)


n, e, d = RSAModule.rsa_module()
hash_liste = hash_list()
code = ['.']
#user_input()
encryption(code)
rsa_decrypt(code)
