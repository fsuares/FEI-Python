nota = input("Digite a nota em letra, e o sinal +/-: ")

if nota == 'A+':
    print('A+ é equivalente a 5.0')

elif nota == 'A':
    print('A é equivalente a 5.0')

elif nota == 'A-':
    print('A- é equivalente a 4.5')

elif nota == 'B+':
    print('B+ é equivalente a 4.0')

elif nota == 'B':
    print('B é equivalente a 3.5')

elif nota == 'B-':
    print('B- é equivalente a 3.0')

elif nota == 'C+':
    print('C+ é equivalente a 2.5')

elif nota == 'C':
    print('C é equivalente a 2.0')

elif nota == 'C-':
    print('C- é equivalente a 1.5')

elif nota == 'D+':
    print('D+ é equivalente a 1.0')

elif nota == 'D':
    print('D é equivalente a 0.5')

elif nota == 'F':
    print('F é equivalente a 0.0')

else:
    print('Nota inválida')