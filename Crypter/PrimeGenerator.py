import secrets
import time
from random import randrange


def miller_rabin(p):
    if p % 2 == 0 or p <= 1:
        return False
    d = p - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    a = randrange(1, p)
    x = pow(a, d, p)
    if x == 1 or x == p - 1:
        return True
    while r > 1:
        x = pow(x, 2, p)
        if x == 1:
            return False
        if x == p - 1:
            return True
        r -= 1
    return False


def prime_number():
    # 4 is no prime
    p = 4
    bits = 2000
    while not miller_rabin(p):
        p = pot_prime(bits)
    t = 10
    while t != 0:
        if miller_rabin(p):
            t -= 1
        else:
            prime_number()
    with open("Rabin_Miller.txt", "a+")as f:
        f.write(f"{p}\n")
    prime_number()

def pot_prime(size):
    p = secrets.randbits(size)
    return p

prime_number()



