from tkinter import*
from tkinter import ttk

#cores para ser usada na interface
cor1 = "#a3a7b5" #cinza
cor2 = "#050505" #preto
cor3 = "#fc0505" #vermelho
cor4 = "#fca605" #laranja
cor5 = "#f5f3f0" #branco
cor6 = "#2142b8" #azul

janela = Tk()
janela.title =("Calculadora")
janela.geometry("280x415")
janela.configure(bg=cor1)

#dimensões da calculadora
frame_tela = Frame(janela, width=280, height=80, bg=cor2)
frame_tela.grid(row=0, column=0)
frame_teclado = Frame(janela, width=280, height=380, bg=cor5)
frame_teclado.grid(row=1, column=0)

todos_valores = ""

#função de entrada de valores
def entrar_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    valor_texto.set(todos_valores)

#função de calcular valores
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))

#função para limpar a tela
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

valor_texto = StringVar()

#display da calculadora
app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=3, padx=7, relief=FLAT, anchor="e", justify=RIGHT, bg=cor2, fg=cor5, font=("Ivy 20 bold"))
app_label.place(x=0, y=0)

#botões da calculadora
b_1 = Button(frame_teclado, command= limpar_tela, text= "C", width=11, height=2, bg=cor1, font=("Ivy 15 bold"), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0,y=0)
b_2 = Button(frame_teclado, command= lambda: entrar_valores("%"), text= "%", width=5, height=2, bg=cor1, font=("Ivy 15 bold"), relief=RAISED, overrelief=RIDGE)
b_2.place(x=140,y=0)
b_3 = Button(frame_teclado, command= lambda: entrar_valores("/"), text= "/", width=5, height=2, bg=cor4, fg=cor5, font=("Ivy 15 bold"), relief=RAISED, overrelief=RIDGE)
b_3.place(x=210,y=0)
b_4 = Button(frame_teclado, command= lambda: entrar_valores("7"), text= "7", width=5, height=2, bg=cor1, font=("Ivy 15 bold"), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0,y=67)
b_5 = Button(frame_teclado, command= lambda: entrar_valores("8"), text= "8", width=5, height=2, bg=cor1, font=("Ivy 15 bold"), relief=RAISED, overrelief=RIDGE)
b_5.place(x=70,y=67)
b_6 = Button(frame_teclado, command= lambda: entrar_valores("9"), text= "9", width=5, height=2, bg=cor1, font=("Ivy 15 bold"), relief=RAISED, overrelief=RIDGE)
b_6.place(x=140,y=67)
b_7 = Button(frame_teclado, command= lambda: entrar_valores("*"), text= "*", width=5, height=2, bg=cor1, font=("Ivy 15 bold"), relief=RAISED, overrelief=RIDGE)
b_7.place(x=210,y=67)
b_8 = Button(frame_teclado, command= lambda: entrar_valores("4"), text= "4", width=5, height=2, bg=cor1, font=("Ivy 15 bold"), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0,y=134)
b_9 = Button(frame_teclado, command= lambda: entrar_valores("5"), text= "5", width=5, height=2, bg=cor1, font=("Ivy 15 bold"), relief=RAISED, overrelief=RIDGE)
b_9.place(x=70,y=134)
b_10 = Button(frame_teclado, command= lambda: entrar_valores("6"), text= "6", width=5, height=2, bg=cor1, font=("Ivy 15 bold"), relief=RAISED, overrelief=RIDGE)
b_10.place(x=140,y=134)
b_11 = Button(frame_teclado, command= lambda: entrar_valores("-"), text= "-", width=5, height=2, bg=cor1, font=("Ivy 15 bold"), relief=RAISED, overrelief=RIDGE)
b_11.place(x=210,y=134)
b_12 = Button(frame_teclado, command= lambda: entrar_valores("1"), text= "1", width=5, height=2, bg=cor1, font=("Ivy 15 bold"), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0,y=201)
b_13 = Button(frame_teclado, command= lambda: entrar_valores("2"), text= "2", width=5, height=2, bg=cor1, font=("Ivy 15 bold"), relief=RAISED, overrelief=RIDGE)
b_13.place(x=70,y=201)
b_14 = Button(frame_teclado, command= lambda: entrar_valores("3"), text= "3", width=5, height=2, bg=cor1, font=("Ivy 15 bold"), relief=RAISED, overrelief=RIDGE)
b_14.place(x=140,y=201)
b_15 = Button(frame_teclado, command= lambda: entrar_valores("+"), text= "+", width=5, height=2, bg=cor1, font=("Ivy 15 bold"), relief=RAISED, overrelief=RIDGE)
b_15.place(x=210,y=201)
b_16 = Button(frame_teclado, command= lambda: entrar_valores("0"), text= "0", width=11, height=2, bg=cor1, font=("Ivy 15 bold"), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0,y=268)
b_17 = Button(frame_teclado, command= lambda: entrar_valores("."), text= ".", width=5, height=2, bg=cor1, font=("Ivy 15 bold"), relief=RAISED, overrelief=RIDGE)
b_17.place(x=140,y=268)
b_18 = Button(frame_teclado, command= calcular , text= "=", width=5, height=2, bg=cor4, fg=cor5, font=("Ivy 15 bold"), relief=RAISED, overrelief=RIDGE)
b_18.place(x=210,y=268)

janela.mainloop()