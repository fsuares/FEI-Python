
inteira = []
par = []
impar = []

for _ in range(20):
    elemento = int(input())
    inteira.append(elemento)
    if elemento % 2 == 0:
        par.append(elemento)

    else:
        impar.append(elemento)

print(inteira)
print(par)
print(impar)