import pygame
from math import *
import random
import time
import sys,os
from pygame.locals import*
clock=pygame.time.Clock()

zeit=100
SCREEN=(1800,1600)
pygame.init()
white=(255,255,255)
blue=(122,122,122)
#Colors
display_width=800
display_height=600
StageColor=(200,200,200)
StartColor=(100,100,100)
red=(255,0,0)
gameDisplay=pygame.display.set_mode((display_width,display_height))
player1goal=0
player2goal=0
gameDisplay.fill(StartColor)
black=(0,0,0)
rosa=(40,33,199)
gruen=(222,111,55)

class Ball:
    def __init__(self):
        self.position=[(int(display_width/3),int(display_height/2))]
        self.rotation=0.0
        self.mass=3
        self.speed=[0.0,10]
        self.maxSpeed=5
        self.being_hit=0
        self.color=red
        self.size=10
        self.decel=0.991

b1=Ball()
class Player:
    def __init__(self):
        self.position=[(int(display_width/2),int(display_height/2))]
        self.rotation=0.0
        self.mass=40
        self.speed=[0.0,0.0]
        self.maxSpeed=3.7
        self.accel=0.5
        self.decel=0.99
        self.being_hit=0
        self.color=blue
        self.size=20
        
p1=Player()
p2=Player()

def DrawPlayers():
    global p1,p2
    p1.position=[int(display_width/3),int(display_height/2)]
    p2.position=[int(display_width/2+100),int(display_height/2)]
    b1.position=[int(display_width/2),int(display_height/2)]
    
    
    

def GetInput():
    global p1,p2
    key=pygame.key.get_pressed()
    for event in pygame.event.get():
        

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_q:
                    pygame.quit()
      
        if key[K_LEFT] and p1.speed[0] > p1.maxSpeed*-1:  p1.speed[0] -= p1.accel
        if key[K_RIGHT]  and p1.speed[0] < p1.maxSpeed: p1.speed[0] += p1.accel
        if key[K_UP]  and p1.speed[1] < p1.maxSpeed: p1.speed[1] -= p1.accel
        if key[K_DOWN]  and p1.speed[1] > p1.maxSpeed*-1: p1.speed[1] += p1.accel
        if key[K_a] and p2.speed[0] > p1.maxSpeed*-1:  p2.speed[0] -= p1.accel
        if key[K_d] and p2.speed[0] < p1.maxSpeed*1:  p2.speed[0]+= p1.accel
        if key[K_w] and p2.speed[1] < p1.maxSpeed*1:  p2.speed[1] -= p1.accel
        if key[K_s] and p2.speed[1] > p1.maxSpeed*-1:  p2.speed[1] += p1.accel
        
        

        
   
                
                

                
def Move():
    global player1goal,player2goal
    a=-1.5
    b1.position[0]+=b1.speed[0]
    b1.position[1]+=b1.speed[1]
    p1.position[0]  += p1.speed[0]
    p1.position[1] += p1.speed[1]
    p2.position[0] += p2.speed[0]
    p2.position[1] += p2.speed[1]
    p1.speed[0]*=p1.decel
    p1.speed[1]*=p1.decel
    p2.speed[0]*=p1.decel
    p2.speed[1]*=p1.decel
    b1.speed[0]*=b1.decel
    b1.speed[1]*=b1.decel
   
    
    if abs (p1.speed[0])<0.1:
                p1.speed[0]=0
    if abs (p1.speed[1])<0.1:
                p1.speed[1]=0
    if abs (p2.speed[0])<0.1:
                p2.speed[0]=0
    if abs (p2.speed[1])<0.1:
                p2.speed[1]=0
    if p1.speed[0]>=p1.maxSpeed:
        p1.speed[0]=1.7
    if p1.speed[1]>=p1.maxSpeed:
        p1.speed[1]=1.7
    if p2.speed[0]>=p1.maxSpeed:
        p2.speed[0]=1.7
    if p2.speed[1]>=p1.maxSpeed:
        p2.speed[1]=1.7

    if b1.speed[0]>=b1.maxSpeed:
        b1.speed[0]=5
    if b1.speed[1]>=b1.maxSpeed:
        b1.speed[1]=5
    pygame.draw.rect(gameDisplay,white,(145,250,5,100))
    pygame.draw.rect(gameDisplay,white,(650,250,5,100))
    if p1.position[0]<168 or p1.position[0]>632:
        p1.speed[0]*=a
    if p1.position[1]<168 or p1.position[1]>432:
        p1.speed[1]*=a
    if p2.position[0]<168 or p2.position[0]>632:
        p2.speed[0]*=a
    if p2.position[1]<168 or p2.position[1]>432:
        p2.speed[1]*=a
    if b1.position[0]<160 or b1.position[0]>640:
        b1.speed[0]*=a
        if 160<b1.position[0] and 250<b1.position[1]<350:
            player1goal+=1
           
        if 640>b1.position[0] and 250<b1.position[1]<350:
            player2goal+=1
          
            
    if b1.position[1]<160 or b1.position[1]>440:
        b1.speed[1]*=a

    if b1.position[0]<100 or b1.position[0]>1000 or b1.position[1]<20 or b1.position[1]>900:
        b1.position[0]=300
        b1.position[1]=300

        
    
    distanceplayers = calcDistance(p1, p2)
    distanceplayer1ball= calcDistance(p1,b1)
    distanceplayer2ball=calcDistance(p2,b1)
    if p1.being_hit==0 and b1.being_hit==0 and distanceplayer1ball < (p1.size+b1.size-0.5):
        p1.being_hit=1
        b1.being_hit=1
        calcOrientation(p1)
        calcOrientation(b1)
        distance=calcDistance(p1,b1)
        while distanceplayer1ball < p1.size+b1.size:
                
                if p1.position[0]!=b1.position[0]:
                    b1.position[0]+=.1*(b1.position[0]-p1.position[0])/abs(p1.position[0]-b1.position[0])*abs(b1.position[0]-p1.position[0])/(abs(b1.position[1]-p1.position[1])+1)
                    p1.position[0]-=.1*(b1.position[0]-p1.position[0])/abs(p1.position[0]-b1.position[0])*abs(b1.position[0]-p1.position[0])/(abs(b1.position[1]-p1.position[1])+1)
                if p1.position[1]!=b1.position[1]:
                    b1.position[1]+=.1*(b1.position[1]-p1.position[1])/abs(p1.position[1]-b1.position[1])
                    p1.position[1]-=.1*(b1.position[1]-p1.position[1])/abs(p1.position[1]-b1.position[1])
                distanceplayer1ball=calcDistance(p1,b1)
        
        calcFinalSpeeds(p1,b1)
    if p2.being_hit==0 and b1.being_hit==0 and distanceplayer2ball < (p2.size+b1.size-0.5):
        p2.being_hit=1
        b1.being_hit=1
        calcOrientation(p2)
        calcOrientation(b1)
        distance=calcDistance(p2,b1)
        while distanceplayer2ball < p2.size+b1.size:
                
                if p2.position[0]!=b1.position[0]:
                    b1.position[0]+=.1*(b1.position[0]-p2.position[0])/abs(p2.position[0]-b1.position[0])*abs(b1.position[0]-p2.position[0])/(abs(b1.position[1]-p2.position[1])+1)
                    p2.position[0]-=.1*(b1.position[0]-p2.position[0])/abs(p2.position[0]-b1.position[0])*abs(b1.position[0]-p2.position[0])/(abs(b1.position[1]-p2.position[1])+1)
                if p2.position[1]!=b1.position[1]:
                    b1.position[1]+=.1*(b1.position[1]-p2.position[1])/abs(p2.position[1]-b1.position[1])
                    p2.position[1]-=.1*(b1.position[1]-p2.position[1])/abs(p2.position[1]-b1.position[1])
                distanceplayer2ball=calcDistance(p2,b1)
        
        calcFinalSpeeds(p2,b1)
        
    if p1.being_hit==0 and p2.being_hit==0 and distanceplayers < (p1.size+p2.size-1):
        p1.being_hit=1
        p2.being_hit=1
        calcOrientation(p1)
        calcOrientation(p2)
        distanceplayers=calcDistance(p1,p2)
        while distanceplayers < p1.size+p2.size:
                
                if p1.position[0]!=p2.position[0]:
                    p2.position[0]+=.1*(p2.position[0]-p1.position[0])/abs(p1.position[0]-p2.position[0])*abs(p2.position[0]-p1.position[0])/(abs(p2.position[1]-p1.position[1])+1)
                    p1.position[0]-=.1*(p2.position[0]-p1.position[0])/abs(p1.position[0]-p2.position[0])*abs(p2.position[0]-p1.position[0])/(abs(p2.position[1]-p1.position[1])+1)
                if p1.position[1]!=p2.position[1]:
                    p2.position[1]+=.1*(p2.position[1]-p1.position[1])/abs(p1.position[1]-p2.position[1])
                    p1.position[1]-=.1*(p2.position[1]-p1.position[1])/abs(p1.position[1]-p2.position[1])
                distanceplayers=calcDistance(p1,p2)
        
        calcFinalSpeeds(p1,p2)

def player1g(goals):
    font= pygame.font.SysFont('comicsansms',20)
    text=font.render('goals:'+str(goals),True,black)
    gameDisplay.blit(text,(175,155))
def player2g(goals):
    font= pygame.font.SysFont('comicsansms',20)
    text=font.render('goals:'+str(goals),True,black)
    gameDisplay.blit(text,(560,155))
    
def Positionplayer():
    
    pygame.draw.circle(gameDisplay,rosa,[int(p1.position[0]),int(p1.position[1])],20)
    pygame.draw.circle(gameDisplay,blue,[int(p2.position[0]),int(p2.position[1])],20)
    pygame.draw.circle(gameDisplay,b1.color,[int(b1.position[0]),int(b1.position[1])],10)
   
def Drawball(x,y):
    pygame.draw.circle(gameDisplay,white,(x,y),10)
def DrawObjects(x,y):
        
        x_change=0
        x-=x_change
        pygame.draw.circle(gameDisplay,blue,(x,y),40)
    

def calcDistance(ball1, ball2):
    return sqrt(abs(ball1.position[0]-ball2.position[0])*abs(ball1.position[0]-ball2.position[0])+abs(ball1.position[1]-ball2.position[1])*abs(ball1.position[1]-ball2.position[1]))

def calcOrientation(ball):
    ball.rotation=atan2(ball.speed[1],ball.speed[0])


def calcFinalSpeeds(ball1, ball2):
    mass1 = ball1.mass
    mass2 = ball2.mass
    phi = atan2(-(ball1.position[1]-ball2.position[1]),(ball1.position[0]-ball2.position[0]))
    theta1 = ball1.rotation
    theta2 = ball2.rotation
    v1i = sqrt(ball1.speed[0]*ball1.speed[0]+ball1.speed[1]*ball1.speed[1])
    v2i = sqrt(ball2.speed[0]*ball2.speed[0]+ball2.speed[1]*ball2.speed[1])
    ball1.speed[0] = ((v1i*cos(theta1-phi)*(mass1-mass2)+2*mass2*v2i*cos(theta2-phi))*cos(phi)/(mass1+mass2)+v1i*sin(theta1-phi)*cos(phi+pi/2))
    ball1.speed[1] = ((v1i*cos(theta1-phi)*(mass1-mass2)+2*mass2*v2i*cos(theta2-phi))*sin(phi)/(mass1+mass2)+v1i*sin(theta1-phi)*sin(phi+pi/2))
    ball2.speed[0] = (v2i*cos(theta2-phi)*(mass2-mass1)+2*mass1*v1i*cos(theta1-phi))*cos(phi)/(mass1+mass2)+v2i*sin(theta2-phi)*cos(phi+pi/2)
    ball2.speed[1] = ((v2i*cos(theta2-phi)*(mass2-mass1)+2*mass1*v1i*cos(theta1-phi))*sin(phi)/(mass1+mass2)+v2i*sin(theta2-phi)*sin(phi+pi/2))
    ball1.being_hit=0
    ball2.being_hit=0

def gameloop():
    
    x_change=0
    y_change=0
    x=200
    y=200
    a=400
    b=200
    a_change=0
    b_change=0
    c=300
    d=200 

    x-=x_change
    y+=y_change
    a-=a_change
    b+=b_change
    gameDisplay.fill(StartColor)
        
   
       
    DrawPlayers()
    while True:
        global player1goal,player2goal
        gameDisplay.fill(StartColor)
        pygame.draw.rect(gameDisplay,StageColor,(150,150,500,300))
        pygame.draw.rect(gameDisplay,white,(145,250,5,100))
        pygame.draw.rect(gameDisplay,white,(650,250,5,100))
        player1g(player1goal)
        player2g(player2goal)
        
        GetInput()
        if 1==1:
            Move()
        
            Positionplayer()
            pygame.time.wait
        pygame.display.flip()
        clock.tick(zeit)

if __name__=="__main__":
    gameloop()
