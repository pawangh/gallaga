import pgzrun
import random
WIDTH=800
HEIGHT=600
TITLE="GALLAGA"

player=Actor("ship")
player.pos=(400,500)
bullets=[]
wasp=Actor("wasp")
wasp.pos=random.randint(50,750),50
def draw():
    screen.blit("background",(0,0))
    player.draw()
    wasp.draw()
    for bullet in bullets:
        bullet.draw()
def update():
    if keyboard.right:
        player.x=player.x+10
    if keyboard.left:
        player.x=player.x-10
    wasp.y=wasp.y+2
    if wasp.y>600:
        wasp.y=50
        wasp.x=random.randint(50,750)
    if keyboard.space:
        bullet=Actor("bullet")
        bullet.pos=player.pos
        bullets.append(bullet)
    for bullet in bullets:
        bullet.y=bullet.y-2
        if bullet.y<=0:
            bullets.remove(bullet) 
    
       
pgzrun.go()