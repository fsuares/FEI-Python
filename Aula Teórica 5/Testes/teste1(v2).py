def par(i):
    return (i%2==0)

def parOuImpar(i):
    if i%2!=0:
        return ('Impar')
    elif par(i):
        return('Par')

while True:
    a = int(input('Digite um Nº: '))
    print(parOuImpar(a))

    if a == 0:
        print()
        print('Obrigado por testar seus números!')
        break
