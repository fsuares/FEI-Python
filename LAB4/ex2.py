a = float(input("Digite o valor de a: "))

if a == 0:
    print("Essa equação não é do segundo grau!")

else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    delta = ((b**2 - 4*a*c))

    if delta < 0:
        print("Não existem raizes reais!")

    elif delta == 0:
        x1 = (-(b) + (delta**0.5)) / (2 * a)
        print("Raiz: {:.3f}".format(x1))

    elif delta > 0:
        x1 = (-(b) + (delta**0.5)) / (2 * a)
        x2 = (-(b) - (delta**0.5)) / (2 * a)
        print("Primeira raiz: {:.3f} \nSegunda raiz: {:.3f}".format(x1,x2))