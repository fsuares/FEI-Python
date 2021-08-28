def multiplo(x, y):
        return x % y == 0

def main():
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    print(multiplo(a, b))

main()