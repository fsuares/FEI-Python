n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
operacao = input("Qual operacão deseja realizar: \nAição [+] \nSubtração [-] \nMultiplicação [*] \nDivisão [/] \n")

if operacao == "+":
    print("Resultado: {:.1f}".format(n1+n2))

elif operacao == "-":
    print("Resultado: {:.1f}".format(n1-n2))

elif operacao == "*":
    print("Resultado: {:.1f}".format(n1*n2))

elif operacao == "/":
    print("Resultado: {:.1f}".format(n1/n2))

else:
    print("Por favor digite uma operação valida.")