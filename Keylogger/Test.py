import pickle
x = []
for i in range(0, 1000):
    x.append(i)
print(x)
x = pickle.dumps(x)

x = str(x).encode("utf-8")