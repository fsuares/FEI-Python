quantidade = int(input('Entre com a quantidade de números que serão digitados: '))
maior = -1000

for i in range(0, quantidade):
    n = int(input('{}º número : '.format(i+1)))

    if n > maior:
        maior = n

print('Maior número digitado:', maior)