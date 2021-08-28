matriz = []

for numLinha in range(3):
    linha = []
    for numColuna in range(3):
        linha.append(int(input('Elemento: ')))
    matriz.append(linha)

for numlinha in range(len(matriz)):
    for numcoluna in range(len(matriz[numlinha])):
        print('%4d' % matriz[numlinha][numcoluna], end=' ')
    print()

#for linha in range(3):
#    for coluna in range(3):
#       if linha == coluna:
#           soma = soma + matriz[linha][coluna]
#print('Traço da matriz = ', soma)


#for linha_coluna in range(3):
#    soma = soma + matriz[linha_coluna][linha_coluna]
#print('Traço da matriz = ', soma)


print('Traço da matriz = ', matriz[0][0] + matriz[1][1] + matriz[2][2])
