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

with open("F:\Python_Projects\Crypter\Rabin_Miller.txt", "r")as f:
    prime_array = f.readlines()

start = time.time()
for _ in range(0, 100):
    for prime in prime_array:
        miller_rabin(int(prime))
end = time.time()




with open("Log_File.txt", "a+")as f:
    f.write(f"Time to work array: {end - start} seconds\n")

print(f"{end - start} seconds")
