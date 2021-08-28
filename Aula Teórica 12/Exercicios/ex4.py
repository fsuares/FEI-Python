
dicionario1 = {}
dicionario2 = {}

def anagrama(palavra1, palavra2):
    for letra in palavra1:
        if letra.isalpha():
            dicionario1[letra] = 1

    for letra in palavra2:
        if letra.isalpha():
            dicionario2[letra] = 1

    if len(dicionario1) == len(dicionario2):
        print('As palavras são anagramas.')
    
    else:
        print('As palavras não são anagramas.')


def main():
    palavra1 = input('Digite uma palavra: ')
    palavra2 = input('Digite uma palavra: ')
    anagrama(palavra1, palavra2)

main()
