
from tkinter import *

janela = Tk()
janela.title('Conversor')
janela.geometry('400x400')

#---------------------------------BUTTONS----------------------------------
btn1 = Button(janela, text='Hexadecimal', height=3, width=6)
btn1.place(x = 160, y = 75)

# chama a função  mainloop:
# loop infinito para manter a janela aberta
janela.mainloop()