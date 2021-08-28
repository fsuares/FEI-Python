print("==============-Integrantes-==============")
print("Nome: Gabriel de Almeida RA: 22121079-2")
print("Nome: Fernando Suares RA: 22121133-7")
print("Nome: Henry Araujo RA: 22121129-5")
print("\n") 


def conta(w, eps, M):
    valores = []
    matriz = []
    valores.append(w)     
                                             
    for numero in range(1, M):
        sequencia = valores[numero-1]**2 + w
        valores.append(sequencia)

    for elem in range(len(valores)-1):                        
        distancias = []                                                  
        for diferenca in range(elem + 1, len(valores)):          
           dist = valores[elem] - valores[diferenca]        
           valReal = dist.real                         
           valImg =  dist.imag                          
           hip = (valReal**2 + valImg**2)**0.5
           distancias.append(hip)                                        
        matriz.append(distancias)         
                                       
    for linha in range(len(matriz)):
        contador = 0
        for n in matriz[linha]:                         
            if n > eps:                                     
                contador = 1
        if contador == 0:
            return linha + 1                                      
    return False                                                


def main():
    w = complex(input("Digite o valor de w: "))      
    eps = float(input("Digite o valor de epsilon: "))       
    M = int(input("Digite o valor de M: "))        
    seq = conta(w, eps, M)
    
    if seq == False:
        print("Não há índice a partir do qual um elemento e seus subsequentes estejam a uma distância menor que: {}".format(eps))
    elif seq != False:
        print("O menor índice  procurado é: {}".format(seq))


main()

