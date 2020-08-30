import pgzrun

WIDTH=400
HEIGHT=600

rocket=Actor('rocket',center=(200,100))

speed=0
acceleration=0.1
key_flg=False

def draw():
    screen.clear()
    if key_flg:
        for i in range(10):
            screen.draw.circle(rocket.midbottom,i+1,(255,i*20,0))
            rocket.draw()

def update():
    global speed
    global acceleration
    global key_flg
    if keyboard.up:
        key_flg=True
        acceleration=-0.1
    else:
        key_flg=False
        acceleration=0.1
    speed+=acceleration
    rocket.y+=speed

pgzrun.go()
            
