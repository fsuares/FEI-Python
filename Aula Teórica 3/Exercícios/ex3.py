x = float(input("Digite a coordenada X: "))
y = float(input("Digite a coordenada Y: "))

if (x > 0) and (y > 0):
    print("A coordenada pertencem ao Q1")

elif (x < 0) and (y > 0):
    print("A coordenada pertencem ao Q2")

elif (x < 0) and (y < 0):
    print("A coordenada pertencem ao Q3")

elif (x > 0) and (y < 0):
    print("A coordenada pertencem ao Q4")

elif (x == 0) or (y == 0):
    if (x == 0) and (y == 0):
        print("As coordenadas de X e Y se encontram na origem.")

    elif x == 0:
        print("A coordenada pertencem eixo das abscissas (X).")

    elif y == 0:
        print("A coordenada pertencem eixo das ordenadas (Y).")