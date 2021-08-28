list = [1, 3, 5, 7, 9, 11]
a = int(input('Procure um elemento: '))#

for index in range(len(list)):
    if list[index] == a:
        print('Elemento encontrado na posição', index)
        break

else:
    print('Elemento não encontrado na lista.')