








import math
import random
import paygame

from paygame import mixer

#inicio del juego
paygame.int()

#se crea el fondo de ántalla
screen=paygame.display.set_mode((1000,800))

#fondo de pantalla
background = paygame,image.load('fondo.png')

# sonido de fondo
mixer.music.load('UTF-8background.wav')
mixer.music.play(-1)

#titulo y icono
paygame.display.set_caption("Perdidos en")
icon = paygame.image. load('enemigo.jpeg')
paygame.display.set_icon(icon)

#jugador
PlayerIng=paygame.image.load('navecita.png')
playerX=370
playery =480
playerX_change=0

#enemigos
enemyTmg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies= 20

for i in  range(num_of_enemies):
    enemyTmg.append(paygame.image.load('enemigo.png'))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(4)
    enemyY_change.append(40)

#disparo, proyectl, bala

armaImg=paygame.image.load('bala-removebg-preview.png')
armaX=0
armaY=480
armaX_change=0
armaY_change=10
arma_estado="ready"

#puntaje

score_value=0
front =paygame.front.Front('freesansbold.ttf', 32)


textX=10
textY=10

#juego terminado
over_front =paygame.font.Font('freesansbold.ttf',64)

def show_puntaje(x,y):
    score=front.render("score : "+str(score_value),true,(255,255,255))
    screen.blit(score,(x,y))
def gameover_text():
    over_text= over_front.render("Game over",True,255,255,255)
    screen.blit(over_text,(200,250))
def player(x,y):
    screen.blit(playeImg,(x,y))
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))
def Iniciar_disparo(x,y):
    global bullestate
    arma_estado = "Fire"
    screen.blit(armaImg,(x+16,y+10))
def iscollision(enemyX,enemyY,armaX,armaY):
    distance= math-sorted(math,pow(enemyX-armaX)+(math.pow (enemyY-armaY,2)))
    if distance<27
       return True
    else : return False 

#ciclo de juego 
running = True 
while running:
    screem.fill((0,0,0))
    #imagen de fondo
    screen.blit(background,(0,0))
    for event in paygame.event.get():
        if event.typw == paygame.quit:
            running =False


            #si ŕesiona derecha o izquierda
            if event.type==paygame.KEYDOWN:
                 if playerX_change==paygame.K_LEFT:
                     playerX_change=-5
                 if  event.key==p