area = lambda base, altura : base * altura/2

def main():
    base = float(input('Base = '))
    altura = float(input('Altura = '))
    print('Area =', area(base, altura))

main()