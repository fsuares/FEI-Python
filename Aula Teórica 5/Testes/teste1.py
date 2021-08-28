def par(i):
    if i % 2 == 0:
        return True
    return False

while True:
    a = int(input('Digite um Nº: '))
    print(par(a))

    if a == 0:
        print()
        print('Obrigado por testar seus números!')
        break
