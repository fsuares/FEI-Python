
from tkinter import *

#-----------Função de clique do botão-------------
def clique():
    rotulo['text'] = 'Novo Texto!'

#-----------------Cria Uma Janela-----------------
janela = Tk()
# titulo para a janela
janela.title('Teste GUI')
# configura o tamanho da janela
janela.geometry('500x500')

# cria rotulo na janela desejada, com o texto desejado e configura a fonte
rotulo = Label(janela, text='Primeira aplicação gráfica no Python!', font=('Arial Bold', 14))

#----------Posicionamento absoluto-----------------
# configura onde o texto vai aparecer na janela
# x = 250 e y = 250
# a referencia é o centro (CENTER) do rótulo
#rotulo.place(x = 250, y = 250, anchor=CENTER)


#------------Posicionamento relativo---------------
rotulo.place(relx = 0.5, rely = 0.5, anchor=CENTER)


#-----------------Criando Botões-------------------
btn = Button(janela, text='Clique Aqui!', command=clique , height=2, width=20, font=('Arial Bold', 10))
btn.place(relx = 0.2, rely = 0.2, anchor=CENTER)


# chama a função  mainloop:
# loop infinito para manter a janela aberta
janela.mainloop()

