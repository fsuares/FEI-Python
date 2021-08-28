lin = str(input("Digite a linha desejada: "))
col = str(input("Digite a coluna desejada: "))

if lin in '8642':
    if col in 'aceg':
        print("Branco")

    elif col in 'bdfh':
        print("Preto")

elif lin in '7531':
    if col in 'bdfh':
        print("Branco")

    elif col in 'aceg':
        print("Preto")