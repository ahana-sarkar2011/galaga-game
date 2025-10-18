import pgzrun

WIDTH = 1000
HEIGHT = 600

direction = 1
movedown=False

b=[]

galaga=Actor("galaga")
galaga.x=500
galaga.y=540

bugs=[]
for o in range(4):
    for i in range(5):
        bug=Actor("bug")
        bug.x=(i*70)+40
        bug.y=(o*70)+40
        bugs.append(bug)

def draw():
    screen.fill("blue")
    galaga.draw()
    for bullet in b:
        bullet.draw()
    for i in bugs:
        i.draw()


def update():
    global movedown, direction
    movedown = False
    if keyboard.left:
        galaga.x+=-10
        if galaga.x<0:
            galaga.x=0
    if keyboard.right:
        galaga.x+=10
        if galaga.x>1000:
            galaga.x=1000
    if bugs[-1].x>1000 or bugs[0].x<0:
        movedown=True
        direction = direction*-1
    for bug in bugs:
        bug.x+=8*direction
        if movedown == True:
            bug.y+=40
    for bullet in b:
        bullet.y-=10
        for bug in bugs:
            if bug.colliderect(bullet):
                bugs.remove(bug)
                b.remove(bullet)

def on_key_down(key):
    if key == keys.SPACE:
        bullet=Actor("bullet")
        b.append(bullet)
        bullet.x=galaga.x
        bullet.y=galaga.y

pgzrun.go()