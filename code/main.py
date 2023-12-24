import pygame
import random
import time
import sys

pygame.init()

size=20
score=0
snake_pos=[100,60]
snake_body=[[100,60],[80,60],[60,60]]
food_x=random.randrange(0,84)
food_y=random.randrange(1,60)
if food_x%2!=0: food_x+=1
if food_y%2!=0: food_y+=1
food_pos=[food_x*10,food_y*10]
f=True
direction='RIGHT'
change=direction

screen=pygame.display.set_mode((860,620))
pygame.display.set_caption('Nht_Alva')

Head=pygame.transform.scale(pygame.image.load('graphic/Snake.jpg'),(size,size)).convert()
Body=pygame.transform.scale(pygame.image.load('graphic/Snake.jpg'),(size,size)).convert()
Food=pygame.transform.scale(pygame.image.load('graphic/Food.jpg'),(size,size)).convert()
game_font1=pygame.font.Font('font/04B_19.ttf',20)
game_font2=pygame.font.Font('font/Chomixi3D-Regular.ttf',50)
game_font3=pygame.font.Font('font/Chomixi3D-Regular.ttf',80)

Black=pygame.Color(0,0,0)
Red=pygame.Color(255,0,0)
Lime=pygame.Color(0,255,0)
White=pygame.Color(255,255,255)

def show_score(c=1):	
    surf1=game_font1.render('Score: {0}'.format(score),True,White)
    srect1=surf1.get_rect()
    surf2=game_font2.render('Score: {0}'.format(score),True,White)
    srect2=surf2.get_rect()
    if c==1:
        srect1.midtop=(50,10)
        screen.blit(surf1,srect1)
    else:
        srect2.midtop=(430,310)
        screen.blit(surf2,srect2)

def game_over():
    gsurf=game_font3.render('GAME OVER!',True,Red)
    grect=gsurf.get_rect()
    grect.midtop=(440,230)
    screen.blit(gsurf,grect)
    show_score(0)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()

while True:

    pygame.time.delay(80)
    screen.fill(Black)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                change='RIGHT'
            if event.key==pygame.K_LEFT:
                change='LEFT'
            if event.key==pygame.K_UP:
                change='UP'
            if event.key==pygame.K_DOWN:
                change='DOWN'
            if event.key==pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    if change=='RIGHT' and not direction=='LEFT':
        direction='RIGHT'
    if change=='LEFT' and not direction=='RIGHT':
        direction='LEFT'
    if change=='DOWN' and not direction=='UP':
        direction='DOWN'
    if change=='UP' and not direction=='DOWN':
        direction='UP'

    if direction=='RIGHT':
        snake_pos[0]+=size
    if direction=='LEFT':
        snake_pos[0]-=size
    if direction=='UP':
        snake_pos[1]-=size
    if direction=='DOWN':
        snake_pos[1]+=size
    
    snake_body.insert(0,list(snake_pos))

    if snake_pos[0]==food_pos[0] and snake_pos[1]==food_pos[1]:
        score+=1
        f=False
    else:
        snake_body.pop()

    if f==False:
        food_x=random.randrange(1,71)
        food_y=random.randrange(1,45)
        if food_x%2!=0: food_x+=1
        if food_y%2!=0: food_y+=1
        food_pos=[food_x*10,food_y*10]
        f=True

    for p in snake_body:
        screen.blit(Body,pygame.Rect(p[0], p[1], size, size))
        screen.blit(Head,pygame.Rect(snake_body[0][0], snake_body[0][1], size, size))
        screen.blit(Food,pygame.Rect(food_pos[0], food_pos[1], size, size))

    if snake_pos[0] > 850 or snake_pos[1] < 0:
        game_over()
    if snake_pos[1] > 610 or snake_pos[0] < 0:
        game_over()

    for i in snake_body[1:]:
        if snake_pos[0]==i[0] and snake_pos[1]==i[1]:
            game_over()
    
    show_score()

    pygame.display.flip()
