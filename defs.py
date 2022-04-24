from genericpath import exists
from tkinter import *
from tkinter import ttk
from tkinter.tix import IMAGE
from random import randint
from classes import *
#from perguntas import *
import os
from typing_extensions import Self
import pygame
import time


iniciar = Inicializar()
id = 0
i = -10
j = 0
btn_h = 3
btn_w = 40
n_pulos = 2
m = ""
def voltar_menu():
    global res_1
    global res_2
    global res_3
    global res_4
    global frame_p1
    global contador
    global txt_tempo

    res_1.destroy()
    res_2.destroy()
    res_3.destroy()
    res_4.destroy()
    frame_p1.destroy()
    Tela_Inicial()
    #voltar_img = PhotoImage(file=PastaApp+"/img/voltar.png") 
    
def Botoes_De_Tela():
    global voltar
    global pular
    global n_pulos
    print(f"PULOS: {n_pulos}")
    voltar = Button(iniciar.janela,text="Sair",border=0,command=voltar_menu)
    voltar.place(x=970,y=3)
    
    if n_pulos >= 1:
        
        pular = Button(iniciar.janela,
        text=f"PULAR PERGUNTA ",
        width=13,
        command=lambda m="pular1": resposta1(m)
        )
        pular.place(x=710,y=550)
        
    
    pass


def aleatorio():
    titulo = False
    
    #tempo()
    texto_iniciar.destroy()
    texto_opcoes.destroy() 
    texto_sair.destroy() 
    lb_fundo.destroy() 
    pygame.mixer.music.stop()
    iniciar.janela['bg'] = "#FF0000"
    #iniciar.janela.after(2000,aa())
    #p1() #NÂO APAGAR
    perg_aleatoria = randint(1,3)

    if perg_aleatoria == 1: Perguntas("perguntas","FundoPergunta","BASE","ALICERCE","FUNDAMENTO","RUINA") 
    if perg_aleatoria == 2: Perguntas("perguntas2","FundoPergunta2","UM TREM","UMA CARAVELA","UMA BICICLETA","UMA MOTO") 
    if perg_aleatoria == 3: Perguntas("certaresposta","FundoPerguntasemtexto","P5","bruno","Alala","asdf") 
    #if perg_aleatoria == 4: p6()
    print (perg_aleatoria)
    
        
    pass
    


secs = 60
def tempo():
    global secs
    global contador
    global txt_tempo
    txt_tempo = Label(iniciar.janela,text="Tempo",font="arial 15",width=6)
    txt_tempo.place(x=950,y=155)
    contador = Label(iniciar.janela,text="",width=6,height=2,bg="#ae2012",fg=Cores.branco,font="arial 15")
    contador.place(x=950,y=184)
    if secs == 0:
        print("fim do tempo")    
    if secs > 0:
        secs = secs - 1
        contador['text'] = secs
        contador.after(1000, tempo)
    pass
def destroir():
    res_1.destroy()
    res_2.destroy()
    res_3.destroy()
    res_4.destroy()
    
    frame_p1.destroy()
        
    pass
def resposta1(m):
    
    global res_1
    global n_pulos
    global icone_certo
    print(m)

    if m == "RUINA" or m == "UMA CARAVELA":
        pygame.mixer.music.load(iniciar.PastaApp+"/sons/certaresposta.mp3")
        pygame.mixer.music.play()
        iniciar.janela.after(9000)
        destroir()
        
        pygame.mixer.music.stop()
        aleatorio()
        pass


    if m == "pular1" or m == "certa":
        global secs
        secs = 60
        pygame.mixer.music.stop()

    if m == "pular1":
        global pular
        global n_pulos
        global contador

        #contador.destroy()
        pular['text'] = f"Pular X{n_pulos}"
        if n_pulos == 1:
            pular['state'] = DISABLED
        aleatorio()
        
        n_pulos -= 1
        
    if m == "certa":
       #cone_certo = Label(iniciar.janela,text="Certo")
        #icone_certo.place(x=0,y=0)
        
        pygame.mixer.music.load(iniciar.PastaApp+"/sons/certaresposta.mp3")
        pygame.mixer.music.play()
        iniciar.janela.after(9000)
        destroir()
        
        pygame.mixer.music.stop()
        aleatorio()
        
    if m == "certa2":
        
        pygame.mixer.music.load(iniciar.PastaApp+"/sons/certaresposta.mp3")
        pygame.mixer.music.play()
        iniciar.janela.after(9000)
        destroir()
        aleatorio()
        
    pass    
    pass
def move_btn():
    global i
    global num_1
    global num_2
    global num_3
    global num_4
    i+=3
    num_1 = Label(iniciar.janela,text="1",width=5,height=3)
    num_2 = Label(iniciar.janela,text="2",width=5,height=3)
    num_3 = Label(iniciar.janela,text="3",width=5,height=3)
    num_4 = Label(iniciar.janela,text="4",width=5,height=3)
    
    num_1.place(x=i-48,y=300)
    num_2.place(x=i-48,y=370)
    num_3.place(x=i-48,y=440)
    num_4.place(x=i-48,y=510)
    res_1.place(x=i,y=300)
    res_2.place(x=i,y=370)
    res_3.place(x=i,y=440)
    res_4.place(x=i,y=510)
    if i < 50:
        iniciar.janela.after(100,lambda:move_btn())
    pass


############# PERGUNTA 3##########################################
def Perguntas(som,img,r1,r2,r3,r4):
    
    global secs
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
    global rs_1000
    global fundo_jogo
    global frame_right
    fundo_jogo = PhotoImage(file=iniciar.PastaApp+"/img/a.png")
    frame_right=Label(iniciar.janela,width=1024,height=680, image=fundo_jogo)
    frame_right.place(x=0,y=0)
    Botoes_De_Tela()
    
    
    secs = 60
    font_perguntas = "Arial 25 bold"
    font_respostas = "Sans-serif 10 bold"
    iniciar.janela['bg'] = "#FF0000"
    pygame.mixer.init()
    pygame.mixer.music.load(iniciar.PastaApp+f"/sons/{som}.mp3")
    pygame.mixer.music.play()
    
    frame_p1=Frame(iniciar.janela,width=660,height=150)
    frame_p1.place(x=50,y=148)
    fundo_pergunta2 = PhotoImage(file=iniciar.PastaApp+f"/img/{img}.png")
    lb_p1 = Label(frame_p1,text=f"QUAL DESSAS PALAVRAS NÂO TEM RELAÇÂO COM SUTENTAÇÂO",image=fundo_pergunta2,border=0)
    lb_p1.place(x=0,y=0)
    iniciar.janela.after(100,lambda:move_btn())
        
    
    res_1 = Button(iniciar.janela,
    text=f"{r1}",
    font=font_respostas,
    width=btn_w,
    height=btn_h,
    fg=Cores.branco,
    bg=Cores.vermelho,
    activebackground=Cores.azul,
    
    activeforeground=Cores.branco,
    command=lambda m=f"{r1}": resposta1(m),
    relief=SUNKEN )
    
    res_2 = Button(iniciar.janela,
    text=f"{r2}",
    font=font_respostas,
    width=btn_w,
    height=btn_h,
    fg=Cores.branco,
    bg=Cores.vermelho,
    activebackground=Cores.azul,
    
    activeforeground=Cores.branco,
    command=lambda m=f"{r2}": resposta1(m),
    relief=SUNKEN)
    
    res_3 = Button(iniciar.janela,
    text=f"{r3}",
    font=font_respostas,
    width=btn_w,
    height=btn_h,
    fg=Cores.branco,
    bg=Cores.vermelho,
    activebackground=Cores.azul,
    
    activeforeground=Cores.branco,
    command=lambda m=f"{r3}": resposta1(m),
    relief=SUNKEN) 
    
    res_4 = Button(iniciar.janela,
    text=f"{r4}",
    font=font_respostas,
    width=btn_w,
    height=btn_h,
    fg=Cores.branco,
    bg=Cores.vermelho,
    activebackground=Cores.azul,
    
    activeforeground=Cores.branco,
    command=lambda m=f"{r4}": resposta1(m),
    relief=SUNKEN
     ) 

'''
def perguntaN1():
    
    titulo = False
    texto_iniciar.destroy()
    texto_opcoes.destroy() 
    texto_sair.destroy() 
    lb_fundo.destroy() 
    pygame.mixer.music.stop()
    iniciar.janela['bg'] = "#FF0000"
    #iniciar.janela.after(2000,aa())
    
 
    pass
'''
    
def Tela_Inicial():
    global n_pulos
    global secs
    global texto_iniciar
    global texto_opcoes
    global texto_sair
    global fundo
    global lb_fundo
    
    n_pulos = 2
    secs = 60
    fundo = PhotoImage(file=iniciar.PastaApp+"/img/fundo.png",width=iniciar.width)
    lb_fundo = Label(iniciar.janela,image=fundo)
    lb_fundo.place(x=0,y=0)
    tamanho_fonte = 30
    posx = 400
    musica_titulo()
    
    texto_iniciar = Button(iniciar.janela,
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
    command=aleatorio
    #command=perguntaN1
    
    )
    texto_iniciar.place(x=posx,y=400)
    
    
    texto_opcoes = Button(iniciar.janela,
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

    texto_sair = Button(iniciar.janela,
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
    command=iniciar.janela.destroy
    )
    texto_sair.place(x=posx,y=520)



def musica_titulo():
    
    pygame.mixer.init()
    pygame.mixer.music.load(iniciar.PastaApp+"/sons/intro.mp3")

    pygame.mixer.music.play()
    pass

def fechamento():
    iniciar.janela.mainloop()

