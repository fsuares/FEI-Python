
lojas = []
for n in range(3):
    input_lojas = lojas.append(input('Digite o nome da loja: '))

produtos = []
for n in range(5):
    input_produtos = produtos.append(input('Digite o nome do produto: '))

precos = []
for linha in range(3):
    lista_linha = []
    for coluna in range(5):
        input_precos = int(input('Digite o preco do produto %d na loja %d: ' % (coluna, linha)))
        lista_linha.append(input_precos)
    precos.append(lista_linha)

print()
print('Lojas: ')
for nome_lojas in range(3):
    print('%s' % lojas[nome_lojas], end='')
    print()

print()
print('Produtos: ')
for nome_produtos in range(5):
    print('%s' % produtos[nome_produtos], end='')
    print()

print()
print('Preços: ')
for linha in range(3):
    for coluna in range(5):
        print('%3d ' % precos[linha][coluna], end='')
    print()

print()
print('Preços menores que R$ 50.00: ')
cont0 = 0
cont1 = 0
for linha in range(3):
    for coluna in range(5):
        if precos[linha][coluna] < 50:
            print('Loja: {}, produto {} e preço {}'.format(lojas[cont0], produtos[cont1], precos[linha][coluna]))
        cont1 += 1
    else:
        cont1 = 0
    print()
    cont0 += 1
