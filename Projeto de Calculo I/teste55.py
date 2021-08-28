from math import sqrt
print("==============-Integrantes-==============")
print("Nome: Gabriel de Almeida RA: 22121079-2")
print("Nome: Fernando Suares RA: 22121133-7")
print("Nome: Henry Araujo RA: 22121129-5")
print("\n") 

def conta(complexo, distancia, limite):
    distancias = []
    lista_sequencia = []
    matriz = []
    lista_sequencia.append(complexo)                                             
    for valor in range(1, limite):                                                        
        sequencia = lista_sequencia[valor-1]**2+complexo
        lista_sequencia.append(sequencia)
   
    for elements in range(len(lista_sequencia)-1):                                                                     
        for diferenca in range(elements+1,len(lista_sequencia)):         
           d = lista_sequencia[elements]-lista_sequencia[diferenca]         
           valor_real = d.real                          
           valor_img =  d.imag                         
           hip = sqrt(valor_real*2+valor_img*2)               
           distancias.append(hip)                                       
        matriz.append(distancias)
    
    for linha in range(len(matriz)):
        cont = 0
        for componente in matriz[linha]:                         
            if componente > distancia:                                   
                cont = 1
        if cont == 0:
            return linha + 1                                      
    return False                                                
                                            

def main():
    w = complex(input("Informe o valor de w: "))
    e = float(input("Informe o valor de epsilon: "))
    limite_M = int(input("Informe o valor de M: "))
    print("\n")
    
    k = conta(w, e, limite_M)   
    if k == False:
        print(f'Não existem indices nem subsequentes menores que {e}')
    else:
        print(f'O valor minimo do indice é: {k}')


main()