import pygame, time, random

pygame.init()

color1=[[0,255,0],[0,255,255],[255,0,255],[124,252,0],
       [107,142,35],[0,128,0],[144,238,144],[135,206,235],
       [30,144,255],[173,216,230],[65,105,225],[138,43,226],
       [147,112,219],[186,85,211],[128,0,128],[216,191,216],
       [221,160,221],[255,182,193],[210,105,30],[188,143,143],
       [112,128,144],[176,196,222],[192,192,192],[64,224,208],
       [72,61,139],[128,128,0],[189,183,107],[255,140,0],
       [165,42,42],[205,92,92],[255,215,0],[127,255,212]]
color2=[[0,191,255],[0,255,0],[221,160,221],[105,105,105],[255,105,180]]
color3=[[0,0,0],[255,255,255],[255,0,0]]

screen=pygame.display.set_mode((300,345))
pygame.display.set_caption('Snake Game')

clock=pygame.time.Clock()

def draw_snake(size):
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(6*size,2*size,7*size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(5*size,3*size,size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(13*size,3*size,size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(4*size,4*size,11*size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(4*size,5*size,11*size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(4*size,6*size,12*size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(5*size,7*size,11*size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(6*size,8*size,10*size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(9*size,9*size,7*size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(9*size,10*size,6*size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(8*size,11*size,7*size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(8*size,12*size,6*size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(7*size,13*size,7*size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(6*size,14*size,7*size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(26*size,14*size,size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(6*size,15*size,6*size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(13*size,15*size,8*size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(25*size,15*size,3*size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(5*size,16*size,17*size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(25*size,16*size,3*size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(5*size,17*size,18*size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(25*size,17*size,3*size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(5*size,18*size,19*size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(25*size,18*size,3*size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(4*size,19*size,24*size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(3*size,20*size,24*size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(2*size,21*size,25*size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(2*size,22*size,25*size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(2*size,23*size,25*size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(2*size,24*size,25*size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(3*size,25*size,23*size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(3*size,26*size,23*size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(4*size,27*size,21*size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(5*size,28*size,19*size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(7*size,29*size,15*size,size))

    pygame.draw.rect(screen,(154,205,50),pygame.Rect(12*size,7*size,size,3*size))
    pygame.draw.rect(screen,(154,205,50),pygame.Rect(11*size,8*size,size,3*size))
    pygame.draw.rect(screen,(154,205,50),pygame.Rect(10*size,9*size,size,15*size))
    pygame.draw.rect(screen,(154,205,50),pygame.Rect(9*size,11*size,size,13*size))
    pygame.draw.rect(screen,(154,205,50),pygame.Rect(8*size,13*size,size,10*size))
    pygame.draw.rect(screen,(154,205,50),pygame.Rect(7*size,14*size,size,8*size))
    pygame.draw.rect(screen,(154,205,50),pygame.Rect(6*size,16*size,size,4*size))
    pygame.draw.rect(screen,(154,205,50),pygame.Rect(13*size,19*size,5*size,size))
    pygame.draw.rect(screen,(154,205,50),pygame.Rect(11*size,23*size,11*size,size))
    pygame.draw.rect(screen,(154,205,50),pygame.Rect(11*size,24*size,9*size,size))
    pygame.draw.rect(screen,(154,205,50),pygame.Rect(3*size,24*size,size,size))
    pygame.draw.rect(screen,(154,205,50),pygame.Rect(25*size,24*size,size,size))
    pygame.draw.rect(screen,(154,205,50),pygame.Rect(4*size,26*size,size,size))
    pygame.draw.rect(screen,(154,205,50),pygame.Rect(24*size,26*size,size,size))
    pygame.draw.rect(screen,(154,205,50),pygame.Rect(5*size,27*size,2*size,size))
    pygame.draw.rect(screen,(154,205,50),pygame.Rect(22*size,27*size,2*size,size))
    pygame.draw.rect(screen,(154,205,50),pygame.Rect(7*size,28*size,15*size,size))

    pygame.draw.rect(screen,(32,178,170),pygame.Rect(6*size,3*size,7*size,size))
    pygame.draw.rect(screen,(32,178,170),pygame.Rect(5*size,4*size,9*size,size))
    pygame.draw.rect(screen,(32,178,170),pygame.Rect(14*size,6*size,size,size))
    pygame.draw.rect(screen,(32,178,170),pygame.Rect(14*size,7*size,size,size))
    pygame.draw.rect(screen,(32,178,170),pygame.Rect(14*size,8*size,size,2*size))
    pygame.draw.rect(screen,(32,178,170),pygame.Rect(13*size,11*size,size,size))
    pygame.draw.rect(screen,(32,178,170),pygame.Rect(12*size,10*size,size,4*size))
    pygame.draw.rect(screen,(32,178,170),pygame.Rect(11*size,11*size,size,4*size))
    pygame.draw.rect(screen,(32,178,170),pygame.Rect(10*size,13*size,size,9*size))
    pygame.draw.rect(screen,(32,178,170),pygame.Rect(13*size,16*size,8*size,size))
    pygame.draw.rect(screen,(32,178,170),pygame.Rect(12*size,17*size,10*size,size))
    pygame.draw.rect(screen,(32,178,170),pygame.Rect(22*size,18*size,size,size))
    pygame.draw.rect(screen,(32,178,170),pygame.Rect(13*size,21*size,5*size,size))
    pygame.draw.rect(screen,(32,178,170),pygame.Rect(12*size,20*size,size,size))
    pygame.draw.rect(screen,(32,178,170),pygame.Rect(11*size,19*size,size,size))
    pygame.draw.rect(screen,(32,178,170),pygame.Rect(11*size,26*size,9*size,size))
    pygame.draw.rect(screen,(32,178,170),pygame.Rect(9*size,25*size,2*size,size))
    pygame.draw.rect(screen,(32,178,170),pygame.Rect(20*size,25*size,2*size,size))
    pygame.draw.rect(screen,(32,178,170),pygame.Rect(8*size,24*size,size,size))
    pygame.draw.rect(screen,(32,178,170),pygame.Rect(22*size,24*size,size,size))
    pygame.draw.rect(screen,(32,178,170),pygame.Rect(7*size,23*size,size,size))
    pygame.draw.rect(screen,(32,178,170),pygame.Rect(19*size,23*size,size,size))
    pygame.draw.rect(screen,(32,178,170),pygame.Rect(6*size,22*size,size,size))
    pygame.draw.rect(screen,(32,178,170),pygame.Rect(5*size,21*size,size,size))
    pygame.draw.rect(screen,(32,178,170),pygame.Rect(24*size,20*size,size,3*size))
    pygame.draw.rect(screen,(32,178,170),pygame.Rect(25*size,19*size,size,size))
    pygame.draw.rect(screen,(32,178,170),pygame.Rect(26*size,15*size,size,5*size))

    pygame.draw.rect(screen,(0,128,128),pygame.Rect(6*size,4*size,size,size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(8*size,4*size,size,size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(10*size,4*size,size,size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(12*size,4*size,size,size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(5*size,5*size,size,size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(7*size,5*size,3*size,size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(11*size,5*size,size,size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(13*size,5*size,size,size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(5*size,6*size,7*size,size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(13*size,6*size,size,size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(6*size,7*size,5*size,size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(13*size,7*size,size,size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(6*size,7*size,5*size,size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(13*size,7*size,size,size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(13*size,8*size,size,3*size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(12*size,17*size,9*size,size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(12*size,18*size,5*size,size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(18*size,18*size,4*size,size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(19*size,19*size,4*size,size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(19*size,20*size,4*size,size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(18*size,21*size,5*size,size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(11*size,22*size,12*size,size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(12*size,23*size,8*size,size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(11*size,20*size,size,2*size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(12*size,21*size,size,size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(11*size,20*size,size,3*size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(7*size,27*size,15*size,size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(12*size,10*size,size,3*size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(11*size,11*size,size,3*size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(10*size,13*size,size,2*size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(10*size,19*size,size,3*size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(9*size,14*size,size,7*size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(8*size,16*size,size,4*size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(4*size,20*size,2*size,size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(3*size,21*size,2*size,size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(3*size,22*size,3*size,size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(3*size,23*size,4*size,size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(4*size,24*size,4*size,size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(4*size,25*size,5*size,size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(5*size,26*size,6*size,size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(20*size,26*size,4*size,size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(22*size,25*size,3*size,size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(23*size,24*size,2*size,size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(24*size,23*size,2*size,size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(25*size,20*size,size,3*size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(26*size,18*size,size,2*size))
    pygame.draw.rect(screen,(0,128,128),pygame.Rect(26*size,16*size,size,size))

    pygame.draw.rect(screen,(255,20,147),pygame.Rect(8*size,8*size,size,2*size))

def draw_food(size):
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(45*size,12*size,3*size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(42*size,13*size,size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(44*size,13*size,6*size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(43*size,14*size,8*size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(39*size,15*size,3*size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(43*size,15*size,7*size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(38*size,16*size,11*size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(37*size,17*size,13*size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(36*size,18*size,15*size,5*size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(37*size,23*size,13*size,2*size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(38*size,25*size,11*size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(39*size,26*size,9*size,size))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(41*size,27*size,5*size,size))

    pygame.draw.rect(screen,(60,179,113),pygame.Rect(45*size,13*size,3*size,size))
    pygame.draw.rect(screen,(60,179,113),pygame.Rect(44*size,14*size,6*size,size))

    pygame.draw.rect(screen,(46,139,87),pygame.Rect(44*size,14*size,5*size,size))

    pygame.draw.rect(screen,(255,0,0),pygame.Rect(39*size,16*size,3*size,size))
    pygame.draw.rect(screen,(255,0,0),pygame.Rect(38*size,17*size,11*size,size))
    pygame.draw.rect(screen,(255,0,0),pygame.Rect(37*size,18*size,13*size,5*size))
    pygame.draw.rect(screen,(255,0,0),pygame.Rect(38*size,23*size,11*size,2*size))
    pygame.draw.rect(screen,(255,0,0),pygame.Rect(39*size,25*size,9*size,size))

    pygame.draw.rect(screen,(255,255,255),pygame.Rect(38*size,19*size,size,size))
    pygame.draw.rect(screen,(255,255,255),pygame.Rect(39*size,18*size,size,size))

    pygame.draw.rect(screen,(178,34,34),pygame.Rect(41*size,16*size,size,size))
    pygame.draw.rect(screen,(178,34,34),pygame.Rect(42*size,17*size,6*size,size))
    pygame.draw.rect(screen,(178,34,34),pygame.Rect(45*size,18*size,4*size,size))
    pygame.draw.rect(screen,(178,34,34),pygame.Rect(46*size,19*size,3*size,4*size))
    pygame.draw.rect(screen,(178,34,34),pygame.Rect(46*size,23*size,2*size,size))
    pygame.draw.rect(screen,(178,34,34),pygame.Rect(45*size,24*size,2*size,size))
    pygame.draw.rect(screen,(178,34,34),pygame.Rect(38*size,24*size,size,size))
    pygame.draw.rect(screen,(178,34,34),pygame.Rect(43*size,25*size,3*size,size))
    pygame.draw.rect(screen,(178,34,34),pygame.Rect(39*size,25*size,size,size))

    pygame.draw.rect(screen,(139,0,0),pygame.Rect(45*size,16*size,3*size,size))
    pygame.draw.rect(screen,(139,0,0),pygame.Rect(43*size,17*size,size,size))
    pygame.draw.rect(screen,(139,0,0),pygame.Rect(48*size,17*size,size,size))
    pygame.draw.rect(screen,(139,0,0),pygame.Rect(49*size,18*size,size,5*size))
    pygame.draw.rect(screen,(139,0,0),pygame.Rect(48*size,23*size,size,2*size))
    pygame.draw.rect(screen,(139,0,0),pygame.Rect(47*size,24*size,size,2*size))
    pygame.draw.rect(screen,(139,0,0),pygame.Rect(46*size,25*size,size,size))
    pygame.draw.rect(screen,(139,0,0),pygame.Rect(41*size,26*size,5*size,size))


def show_page1(cl):
    screen.fill((216,191,216))

    font=pygame.font.SysFont('consolas',12)
    s_font=font.render('-->',True,(color3[cl][0],color3[cl][1],color3[cl][2]))

    r_font=s_font.get_rect()
    r_font.midtop=(150,330)
    screen.blit(s_font,r_font)

    font1=pygame.font.SysFont('consolas',12)
    s_font1=font1.render('Press SPACE to continue',True,(color3[cl][0],color3[cl][1],color3[cl][2]))
    r_font1=s_font1.get_rect()
    r_font1.midtop=(150,315)
    screen.blit(s_font1,r_font1)

    font2=pygame.font.SysFont('arial',40)
    s_font2=font2.render('Snake Game',True,(color3[cl+2][0],color3[cl+2][1],color3[cl+2][2]))
    r_font2=s_font2.get_rect()
    r_font2.midtop=(150,140)
    screen.blit(s_font2,r_font2)

    font3=pygame.font.SysFont('arial',20)
    s_font3=font3.render('Welcome to',True,(color3[cl][0],color3[cl][1],color3[cl][2]))
    r_font3=s_font3.get_rect()
    r_font3.midtop=(150,120)
    screen.blit(s_font3,r_font3)

    font4=pygame.font.SysFont('consolas',12)
    s_font4=font4.render('Created by: _nht.Alvaˇ',True,(color3[cl][0],color3[cl][1],color3[cl][2]))
    r_font4=s_font4.get_rect()
    r_font4.midtop=(150,190)
    screen.blit(s_font4,r_font4)

    pygame.display.update()

def show_page2(cl):
    screen.fill((216,191,216))
    pygame.draw.rect(screen,(color3[0][0],color3[0][1],color3[0][2]),pygame.Rect(40,105,220,135))
    pygame.draw.rect(screen,(color3[1][0],color3[1][1],color3[1][2]),pygame.Rect(45,110,210,125))

    pygame.draw.rect(screen,(192,192,192),pygame.Rect(125,135,50,30))
    pygame.draw.rect(screen,(192,192,192),pygame.Rect(75,165,50,30))
    pygame.draw.rect(screen,(192,192,192),pygame.Rect(175,165,50,30))
    pygame.draw.rect(screen,(192,192,192),pygame.Rect(125,195,50,30))

    font=pygame.font.SysFont('consolas',12)
    s_font=font.render('Press SPACE to continue',True,(color3[cl][0],color3[cl][1],color3[cl][2]))
    r_font=s_font.get_rect()
    r_font.midtop=(150,315)
    screen.blit(s_font,r_font)

    font1=pygame.font.SysFont('consolas',15)
    s_font1=font1.render('Press this to move:',True,(color3[cl][0],color3[cl][1],color3[cl][2]))
    r_font1=s_font1.get_rect()
    r_font1.midtop=(150,120)
    screen.blit(s_font1,r_font1)

    font2=pygame.font.SysFont('consolas',15)
    s_font2=font2.render('UP',True,(color3[cl][0],color3[cl][1],color3[cl][2]))
    r_font2=s_font2.get_rect()
    r_font2.midtop=(151,143)
    screen.blit(s_font2,r_font2)

    font3=pygame.font.SysFont('consolas',15)
    s_font3=font3.render('LEFT        RIGHT',True,(color3[cl][0],color3[cl][1],color3[cl][2]))
    r_font3=s_font3.get_rect()
    r_font3.midtop=(152,173)
    screen.blit(s_font3,r_font3)

    font4=pygame.font.SysFont('consolas',15)
    s_font4=font4.render('DOWN',True,(color3[cl][0],color3[cl][1],color3[cl][2]))
    r_font4=s_font4.get_rect()
    r_font4.midtop=(150,203)
    screen.blit(s_font4,r_font4)

    font6=pygame.font.SysFont('consolas',12)
    s_font6=font6.render('-->',True,(color3[cl][0],color3[cl][1],color3[cl][2]))
    r_font6=s_font6.get_rect()
    r_font6.midtop=(150,330)
    screen.blit(s_font6,r_font6)

    pygame.display.update()

def show_page3(cl):
    screen.fill((216,191,216))
    pygame.draw.rect(screen,(color3[0][0],color3[0][1],color3[0][2]),pygame.Rect(20,115,260,100))
    pygame.draw.rect(screen,(color3[1][0],color3[1][1],color3[1][2]),pygame.Rect(25,120,250,90))

    font1=pygame.font.SysFont('consolas',12)
    s_font1=font1.render('Press SPACE to continue',True,(color3[cl][0],color3[cl][1],color3[cl][2]))
    r_font1=s_font1.get_rect()
    r_font1.midtop=(150,315)
    screen.blit(s_font1,r_font1)

    font2=pygame.font.SysFont('consolas',12)
    s_font2=font2.render('<> Press Q to change snake_color',True,(color3[cl][0],color3[cl][1],color3[cl][2]))
    r_font2=s_font2.get_rect()
    r_font2.midtop=(150,150)
    screen.blit(s_font2,r_font2)

    font3=pygame.font.SysFont('consolas',12)
    s_font3=font3.render('<> Press W to change board_color',True,(color3[cl][0],color3[cl][1],color3[cl][2]))
    r_font3=s_font3.get_rect()
    r_font3.midtop=(150,170)
    screen.blit(s_font3,r_font3)

    font4=pygame.font.SysFont('consolas',12)
    s_font4=font4.render('<> Press E to change font_color',True,(color3[cl][0],color3[cl][1],color3[cl][2]))
    r_font4=s_font4.get_rect()
    r_font4.midtop=(147,190)
    screen.blit(s_font4,r_font4)

    font5=pygame.font.SysFont('consolas',15)
    s_font5=font5.render('Note:',True,(color3[cl][0],color3[cl][1],color3[cl][2]))
    r_font5=s_font5.get_rect()
    r_font5.midtop=(147,130)
    screen.blit(s_font5,r_font5)

    font6=pygame.font.SysFont('consolas',12)
    s_font6=font6.render('-->',True,(color3[cl][0],color3[cl][1],color3[cl][2]))
    r_font6=s_font6.get_rect()
    r_font6.midtop=(150,330)
    screen.blit(s_font6,r_font6)

    pygame.display.update()

def show_page4(cl):
    screen.fill((216,191,216))

    font=pygame.font.SysFont('consolas',12)
    s_font=font.render('-->',True,(color3[cl][0],color3[cl][1],color3[cl][2]))
    r_font=s_font.get_rect()
    r_font.midtop=(150,330)
    screen.blit(s_font,r_font)

    font1=pygame.font.SysFont('consolas',12)
    s_font1=font1.render('Press SPACE to start',True,(color3[cl][0],color3[cl][1],color3[cl][2]))
    r_font1=s_font1.get_rect()
    r_font1.midtop=(150,315)
    screen.blit(s_font1,r_font1)

    font2=pygame.font.SysFont('consolas',17)
    s_font2=font2.render('Are You Ready?',True,(color3[cl][0],color3[cl][1],color3[cl][2]))
    r_font2=s_font2.get_rect()
    r_font2.midtop=(230,20)
    screen.blit(s_font2,r_font2)

    font3=pygame.font.SysFont('consolas',15)
    s_font3=font3.render('Have a good game!',True,(color3[cl][0],color3[cl][1],color3[cl][2]))
    r_font3=s_font3.get_rect()
    r_font3.midtop=(230,40)
    screen.blit(s_font3,r_font3)

    draw_snake(10)
    draw_food(5)

    pygame.display.update()

def show_end(cl,sc,h_sc):
    screen.fill((216,191,216))
    pygame.draw.rect(screen,(color3[0][0],color3[0][1],color3[0][2]),pygame.Rect(20,105,260,135))
    pygame.draw.rect(screen,(color3[1][0],color3[1][1],color3[1][2]),pygame.Rect(25,110,250,125))

    font=pygame.font.SysFont('consolas',12)
    s_font=font.render('-->',True,(color3[cl][0],color3[cl][1],color3[cl][2]))
    r_font=s_font.get_rect()
    r_font.midtop=(150,330)
    screen.blit(s_font,r_font)

    font1=pygame.font.SysFont('consolas',12)
    s_font1=font1.render('Press SPACE to try again',True,(color3[cl][0],color3[cl][1],color3[cl][2]))
    r_font1=s_font1.get_rect()
    r_font1.midtop=(150,315)
    screen.blit(s_font1,r_font1)

    font2=pygame.font.SysFont('arial',15)
    s_font2=font2.render('SCORE: {0}'.format(sc),True,(color3[cl][0],color3[cl][1],color3[cl][2]))
    r_font2=s_font2.get_rect()
    r_font2.midtop=(150,135)
    screen.blit(s_font2,r_font2)

    font3=pygame.font.SysFont('arial',15)
    s_font3=font3.render('HIGH SCORE: {0}'.format(h_sc),True,(color3[cl][0],color3[cl][1],color3[cl][2]))
    r_font3=s_font3.get_rect()
    r_font3.midtop=(150,155)
    screen.blit(s_font3,r_font3)

    font4=pygame.font.SysFont('consolas',15)
    s_font4=font4.render('PLAY AGAIN?',True,(color3[cl][0],color3[cl][1],color3[cl][2]))
    r_font4=s_font4.get_rect()
    r_font4.midtop=(150,217)
    screen.blit(s_font4,r_font4)

    font5=pygame.font.SysFont('consolas',20)
    s_font5=font5.render('Game Over!',True,(color3[cl+2][0],color3[cl+2][1],color3[cl+2][2]))
    r_font5=s_font5.get_rect()
    r_font5.midtop=(150,115)
    screen.blit(s_font5,r_font5)

    font6=pygame.font.SysFont('arial',15)
    s_font6=font6.render('Be careful with the walls and snake_body!',True,(color3[cl][0],color3[cl][1],color3[cl][2]))
    r_font6=s_font6.get_rect()
    r_font6.midtop=(150,175)
    screen.blit(s_font6,r_font6)

    font7=pygame.font.SysFont('arial',15)
    s_font7=font7.render('Good luck!',True,(color3[cl][0],color3[cl][1],color3[cl][2]))
    r_font7=s_font7.get_rect()
    r_font7.midtop=(150,195)
    screen.blit(s_font7,r_font7)

    pygame.display.update()

def show_ingame(k,score,cl):
    if k==0:
        font=pygame.font.SysFont('arial',15)
        s_font=font.render('SCORE: {0}'.format(score),True,(color3[cl][0],color3[cl][1],color3[cl][2]))
        r_font=s_font.get_rect()
        r_font.midtop=(150,5)
        screen.blit(s_font,r_font)

    if k==1:
        font=pygame.font.SysFont('arial',15)
        s_font=font.render('PAUSED!',True,(color3[cl][0],color3[cl][1],color3[cl][2]))
        r_font=s_font.get_rect()
        r_font.midtop=(150,5)
        screen.blit(s_font,r_font)

    if k==2:
        font=pygame.font.SysFont('consolas',15)
        s_font=font.render('Press SPACE to pause the game',True,(color3[cl][0],color3[cl][1],color3[cl][2]))
        r_font=s_font.get_rect()
        r_font.midtop=(150,23)
        screen.blit(s_font,r_font)

    if k==3:
        font=pygame.font.SysFont('consolas',15)
        s_font=font.render('Press SPACE to continue the game',True,(color3[cl][0],color3[cl][1],color3[cl][2]))
        r_font=s_font.get_rect()
        r_font.midtop=(150,23)
        screen.blit(s_font,r_font)

def run_game():
    start1=True
    start2=False
    start3=False
    start4=False
    end=False
    run=False
    pause=False

    size=15
    w_size=45
    sn_cl=7
    tsc_cl=0
    f_cl=0
    x=random.randrange(20)*size
    y=random.randrange(3,23)*size
    snake_change=[0,0]
    snake=[]
    direction='snake_direction'
    length=1
    h_score=0
    score=0
    f_x=random.randrange(1,19)*size
    f_y=random.randrange(4,22)*size

    while start1:
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                pygame.quit()
            if i.type==pygame.KEYDOWN:
                if i.key==pygame.K_SPACE:
                    time.sleep(1)
                    start1=False
                    start2=True
        show_page1(0)

    while start2:
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                pygame.quit()
            if i.type==pygame.KEYDOWN:
                if i.key==pygame.K_SPACE:
                    time.sleep(1)
                    start2=False
                    start3=True
        show_page2(0)

    while start3:
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                pygame.quit()
            if i.type==pygame.KEYDOWN:
                if i.key==pygame.K_SPACE:
                    time.sleep(1)
                    start3=False
                    start4=True
        show_page3(0)

    while start4:
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                pygame.quit()
            if i.type==pygame.KEYDOWN:
                if i.key==pygame.K_SPACE:
                    time.sleep(1)
                    start4=False
                    run=True
        show_page4(0)             

    while run:
        if end:
            for i in pygame.event.get():
                if i.type==pygame.QUIT:
                    pygame.quit()
                if i.type==pygame.KEYDOWN:
                    if i.key==pygame.K_SPACE:
                        x=random.randrange(20)*size
                        y=random.randrange(3,23)*size
                        snake_change=[0,0]
                        snake=[]
                        direction='snake_direction'
                        length=1
                        score=0
                        f_x=random.randrange(1,19)*size
                        f_y=random.randrange(4,22)*size
                        end=not end

            show_end(0,score,h_score)
        else:
            for i in pygame.event.get():
                if i.type==pygame.QUIT:
                    pygame.quit()
                if i.type==pygame.KEYDOWN:
                    if i.key==pygame.K_q:
                        sn_cl=random.randrange(32)
                    if i.key==pygame.K_w:
                        a=random.randrange(5)
                        while a==tsc_cl:
                            a=random.randrange(5)
                        tsc_cl=a
                    if i.key==pygame.K_e:
                        a=random.randrange(2)
                        while a==f_cl:
                            a=random.randrange(2)
                        f_cl=a
                    if i.key==pygame.K_SPACE:
                        pause=not pause
                    if pause==False:
                        if i.key==pygame.K_UP:
                            if direction!='down':
                                snake_change[0]=0
                                snake_change[1]=-size
                                direction='up'
                                run=True
                        if i.key==pygame.K_DOWN:
                            if direction!='up':
                                snake_change[0]=0
                                snake_change[1]=size
                                direction='down'
                                run=True
                        if i.key==pygame.K_RIGHT:
                            if direction!='left':
                                snake_change[0]=size
                                snake_change[1]=0
                                direction='right'
                                run=True
                        if i.key==pygame.K_LEFT:
                            if direction!='right':
                                snake_change[0]=-size
                                snake_change[1]=0
                                direction='left'
                                run=True

            if pause==False:
                x+=snake_change[0]
                y+=snake_change[1]

                snake.append([x,y])

            if x==f_x and y==f_y:
                f_x=random.randrange(1,19)*size
                f_y=random.randrange(4,22)*size
                length+=1
                score+=1
        
            if x<0 or x>300-size or y<45+size or y>345-size:
                if score>h_score: h_score=score
                end=not end

            if len(snake)>length:
                snake.pop(0)

            for i in range(length-1):
                if snake[i][0]==x and snake[i][1]==y:
                    if score>h_score: h_score=score
                    end=not end
                if f_x==snake[i][0] and f_y==snake[i][1]:
                    f_x=random.randrange(1,19)*size
                    f_y=random.randrange(4,22)*size
    
            screen.fill((color3[0][0],color3[0][1],color3[0][2]))
            pygame.draw.rect(screen,(color3[1][0],color3[1][1],color3[1][2]),pygame.Rect(0,0,300,w_size))
            pygame.draw.rect(screen,(color2[tsc_cl][0],color2[tsc_cl][1],color2[tsc_cl][2]),pygame.Rect(5,5,290,w_size-10))
            for i in range(length-1,-1,-1):
                pygame.draw.rect(screen,(color1[sn_cl][0],color1[sn_cl][1],color1[sn_cl][2]),pygame.Rect(snake[i][0],snake[i][1],size,size))
            pygame.draw.rect(screen,(color3[2][0],color3[2][1],color3[2][2]),pygame.Rect(f_x,f_y,size,size))
            if pause:
                for i in range(length-1,-1,-1):
                    pygame.draw.rect(screen,(192,192,192),pygame.Rect(snake[i][0],snake[i][1],size,size))
                pygame.draw.rect(screen,(192,192,192),pygame.Rect(f_x,f_y,size,size))
                show_ingame(1,score,2)
                show_ingame(3,score,f_cl)
            else:
                for i in range(length-1,-1,-1):
                    pygame.draw.rect(screen,(color1[sn_cl][0],color1[sn_cl][1],color1[sn_cl][2]),pygame.Rect(snake[i][0],snake[i][1],size,size))
                pygame.draw.rect(screen,(color3[2][0],color3[2][1],color3[2][2]),pygame.Rect(f_x,f_y,size,size))
                show_ingame(0,score,f_cl)
                show_ingame(2,score,f_cl)

            pygame.display.update()

            clock.tick(20)

run_game()