
matriz = []

for numLinha in range(10):
    linha = []
    for numColuna in range(15):
        elemento = numLinha + numColuna
        linha.append(elemento)
    matriz.append(linha)

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        print('%4d' % matriz[linha][coluna], end='')
    print()