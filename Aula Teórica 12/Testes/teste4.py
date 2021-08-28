from random import randint, choice

bingo = {
    'B' : [],
    'I' : [],
    'N' : [],
    'G' : [],
    'O' : []
}


def bingo():
    for n in range(5):
        bingo['B'] = list.append(randint(1, 15))
        bingo['I'] = list.randint(16, 30)
        bingo['N'] = list.randint(31, 45)
        bingo['G'] = randint(46, 60)
        bingo['O'] = randint(61, 75)
        
    print(bingo.items())
bingo()
