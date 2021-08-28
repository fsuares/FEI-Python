neg = []
pos = []

while True:
    x = int(input())
    if x == 0:
        break
    neg.append(x) if x < 0 else pos.append(x)

print(neg + pos)