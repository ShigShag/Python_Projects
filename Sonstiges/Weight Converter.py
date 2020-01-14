unit = input("1: Pounds 2:Kilograms: ")
if int(unit) > 2 or int(unit) < 1:
    print("Please choose between one or two")

weight = int(input("Enter your weight: "))
if int(unit) == 1:
    result = weight / 2.205
    print(f"In KG: {result} KG")
else:
    result = weight * 2.205
    print(f"In Pounds: {result} Pounds")


