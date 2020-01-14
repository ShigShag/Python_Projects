import random
i = 1
switch = 0
while i < 10:
    i = 1
    x = random.randint(0, 8)
    i = i + x
    guess = int(input("Guess a number from 1 to 9: "))
    if guess == i:
        print(f"You choose the right Number: {guess}")
        i = 10
        break
    else:
        print(f"You have choosen the wrong number: {guess}")
        switch = switch + 1
        if switch == 3:
            i = 10

else:
    print("Too many Tries!")






