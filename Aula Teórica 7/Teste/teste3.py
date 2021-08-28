z = [0, 1, 2, 3, 4, 5, 6]

#z1 referencía z
z1 = z

#z2 é cópia de z
z2 = z[:]

z1.pop(4)
z2.remove(5)

print(z)
print(z1)
print(z2)