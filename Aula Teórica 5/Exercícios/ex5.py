def ordem(i,a,b,c):
    maior = 0
    meio = 0
    menor = 0
    outra1 = 0
    outra2 = 0

    if i == 3:
        if a > b and a > c:
            maior = a
            outra1 =b
            outra2 = c

        elif c > b and c > a:
            maior = c
            outra1 = a
            outra2 = b

        elif b > a and b > c:
            maior = b
            outra1 = a
            outra2 = c
        print(outra1, '' ,maior, '' ,outra2)

    if i == 2:
        if a > b and a > c and b > c:
            maior = a
            meio =b
            menor = c

        elif a > b and a > c and c > b:
            maior = a
            meio = c
            menor = b


        elif c > b and c > a and a > b:
            maior = c
            meio = a
            menor = b

        elif c > b and c > a and b > a:
            maior = c
            meio = b
            menor = a


        elif b > a and b > c and a > c:
            maior = b
            meio = a
            menor = c

        elif b > a and b > c and c > a:
            maior = b
            meio = c
            menor = a
        print(menor, '' ,meio, '' ,maior)

    if i == 1:
        if a > b and a > c and b > c:
            maior = c
            meio = b
            menor = a

        elif a > b and a > c and c > b:
            maior = b
            meio = c
            menor = a


        elif c > b and c > a and a > b:
            maior = b
            meio = a
            menor = c

        elif c > b and c > a and b > a:
            maior = a
            meio = b
            menor = c


        elif b > a and b > c and a > c:
            maior = c
            meio = a
            menor = b

        elif b > a and b > c and c > a:
            maior = a
            meio = c
            menor = b
        print(menor, '', meio, '', maior)

def main():
    i = int(input('I = '))
    a = float(input('A = '))
    b = float(input('B = '))
    c = float(input('C = '))
    ordem(i, a, b, c)

main()