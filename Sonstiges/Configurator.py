import time
print("Civic or Hyundai ?")
time.sleep(1)
print("Choose you engine:")
print("1: Honda 320 HP manual transmission")
print("2: Hyundai 275 HP manual transmission")
model = input("Choose an engine by typing the number: ")
if model < str(1):
    print("Number not aviable")
    exit
elif model > str(2):
    print("Number not aviable")
    exit
else:
    if int(model) == 1:
        print("You choosed the Honda")
        print("Choose your Model:")
        print("1:GT")
        print("2:GTR")
        line = input("Select a number: ")
        if line < str(1):
            print("Number not aviable")
            exit
        elif line > str(2):
            print("Number not aviable")
            exit
        else:
            if int(line) == 1:
                line = "GT"
            else:
                line = "GTR"
            print("You choosed: " + str(line))
    else:
        if int(model) == 2:
            print("You choosed Hyundai")
            print("Choose your Model:")
            print("1:Hyundai I30n")
            print("2:Hyundai I30n performance")
            line1 = input("Select a number: ")
            if line1  < str(1):
                print("Number not aviable")
                exit
            elif line1 > str(2):
                print("Number not aviable")
                exit
            else:
                if int(line1) == 1:
                    line1 = "Hyundai I30n"
                else:
                    line1 = "Hyundai I30n perfornance"
                print("You choosed: " + str(line1))








#first = "Leon"
#last = "Weinmann"
#msg = f'{first} {last} is a coder '
#print(msg)
#weight = input("Whats your wheight(in pounds)? " )
#Kilos = int(weight) / 2.205
#print("Kgs: " + str(Kilos))
#name = 'Jennifer'
#print  (name[1:-1])
