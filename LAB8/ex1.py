list_carros = []
list_consumo = []
melhor = 1

for i in range (1,6):
    list_carros.append(input())

for i in range(1, 6):
    list_consumo.append(int(input()))
    if list_consumo[i] > list_consumo[melhor]:
        melhor = i


print(list_carros[melhor])

for x in list_consumo:
    print(round(1000/list_consumo))
