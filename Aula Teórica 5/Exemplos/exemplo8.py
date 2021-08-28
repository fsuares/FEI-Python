def aumento(salario, p):
    return salario*p/100

#aumento = lambda salario, p : salario*p/100

salario = int(input('Digite o salario: '))
porcentagem = int(input('Digite a porcentagem de aumento: '))
print(aumento(salario, porcentagem))