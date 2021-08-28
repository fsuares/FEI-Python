#programa pra calcular media e exibir situação do aluno
p1 = float(input("'Digite a primeira nota: "))
p2 = float(input("'Digite a segunda nota: "))
mf = (p1 + p2)/2

if mf == 10:
    print("Aprovado com Distinção!")
    print("Media final: {:.1f}".format(mf))

elif mf >= 5:
    print("Aprovado")
    print("Media final: {:.1f}".format(mf))

else:
    print("Reprovado")
    print("Media final: {:.1f}".format(mf))