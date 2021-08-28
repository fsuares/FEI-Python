num = int(input('Digite o número desejado: '))
f = 1

for i in range(1, num+1):
    e = (1/(i))
    f += e

print('{:.3f}'.format(f))