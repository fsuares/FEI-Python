
#O jogo deve começar solicitando a palavra secreta para o usuário 1 
# (o usuário 1 pode entrar com letras maiúsculas ou minúsculas, isto não deve influenciar no jogo).

#Então, o usuário 2, deve chutar as letras da palavra secreta e tentar acertá-la. Lembre-se de que o 
# usuário 2 não deve poder ver a palavra secreta digitada pelo usuário 1.

#O usuário 2 pode errar a letra 5 vezes. No sexto erro, o jogo termina. 

#O jogo deve verificar se a letra digitada pelo usuário 2 já foi ou não digitada. 
# Letras repetidas não devem contar. 

#O jogo deve também mostrar a quantidade de letras da palavra secreta, 
# assim como as letras corretas em suas devidas posições.

palavra = input("Digite a palavra secreta:").lower().strip()
print("""








""")
digitadas = []
acertos = []
erros = 0
while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "-"
    print(senha)
    if senha == palavra:
        print("Você acertou!")
        break
    tentativa = input("\nDigite uma letra:").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
    print("X==:==\nX  :   ")
    print("X  O   " if erros >= 1 else "X")
    linha2 = ""
    if erros == 2:
        linha2 = "  |   "
    elif erros == 3:
        linha2 = " \|   "
    elif erros >= 4:
        linha2 = " \|/ "
    print("X%s" % linha2)
    linha3 = ""
    if erros == 5:
        linha3 += " /     "
    elif erros >= 6:
        linha3 += " / \ "
    print("X%s" % linha3)
    print("X\n===========")
    if erros == 6:
        print("Enforcado!")
        break