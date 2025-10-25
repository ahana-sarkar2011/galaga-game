import pgzrun

WIDTH = 1000
HEIGHT = 600

endtime = False
gamewin = False
gameover = False
score = 0
direction = 1
movedown=False

btr=[]
bulltr=[]

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
    screen.draw.text("Score:"+str(score),(20,20),color = "black")
    for bullet in b:
        bullet.draw()
    for i in bugs:
        i.draw()
    if gameover == True:
        endgame()
    if gamewin == True:
        wingame()
    if endtime == True:
        timeup()


def update():
    global movedown, direction, score
    movedown = False
    if keyboard.left:
        galaga.x+=-10
        if galaga.x<0:
            galaga.x=0
    if keyboard.right:
        galaga.x+=10
        if galaga.x>1000:
            galaga.x=1000
    if len(bugs)>0 and (bugs[-1].x>1000 or bugs[0].x<0):
        movedown=True
        direction = direction*-1
    for bug in bugs:
        bug.x+=8*direction
        if movedown == True:
            bug.y+=40
        if bug.colliderect(galaga):
            endgame()
    for bullet in b:
        bullet.y-=10
        for bug in bugs:
            if bug.colliderect(bullet):
                btr.append(bug)
                bulltr.append(bullet)
                score+=1
    for bullet in bulltr:
        if bullet in b:
            b.remove(bullet)
    for bug in btr:
        if bug in bugs:
            bugs.remove(bug)
    if len(bugs)==0:
        wingame()

def on_key_down(key):
    if key == keys.SPACE:
        bullet=Actor("bullet")
        b.append(bullet)
        bullet.x=galaga.x
        bullet.y=galaga.y

def endgame():
    global gameover
    gameover = True
    screen.fill("red")
    screen.draw.text("GAMEOVER",(500,300),color = "black", fontsize=50)

def wingame():
    global gamewin
    gamewin = True
    screen.fill("green")
    screen.draw.text("YOU WIN",(500,300), color = "black", fontsize=50)

def timeup():
    global endtime
    endtime = True
    screen.fill("pink")
    screen.draw.text("TIMEUP",(500,300), color = "black", fontsize=50)

clock.schedule(timeup,10)
pgzrun.go()