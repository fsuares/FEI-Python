res = 0

while True:
    n = float(input('Digite um numero: '))
    op = input("Digite a operação: \n [+]\n [-]\n [*]\n [/]")
    if op == '+':
        res += n

    elif op == '-':
        res -= n

    elif op == '*':
        res = res * n

    elif op == '/':
        res = res / n

    elif n == 0 or res == 0:
        break

print('Resultado = {}'.format(res))