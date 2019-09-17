def Eingabe():
    Name = input("Name: ")
    if Name.isalpha():
        Formular(Name)
    else:
        Eingabe()


def Formular(Name):
    print(f"Name: {Name}")


Eingabe()
