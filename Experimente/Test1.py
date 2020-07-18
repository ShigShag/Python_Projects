from random import randrange

def miller_rabin(pp, iterations):
    if pp % 2 == 0 or pp <= 1:
        return False
    d = pp - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    i = 0
    for _ in range(0, iterations):
        a = randrange(1, pp)
        x = pow(a, d, pp)
        if x == 1 or x == pp - 1:
            continue
        for _ in range(r - 1, 0, -1):
            x = pow(x, 2, pp)
            if x == pp - 1:
                break
        else:
            return False
    return True

def main(top):
    import time
    primes = [2]
    start = time.time()
    for pot_prime in range(3, top + 1, 2):
        if miller_rabin(pot_prime, 5):
            primes.append(pot_prime)

    end = time.time()
    return primes, end - start


print("Something is wrong here")
#p, t = main(int(input("Top Border: ")))
p, t = main(21)
print(t, "seconds")

#if input("Print Numbers(y):") == "y":
print(p)

# 44 seconds for 100_000_000 without rabin miller internal loop(iterations)
# 38 seconds for 100_000_000 with internal loop