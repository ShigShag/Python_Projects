import random
import time

def partition(array, l, r):
    p = array[l]
    i = l + 1
    j = r

    while j > i:
        while array[i] <= p and i < r:
            i += 1
        while array[j] >= p and j > l:
            j -= 1

        if i < j:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

    temp = array[l]
    array[l] = array[j]
    array[j] = temp
    return j


def quick_sort(array, l, r):
    if l < r:
        m = partition(array, l ,r)
        quick_sort(array, l, m - 1)
        quick_sort(array, m + 1, r)

a = []

for i in range(0, 20000000 +1):
    a.append(random.randrange(0, 30000))

b = a



start = time.time()
b.sort()
end = time.time()
print("Time to sort with normal sort: " + str(end - start) + " Seconds")

