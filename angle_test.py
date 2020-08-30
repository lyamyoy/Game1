import pgzrun
import math

WIDTH=800
HEIGHT=600

shooter=Actor('shooter.png',(400,500))
enemy=Actor('enemy.png',(700,100))

def draw():
    screen.clear()
    shooter.draw()
    enemy.draw()

    angle=enemy.angle_to(shooter)
    red=math.radians(-angle)
    x=math.cos(red)
    y=math.sin(red)
    screen.draw.text('angle = '+str(angle),(50,300),color='YELLOW',fontsize=32)
    screen.draw.text('x = '+str(x),(50,350),color='YELLOW',fontsize=32)
    screen.draw.text('y = '+str(y),(50,400),color='YELLOW',fontsize=32)

pgzrun.go()
