
def verifica(frase):
    frase=frase.replace("-","")
    upper = 0
    lower = 0
    for i in range(len(frase)):
        if i.isupper() == True:
            upper += 1
        elif i.islower() == True:
            lower += 1
    return upper,lower

    print(upper)
    print(lower)

texto = str(input('Texto: '))
verifica(texto)