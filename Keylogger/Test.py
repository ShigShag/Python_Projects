x = []
for i in range(0, 100):
    x.append(i)

with open("wasd.txt", "a+")as f:
    f.write(x)