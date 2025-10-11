import pgzrun

WIDTH = 1000
HEIGHT = 600

movedown=False

galaga=Actor("galaga")
galaga.x=500
galaga.y=540

bullet=Actor("bullet")

bugs=[]
for i in range(5):
    bug=Actor("bug")
    bug.x=(i*70)+40
    bugs.append(bug)

def draw():
    screen.fill("blue")
    galaga.draw()
    for i in bugs:
        i.draw()


def update():
    global movedown
    movedown = False
    if keyboard.left:
        galaga.x+=-10
        if galaga.x<0:
            galaga.x=0
    if keyboard.right:
        galaga.x+=10
        if galaga.x>1000:
            galaga.x=1000
    if bugs[-1].x>1000:
        movedown=True
    for bug in bugs:
        bug.x+=4
        if movedown == True:
            bug.y+=40
            movedown = False

pgzrun.go()