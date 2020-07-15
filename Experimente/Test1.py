from random import randrange

def miller_rabin(p):
    if (p % 2 == 0 and p != 2) or p <= 1:
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

def main(top):
    import time
    primes = [2]
    start = time.time()
    for pot_prime in range(3, top + 1, 2):
        i = 0
        while i != 5:
            if miller_rabin(pot_prime):
                i += 1
            else:
                break
        if i == 5:
            primes.append(pot_prime)
    end = time.time()
    return primes, end - start


p, t = main(int(input("Top Border: ")))
print(t, "seconds")

if input("Print Numbers(y):") == "y":
    print(p)