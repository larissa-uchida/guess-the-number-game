from tkinter import * 
import tkinter as tk
import random




class Janela(tk.Toplevel):
    def __init__(self, master=None, title=''):
        super().__init__(master)
        self.geometry('500x500')
        self.title()

def fecha_inicial_abre_dificuldade():
    janela_inicial.destroy()
    janela_dificuldade.deiconify()

def fecha_dificuldade_abre_jogo():
    janela_dificuldade.destroy()
    janela_jogo.deiconify()




janela_inicial = Janela(title='Jogo da Advinhação!')
"""janela_dificuldade = Janela(title='Nível de Dificuldade')
janela_jogo = Janela(title='Você consegue!')

class Botao(tk.Button):
    def __init__(self, master, janela="", text="", width=20, bg="", font=("Arial", 15), command=None, row="", pady="", tentativas=0):
        super().__init__(master=master, text=text, width=width,bg=bg, font=font, command=command)
        self.grid(column=0,row=row, pady=pady)

    def set_callback(self, callback):
        self.config(command=callback)

botao_jogar = Botao(janela_inicial, text="Jogar",bg="white", pady=50, row=2, command=fecha_inicial_abre_dificuldade)

botao1 = Botao(janela_dificuldade, text="Nível 1 - Fácil", bg="green", row=1, pady=10, tentativas=20, command=fecha_dificuldade_abre_jogo)
botao2 = Botao(janela_dificuldade, text="Nível 2 - Médio", bg="orange", row=2, pady=10, tentativas=10, command=fecha_dificuldade_abre_jogo)
botao3 = Botao(janela_dificuldade, text="Nível 3 - Difícil", bg="red", row=3, pady=10, tentativas=5, command=fecha_dificuldade_abre_jogo)

class Texto(tk.Label):
    def __init__(self, master, janela="", text="", font=("Arial"),column=0, row=0, padx=0, pady=0):
        super().__init__(master=master, text=text, font=font)
        self.grid(column=column ,row=row, padx=padx, pady=pady)"""

janela_inicial.mainloop()




"""class JanelaPrincipal(tk.Tk):
    def __init__(self, master, geometry='500x500', title='Advinhe'):

janela_principal = tk.Tk()
janela_principal.geometry('500x500')
janela_principal.title('Advinhe o Número')

titulo_jogo = Texto(janela_principal, text="Jogo da Advinhação: Número!", font=("Arial", 25), padx=30, pady=70)
descricao_jogo = Texto(janela_principal, text="nesse game, você terá que advinhar o número \nsecreto gerado aleatoriamente pela máquina", font=("Arial", 15), row=1)

def fecha_principal():
    janela_principal.destroy()

def nova_janela():
    janela_dificuldade = tk.Toplevel(janela_principal)
    janela_dificuldade.geometry('500x500')
    janela_dificuldade.title('Escolha Dificuldade')

    titulo_dificuldade = Label(janela_dificuldade, text="Escolha o Nível de Dificuldade:", font=("Arial", 25))
    titulo_dificuldade.grid(column=0, row=0, padx=25, pady=70)"""





