from curses import KEY_PREVIOUS
from typing_extensions import Self
from pygame.locals import *
import pygame
import os
import time
from sys import exit
from random import randint

pygame.init()
font  = pygame.font.SysFont('arial',30,True,True)
q_posx = 400
q_posy = 250
velocidade = 5
angle = randint(1,5)
playerx = 0
playery = 0
pontos = 0
r = False
r2 = False
class config():
    def __init__(self):
        self.width = 500
        self.height = 500
        self.janela = pygame.display.set_mode((self.width,self.height))
        self.relogio = pygame.time.Clock()
        
iniciar = config() 

    
def quadrado():
    global q_posx
    global q_posy
   
    return q_posx, q_posy
def bola_move():    
    global r
    global r2
    global q_posx
    global q_posy
    global angle
    global velocidade
    global pontos
    bola = pygame.draw.rect(iniciar.janela,(255,0,0),(q_posx,q_posy,20,20))
    player = pygame.draw.rect(iniciar.janela,(0,255,0),(playerx,playery,10,70))
    
    if player.colliderect(bola):   
        pygame.mixer.init()
        pygame.mixer.music.load("/home/brunodlucas/Música/01.mp3")
        pygame.mixer.music.play()
        angle = randint(-3,5) 
        q_posx =q_posx+10
        pontos +=1 
        print ("Ponto")
        print(angle)
        velocidade = velocidade + 0.1
    if q_posx <= iniciar.width - iniciar.width:
        print("Errou")
        q_posx = 400
        q_posy = 250
        pontos = pontos - 1
    if q_posx < iniciar.width and r  == False:
        q_posx += velocidade 
    else:
        r = True
        if not player.colliderect(bola):
            
            q_posx -= velocidade
            if q_posx <= iniciar.width-iniciar.width:
                r = False
        else:
            r = False
    
    if q_posy < iniciar.height and r2 == False:
        q_posy += velocidade + angle
    else:
        r2 = True
        if not player.colliderect(bola):
            
            q_posy -= velocidade
            if q_posy < 50:
                r2 = False
        else:
            r2 = False
   
iniciar

while True:
    iniciar.relogio.tick(30)
    iniciar.janela.fill((0,0,0))
    msg = f"PONTOS:{pontos}"
    txt_points = font.render(msg,True,(255,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit
            exit()
    
    
    if pygame.key.get_pressed()[K_DOWN]:
        playery += 15    
    if pygame.key.get_pressed()[K_UP]:
        playery -= 15
        
    pygame.draw.rect(iniciar.janela,(255,255,255),(0,0,500,50))
    iniciar.janela.blit(txt_points,(190,20))    
    quadrado()
    bola_move()    
    pygame.display.update()
    
