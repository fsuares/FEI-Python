from time import sleep
n = int(input('Digite um numero para iniciar a contagem: '))
x = 0

while x <= n:
    if x % 2 == 0:
        print(x)
        sleep(1)
    x += 1