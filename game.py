import pgzrun
import random
TITLE= "Good Shot"
WIDTH=500
HEIGHT=500
message= ""
score=0
minion=Actor("minion")
def draw():
    screen.clear()
    screen.fill(color=(128,0,0))
    minion.draw()
    screen.draw.text(message, (40, 10), fontsize=30, color="cyan")
    screen.draw.text(score, (80, 10), fontsize=30, color="black")
def place_minion():
    minion.x= random.randint(50, WIDTH-50)
    minion.y= random.randint(50, HEIGHT-50)
def on_mouse_down(pos):
    global message
    global score
    if minion.collidepoint(pos):
        message= "Good Shot"
        place_minion()
        score+=1
    else:
        message= "You Missed,Try Again"

place_minion()
pgzrun.go()