dicionario = {
    '1' : 'Ola',
    '2' : 'Mundo'
}

chave = input('Chave: ')
novo = input('Item: ')

dicionario[chave] = novo

print(dicionario)
print(list(dicionario.keys()))
print(list(dicionario.items()))
print(list(dicionario.values()))