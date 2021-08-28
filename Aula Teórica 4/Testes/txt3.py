# leia o valor de n
n = int(input("Digite o valor de n (n > 0): "))

# leia o valor de m
m = int(input("Digite o valor de m (m > 0): "))

# em cada iteração mdc é o candidato a mdc(n,m)
mdc = n
while n % mdc != 0 or m % mdc != 0:
    mdc = mdc - 1

print("MDC(%d,%d)=%d" % (n, m, mdc))