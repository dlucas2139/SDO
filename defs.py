from genericpath import exists
from tkinter import *
from tkinter import ttk
from tkinter.tix import IMAGE
import os
import pygame
import time

i = -10
j = 0
btn_h = 3
btn_w = 40
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
    pass

secs = 60
def tempo():
    global secs
    global contador
    contador = Label(janela,text="",width=5,height=3,bg="#ae2012",fg="#000000")
    contador.place(x=900,y=180)
    if secs == 0:
        print("fim do tempo")    
    else:
        secs = secs - 1
        contador['text'] = secs
        contador.after(1000, tempo)
    pass
def resposta1(m):
    global res_1
    global icone_certo
    if m == "certa":
        
        #cone_certo = Label(janela,text="Certo")
        #icone_certo.place(x=0,y=0)
        global secs
        secs = 60
        pygame.mixer.music.load(PastaApp+"/sons/certaresposta.mp3")
        pygame.mixer.music.play()
        janela.after(9000)
        res_1.destroy()
        res_2.destroy()
        res_3.destroy()
        res_4.destroy()
        frame_p1.destroy()
        pygame.mixer.music.stop()
        p2()
        
    if m == "certa2":
        
        pygame.mixer.music.load(PastaApp+"/sons/certaresposta.mp3")
        pygame.mixer.music.play()
        janela.after(9000)
        res_1.destroy()
        res_2.destroy()
        res_3.destroy()
        res_4.destroy()
        frame_p1.destroy()
        p3()
    pass    
    pass
def move_btn():
    global i
    i+=3
    res_1.place(x=i,y=300)
    res_2.place(x=i,y=370)
    res_3.place(x=i,y=440)
    res_4.place(x=i,y=510)
    if i < 50:
        janela.after(100,lambda:move_btn())
    pass

########## PERGUNTA 1
def p1(p1):
    global font_perguntas
    global frame_p1
    global res_1
    global res_2
    global res_3
    global res_4
    global btn
    global n1
    global logo_lb
    global logo
    global voltar
    global voltar_img
    global btn_h
    global btn_w
    global fundo_pergunta
    global fundo_jogo

    tempo()
    font_perguntas = "Arial 25 bold"
    font_respostas = "Sans-serif 10 bold"
    btn_h = 3
    btn_w = 40
    font_perguntas = "Arial 25 bold"
    #janela['bg'] = "#FF0000"
    pygame.mixer.init()
    pygame.mixer.music.load(PastaApp+"/sons/perguntas.mp3")
    pygame.mixer.music.play()
    fundo_jogo = PhotoImage(file=PastaApp+"/img/a.png")
    
    frame_right=Label(janela,width=1024,height=680, image=fundo_jogo)
    frame_right.place(x=0,y=0)
    
    frame_p1=Frame(janela,width=660,height=150)
    frame_p1.place(x=50,y=148)
    fundo_pergunta = PhotoImage(file=PastaApp+"/img/FundoPergunta.png")
    lb_p1 = Label(frame_p1,text=f"QUAL DESSAS PALAVRAS NÂO TEM RELAÇÂO COM SUTENTAÇÂO",image=fundo_pergunta,border=0)
    lb_p1.place(x=0,y=0)
    janela.after(100,lambda:move_btn())
    
    def voltar_menu():
        global res_1
        global res_2
        global res_3
        global res_4
        global frame_p1
        global contador
        contador.destroy()
        res_1.destroy()
        res_2.destroy()
        res_3.destroy()
        res_4.destroy()
        frame_p1.destroy()
        fundo_menu()
    voltar_img = PhotoImage(file=PastaApp+"/img/voltar.png") 
    voltar = Button(janela,text="Voltar",image=voltar_img,border=0,command=voltar_menu)
    voltar.place(x=750,y=600)
  
    

    res_1 = Button(janela,
    text="1 Base",
    font=font_respostas,
    width=btn_w,
    height=btn_h,
    fg=Cores.branco,
    bg=Cores.vermelho,
    activebackground=Cores.azul,
    
    activeforeground=Cores.branco,
    command=lambda m="errado": resposta1(m),
    relief=SUNKEN
    )
    res_2 = Button(janela,
    text="2 ALICERECE" ,
    font=font_respostas,
    width=btn_w,
    height=btn_h,
    fg=Cores.branco,
    bg=Cores.vermelho,
    activebackground=Cores.azul,
    activeforeground=Cores.branco, 
    command=lambda m="errado": resposta1(m),
    relief=SUNKEN
    )
    

    res_3 = Button(janela,
    text="3 FUNDAMENTO" ,
    font=font_respostas,
    width=btn_w,
    height=btn_h,
    fg=Cores.branco,
    bg=Cores.vermelho,
    activebackground=Cores.azul,
    activeforeground=Cores.branco,
    command=lambda m="errado": resposta1(m),
    relief=SUNKEN
    )
    
    res_4 = Button(janela,
    text="4 RUINA", 
    font=font_respostas ,
    width=btn_w,
    height=btn_h,
    fg=Cores.branco,
    bg=Cores.vermelho,
    activebackground=Cores.azul,
    activeforeground=Cores.branco,
    command=lambda m="certa": resposta1(m),
    relief=SUNKEN
)
############# PERGUNTA 2
def p2():
    global fundo_pergunta2
    global font_perguntas
    global frame_p1
    global res_1
    global res_2
    global res_3
    global res_4
    global font_respostas
    global btn_w
    global btn_h
    
    font_perguntas = "Arial 25 bold"
    font_respostas = "Sans-serif 10 bold"
    janela['bg'] = "#FF0000"
    pygame.mixer.init()
    pygame.mixer.music.load(PastaApp+"/sons/perguntas2.mp3")
    pygame.mixer.music.play()
    
    frame_p1=Frame(janela,width=660,height=150)
    frame_p1.place(x=50,y=148)
    fundo_pergunta2 = PhotoImage(file=PastaApp+"/img/FundoPergunta2.png")
    lb_p1 = Label(frame_p1,text=f"QUAL DESSAS PALAVRAS NÂO TEM RELAÇÂO COM SUTENTAÇÂO",image=fundo_pergunta2,border=0)
    lb_p1.place(x=0,y=0)
    janela.after(100,lambda:move_btn())

    res_1 = Button(janela,
    text="1 Base",
    font=font_respostas,
    width=btn_w,
    height=btn_h,
    fg=Cores.branco,
    bg=Cores.vermelho,
    activebackground=Cores.azul,
    
    activeforeground=Cores.branco,
    command=lambda m="errado": resposta1(m),
    relief=SUNKEN )
    
    res_2 = Button(janela,
    text="2 UMA CARAVELA",
    font=font_respostas,
    width=btn_w,
    height=btn_h,
    fg=Cores.branco,
    bg=Cores.vermelho,
    activebackground=Cores.azul,
    
    activeforeground=Cores.branco,
    command=lambda m="certa2": resposta1(m),
    relief=SUNKEN)
    
    res_3 = Button(janela,
    text="3 UMA BICICLETA",
    font=font_respostas,
    width=btn_w,
    height=btn_h,
    fg=Cores.branco,
    bg=Cores.vermelho,
    activebackground=Cores.azul,
    
    activeforeground=Cores.branco,
    command=lambda m="errado": resposta1(m),
    relief=SUNKEN) 
    
    res_4 = Button(janela,
    text="4 UMA MOTO",
    font=font_respostas,
    width=btn_w,
    height=btn_h,
    fg=Cores.branco,
    bg=Cores.vermelho,
    activebackground=Cores.azul,
    
    activeforeground=Cores.branco,
    command=lambda m="errado": resposta1(m),
    relief=SUNKEN
     ) 
############# PERGUNTA 3
def p3():
    
    pass

def perguntaN1():
    
    titulo = False
    texto_iniciar.destroy()
    texto_opcoes.destroy() 
    texto_sair.destroy() 
    lb_fundo.destroy() 
    pygame.mixer.music.stop()
    janela['bg'] = "#FF0000"
    #janela.after(2000,aa())
    p1("1")
 
    pass

def initf():
    global width 
    global height 
    global janela
    global PastaApp
    PastaApp = os.path.dirname(__file__)
    width = 1024
    height = 680
    janela = Tk()
    janela.geometry(f"{width}x{height}")
    janela.title("Show do Milhão")
    
def fundo_menu():
    global secs
    global texto_iniciar
    global texto_opcoes
    global texto_sair
    global fundo
    global lb_fundo
    secs = 60
    fundo = PhotoImage(file=PastaApp+"/img/fundo.png",width=width)
    lb_fundo = Label(janela,image=fundo)
    lb_fundo.place(x=0,y=0)
    tamanho_fonte = 30
    posx = 400
    musica_titulo()
    
    texto_iniciar = Button(janela,
    highlightthickness = 0, 
    bd = 0,
    text="Jogar",
    font=f"Arial {tamanho_fonte} bold",
    fg=Cores.branco,
    bg=Cores.fundo,
    activebackground=Cores.verde,
    activeforeground=Cores.branco,
    highlightcolor=Cores.vermelho,
    width=10,
    command=perguntaN1
    
    )
    texto_iniciar.place(x=posx,y=400)
    
    
    texto_opcoes = Button(janela,
    highlightthickness = 0, 
    bd = 0,
    text="Opções",
    font=f"Arial {tamanho_fonte} bold",
    fg=Cores.branco,
    bg=Cores.fundo,
    activebackground=Cores.verde,
    activeforeground=Cores.branco,
    highlightcolor=Cores.vermelho,
    width=10
    )
    texto_opcoes.place(x=posx,y=460)

    texto_sair = Button(janela,
    highlightthickness = 0, 
    bd = 0,
    text="Sair",
    font=f"Arial {tamanho_fonte} bold",
    fg=Cores.branco,
    bg=Cores.fundo,
    activebackground=Cores.verde,
    activeforeground=Cores.branco,
    highlightcolor=Cores.vermelho,
    width=10,
    command=janela.destroy
    )
    texto_sair.place(x=posx,y=520)



def musica_titulo():
    
    pygame.mixer.init()
    pygame.mixer.music.load(PastaApp+"/sons/intro.mp3")

    pygame.mixer.music.play()
    pass

def fechamento():
    janela.mainloop()

