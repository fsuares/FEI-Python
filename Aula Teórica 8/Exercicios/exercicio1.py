from random import randint
from random import uniform

inteiro = []
reais = []
for _ in range(10):
    inteiro.append(randint(0,11))

for _ in range(2):
    reais.append(uniform(0,15))

listaString = ['oi', 'tudo bem?', 'como vai?', 'tudo tranquilo?']
complexos = [1+2j, 4+1j, 2-2j, 9+7j]
completa = [inteiro, reais, listaString, complexos]

del inteiro, reais, listaString, complexos

print(completa)

for _ in range(50):
    completa[0].append(randint(0,100))

print(completa[0])