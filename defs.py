from genericpath import exists
from tkinter import *
from tkinter import ttk
from tkinter.tix import IMAGE
from random import randint
from classes import *
import os
from typing_extensions import Self
import pygame
import time
result = []
acertos = 0
Tempo = False

iniciar = Inicializar()
id = 0
i = -10
j = 0
btn_h = 3
btn_w = 40
n_pulos = 100
m = ""
print(m)
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


def passar(event):
    global pular
    global n_pulos
    global contador
    global secs
    secs = 60
    #contador.destroy()
    #pular['text'] = f"Pular X{n_pulos}"
    if n_pulos == 1:
        pular['state'] = DISABLED
    aleatorio()
    
    n_pulos -= 1
    print("Teste")
def passar_cor1(event):
    pular['bg'] = Cores.verde
    pular['fg'] = Cores.branco
    

def passar_cor2(event):
    pular['bg'] = Cores.branco
    pular['fg'] = Cores.preto
    

def voltar_cor1(event):
    voltar['bg'] = Cores.verde
    voltar['fg'] = Cores.branco

def voltar_cor2(event):
    voltar['bg'] = Cores.branco
    voltar['fg'] = Cores.preto

def cartas():
    print(m)
    pass


def Botoes_De_Tela():
    global voltar
    global pular
    global n_pulos
    print(f"PULOS: {n_pulos}")
   

    Fundo_Direito = Label(iniciar.janela,width=34,height=50,bg=Cores.preto)
    Fundo_Direito.place(x=710,y=150)

    voltar = Label(iniciar.janela,text=f"Sair",width=13,bg=Cores.branco)
    voltar.place(x=855,y=550)
    voltar.bind("<Button-1>",Tela_Inicial)
    voltar.bind("<Enter>",voltar_cor1)
    voltar.bind("<Leave>",voltar_cor2)

    cartas = Label(iniciar.janela,text=f"Carta",width=13,bg=Cores.branco)
    cartas.place(x=855,y=490)
    cartas.bind("<Button-1>",cartas)
    

    if n_pulos >= 1:
        pular = Label(iniciar.janela,text=f"PULAR PERGUNTA ",width=14)
        pular.bind("<Button-1>",passar)
        pular.bind("<Enter>",passar_cor1)
        pular.bind("<Leave>",passar_cor2)
        pular.place(x=720,y=550)


def aleatorio():
    titulo = False
    global Tempo
    Tempo = True
    print(Tempo)
    
    #iniciar.janela.after(3000)
    
    texto_iniciar.destroy()
    texto_opcoes.destroy() 
    texto_sair.destroy() 
    lb_fundo.destroy() 
    pygame.mixer.music.stop()
    iniciar.janela['bg'] = "#FF0000"
    #iniciar.janela.after(2000,aa())
    
    perg_aleatoria = randint(1,7)
    if perg_aleatoria in result:
        perg_aleatoria = randint(1,7)
    if not perg_aleatoria in result:
        
        result.append(perg_aleatoria)
    else:
        pass
    for i in range(len(result)):
        print(result[i])
    
    if result[-1] == 1: Perguntas("somp1","imgp1","BASE","ALICERCE","FUNDAMENTO","RUINA")
    if result[-1] == 2: Perguntas("somp2","imgp2","UM TREM","UMA CARAVELA","UMA BICICLETA","UMA MOTO")
    if result[-1] == 3: Perguntas("somp3","imgp3","ITALIA","ALEMANHA","RÚSSIA","ESPANHA")
    if result[-1] == 4: Perguntas("somp4","imgp4","QUEIJO","PEDRA","FRUTA","AGUA")
    if result[-1] == 5: Perguntas("somp5","imgp5","FOGO","MAR","CÉU","CAMPO")
    if result[-1] == 6: Perguntas("somp6","imgp6","JEJUNO","ÚTERO","BAÇO","DELGADO")
    if result[-1] == 7: Perguntas("somp7","imgp7","NO MAR","NO PARAISO","NA TERRA","NO INFERNO")
    #if perg_aleatoria == 4: p6()
    print (f"NUMERO DA PERGUNTA: {perg_aleatoria}")
    
        
    pass

secs = 60
def tempo():
    global secs
    global contador
    global txt_tempo
    
    txt_tempo = Label(iniciar.janela,text="Tempo",font="arial 15",width=6)
    contador = Label(iniciar.janela,text="",width=6,height=2,bg="#ae2012",fg=Cores.branco,font="arial 15")
    if Tempo == True:
        contador.place(x=950,y=184)
        txt_tempo.place(x=950,y=155)
    if secs == 0:
        print("fim do tempo")    
    if secs > 0:
        
        secs -= 1
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
def Btn_cor1(r):
    r['bg'] = Cores.azul
    
def Btn_cor2(r):
    r['bg'] = Cores.vermelho

def resposta1(m,r):
    global acertos
    global secs
    global res_1
    global n_pulos
    global icone_certo
    respostas = ["RUINA","UMA CARAVELA","RÚSSIA","FRUTA","CÉU","ÚTERO","NO PARAISO"]
    print(m)
    

    if m in respostas and acertos  < 24:
        secs = 60
        acertos += 1
        print (f"Numero de Acertos: {acertos}")
        pygame.mixer.music.load(iniciar.PastaApp+"/sons/certaresposta.mp3")
        pygame.mixer.music.play()
        iniciar.janela.after(9000)
        destroir()
    
        pygame.mixer.music.stop()
        aleatorio()
    else:
        #print("Resposta Errada")
        pass


  
        
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
        
    
def move_btn():
    global i
    global num_1
    global num_2
    global num_3
    global num_4
    i+=3
    num_1 = Label(iniciar.janela,text="A",width=5,height=3)
    num_2 = Label(iniciar.janela,text="B",width=5,height=3)
    num_3 = Label(iniciar.janela,text="C",width=5,height=3)
    num_4 = Label(iniciar.janela,text="D",width=5,height=3)
    
    num_1.place(x=i-48,y=330)
    num_2.place(x=i-48,y=400)
    num_3.place(x=i-48,y=470)
    num_4.place(x=i-48,y=540)
    res_1.place(x=i,y=330)
    res_2.place(x=i,y=400)
    res_3.place(x=i,y=470)
    res_4.place(x=i,y=540)
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
    
    font_perguntas = "Arial 25 bold"
    font_respostas = "Sans-serif 10 bold"
    iniciar.janela['bg'] = "#FF0000"
    pygame.mixer.init()
    pygame.mixer.music.load(iniciar.PastaApp+f"/sons/{som}.mp3")
    pygame.mixer.music.play()

    #pygame.mixer.music.load(iniciar.PastaApp+f"/sons/Somsuspense.mp3")
    #pygame.mixer.music.play()
    
    frame_p1=Frame(iniciar.janela,width=660,height=150)
    frame_p1.place(x=50,y=148)
    
    fundo_pergunta2 = PhotoImage(file=iniciar.PastaApp+f"/img/imgs_perguntas/{img}.png")
    lb_p1 = Label(frame_p1,text=f"QUAL DESSAS PALAVRAS NÂO TEM RELAÇÂO COM SUTENTAÇÂO",image=fundo_pergunta2,border=0)
    lb_p1.place(x=0,y=0)
    iniciar.janela.after(100,lambda:move_btn())
        
    
    res_1 = Label(iniciar.janela,
    text=f"{r1}",
    font=font_respostas,
    width=btn_w,
    height=btn_h,
    fg=Cores.branco,
    bg=Cores.vermelho,
    activebackground=Cores.azul,
    
    activeforeground=Cores.branco,
    #command=lambda m=f"{r1}": resposta1(m),
    relief=SUNKEN )
    
    res_2 = Label(iniciar.janela,
    text=f"{r2}",
    font=font_respostas,
    width=btn_w,
    height=btn_h,
    fg=Cores.branco,
    bg=Cores.vermelho,
    activebackground=Cores.azul,
    
    activeforeground=Cores.branco,
    #command=lambda m=f"{r2}": resposta1(m),
    relief=SUNKEN)
    img_btn = PhotoImage(file="/home/brunodlucas/Documentos/GitHub/SDO/img/fundobtn.png")
    res_3 = Label(iniciar.janela,
    text=f"{r3}",
    
    font=font_respostas,
    width=btn_w,
    height=btn_h,
    fg=Cores.branco,
    bg=Cores.vermelho,
    activebackground=Cores.azul,
    
    activeforeground=Cores.branco,
    #command=lambda m=f"{r3}": resposta1(m),
    relief=SUNKEN) 
    
    res_4 = Label(iniciar.janela,
    text=f"{r4}",
    font=font_respostas,
    width=btn_w,
    height=btn_h,
    fg=Cores.branco,
    bg=Cores.vermelho,
    activebackground=Cores.azul,
    
    activeforeground=Cores.branco,
    #command=lambda m=f"{r4}": resposta1(m),
    relief=SUNKEN
     )
    
    res_1.bind("<Button-1>",lambda m=f"{r1}": resposta1(r1,res_1))
    res_2.bind("<Button-1>",lambda m=f"{r2}": resposta1(r2,res_2))
    res_3.bind("<Button-1>",lambda m=f"{r3}": resposta1(r3,res_3))
    res_4.bind("<Button-1>",lambda m=f"{r4}": resposta1(r4,res_4))
    ################MUDANDO BG DAS LABEL
    res_1.bind("<Enter>",lambda m=f"{r1}": Btn_cor1(res_1))
    res_2.bind("<Enter>",lambda m=f"{r2}": Btn_cor1(res_2))
    res_3.bind("<Enter>",lambda m=f"{r3}": Btn_cor1(res_3))
    res_4.bind("<Enter>",lambda m=f"{r4}": Btn_cor1(res_4))
    
    res_1.bind("<Leave>",lambda m=f"{r1}": Btn_cor2(res_1))
    res_2.bind("<Leave>",lambda m=f"{r2}": Btn_cor2(res_2))
    res_3.bind("<Leave>",lambda m=f"{r3}": Btn_cor2(res_3))
    res_4.bind("<Leave>",lambda m=f"{r4}": Btn_cor2(res_4))


def Tela_Inicial(event):
    global n_pulos
    global secs
    global texto_iniciar
    global texto_opcoes
    global texto_sair
    global fundo
    global lb_fundo
    global result
    
    secs = 60
    result = []
    n_pulos = 100
    global Tempo
    Tempo = False
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
    
tempo()
#iniciar.teste.pack()

def musica_titulo():
    
    pygame.mixer.init()
    pygame.mixer.music.load(iniciar.PastaApp+"/sons/intro.mp3")

    pygame.mixer.music.play()
    pass

def fechamento():
    iniciar.janela.mainloop()

