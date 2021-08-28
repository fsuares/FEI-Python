n = int(input('Digite n: '))
m = int(input('Digite m: '))
maior = 1
if n > m:
    maior = n

elif n < m:
   maior = m

while m % maior != 0 or n % maior != 0:
    maior = maior - 1

else:
    print(maior)