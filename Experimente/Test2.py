from time import time
def prime_list(top):
    r = [2]
    start = time()
    for i in range(3, top + 1, 2):
        passed = 1
        for x in r:
            if i % x == 0:
                passed = 0
                break
        if passed:
            r.append(i)
    end = time()
    return r, end - start

