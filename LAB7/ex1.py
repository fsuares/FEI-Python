from math import sqrt
def hipo(a,b):
    return sqrt(a**2 + b**2)

def main():
    a = float(input('Digite o primeiro lado do triângulo: '))
    b = float(input('Digite o segundo lado do triângulo: '))
    print('Hipotenusa: {:.2f}'.format(hipo(a,b)))
main()