from tkinter import *
import os
class Cores():
    fundo = "#6d60ff"
    azul = "#1947e0"
    azul_s = "#3762f0"	
    branco = "#FFFFFF"	
    cinza = "#CCCCCC"	
    vermelho = "#5b0800"	
    verde = "#006600"	
    amarelo = "#D9D919"	
    laranja = "#fa7414"
    laranja_s = "#f58b49"
    preto = "#3b3b3b"
    azul3 = "#800e21"
    pass

class Inicializar:
 
    def __init__(Self):
        global width 
        global height 
        global janela
        global PastaApp
        Self.janela = Tk()
        Self.PastaApp = os.path.dirname(__file__)
        Self.width = 1024
        Self.height = 680
        #Self.width = Self.janela.winfo_screenwidth()               
        #Self.height= Self.janela.winfo_screenheight()               
        Self.janela.geometry("%dx%d" % (Self.width, Self.height))
        Self.janela['bg'] = "#FFFF00"
        Self.janela.geometry(f"{Self.width}x{Self.height}")
        #Self.janela.attributes('-fullscreen',True)
        #Self.janela.attributes('-zoomed',True)
        #Self.janela.resizable(height=0,width=0)
        Self.janela.title("Bruno Lucas / Project Game")
        
    
