matriz = []

for numLinha in range(3):
    linha = []
    for numColuna in range(3):
        linha.append(int(input()))
    matriz.append(linha)

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        print('%4d' % matriz[linha][coluna], end='')
    print()