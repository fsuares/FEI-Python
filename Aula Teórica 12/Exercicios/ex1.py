def procuraReversa():
    valor = int(input('Digite o valor que quer procurar: '))

    dicionario = {
        'Primeiro' : 10,
        'Segundo' : 20,
        'Terceiro' : 25,
        'Quarto' : 10,
        'Quinto' : 84,
        'Sexto' : 10
    }

    for chav, num in dicionario.items():
        if num == valor:
            print(chav)


def main():
    procuraReversa()

main()
