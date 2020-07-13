import time
r = [2]
start = time.time()
top = 100000
for i in range(3, top, 2):
    r.append(i)
    for x in r:
        if i % x == 0 and i != x:
            r.remove(i)
            break
end = time.time()
with open("Time.txt", "a+")as f:
    f.write(f"Range: {top}  time: {end - start} seconds\n")
print(end - start)




