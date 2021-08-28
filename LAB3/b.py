from math import *

forma = input("Você deseja calcular o volume do dodecaedro ou icosaedro: ")
aresta = float(input("Digite o valor da aresta a em metros: "))

if forma == "dodecaedro":
    volume = ((15+(7*(sqrt(5))))/4)*aresta**3
    print("O volume de um dodecaedro regular com {} de aresta é: {:.2f}".format(aresta,volume))

elif forma == "icosaedro":
    volume = (5/12)*(3+(sqrt(5)))*(aresta**3)
    print("O volume de um icosaedro regular com {} de aresta é: {:.2f}".format(aresta, volume))