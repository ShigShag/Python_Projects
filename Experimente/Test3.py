import math
import time

def is_prime(n):
    if n==1:
        return False
    if n==2:
        return True
    if n > 2 and n % 2 == 0:
        return False

    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return False
    return True



s = time.time()
#for n in range(1, 10_000_000):
    #is_prime(n)
print(is_prime(71))
e = time.time()
print(e - s)


# 101 seconds for 100.000.000