from math import sqrt
a = input("[a] > ")
b = input("[b] > ")
c = input("[c] > ")


def pq(a, b, c):
    a, b, c = int(a), int(b), int(c)
    b = b / a
    c = c / a
    try:
        lsg1 = (-1 * b)/2 + sqrt((b / 2) ** 2 - c)
        lsg2 = (-1 * b) / 2 - sqrt((b / 2) ** 2 - c)
    except ValueError:
        return False, False

    return lsg1, lsg2


ls1, ls2 = pq(a, b, c)
if not ls1 and not ls2:
    print("No solution")
else:
    print(f"X1 = {ls1}")
    print(f"X2 = {ls2}")
input("Press Enter to exit")
