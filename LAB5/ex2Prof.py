min = int(input("Digite o valor mínimo em graus C: "))
max = int(input("Digite o valor máximo em graus C: "))

print('%18s %18s' % ('Temperatura em C','Temperatura em F'))

for i in range(min, max+1, 5):
    print('%18d %18d' % (i, i*9/5+32))