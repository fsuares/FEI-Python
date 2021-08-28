mf = 0
for m in range(0,5):
    n = int(input('Digite a {}º nota: '.format(m+1)))
    mf += n

print('Média final: {:.1f}'.format(mf/5))
