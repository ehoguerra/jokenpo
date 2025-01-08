import tkinter as tk
from tkinter import Label, Frame, Button, LabelFrame, PhotoImage
import random

def pedra():
    jokenpo('Pedra')
def papel():
    jokenpo('Papel')
def tesoura():
    jokenpo('Tesoura')


def jokenpo(escolha_usuario):
    escolha_computador = random.choice(['Pedra', 'Papel', 'Tesoura'])
    global result
    if escolha_usuario == escolha_computador:
        mensagem = f'''
        Você: {escolha_usuario}
        Eu: {escolha_computador}

        Resultado: Empate!
        '''
    elif escolha_usuario == 'Pedra' and escolha_computador == 'Tesoura' or escolha_usuario == 'Papel' and escolha_computador == 'Pedra' or escolha_usuario == 'Tesoura' and escolha_computador == 'Papel':
        mensagem = f'''
        Você: {escolha_usuario}
        Eu: {escolha_computador}

        Resultado: Vitória!
        ''' 
        result = 'vitoria'
    else:
        mensagem = f'''
        Você: {escolha_usuario}
        Eu: {escolha_computador}

        Resultado: Derrota!
        ''' 
        result = 'derrota'
    resultado.config(text=mensagem)
    contagem()

def contagem():
    global vitorias, derrotas
    if 'vitorias' not in globals():
        vitorias = 0
    if 'derrotas' not in globals():
        derrotas = 0
    if result == 'vitoria':
        vitorias += 1
    elif result == 'derrota':
        derrotas += 1
    msg= f'''
    Vitórias: {vitorias}
    Derrotas: {derrotas}
    '''
    placar.config(text=msg)


janela = tk.Tk()

frame = LabelFrame(janela, text='Escolha uma opção:', padx=10, pady=10)
frame.pack()


icon_papel = PhotoImage(file='./img/papel.png')
icon_pedra = PhotoImage(file='./img/pedra.png')
icon_tesoura = PhotoImage(file='./img/tesoura.png')


Button(frame, text='Pedra', command=pedra, image=icon_pedra, compound=tk.LEFT).grid(column=0, row=1)
Button(frame, text='Papel', command=papel, image=icon_papel, compound=tk.LEFT).grid(column=1, row=1)
Button(frame, text='Tesoura', command=tesoura, image=icon_tesoura, compound=tk.LEFT).grid(column=2, row=1)

resultado = Label(frame, pady=10, padx=10, justify=tk.LEFT)
resultado.grid(column=0, row=2, columnspan=3)

placar = Label(frame, pady=10, padx=10, justify=tk.LEFT)
placar.grid(column=0, row=3, columnspan=3)




janela.title('Pedra, papel, tesoura')
janela.geometry("500x400+700+200")
janela.mainloop()