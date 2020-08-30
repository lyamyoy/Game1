import pgzrun
import random
import math

WIDTH=800
HEIGHT=600

shooter_hp=10
enemy_hp=30
eshot=60
turn=False
s_missiles=[]
e_missiles=[]
status=0

enemy=Actor('enemy.png',(400,100))
shooter=Actor('shooter.png',(400,500))

star=[]
for i in range(30):
    rect=Rect((random.randrange(WIDTH),random.randrange(HEIGHT)),(2,2))
    star.append(rect)
    
def draw():
    screen.clear()
    for i in range(len(star)):
        screen.draw.rect(star[i],'WHITE')
    if status==0:
        screen.draw.text('S H U N B E Y   S P A C E',(70,290),color='WHITE',gcolor='YELLOW',fontsize=72)
    elif status==1:

        #missile_painting
        for missile in s_missiles:
            missile.draw()
        for missile in e_missiles:
            missile.draw()
        screen.draw.text('Enemy HP = '+str(enemy_hp),(50,50),color='YELLOW',fontsize=32)
        screen.draw.text('Shunbey HP = '+str(shooter_hp),(580,50),color='YELLOW',fontsize=32)
    elif status==2:
        screen.draw.text('G A M E   O V E R',(200,290),color='WHITE',gcolor='YELLOW',fontsize=72)
    else:
        screen.draw.text('G A M E   C L E A R',(180,290),color='WHITE',gcolor='YELLOW',fontsize=72)        
    enemy.draw()
    shooter.draw()

def update():
    global enemy_hp,shooter_hp,turn,eshot,status
    for i in range(len(star)):
        star[i].y+=i
        if star[i].y>HEIGHT:
            star[i].y=0
            
    if status==1:
        #shunbey
        if keyboard.left:
            if shooter.x>47:
                shooter.x-=3
        if keyboard.right:
            if shooter.x<WIDTH-47:
                shooter.x+=3
        #enemy
        if turn:
            enemy.x+=5
            if enemy.x>WIDTH:
                turn=False
        else:
            enemy.x-=5
            if enemy.x<0:
                turn=True
        if eshot==0:
            angle=enemy.angle_to(shooter)
            missile1=Actor('emissile.png',(enemy.x-25,enemy.y+10))
            missile2=Actor('emissile.png',(enemy.x+25,enemy.y+10))
            missile1.angle=90+angle
            missile2.angle=90+angle
            e_missiles.append(missile1)
            e_missiles.append(missile2)
            eshot=60
        else:
            eshot-=1
        
        for missile in e_missiles:
            red=math.radians(-(missile.angle-90))
            missile.x+=(math.cos(red))*3
            missile.y+=(math.sin(red))*3
            rect=Rect(missile.topleft,(11,35))
            if shooter.colliderect(rect):
                shooter_hp-=1
                if shooter_hp==0:
                    status=2
                    e_missiles.remove(missile)
        for missile in s_missiles:
            missile.y-=10
            rect=Rect(missile.topleft,(16,22))
            if enemy.colliderect(rect):
                enemy_hp-=1
                if enemy_hp==0:
                    status=3
                    s_missiles.remove(missile)
                    
def on_key_down(key):
    global status,s_missiles,e_missiles,enemy_hp,shooter_hp
    if key==key.SPACE:
        if status==0 or status==2 or status==3:
            enemy_hp=30
            shooter_hp=10
            s_missiles=[]
            e_missiles=[]
            status=1
        elif status==1:
            s_missiles.append(Actor('smissile.png',shooter.pos))

pgzrun.go()
