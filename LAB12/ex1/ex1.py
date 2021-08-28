
from random import choice, randint
from string import ascii_uppercase

def random_char(y):
       return ''.join(choice(ascii_uppercase) for x in range(y))

def criar_placa():
    placa = []
    placa.append(random_char(1))
    placa.append(random_char(1))
    placa.append(random_char(1))
    placa.append(randint(0, 9))
    placa.append(random_char(1))
    placa.append(randint(0, 9))
    placa.append(randint(0, 9))

    print('Placa =', end='')
    for n in range(len(placa)):
        print(placa[n], end='')



