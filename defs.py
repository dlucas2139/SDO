
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
pontos = 0
Tempo = False

iniciar = Inicializar()
def dfcreditos():
    global Tempo
    global num_cartas
    global active_cartas
    global pontos
    global secs
    global n_pulos
    global creditos_img
    global lb_creditos
    global creditos
    global voltar
    texto_iniciar.destroy()
    texto_opcoes.destroy() 
    texto_sair.destroy() 
    lb_fundo.destroy() 
    creditos.destroy()

    num_cartas = 10
    active_cartas = True
    pontos = 0
    secs = 60
    result = []
    n_pulos = 100
    
    Tempo = False
    creditos_img = PhotoImage(file="/img/creditos.png",width=1024,height=680)
    lb_creditos = Label(iniciar.janela,image=creditos_img)
    lb_creditos.pack()
    voltar = Label(iniciar.janela,text=f"Sair",width=13,bg=Cores.branco)
    voltar.place(x=855,y=550)
    voltar.bind("<Button-1>",Tela_Inicial)
    voltar.bind("<Enter>",voltar_cor1)
    voltar.bind("<Leave>",voltar_cor2)

    pass

respostas = ["RUINA","UMA CARAVELA","RÚSSIA","FRUTA","CÉU","ÚTERO","NO PARAISO"]
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

def mutar():
    print(f"Audio: {var.get()}")
    if var.get() == 1:
        pygame.mixer.music.stop()
def Botoes_De_Tela():
    global voltar
    global pular
    global n_pulos
    global pontos
    global Tempo
    global Pontuacao
    global check_som
    global var
    global Fundo_direito_img
    global img_pulo
    global img_voltar
    print(f"PULOS: {n_pulos}")
   
    var = IntVar()
    img_voltar = PhotoImage(file="/img/voltarso0.png")
    img_pulo = PhotoImage(file="/img/pular.png")
    Fundo_direito_img = PhotoImage(file="/img/fundodireita.png",width=500,height=500)
    Fundo_Direito = Label(iniciar.janela,width=320,height=580,image=Fundo_direito_img,border=0)
    Fundo_Direito.place(x=710,y=150)
    check_som = Checkbutton(iniciar.janela,text="som",variable=var,command=lambda m=var: mutar())
    #check_som.pack()
    voltar = Label(iniciar.janela,text=f"Sair",width=80,height=40,bg=Cores.branco,image=img_voltar)
    voltar.place(x=720,y=635)
    voltar.bind("<Button-1>",Tela_Inicial)
    voltar.bind("<Enter>",voltar_cor1)
    voltar.bind("<Leave>",voltar_cor2)

 
    

    if n_pulos >= 1:
        pular = Label(iniciar.janela,image=img_pulo,width=150,height=119,bg=Cores.branco,border=0)
        txt_pular = Label(iniciar.janela,text=f"Pular {n_pulos}",width=17,font="SERIF")
        pular.bind("<Button-1>",passar)
        pular.bind("<Enter>",passar_cor1)
        pular.bind("<Leave>",passar_cor2)
        txt_pular.bind("<Button-1>",passar)
        txt_pular.bind("<Enter>",passar_cor1)
        txt_pular.bind("<Leave>",passar_cor2)
        pular.place(x=715,y=280)
        txt_pular.place(x=710,y=419)

lb_creditos = Label()
def aleatorio():
    titulo = False
    global lb_creditos
    global Tempo
    Tempo = True
    print(Tempo)
    print(secs)
    
    #iniciar.janela.after(3000)
    lb_creditos.destroy()
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
    
    txt_pontuacao = Label(iniciar.janela,text="PONTUAÇÂO",width=25,height=2,font="SERIF")
    Pontuacao = Label(iniciar.janela,text=f"{pontos}",width=26,height=3,bg="#ae2012",fg=Cores.branco,font="SERIF")
    if Tempo == True:
        txt_pontuacao.place(x=710,y=150)
        Pontuacao.place(x=710,y=190)    
        
    pass

secs = 60
def tempo():
    global secs
    global contador
    global txt_tempo
    
    txt_tempo = Label(iniciar.janela,text="Tempo",width=8,height=2,font="SERIF")
    contador = Label(iniciar.janela,text="",width=9,height=3,bg="#ae2012",fg=Cores.branco,font="SERIF")
    if Tempo == True:
        txt_tempo.place(x=940,y=150)
        contador.place(x=940,y=190)
        
    if secs == 0:
        secs = 60
        print("fim do tempo")    
    if secs > 0:
        
        secs -= 1
        contador['text'] = secs
        contador.after(1000, tempo)
    if secs <= 0:
        secs = 0 
   
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
active_cartas = True
num_cartas = 10

def resposta1(m,r,lb,*args):
    global acertos
    global secs
    global active_cartas
    global n_pulos
    global pontos
    global lb_cartas
    global a
    global num_cartas
    al = randint(1,3)
    a = lb
    respostas = ["RUINA","UMA CARAVELA","RÚSSIA","FRUTA","CÉU","ÚTERO","NO PARAISO"]
    respostas_erradas = ["NO MAR","NA TERRA","NO INFERNO"]

    global r1
    '''
    respostas = {"certa":"RUINA","certa":"UMA CARAVELA","certa":"RÚSSIA","certa":"FRUTA","certa":"CÉU","certa":"ÚTERO","certa":"NO PARAISO",
    "errada":"NO MAR","errada":"NA TERRA","errada":"NO INFERNO"}'''
    ######################################################################
    ######################### CARTAS #####################################
    ######################################################################
    if m == "cartas":

        
        for i in range(len(r)):
            if r[i] in respostas:
                resposta_certa = r[i]
                print(type(resposta_certa))
                print(f"Resposta:Certa: {resposta_certa}")

            if r[i] not in respostas:
                resposta_errada = r[i]
                print(f"Resposta Errada:{resposta_errada}")
                pass
                print(f"Aleatorio {al}")
                if al == 1:
                    if str(res_2['text']) == str(resposta_errada):
                        res_2['bg'] = Cores.preto
                        res_2['fg'] = Cores.preto
                    if str(res_3['text']) == str(resposta_errada):
                        res_3['bg'] = Cores.preto
                        res_3['fg'] = Cores.preto
                    if str(res_4['text']) == str(resposta_errada):
                        res_4['bg'] = Cores.preto
                        res_4['fg'] = Cores.preto
                    if str(res_4['text']) == str(resposta_errada):
                        res_4['bg'] = Cores.preto
                        res_4['fg'] = Cores.preto
                
                if al == 2:
                    if str(res_2['text']) == str(resposta_errada):
                        res_2['bg'] = Cores.preto
                        res_2['fg'] = Cores.preto
                    if str(res_3['text']) == str(resposta_errada):
                        res_3['bg'] = Cores.preto
                        res_3['fg'] = Cores.preto
                    if str(res_4['text']) == str(resposta_errada):
                        res_4['bg'] = Cores.preto
                        res_4['fg'] = Cores.preto
                    if str(res_4['text']) == str(resposta_errada):
                        res_4['bg'] = Cores.preto
                        res_4['fg'] = Cores.preto

                if al == 3:
                    if str(res_2['text']) == str(resposta_errada):
                        res_2['bg'] = Cores.preto
                        res_2['fg'] = Cores.preto
                    if str(res_3['text']) == str(resposta_errada):
                        res_3['bg'] = Cores.preto
                        res_3['fg'] = Cores.preto
                        
                    if str(res_4['text']) == str(resposta_errada):
                        res_4['bg'] = Cores.preto
                        res_4['fg'] = Cores.preto
                    if str(res_4['text']) == str(resposta_errada):
                        res_4['bg'] = Cores.preto
                        res_4['fg'] = Cores.preto
                
        num_cartas -= 1
        if active_cartas == True and num_cartas <= 0:
            #lb_cartas.destroy()
            lb_cartas.configure(text="Sem cartas")
        else:
            lb_cartas.configure(text=f"Cartas: {num_cartas}")
            pass
    ############ FIM CARTAS    
        

           
           
            
            
            
    
    if m in respostas:
        

        print(m)
        acertos += 1
        tempo_pergunta = secs
        pontos = tempo_pergunta * 10 + pontos
        secs = 60
        print (f"Numero de Acertos: {acertos}")
        pygame.mixer.music.load("/sons/certaresposta.mp3")
        pygame.mixer.music.play()
        iniciar.janela.after(9000)
        destroir()
        pygame.mixer.music.stop()
        aleatorio()
    else:
        pass


  
        
    if m == "certa":
        #cone_certo = Label(iniciar.janela,text="Certo")
        #icone_certo.place(x=0,y=0)
        pygame.mixer.music.load("/sons/certaresposta.mp3")
        pygame.mixer.music.play()
        iniciar.janela.after(9000)
        destroir()
        pygame.mixer.music.stop()
        aleatorio()
    if m == "certa2":
        pygame.mixer.music.load("/sons/certaresposta.mp3")
        pygame.mixer.music.play()
        iniciar.janela.after(9000)
        destroir()
        aleatorio()
    return m
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

######################################################################
######################### PERGUNTAS ##################################
######################################################################
def Perguntas(som,img,r1,r2,r3,r4):
    global lb_creditos
    global creditos_img
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

    
    fundo_jogo = PhotoImage(file="/img/a.png")
    frame_right=Label(iniciar.janela,width=1024,height=680, image=fundo_jogo)
    frame_right.place(x=0,y=0)

    
   
    Botoes_De_Tela()
    
    font_perguntas = "Arial 25 bold"
    font_respostas = "SERIF 10 bold"
    iniciar.janela['bg'] = "#FF0000"
    pygame.mixer.init()
    pygame.mixer.music.load(f"/sons/{som}.mp3")
    pygame.mixer.music.play()

    #pygame.mixer.music.load(f"/sons/Somsuspense.mp3")
    #pygame.mixer.music.play()
    
    frame_p1=Frame(iniciar.janela,width=660,height=150)
    frame_p1.place(x=50,y=148)
    
    fundo_pergunta2 = PhotoImage(file=f"/img/imgs_perguntas/{img}.png")
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
    global lb_cartas
    global active_cartas
    global num_cartas
    global cartas_img
    res_1.bind("<Button-1>",lambda m=f"{r1}": resposta1(r1,res_1,""))
    res_2.bind("<Button-1>",lambda m=f"{r2}": resposta1(r2,res_2,""))
    res_3.bind("<Button-1>",lambda m=f"{r3}": resposta1(r3,res_3,""))
    res_4.bind("<Button-1>",lambda m=f"{r4}": resposta1(r4,res_4,""))
    jj = [r1,r2,r3,r4]
    hh = [res_1,res_2,res_3,res_4]
    cartas_img = PhotoImage(file="/img/cartas.png")
    cartas_img2 = Label(iniciar.janela,image=cartas_img,width=150,height=119,border=0)
    
    lb_cartas = Label(iniciar.janela,text=f"Cartas {num_cartas}",width=17,bg=Cores.branco,font="SERIF")
    print(active_cartas)
    if active_cartas == True:
        lb_cartas.place(x=870,y=419)
        cartas_img2.place(x=870,y=280)
    if num_cartas > 0:
        lb_cartas.bind("<Button-1>",lambda m="Cartas":resposta1("cartas",jj,img,res_1,res_2,res_3,res_4))
        cartas_img2.bind("<Button-1>",lambda m="Cartas":resposta1("cartas",jj,img,res_1,res_2,res_3,res_4))

    else: lb_cartas.configure(text="Sem Cartas")
    
    
    

    ################MUDANDO BG DAS LABEL
    res_1.bind("<Enter>",lambda m=f"{r1}": Btn_cor1(res_1))
    res_2.bind("<Enter>",lambda m=f"{r2}": Btn_cor1(res_2))
    res_3.bind("<Enter>",lambda m=f"{r3}": Btn_cor1(res_3))
    res_4.bind("<Enter>",lambda m=f"{r4}": Btn_cor1(res_4))
    
    res_1.bind("<Leave>",lambda m=f"{r1}": Btn_cor2(res_1))
    res_2.bind("<Leave>",lambda m=f"{r2}": Btn_cor2(res_2))
    res_3.bind("<Leave>",lambda m=f"{r3}": Btn_cor2(res_3))
    res_4.bind("<Leave>",lambda m=f"{r4}": Btn_cor2(res_4))
   
    

def cartas():
    teste=res_1
    global respostas
    print(teste)
    
      
    pass


def Tela_Inicial(event):
    global n_pulos
    global secs
    global texto_iniciar
    global texto_opcoes
    global texto_sair
    global fundo
    global lb_fundo
    global result
    global pontos
    global num_cartas
    global active_cartas
    global creditos
    num_cartas = 10
    active_cartas = True
    pontos = 0
    secs = 60
    result = []
    n_pulos = 100
    global Tempo
    Tempo = False
    fundo = PhotoImage(file="/img/fundo.png",width=iniciar.width,height=iniciar.height)
    
    lb_fundo = Label(iniciar.janela,image=fundo,width=iniciar.width,height=iniciar.height)
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

    creditos = Button(iniciar.janela,
    highlightthickness = 0, 
    bd = 0,
    text="Creditos",
    font=f"Arial {tamanho_fonte} bold",
    fg=Cores.branco,
    bg=Cores.fundo,
    activebackground=Cores.verde,
    activeforeground=Cores.branco,
    highlightcolor=Cores.vermelho,
    width=10,
    command=dfcreditos
    )
    creditos.place(x=posx,y=520)

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
    texto_sair.place(x=posx,y=580)

    
tempo()
#iniciar.teste.pack()

def musica_titulo():
    
    pygame.mixer.init()
    pygame.mixer.music.load("/sons/intro.mp3")

    pygame.mixer.music.play()
    pass

def fechamento():
    iniciar.janela.mainloop()

