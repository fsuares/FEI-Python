from random import randint

matriz = []
for numlinha in range(20):
    linha = []
    for numcoluna in range(10):
        linha.append(randint(0, 10))
    matriz.append(linha)

print('Matriz original: ')
for numlinha in range(20):
    for numcoluna in range(10):
        print('%4d ' % matriz[numlinha][numcoluna], end='')
    print()

somatoria = []
soma = 0

print()
print('Vetor com a somatória de cada linha: ')
for numlinha in range(20):
    for numcoluna in range(10):
        soma = soma + matriz[numlinha][numcoluna]
    somatoria.append(soma)
print(somatoria)

matriz_multiplicada = []
cont = 0

print()
print('matriz depois da multiplicação: ')
for numlinha in range(20):
    linha_multiplicada = []
    for numcoluna in range(10):
        linha_multiplicada.append(matriz[numlinha][numcoluna] * somatoria[cont])
    matriz_multiplicada.append(linha_multiplicada)
    cont += 1

for numlinha in range(20):
    for numcoluna in range(10):
        print('%4d ' % matriz_multiplicada[numlinha][numcoluna], end='')
    print()
