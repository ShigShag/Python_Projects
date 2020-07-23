import math

def peer(i):
    return (-1) ** i * math.ceil(i / 2) ** 2


for i in range(0, 11):
    print(f"for i = {i}: " + str(peer(i)))


