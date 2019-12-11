import secrets
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
    while not miller_rabin(p):
        p = pot_prime()
    t = 124
    while t != 0:
        if miller_rabin(p):
            print(t)
            t -= 1
        else:
            prime_number()
    print(p)


def pot_prime():
    p = secrets.randbits(5000)
    return p


prime_number()
