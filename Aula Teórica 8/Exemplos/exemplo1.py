
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

#alterando o valor de um determinado elemento
#matriz[0][2] = 10

print(matriz)

#acessando um elemento especifico da matriz
#print(matriz[x][y])

#for linha in range(3):
    #print(matriz[linha])
    #for coluna in range(3):
        #print(matriz[linha][coluna])

for linha in range(len(matriz)):
    print(matriz[linha])
    for coluna in range(len(matriz[linha])):
        print(matriz[linha][coluna])