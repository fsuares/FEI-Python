#escrever um programa que identifica se umm número é primo ou não
#variavel que receb o numero do usuário
num = int(input('Digite o número desejado: '))
primo = True
#laço que testa o numero
for i in range(2, num):
    if i < num and primo == True:
        if num % i == 0:
            primo = False
            i = i + 1

        else:
            i = i + 1

if primo == False:
    print('Número não primo')

elif primo == True:
    print('Número primo')