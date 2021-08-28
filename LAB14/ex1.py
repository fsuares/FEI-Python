from tkinter import * 
from tkinter import scrolledtext
from string import *

window = Tk()
window.title('Algoritmo')
window.geometry('900x600')

#--------------------------LABELS-----------------------
palavra = Label(window, text='Palavra suspeita: ', font=('Arial', 14))
palavra.place(relx=0.05, rely=0.08)

quantidade= Label(window, text='Frequência: ', font=('Arial', 14))
quantidade.place(relx=0.05, rely=0.15)

ocorrencias = Label(window, text='Ocorrências: ', font=('Arial', 14))
ocorrencias.place(relx=0.05, rely=0.24)

#--------------------------ENTRYS-----------------------
palavraEntrada = Entry(window, width=15, font=('Arial', 14))
palavraEntrada.place(relx=0.25, rely=0.08)

quantidadeEntrada = Entry(window, width=15, font=('Arial', 14))
quantidadeEntrada.place(relx=0.25, rely=0.15)

#----------------------SCROLLEDTEXT----------------------
txt = scrolledtext.ScrolledText(window, width=100, height=23)
#txt.configure(state='disabled')
txt.place(relx=0.5, rely=0.6, anchor=CENTER)

def buscaPalavra(palavraEntrada, txt, quantidadeEntrada):
    texto = str(txt)
    texto.lower() 
    for n in punctuation:
        texto = texto.replace(n,' ')

    texto = texto.split()
    plvEntrada = 0
    lista = []

    for palavra in texto:
        if palavra == palavraEntrada:
            plvEntrada += 1
    print(plvEntrada)
    
#-------------------------BUTTONS------------------------
pesquisar = Button(window, text='Pesquisar', command=buscaPalavra(palavraEntrada, txt, quantidadeEntrada))
pesquisar.place(relx=0.5,rely=0.125)

# inicia o loop da janela
window.mainloop()
