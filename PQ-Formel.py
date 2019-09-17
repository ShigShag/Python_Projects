import math
print("[+[+[+ PQ-Formel +]+]+]")
print("[+[+[+ x²+px+q +]+]+]")
print("Bitte Eingaben machen:")
print("Wenn ERROR, dann kein Ergebnis")
xx = input("Faktor von x²: ")
x = input("Faktor von x (p): ")
q = input("Summe von q: ")


def pq(x, fp, fq):
    p = int(fp) / int(x)
    q = int(fq) / int(x)
    lsg1 = (-1 * p)/2 + math.sqrt((p / 2) ** 2 - q)
    lsg2 = (-1 * p) / 2 - math.sqrt((p / 2) ** 2 - q)
    print("X1 und X2 sind:")
    print(f"X1:{lsg1}")
    print(f"X2:{lsg2}")


pq(xx, x, q)

