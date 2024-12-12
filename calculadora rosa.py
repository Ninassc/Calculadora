import customtkinter as ctk 
from tkinter import *
from tkinter import messagebox
import openpyxl, xlrd
from openpyxl import Workbook
import pathlib 

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

class window(ctk.CTk):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.configInicial()
        self.escolherTema()
        self.framePrincipal()
        self.corpo()
        self.botoes()


    
    def configInicial(self):
        self.geometry('500x600')
        self.title('Calculadora')
        self.resizable(False, False)


    def mudarTema(self, novoTema):
        ctk.set_appearance_mode(novoTema)

    
    def escolherTema(self):
        labelTema = ctk.CTkLabel(self, text='Tema:', font=('Lato bold', 14))
        labelTema.place(x=10, y=530)

        selecionarTema = ctk.CTkComboBox(self, values=('Dark', 'System'), command=self.mudarTema, border_color=('#f57fa6'), button_color=('#f57fa6'))
        selecionarTema.place(x=10, y=560)

    
    def framePrincipal(self):
        frame = ctk.CTkFrame(self, width=500, height=120, fg_color=('#f57fa6'))
        frame.place(x=0, y=0)

        self.frameText = ctk.CTkLabel(frame, text='CALCULADORA', font=('Lato bold', 30), text_color='#fff')
        self.frameText.place(relx=0.5, rely=0.5, anchor='center')


    def corpo(self):
        labelDigite = ctk.CTkLabel(self, text='Digite a Operação:', font=('Lato', 18))
        labelDigite.place(relx=0.35 , y=190, anchor='center')

        self.entryNumero = ctk.CTkEntry(self, placeholder_text='Ex: 18/2', border_color=('#f57fa6'), width=300, height=40, font=('Lato bold', 18))
        self.entryNumero.place(relx=0.5, rely=0.4, anchor='center')

    
    def limpar(self):
        self.entryNumero.delete(0, 'end')
        self.frameText.configure(text='Calculadora')

    
    def calcular(self):
        lst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        if self.entryNumero.get() in lst:
            messagebox.showwarning('Sistema', 'Não é possível realizar o cálculo!')
        else:
            self.frameText.configure(text=str(eval(self.entryNumero.get())))


    def botoes(self):
        botaoCalcular = ctk.CTkButton(self, text='CALCULAR', fg_color=('#f57fa6'), text_color='#fff', font=('Lato bold', 16), height=50, width=150, corner_radius=15, command=self.calcular)
        botaoCalcular.place(x=50, y=330)

        botaoLimpar = ctk.CTkButton(self, text='LIMPAR', fg_color=('#f57fa6'), text_color='#fff', font=('Lato bold', 16), height=50, width=150, corner_radius=15, command=self.limpar)
        botaoLimpar.place(x=290, y=330)

        




        








    
Window = window()
Window.mainloop()