matriz = []

for numlinha in range(2):
    linha = []
    for numcoluna in range(2):
        elemento = int(input('Digite o elemento da linha {} e coluna {}: '.format(numlinha, numcoluna)))
        linha.append(elemento)
    matriz.append(linha)

multiplicador = matriz[0][0]

for numlinha in range(2):
    for numcoluna in range(2):
        if matriz[numlinha][numcoluna] > multiplicador:
            multiplicador = matriz[numlinha][numcoluna]

for numlinha in range(2):
    for numcoluna in range(2):
        matriz[numlinha][numcoluna] *= multiplicador

print('Matriz Resultante: ')
for numlinha in range(len(matriz)):
    for numcoluna in range(len(matriz[numlinha])):
        print('%3d' % matriz[numlinha][numcoluna], end=' ')
    print()