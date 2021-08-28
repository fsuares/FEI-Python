n = int(input("Digite um numero de 0 a 10: "))

while n:
    if n >= 0 and n <= 10:
        print('Numero aceito!')
        break

    else:
        print('Numero nnválido!')
        n = int(input("Digite um numero de 0 a 10: "))