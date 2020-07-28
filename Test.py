def binary(t):
    e = t % 2
    q = e
    while q != 0 and e != 0:
        e = q % e
        print(q % e)




binary(23)
