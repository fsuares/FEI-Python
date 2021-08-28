from random import choice, randint
from string import ascii_uppercase

def random_char(y):
    for x in range(y):
       return''.join(choice(ascii_uppercase))

def letras():
    letras = []
    for n in range(4):
        letras.append(random_char(1))
    return letras

def numeros():
    numeros = []
    for n in range(3):
        numeros.append(randint(0, 9))
    return numeros

def criar_placa(letras, numeros):
    placa = []
    for i in range(7):
        if i < 3:
            placa.append(letras[i])
        elif i == 4:
            placa.append(letras[3])
        elif i == 3:
            placa.append(numeros[0])
        elif i == 5:
            placa.append(numeros[1])
        elif i == 6:
            placa.append(numeros[2])

    print('Placa = ', end='')
    for n in range(len(placa)):
        print(placa[n], end='')
        