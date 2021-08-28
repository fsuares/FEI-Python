list = []
maior = -999
for i in range(1,11):
    valor = float(input('Digite o {}º valor: '.format(i)))
    list.append(valor)

    if valor > maior:
        maior = valor

print(list)
print('Posição do maior elemento: ', list.index(maior))