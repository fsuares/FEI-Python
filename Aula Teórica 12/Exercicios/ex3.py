
dicionario = {}

def charUni(frase):
    for letra in frase:
        dicionario[letra] = 1
    print('{} caracteres unicos, são eles: '.format(len(dicionario)))
    print(list(dicionario.keys()))


def main():
    frase = input('Digite uma frase: ')
    charUni(frase)

main()
