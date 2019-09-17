list = []
for i in range(3, 1200, 2):
    list.append(i)
    for x in list:
        if i % x == 0 and i != x:
            list.remove(i)
            break
print(list)





