from math import sqrt
distancias = []

def conta(complexo, distancia, limite):
    lista_sequencia = []
    matriz = []
    lista_sequencia.append(complexo)                                              #primeiro termo da sequencia,caso z0 seja = 0
    for valor in range(1,limite):
                                                                 #adiciona os termos subsequentes na lista
        sequencia = lista_sequencia[valor-1]**2+complexo
        lista_sequencia.append(sequencia)
    for elements in range(len(lista_sequencia)-1):                        #percorre  os valores da lista                                                #lista que vai armazenar as distancias
        for diferenca in range(elements+1,len(lista_sequencia)):          #pega os proximos valores de de elements 
           d = lista_sequencia[elements]-lista_sequencia[diferenca]         #faz a subtracao entre os valores complexos
           valor_real = d.real                          #pega o valor real dessa subtracao
           valor_img =  d.imag                          #pega o valor imaginario dessa subtracao
           hip = sqrt(valor_real**2+valor_img**2)               #faz a conta para encontrar a distancia(representada por uma hipotenusa em um grafico)
           distancias.append(hip)                                        #adiciona essa distancia na lista m
        matriz.append(distancias)
    
    for linha in range(len(matriz)):
        cont = 0
        for componente in matriz[linha]:                         #passa por todos os valores e verifica se tem valores maiores que epsilon
            if componente > distancia:                                     #se tiver, nao e essa lista e passa para a proxima
                cont = 1
        if cont == 0:
            return linha + 1                                      #se for, retorna a linha que e o indice k (+1 porque comeca a contar do zero)
        return False                                                # se nao tiver nenhuma distancia menor que epsilon, retorna falso
                                            

def main():
    global distancias
    w = complex(input("Informe o valor de w: "))     #numero complexo das sequencias
    e = float(input("Informe o valor de epsilon: "))       #distancias entre esses termos
    limite_M = int(input("Informe o valor de M: "))

    
    k = conta(w, e, limite_M)   
    if k == False:
        print(f'Não existem indices nem subsequentes menores que {e}')
    else:
        print(f'O valor minimo do indice é: {k}')


main()