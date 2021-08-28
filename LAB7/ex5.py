def peso_planet():
    planet = input('Digite o nome do planeta desejado: ')
    peso_terra = float(input('Digite o peso da pessoa na Terra em kg: '))

    if planet == 'Terra':
        print('Peso em {}: {:.2f}'.format(planet,peso_terra))

    elif planet == 'Mercúrio':
        print('Peso em {}: {:.2f}'.format(planet, peso_terra*0.37))

    elif planet == 'Vênus':
        print('Peso em {}: {:.2f}'.format(planet, peso_terra*0.88))

    elif planet == 'Marte':
        print('Peso em {}: {:.2f}'.format(planet, peso_terra*0.38))

    elif planet == 'Júpiter':
        print('Peso em {}: {:.2f}'.format(planet, peso_terra * 2.64))

    elif planet == 'Saturno':
        print('Peso em {}: {:.2f}'.format(planet, peso_terra * 1.15))

    elif planet == 'Urano':
        print('Peso em {}: {:.2f}'.format(planet, peso_terra * 1.17))

    elif planet == 'Netuno':
        print('Peso em {}: {:.2f}'.format(planet, peso_terra * 1.18))

def main():
    peso_planet()

main()