list = []

for i in range(1,11):
    valor = float(input('Digite o {}º valor: '.format(i)))
    list.append(valor)
    if valor % 2 == 0:
        soma_elementos = soma_elementos + valor
        soma_indices = soma_indices + list.index(valor)

print('A Soma dos elementos é ', soma_elementos)
print('A soma dos indices é ', soma_indices)