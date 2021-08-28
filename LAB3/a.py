#valor da compra
valor = float(input("Digite o valor da compra: "))
#quantidade de parcelas
quant = float(input("Digite a quantidade de parcelas: "))

#valor do desconto
if valor >= 5000:

    if quant == 1:
        desconto = valor * 0.15
        print("Desconto total: {:.2f}".format(desconto))
        print("Valor final da compra com desconto: {:.2f}".format(valor - desconto))
        print("Cada parcela será de: {:.2f}".format((valor - desconto) / quant))

    elif quant == 2:
        desconto = valor * 0.10
        print("Desconto total: {:.2f}".format(desconto))
        print("Valor final da compra com desconto: {:.2f}".format(valor - desconto))
        print("Cada parcela será de: {:.2f}".format((valor - desconto) / quant))

    elif quant == 3:
        desconto = valor * 0.10
        print("Desconto total: {:.2f}".format(desconto))
        print("Valor final da compra com desconto: {:.2f}".format(valor - desconto))
        print("Cada parcela será de: {:.2f}".format((valor - desconto) / quant))

    elif quant >= 4:
        desconto = valor * 0.05
        print("Desconto total: {:.2f}".format(desconto))
        print("Valor final da compra com desconto: {:.2f}".format(valor - desconto))
        print("Cada parcela será de: {:.2f}".format((valor - desconto) / quant))

else:
    if quant == 1:
        desconto = valor * 0.1
        print("Desconto total: {:.2f}".format(desconto))
        print("Valor final da compra com desconto: {:.2f}".format(valor - desconto))
        print("Cada parcela será de: {:.2f}".format((valor - desconto) / quant))

    elif quant == 2:
        desconto = valor * 0.05
        print("Desconto total: {:.2f}".format(desconto))
        print("Valor final da compra com desconto: {:.2f}".format(valor - desconto))
        print("Cada parcela será de: {:.2f}".format((valor - desconto) / quant))

    elif quant == 3:
        desconto = valor * 0.05
        print("Desconto total: {:.2f}".format(desconto))
        print("Valor final da compra com desconto: {:.2f}".format(valor - desconto))
        print("Cada parcela será de: {:.2f}".format((valor - desconto) / quant))

    elif quant >= 4:
        desconto = valor
        print("Desconto total: {:.2f}".format(desconto))
        print("Valor final da compra com desconto: {:.2f}".format(valor - desconto))
        print("Cada parcela sera de: {:.2f}".format((valor - desconto) / quant))
