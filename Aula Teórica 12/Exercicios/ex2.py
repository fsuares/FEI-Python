from random import randint

somatoria = {
        2 : 0,
        3 : 0,
        4 : 0,
        5 : 0,
        6 : 0,
        7 : 0,
        8 : 0,
        9 : 0,
        10 : 0,
        11 : 0,
        12 : 0
    }

def lancaDados():
    lan1 = randint(1, 6)
    lan2 = randint(1, 6)
    somatoria[lan1+lan2] = somatoria[lan1+lan2] + 1

def main():
    lancamentos = 100000
    for x in range(lancamentos):
        lancaDados()
    for chave, valor in somatoria.items():
        print('%d = %d : %.2f%%' % (chave, valor, (valor * 100/ lancamentos)))

main()