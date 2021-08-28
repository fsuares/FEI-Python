#A Criptografia de César é uma técnica bastante simples e provavelmente a mais conhecida de todas.
#Trata-se de um tipo de substituição, na qual cada letra de um texto a ser criptografado é 
# substituída por outra letra presente no alfabeto, porém deslocada um certo número de posições à 
# esquerda ou à direita.

#Por exemplo, se empregarmos uma troca de quatro posições à esquerda, cada letra é substituída 
# pela letra que está quatro posições adiante no alfabeto, e nesse caso a letra A seria substituída pela letra E, 
# a letra B por F, a letra C por G, e assim sucessivamente.

#Crie uma função chamada criptCesar que recebe uma frase e o valor do deslocamento,
# podendo ser positivo ou negativo. A criptografia deverá ser cíclica, como na imagem acima; 
# isso significa que quando terminar em Z o próximo caractere é A.

#Sua função deve ignorar caracteres minúsculos, especiais e os espaços.

def criptCesar(texto, deslocamento):
    texto = texto.upper()
    resposta = ""
    for letra in texto:
        if letra >= "A" and letra <= "Z":
            resposta = resposta + (chr((ord(letra) + deslocamento - ord("A"))%26 + ord("A")))
        else:
            resposta = resposta + letra
    print(resposta)