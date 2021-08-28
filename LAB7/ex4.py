def tarifa(km):
    return (km/0.125) * 0.5

def main():
    km = float(input('Digite a quantidade de quilômetros: '))
    print('Tarifa {:.2f}'.format(10 + tarifa(km)))
main()