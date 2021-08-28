dia = int(input("Digite o dia desejado: "))
mes = input("Digite o mês desejado: ")

if (dia <= 19 and mes == 'março') or (mes == 'janeiro' or mes == 'fevereiro') or (dia >= 21 and mes == 'dezembro'):
    print('Verão')

elif (dia <= 20 and mes == 'junho') or (mes == 'abril' or mes == 'maio') or (dia >= 20 and mes == 'março'):
    print('Outono')

elif (dia <= 21 and mes == 'setembro') or (mes == 'julho' or mes == 'agosto') or (dia >= 21 and mes == 'junho'):
    print('Inverno')

elif (dia <= 20 and mes == 'dezembro') or (mes == 'novembro' or mes == 'outubro') or (dia >= 22 and mes == 'setembro'):
    print('Primavera')