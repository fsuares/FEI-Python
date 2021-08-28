from math import sqrt


def conta(w,e,M):
    lista = []
    matriz = []
    lista.append(w)                                              #primeiro termo da sequencia,caso z0 seja = 0
    for numero in range(1,M):
                                                                 #adiciona os termos subsequentes na lista
        sequencia = lista[numero-1]**2+w
        lista.append(sequencia)
    for elements in range(len(lista)-1):                        #percorre  os valores da lista
        m = []                                                  #lista que vai armazenar as distancias
        for diferenca in range(elements+1,len(lista)):          #pega os proximos valores de de elements 
           distancia = lista[elements]-lista[diferenca]         #faz a subtracao entre os valores complexos
           valor_real = distancia.real                          #pega o valor real dessa subtracao
           valor_img =  distancia.imag                          #pega o valor imaginario dessa subtracao
           hip = sqrt(valor_real**2+valor_img**2)               #faz a conta para encontrar a distancia(representada por uma hipotenusa em um grafico)
           m.append(hip)                                        #adiciona essa distancia na lista m
        matriz.append(m)                                        #adiciona todas essas distancias na matriz principal
    for linha in range(len(matriz)):
        contador = 0
        for elementos in matriz[linha]:                         #passa por todos os valores e verifica se tem valores maiores que epsilon
            if elementos>e:                                     #se tiver, nao e essa lista e passa para a proxima
                contador = 1
        if contador ==0:
            return linha+1                                      #se for, retorna a linha que e o indice k (+1 porque comeca a contar do zero)
    return False                                                # se nao tiver nenhuma distancia menor que epsilon, retorna falso
                                            
    





def main():
    num_complexo = complex(input("Digite o valor de w: "))      #numero complexo das sequencias
    epsilon = float(input("Digite o valor de epsilon: "))       #distancias entre esses termos
    qntd_de_termos = int(input("Digite o valor de M: "))        #quantos termos tera essa sequencia
    k = conta(num_complexo,epsilon,qntd_de_termos)
    if k == False:
        print("Não há índice a partir do qual um elemento e seus subsequentes estejam a uma distância menor que: %f" %epsilon)
    else:
        print("O menor índice  procurado é: %d" %k)




main()