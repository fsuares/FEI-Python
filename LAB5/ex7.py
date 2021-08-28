x = int(input('Digite o número desejado: '))
palpite = x/2
erro = palpite**2 - x

while erro > 10**(-12):
    palpite = (palpite + x/palpite)/2
    erro = palpite**2 - x

print('{:.3f}'.format(palpite))