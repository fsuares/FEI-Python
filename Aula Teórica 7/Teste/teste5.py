#list = [1, 3, 5, 7, 9, 11]
#a = int(input('Procure um elemento: '))#

#for elemento in list:
#    if elemento == a:
#        print('Elemento encontrado na lista.')

#    else:
#        print('Elemento não encontrado na lista.')

#                       ou

list = [1, 3, 5, 7, 9, 11]
a = int(input('Procure um elemento: '))

if a in list:
    print('Elemento encontrado na lista.')

else:
    print('Elemento não encontrado na lista.')