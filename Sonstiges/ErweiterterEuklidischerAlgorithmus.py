def euklidischer_algorithmus(a, b, sum):
    r = [1]
    g = []
    while r[-1] != 0:
        r.append(a[-1] % b[-1])
        g.append(a[-1] // b[-1])
        a.append(b[-1])
        b.append(r[-1])
    del r[0]
    del a[-1]
    del b[-1]
    ggt = b[-1]
    print(f"ggT: {ggt}")
    if sum % ggt == 0:
        pass
    else:
        print("ERROR")
        return
    back_count(0, 1, g, 2)


def back_count(x, y, g, t):
    while True:
        try:
            xn = x
            ny = y
            y = xn - g[-1 * t] * y
            x = ny
            t += 1
        except IndexError:
            print(f"x: {x} \ny: {y}")
            break


def input_func():
    x = int(input("a: "))
    y = int(input("b: "))
    result = int(input("result: "))
    euklidischer_algorithmus([x], [y], result)


input_func()


