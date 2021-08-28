n = 11

while n > 10 or n < 0:
    n = int(input('Digite um número: '))
    if n < 0 or n > 10:
        print('Numero inválido!')
    else:
        print('Numero aceito!')
