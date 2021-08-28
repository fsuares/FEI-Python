from random import randrange, choice, randint

def letras():
    alphab = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
     'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    letras = []

    for i in range(4):
        letras.append(choice(alphab))
    return letras

def numeros():
    numeros = []
    for n in range(3):
        numeros.append(randrange(9))
    return numeros

def criar_placa(numeros, letras):
    placa = []
    for i in range(7):
        if i <= 2:
            placa.append(letras[i]) 
        elif i == 3:
            placa.append(numeros[0])
        elif i == 4:
            placa.append(letras[3])
        else:
            placa.append(numeros[i - 4])
    return placa


