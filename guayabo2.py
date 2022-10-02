import pygame, random, time
pygame.init()
#Colors
WHITE=(255,255,255)
YELLOWP=(255,254,226)
BLACK=(0,0,0)
#sizes
size=(1250,650)
#images

logo=pygame.image.load("Hera logo.jpg")
pygame.display.set_icon(logo)
pygame.display.set_caption("Hera")
screen=pygame.display.set_mode(size)
background=pygame.image.load("Fondo.png").convert(screen)
guayabo=pygame.image.load("guayabo.png").convert()
enemy=pygame.image.load("villannoP.png").convert()
enemy2=pygame.image.load("vn.png").convert()
titlle=pygame.image.load("tittle.png").convert()
tardigrado_info=pygame.image.load("info2.png").convert()
Luna_info=pygame.image.load("info1.png").convert()
enemy.set_colorkey(BLACK)
enemy2.set_colorkey(BLACK)
guayabo.set_colorkey(BLACK)
#coords guayabo
gameover=pygame.image.load("gameover.png").convert()
ganaste=pygame.image.load("ganaste.png").convert()
Xt=1250
xti=1250
xli=1250
xg=10
yg=550
m=0
n=0
o=0
jump=10
y_move=0
x_move=0
running=True
jumping=False
#coords enemies
xe=1000
ye=550
x=0
clock=pygame.time.Clock()
appered=[]
appered2=[]
enemy_x=[]
enemy_y=[]
enemy2_x=[]
enemy2_y=[]
t=0
for i in range(30):
    enemy_x.append(random.randrange(1000,1250))
    enemy_y.append(random.randrange(450,550))
    enemy2_x.append(random.randrange(1000,1250))
    enemy2_y.append(random.randrange(450,550))
#print(enemy_x,"\n\n",enemy_y)
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:

            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP or event.key==pygame.K_w or event.key==pygame.K_SPACE:
                if yg<650:
                    jumping=True
                else:
                    jumping=False
            if event.key==pygame.K_RIGHT or event.key==pygame.K_d:
                x_move=3
            if event.key==pygame.K_LEFT or event.key==pygame.K_a:
                x_move=-3
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_UP or event.key==pygame.K_w:
                y_move=0
            if event.key==pygame.K_RIGHT or event.key==pygame.K_d:
                x_move=0
            if event.key==pygame.K_LEFT or event.key==pygame.K_a:
                x_move=0

    if jumping:
        if jump>=-10:
            yg -=(jump*abs(jump))*0.5
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT or event.key==pygame.K_d:
                    x_move+=1.25
                if event.key==pygame.K_LEFT or event.key==pygame.K_a:
                    x_move-=1.25    
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_RIGHT or event.key==pygame.K_d:
                    x_move=0
                if event.key==pygame.K_LEFT or event.key==pygame.K_a:
                    x_move=0
            jump-=1
        else:
            jump=10
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT or event.key==pygame.K_d:
                    x_move+=1.25
                if event.key==pygame.K_LEFT or event.key==pygame.K_a:
                    x_move-=1.25 
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_RIGHT or event.key==pygame.K_d:
                    x_move=0
                if event.key==pygame.K_LEFT or event.key==pygame.K_a:
                    x_move=0
            jumping=False
    xg+=x_move    
    yg+=y_move
    
    x_r=x%1250
    screen.blit(background,[x_r-1250,0])
    if x_r<1250:
        screen.blit(background,[x_r,0])
    if Xt>(-titlle.get_width()):
        if Xt>(625-titlle.get_width()/2):
            Xt-=4
        else:
            if m<6:
                m+=0.05
            else:
                Xt-=4
    else:
        if xti>(-tardigrado_info.get_width()):
            if xti>(625-tardigrado_info.get_width()/2):
                xti-=4
            else:
                if n<6:
                    n+=0.01
                else:
                    xti-=4
        else:
            if xli>(-Luna_info.get_width()):
                if xli>(625-Luna_info.get_width()/2):
                    xli-=4
                else:
                    if o<6:
                        o+=0.01 
                    else:
                        xli-=4
                 
    if appered2==[]:
        r=random.randrange(150)
        appered2.append(r)
        t+=1
    if enemy2_x[r//5]<0:
        r=random.randrange(150)
        if r in appered2:
            if r%5==0:
                while r in appered2:
                    r=random.randrange(150)
                appered2.append(r)
            else:
                while r%5!=0:
                    r=random.randrange(150)
                appered2.append(r)
        t+=1

    if appered==[]:
        c=random.randrange(30)
        appered.append(c)
        t+=1
    if enemy_x[c]<0:
        if c in appered:
            while c in appered:
                c=random.randrange(30)
        appered.append(c)
        t+=1
    enemy_x[c]-=6
    
    enemy2_x[r//5]-=9
    x -= 1
    pygame.draw.rect(screen, BLACK, (0,600,1250,50))
    #all_sprite_list.draw(screen)
    screen.blit(titlle, [Xt, 200])
    screen.blit(tardigrado_info, [xti, 200])
    screen.blit(Luna_info, [xli, 200])
    rect1 = pygame.Rect(xg, yg, guayabo.get_width(), guayabo.get_height())
    rect2 = pygame.Rect(enemy_x[c], enemy_y[c], enemy.get_width()-20, enemy.get_height()-30)
    rect3 = pygame.Rect(enemy2_x[r//5], enemy2_y[r//5], enemy2.get_width()-20, enemy2.get_height()-10)
    if rect1.colliderect(rect2):
        while yg<650:
            if jump>=-10:
                yg -=(jump*abs(jump))*0.5
                jump-=1
            else:
                jump=10
                jumping=False
            yg+=3
        if t<=60 and t>35:
            pygame.draw.rect(screen, BLACK, (0,0,1250,650))
            screen.blit(ganaste, [(1250/2-(ganaste.get_width()/2)),(650/2-(ganaste.get_height()/2))])
            pygame.display.update()
            pygame.display.flip()
        print(t)
    if rect1.colliderect(rect3):
        while yg<650:
            if jump>=-10:
                yg -=(jump*abs(jump))*0.5
                jump-=1
            else:
                jump=10
                jumping=False
            yg+=3
        if t<=60 and t>35 :
            pygame.draw.rect(screen, BLACK, (0,0,1250,650))
            screen.blit(ganaste, [(1250/2-(ganaste.get_width()/2)),(650/2-(ganaste.get_height()/2))])
            pygame.display.update()
            pygame.display.flip()
        print(t)


    screen.blit(enemy2,[enemy2_x[r//5],enemy2_y[r//5]])
    screen.blit(enemy,[enemy_x[c],enemy_y[c]])
    screen.blit(guayabo,[xg,yg])
    if yg>650:
        pygame.draw.rect(screen, BLACK, (0,0,1250,650))
        screen.blit(gameover, [(1250/2-(gameover.get_width()/2)),(650/2-(gameover.get_height()/2))])
        pygame.display.update()
        pygame.display.flip()
    if t==60:
            pygame.draw.rect(screen, BLACK, (0,0,1250,650))
            screen.blit(ganaste, [(1250/2-(ganaste.get_width()/2)),(650/2-(ganaste.get_height()/2))])
            pygame.display.update()
            pygame.display.flip()
            print(t)
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)