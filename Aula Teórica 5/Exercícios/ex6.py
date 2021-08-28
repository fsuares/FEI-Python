def divisao(a, b):
    contador = 0
    while a > 0:
        resto = a - b
        contador += 1

    print('A parte inteira é',contador)
    print('O resto é', resto)

def main():
    a = int(input('Digite o primeiro Nº: '))
    b = int(input('Digite o segundo M: '))
    divisao(a,b)

main()