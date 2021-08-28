def doação(sexo, peso):
    if sexo == 'masculino' and peso >= 60:
        print('Parabéns! Você pode doar sangue!')

    elif sexo == 'masculino' and peso < 60:
        print('Você não pode doar sangue por não ter o peso minimo.')

    elif sexo == 'feminino' and peso >= 50:
        print('Parabéns! Você pode doar sangue!')

    elif sexo == 'feminino' and peso < 50:
        print('Você não pode doar sangue por não ter o peso minimo.')

def main():
    sexo = input('Digite seu sexo: ')
    peso = int(input('Digite seu peso: '))
    doação(sexo, peso)
main()
