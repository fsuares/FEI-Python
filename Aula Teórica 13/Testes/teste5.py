
from tkinter import *
from tkinter import  messagebox 

#-----------------Cria Uma Janela-----------------
janela = Tk()
# titulo para a janela
janela.title('Teste GUI')
# configura o tamanho da janela
janela.geometry('500x500')

def show():
    res = messagebox.askyesno('Sim ou Não!', 'Python é legal?')
    print(res)

botao2 = Button(janela, text='Mensagem', command=show)
botao2.place(relx = 0.5, rely = 0.2, anchor=CENTER)

# chama a função  mainloop:
# loop infinito para manter a janela aberta
janela.mainloop()
