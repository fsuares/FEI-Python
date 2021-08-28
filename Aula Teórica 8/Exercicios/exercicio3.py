matriz = []
soma_impar = []

for numLinha in range(4):
    linha = []
    for numColuna in range(4):
        linha.append(int(input('Elemento: ')))
    matriz.append(linha)

for numlinha in range(len(matriz)):
    soma = 0
    for numcoluna in range(len(matriz[numlinha])):
        print('%4d' % matriz[numlinha][numcoluna], end=' ')
        if matriz[numlinha][numcoluna] % 2 != 0:
            soma = soma + matriz[numlinha][numcoluna]
    print()
    soma_impar.append(soma)

print()
print(soma_impar)
