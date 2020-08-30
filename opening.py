import pgzrun
import random

WIDTH=400
HEIGHT=600

rocket=Actor('rocket',center=(200,300))

def draw():
    screen.clear()
    for i in range(20):
        rect = Rect((random.randrange(WIDTH),random.randrange(HEIGHT)),(2,2))
        screen.draw.rect(rect,'WHITE')
    for i in range(10):
        screen.draw.circle(rocket.midbottom,i+1,(255,i*20,0))
    for i in range(50):
        screen.draw.line((150-i*3,550+i),(250+i*3,550+i),(128,128,128))
    screen.draw.text("Shunbey Space",(31,100),owidth=1.5,ocolor=(255,255,0),color=(0,0,0),fontsize=64)
    rocket.draw()

pgzrun.go()
