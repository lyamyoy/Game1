import pgzrun
import random

WIDTH=400
HEIGHT=600

rocket=Actor('rocket',center=(200,300))

star=[]
for i in range(20):
        rect = Rect((random.randrange(WIDTH),random.randrange(HEIGHT)),(2,2))
        star.append(rect)

speed=0
acceleration=0.1
key_flg=False
status=0

def draw():
    global status
    screen.clear()
    #star
    for i in range(20):
        screen.draw.rect(star[i],'WHITE')
    #landing_base
    for i in range(50):
        screen.draw.line((150-i*3,550+i),(250+i*3,550+i),'GRAY')
    if status==0:#opening
        #fire
        for i in range(10):
            screen.draw.circle(rocket.midbottom,i+1,(255,i*20,0))
        #title
            screen.draw.text("Shunbey Space",(31,100),owidth=1.5,ocolor='YELLOW',color='BLACK',fontsize=64)
    elif status==1:#gaming
        if key_flg:
            for i in range(10):
                screen.draw.circle(rocket.midbottom,i+1,(255,i*20,0))
    rocket.draw()

def on_key_down(key):
    global status
    if key==key.SPACE:
        if status==0:
            status=1

def update():
    global speed
    global acceleration
    global key_flg
    global status
    if status==1:
        if keyboard.up:
            key_flg=True
            acceleration=-0.1
        else:
            key_flg=False
            acceleration=0.1
        speed+=acceleration
        rocket.y+=speed
        if rocket.y>500:
            if speed<1.0:
                status=2#clear
            else:
                status=3#over
                anime_r=animate(rocket,'bounce_start_end',1,angle=45)

pgzrun.go()

