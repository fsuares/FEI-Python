"""Elabore um programa cuja entrada seja uma matriz quadrada M de ordem até 3 e a saída seja a matriz 
inversa de M.

Caso o determinante seja nulo, a saída deve ser:
"Matriz Singular"

"""

ordem = int(input("Digite a ordem da matriz (até ordem 3): "))

if ordem == 1:
    aux = 1
    matriz = float(input("Digite o elemento 1 1 da matriz: "))
    inversa = aux/matriz
    print("MATRIZ:\n{}\n".format(matriz))
    print("MATRIZ INVERSA:\n{}".format(inversa))

elif ordem == 2:
    matriz = [['', ''], ['', '']]
    m2_ident = [[1, 0], [0, 1]]

    for i in range(0, ordem):
        for j in range(0, ordem):
            matriz[i][j] = float(
                input("Digite o elemento {} {} da matriz: ".format(i+1, j+1)))

    det = matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    if det != 0:
        a = matriz[1][1]/det
        b = (matriz[0][1]*-1)/det
        c = (matriz[1][0]*-1)/det
        d = matriz[0][0]/det
        inversa = [[a, b], [c, d]]

        print("MATRIZ: ")
        for i in range(0, ordem):
            for j in range(0, ordem):
                print("{} ".format(matriz[i][j]), end="")
            print()
        print()

        print("MATRIZ INVERSA: ")
        for i in range(0, ordem):
            for j in range(0, ordem):
                print("{} ".format(inversa[i][j]), end="")
            print()

    else:
        print("Matriz Singular")

elif ordem == 3:
    matriz = [['', '', ''], ['', '', ''], ['', '', '']]
    m3_ident = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    for i in range(0, ordem):
        for j in range(0, ordem):
            matriz[i][j] = float(
                input("Digite o elemento {} {} da matriz: ".format(i+1, j+1)))

    det = (matriz[0][0] * matriz[1][1] * matriz[2][2]) + (matriz[0][1] * matriz[1][2] * matriz[2][0]) + (matriz[0][2] * matriz[1][0] * matriz[2][1]) - (matriz[0][1] * matriz[1][0] * matriz[2][2]) - (matriz[0][0] * matriz[1][2] * matriz[2][1]) - (matriz[0][2] * matriz[1][1] * matriz[2][0])
    if det != 0:
        a = ((matriz[1][1] * matriz[2][2]) + ((matriz[1][2] * matriz[2][1])*-1))/det
        b = ((matriz[2][1] * matriz[0][2]) + ((matriz[2][2] * matriz[0][1])*-1))/det
        c = ((matriz[0][1] * matriz[1][2]) + ((matriz[0][2] * matriz[1][1])*-1))/det
        d = ((matriz[1][2] * matriz[2][0]) + ((matriz[1][0] * matriz[2][2])*-1))/det
        e = ((matriz[2][2] * matriz[0][0]) + ((matriz[2][0] * matriz[0][2])*-1))/det
        f = ((matriz[0][2] * matriz[1][0]) + ((matriz[0][0] * matriz[1][2])*-1))/det
        g = ((matriz[1][0] * matriz[2][1]) + ((matriz[1][1] * matriz[2][0])*-1))/det
        h = ((matriz[2][0] * matriz[0][1]) + ((matriz[2][1] * matriz[0][0])*-1))/det
        i = ((matriz[0][0] * matriz[1][1]) + ((matriz[0][1] * matriz[1][0])*-1))/det
        inversa = [[a, b, c], [d, e, f], [g, h, i]]

        print("MATRIZ: ")
        for i in range(0, ordem):
            for j in range(0, ordem):
                print("{} ".format(matriz[i][j]), end="")
            print()
        print()

        print("MATRIZ INVERSA: ")
        for i in range(0, ordem):
            for j in range(0, ordem):
                print("{} ".format(inversa[i][j]), end="")
            print()

    else:
        print("Matriz Singular")


else:
    print("Matrizes suportadas:\n\n QUADRADAS DE ORDEM 1 À 3.")

