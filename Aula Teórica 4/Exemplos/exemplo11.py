from random import randint
from time import sleep

maior = 0
contador = 0

for i in range(0, 100): # [0,1,2, 3, ..., 9]
    n = randint(1, 100) # [1,2, 3, ..., 100]
    print()
    print('i:', i)
    print ('n:', n)
    if n > maior:
        maior = n
        contador += 1

print('Maior número: ', maior)
print('Aconteceram {} atualizações.'.format(contador))