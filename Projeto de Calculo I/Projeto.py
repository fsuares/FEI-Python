
def seqNum():
    pass
def main():
    w = complex(input('Digite o valor de w: '))
    e = float(input('Digite o valor de e: '))
    m = int(input('Digite o valor de m: '))
    x = []
    zn = 0

    for n in range(m):
        zn = (zn-1)**2+w
        x.append(zn)
    for n in range(len(x)):
        print(x[n])

main()