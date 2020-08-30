import pgzrun

WIDTH = 700
HEIGHT = 490

file_name = 'alien'
alien = Actor(file_name, center=(200,100))

def draw():
    screen.clear()
    alien.draw()

def update():
    alien.x += 1
    # alien.left += 1

pgzrun.go()
