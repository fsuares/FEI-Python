ano = int(input('Digite o ano desejado: '))
salario = 5000
percentual = 0.015

for i in range(2005, ano):
    salario = salario + (salario * percentual)
    percentual = percentual * 2

print('Salário de {}: R$ {:.2f}'.format(ano,salario))
