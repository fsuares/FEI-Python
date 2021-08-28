
def limite(lim):
    num = []
    for n in range(lim + 1):
        if n == 1:
            num.append(0)
        else:
            num.append(n)

    i = 2
    prim = [0, 1]
    while i < lim:
        for s in range(len(num)):
            if num[s] % i == 0 and num[s] != i:
                num[s] = 0

        for t in range(lim + 1):
            if t != 0 and t != i and t not in prim:
                i = t
                prim.append(t)
                break

    frase = ''
    for f in num:
        frase += str(f)
        frase+=' '
    print(frase)