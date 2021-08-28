matriz = []

for numLinha in range(4):
    linha = []
    soma_impar = 0
    for numColuna in range(4):
        elemento = int(input(''))
        linha.append(elemento)
        if elemento % 2 != 0:
            soma_impar = soma_impar + elemento
    matriz.append(linha)

for numlinha in range(len(matriz)):
    for numcoluna in range(len(matriz[numlinha])):
        print('%4d' % matriz[numlinha][numcoluna], end='')
    print()

print('Soma = %4d' % soma_impar)