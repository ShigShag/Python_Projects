def Namess(First_name,Second_name):       #Identification
    return f"{First_name} {Second_name}"


#Firstname = input("Vorname ")              #Namen
#Secondname = input("Nachname ")
#print(F"Hello {Firstname} {Secondname}")
#print("Choose a Company:")
#Names = Namess(Firstname,Secondname)

def Auto(Marke, Modell):
    return f"{Marke} {Modell}"


print("1. VW")
print("2. Audi")

IMarke = input("Bitte die Nummer eingeben: ")
if int(IMarke) == 1:
    print("You have choosen VW")
    print("1. Golf")
    print("2. Polo")
    print("3. Tiguan")
    IModell = input("Bitte die Nummer eingeben: ")
elif int(IMarke) == 2:
    print("You have choosen Audi ")
    print("1. A1")
    print("2. A3")
    print("3. R8")
    IModell = input("Bitte die Nummer eingeben; ")
else:
    print("You have choosen nothing")
    exit