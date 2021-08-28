salario = float(input("Digite seu salario: "))

if (salario > 0) and (salario <= 400):
    print("Seu salario com reajuste é R$ {:.2f}".format(salario * 1.15))

elif (salario > 400) and (salario <= 800):
    print("Seu salario com reajuste é R$ {:.2f}".format(salario * 1.12))

elif (salario > 800) and (salario <= 1200):
    print("Seu salario com reajuste é R$ {:.2f}".format(salario * 1.10))

elif (salario > 1200) and (salario <= 2000):
    print("Seu salario com reajuste é R$ {:.2f}".format(salario * 1.07))

elif (salario > 2000):
    print("Seu salario com reajuste é R$ {:.2f}".format(salario * 1.04))