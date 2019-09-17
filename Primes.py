import secrets
prime_found = False
while prime_found is False:
    pot_prime = secrets.randbits(60)
    print(pot_prime)
    positive_checks = 0
    for a in range(1, 6, 1):
        if ((a ** pot_prime) - a) % pot_prime == 0:
            positive_checks = positive_checks + 1
        else:
            break
    if positive_checks == 5:
        print(pot_prime)
        prime_found = True






