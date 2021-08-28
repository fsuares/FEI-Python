list = [1, 3, 5, 7, 9, 11]

for elemento in list:
    a = int(input('Adicione um elemento: '))
    if a % 2 != 0:
        list.append(a)
        print(list)
