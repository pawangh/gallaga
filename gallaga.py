import pgzrun
import random
WIDTH=800
HEIGHT=600
TITLE="GALLAGA"

player=Actor("ship")
player.pos=(400,500)
wasp=Actor("wasp")
wasp.pos=random.randint(50,750),50
def draw():
    screen.blit("background",(0,0))
    player.draw()
    wasp.draw()
def update():
    pass
pgzrun.go()