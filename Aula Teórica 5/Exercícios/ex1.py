def maximo(x, y):
    if x > y:
        return x

    elif x == y:
        return ('Os números são iguais e equivalentes.')

    else:
        return y

x = float(input('X = '))
y = float(input('Y = '))
print(maximo(x, y))