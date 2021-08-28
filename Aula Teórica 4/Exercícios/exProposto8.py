#distância entre pontos -> raiz ((xb - xa)^2 + (Yb - Ya)^2)
from math import *

perimetro = 0

xIni = int(input('Digite o X da coordenada: '))
yIni = int(input('Digite o Y da coordenada: '))

anteriorX = xIni
anteriorY = yIni

while True:
    entradaX = str(input('Digite o X da coordenada (em branco para sair): '))
    if entradaX == '':
        distPonto = sqrt(((xIni - x) ** 2) + ((yIni - y) ** 2))
        perimetro = perimetro + distPonto
        break

    elif entradaX != '':
        x = int(entradaX)
        y = int(input('Digite o Y da coordenada: '))

        #distância entre pontos
        distPonto = sqrt(((anteriorX - x)**2) + ((anteriorY - y)**2))
        perimetro = perimetro + distPonto

        anteriorX = x
        anteriorY = y

print('O perimetro deste poligono é: ', perimetro)