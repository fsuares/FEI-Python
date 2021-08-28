a = 5
print(a + a)
print(a)

def imprime():
    global a
    print(a + a)
    a = 7
    print(a + a)

imprime()
print(a)
