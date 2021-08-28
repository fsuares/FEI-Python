#Crie uma função chamada spellChecker() que recebe uma String e verifica 
# se as palavras dessa String estão corretas, para verificação utilize o 
# arquivo words.txt (o arquivo possui 466k palavras), que possuí 
# todas as palavras do inglês. Sua função deverá retornar uma listas das palavras que
# não forem encontradas no arquivo.

def spellChecker(frase):
    global words
    s = frase.lower().replace(",", "").strip().split()
    doc = open("words.txt", "r")
    diferentes = []
    words = doc.read().strip().lower().split()
    for i in range(len(s)):
        if s[i] not in words:
            diferentes.append(s[i])
    return diferentes