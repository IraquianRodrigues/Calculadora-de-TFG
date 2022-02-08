from tkinter import *
from tkinter import ttk


# CORES

co0 = '#ffffff'  # branco / white
co1 = '#444466'  # preto / black
co2 = '#4065a1'  # azul / blue

main = Tk()
main.title('')
main.configure(bg=co0)
main.geometry('295x230')
numerofixo = 72


# -------- DIVIVINDO A JANELA EM 2 FRAMES -----------------------

frame_cima = Frame(main, width=295, height=50, bg=co0,
                   pady=0, padx=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(main, width=295, height=180, bg=co0,
                    pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)

# ------------------ CONFIGURANDO FRAME ACIMA -----------------------

app_name = Label(frame_cima, text='Calculando a Creatinina', width=23, height=1,
                 padx=0, relief='flat', anchor='center', font=('Ivy 16 bold'), bg=co0, fg=co1)
app_name.place(x=0, y=0)

app_linha = Label(frame_cima, text='', width=400, height=1, padx=0,
                  relief='flat', anchor='center', font=('Ivy 1'), bg=co2, fg=co2)
app_linha.place(x=0, y=35)

# ------------------ CONFIGURANDO FRAME BAIXO ------------------------

l_idade = Label(frame_baixo, text='Insira sua idade:', width=25, height=1,
                padx=0, relief='flat', anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co1)
l_idade.grid(row=0, column=0, sticky=NSEW, pady=10, padx=3)
e_idade = Entry(frame_baixo, width=5, relief='solid',
                font=('Ivy 10 bold'), justify='center')
e_idade.grid(row=0, column=1, sticky=NSEW, pady=10, padx=3)

l_peso = Label(frame_baixo, text='Insira seu peso:', width=25, height=1, padx=0,
               relief='flat', anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co1)
l_peso.grid(row=1, column=0, sticky=NSEW, pady=10, padx=3)
e_peso = Entry(frame_baixo, width=5, relief='solid',
               font=('Ivy 10 bold'), justify='center')
e_peso.grid(row=1, column=1, sticky=NSEW, pady=10, padx=3)


l_creatinina = Label(frame_baixo, text='Insira o resultado da creatinina:', width=6, height=1, padx=0,
                     relief='flat', anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co1)
l_creatinina.grid(row=2, column=0, sticky=NSEW, pady=10, padx=3)
e_creatinina = Entry(frame_baixo, width=5, relief='solid',
                     font=('Ivy 10 bold'), justify='center')
e_creatinina.grid(row=2, column=1, sticky=NSEW, pady=10, padx=3)

main.mainloop()

