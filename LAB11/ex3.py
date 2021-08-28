#Implemente uma função que receba um nome completo e apresente apenas 
# o último nome e o 1o nome na seguinte forma:

# último, 1o nome.

def nomeCitacao(texto):
    nomeSeparado = texto.split()
    nome = nomeSeparado[0]
    sobrenome = nomeSeparado[-1]
    print(sobrenome+", "+ nome)