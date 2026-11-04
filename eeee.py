import pgzrun
import random
WIDTH=400
HEIGHT=400

def draw():
    width=WIDTH
    height=HEIGHT-100
    r=255
    g=0
    b=random.randint(0,255)
    for i in range(20):
        rect=Rect((0,0), width, height)
        rect.center=150,150
        screen.draw.rect(rect, (r,g,b))
        r-=10
        g+=10
        width-=10
        height-=10
pgzrun.go()
