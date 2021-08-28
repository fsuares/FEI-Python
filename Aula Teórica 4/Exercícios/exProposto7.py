num_vis = int(input('Digite o nº de visitantes: '))
valor_final = 0

for i in range(0, num_vis):
    tipo_vis = int(input('Digite a idade de cada visitante: '))
    if (0 < tipo_vis < 3):
        valor_final += 0

    elif (2 < tipo_vis < 13):
        valor_final += 14

    elif tipo_vis > 65:
        valor_final += 18

    else:
        valor_final += 23

print('R$',valor_final)