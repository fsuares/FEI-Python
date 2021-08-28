#lista para armazenar os carros
carros = []

#lista para armazenar o consumo
consumo = []

#populamos a lista carros
for x in range(5):
    carros.append(input())

#variavel para guardar o indice do melhor consumo
i = 0

#populamos a lista consimo
for x in range(5):
    consumo.append(int(input()))
    if consumo[x] > consumo[i]:
        i = x

print(carros[i])

#calculo a quantidade de litros para 1000km, para cada carro
for x in consumo:
    print(round(1000/x))