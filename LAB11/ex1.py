#Crie uma função em Python chamada contaPalavras que recebe uma string e conta quantas 
# palavras tem nessa string. Sua função deve  retornar o número de palavras contadas. 

def contaPalavras(frase):
    f = frase.split()
    return len(f)