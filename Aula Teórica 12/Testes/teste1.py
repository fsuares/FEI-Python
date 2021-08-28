dicionario = {
    '1' : 'Ola',
    '2' : 'Mundo'
}

chave = input('Chave: ')
novo = input('Item: ')

dicionario[chave] = novo

print(dicionario)
print(dicionario.keys())
print(dicionario.items())
print(dicionario.values())