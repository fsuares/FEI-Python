matriz = []

for numlinha in range(4):
    linha = []
    for numcoluna in range(2):
        elemento = int(input('Digite o elemento da linha {} e coluna {}: '.format(numlinha, numcoluna)))
        linha.append(elemento)
    matriz.append(linha)

print('Matriz Original: ')
for numlinha in range(len(matriz)):
    for numcoluna in range(len(matriz[numlinha])):
        print('%3d' % matriz[numlinha][numcoluna], end=' ')
    print()

contador = 0

print('')
for numlinha in range(4):
    for numcoluna in range(2):
        if matriz[numlinha][numcoluna] > 10:
            print('%d é maior que 10!' % (matriz[numlinha][numcoluna]))
            contador = contador + 1

print('No total, %d elementos são maiores que 10!' % contador)

for numlinha in range(4):
    for numcoluna in range(2):
        if matriz[numlinha][numcoluna] > 10:
            matriz[numlinha][numcoluna] = 0

for numlinha in range(len(matriz)):
    for numcoluna in range(len(matriz[numlinha])):
        print('%3d' % matriz[numlinha][numcoluna], end=' ')
    print()