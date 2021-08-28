
def verifica(frase):
    print(frase)
    frase=frase.replace("-","")
    upper=0
    lower=0
    for item in frase:
        if item.isupper()==True:
            upper+=1
        else:
            lower+=1
    print('Maiúsculas = ', upper)
    print('Minúsculas = ', lower)

