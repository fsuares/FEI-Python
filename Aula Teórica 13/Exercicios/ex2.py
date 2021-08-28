
from tkinter import *
from tkinter import messagebox

def verifica_letra():
    letra = entrada.get()
    if letra in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
        print(messagebox.showinfo('Resposta', 'A letra {} é uma vogal!'.format(letra)))

    elif letra == 'y':
        print(messagebox.showinfo('Resposta', 'A letra Y pode ser uma vogal em alguns idiomas, e consoante em outros!'))

    else:
        print(messagebox.showinfo('Resposta', 'A letra {} é uma consoante!'.format(letra)))
    entrada.delete('0', 'end')


janela = Tk()
janela.title('Conversor')
janela.geometry('400x250')

#----------------------------------LABEL-----------------------------------
text1 = Label(janela, text='Digite uma Letra: ', font=('Arial Black', 10))
text1.place(x = 30, y= 10)

#---------------------------------TEXTBOX----------------------------------
entrada = Entry(janela, width=14, font=('Ariel Bold', 14))
entrada.place(x = 280, y = 22, anchor=CENTER)

#---------------------------------BUTTONS----------------------------------
btnHex = Button(janela, text='Hexadecimal', command=verifica_letra)
btnHex.place(x = 160, y = 75)

janela.mainloop()
