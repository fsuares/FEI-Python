from random import randint

matriz = []

for numLinha in range(10):
    linha = []
    for numColuna in range(15):
        linha.append(randint(10,99))
    matriz.append(linha)

for numlinha in range(len(matriz)):
    for numcoluna in range(len(matriz[numlinha])):
        print('%4d' % matriz[numlinha][numcoluna], end='')
    print()

for numlinha in range(len(matriz)):
    print('%4d' % matriz[numlinha][0], end='')
    print()
