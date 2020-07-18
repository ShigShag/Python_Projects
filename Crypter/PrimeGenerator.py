import secrets
import time
from random import randrange


def miller_rabin(p, iterations):
    if p % 2 == 0 or p <= 1:
        return False
    d = p - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    i = 0
    while i < iterations:
        a = randrange(1, p)
        x = pow(a, d, p)
        if x == 1 or x == p - 1:
            # return True
            i += 1
            continue
        while r > 1:
            x = pow(x, 2, p)
            if x == 1:
                return False
            if x == p - 1:
                # return True
                i += 1
                continue
            r -= 1
        return False
    return True


def prime_number():
    # 4 is no prime
    p = 4
    bits = 2000
    while not miller_rabin(p, 5):
        #p = secrets.randbits(bits)
        p = 13
    print(p)

prime_number()



