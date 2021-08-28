
from tkinter import *
#-------------Função que converte para Binario-------------
def convertBin():
    resposta.delete('0', 'end')
    numero = int(num.get())
    resultado = format(numero, 'b')
    resposta.insert(0, resultado)

#-----------Função que converte para Hexadecimal-----------
def convertHex():
    resposta.delete('0', 'end')
    numero = int(num.get())
    resultado = format(numero, 'x')
    resposta.insert(0, resultado)

#-------------Função que converte para Octal---------------
def convertOct():
    resposta.delete('0', 'end')
    numero = int(num.get())
    resultado = format(numero, 'o')
    resposta.insert(0, resultado)

janela = Tk()
janela.title('Conversor')
janela.geometry('400x250')

#----------------------------------LABEL-----------------------------------
text1 = Label(janela, text='Número em decimal: ', font=('Arial Black', 10))
text1.place(x = 30, y= 10)

#---------------------------------TEXTBOX----------------------------------
num = Entry(janela, width=14, font=('Ariel Bold', 14))
num.place(x = 280, y = 22, anchor=CENTER)

#---------------------------------BUTTONS----------------------------------
btnBin = Button(janela, text='Binário', command=convertBin)
btnHex = Button(janela, text='Hexadecimal', command=convertHex)
btnOct = Button(janela, text='Hexadecimal', command=convertOct)
btnBin.place(x = 70, y = 75)
btnHex.place(x = 160, y = 75)
btnOct.place(x = 270, y = 75)



#---------------------------------RESPOSTA---------------------------------
#----------------------------------LABEL-----------------------------------
text1 = Label(janela, text='Resposta: ', font=('Arial Black', 10))
text1.place(x = 160, y= 120)
#---------------------------------TEXTBOX----------------------------------
resposta = Entry(janela, width=14, font=('Ariel Bold', 14))
resposta.place(x = 200, y = 175, anchor=CENTER)

# chama a função  mainloop:
# loop infinito para manter a janela aberta
janela.mainloop()
