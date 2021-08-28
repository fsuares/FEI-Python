soma = 0
mult = 0
sub = 0
div = 0

while True:
    n = float(input('Digite um numero: '))
    soma += n
    sub -= n
    mult = mult * n


    if n == 0:
        break

print('A soma dos números é = {:.1f}\n A subtração dos números é = {:.1f}\n A multiplicação dos números é = {:.1f}\n A divisão dos números é = {:.1f}'.format(soma, sub, mult, div))