from math import sqrt

tam = int(input('Qual o tamanho da lista: '))
list = []
somatorio = 0
desvio = 0
soma = 0

print('Digite os valores: ')
for num in range(tam):
    list.append(int(input()))

for elemento in list:
    somatorio = somatorio + elemento

media = somatorio / tam

for n in range(tam):
    soma = soma + (list[n] - media)**2
desvio = sqrt(soma / tam)

print('Média = {:.2f} e Desvio = {:.2f}'.format(media,desvio))