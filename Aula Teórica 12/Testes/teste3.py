dicionario = {
    '1' : 'um',
    '2' : 'dois',
    '3' : 'três'
}

for chave in dicionario:
    print(dicionario[chave])

print()
for n in dicionario.keys():
    print(n)

print()
for chave, valor in dicionario.items():
    print(chave, valor)
