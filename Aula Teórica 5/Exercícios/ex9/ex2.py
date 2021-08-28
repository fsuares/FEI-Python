multiplo = lambda a, b : a % b == 0

def main():
    a = float(input('Digite o primeiro número: '))
    b = float(input('Digite o segundo número: '))
    print(multiplo(a, b))

main()