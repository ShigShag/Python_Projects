import math
print("Dreieck muss einen rechten Winkel haben!")
print("Wenn nicht bekannt: ?")
FK = input("Erste Kathete: ")
SK = input("Zweite Kathete: ")
H = input("Hypotenuse: ")


def Satz(x, y, z):
    a = "?" in x
    b = "?" in y

    if b:
        ahochzwei = int(x) ** 2
        chochzwei = int(z) ** 2
        flsg = int(chochzwei) - int(ahochzwei)
        lsg = math.sqrt(flsg)
        print("Die Lösung ist:")
        print(lsg)
    elif a:
        ahochzwei = int(y) ** 2
        chochzwei = int(z) ** 2
        flsg = int(chochzwei) - int(ahochzwei)
        lsg = math.sqrt(flsg)
        print("Die Lösung ist:")
        print(lsg)

    else:
        ahochzwei = int(x) ** 2
        bhochzwei = int(y) ** 2
        flsg = int(ahochzwei) + int(bhochzwei)
        lsg = int(math.sqrt(flsg))
        print("Die Lösung ist:")
        print(lsg)


Satz(FK, SK, H)