import pgzrun
import random
WIDTH=500
HEIGHT=500

def draw():
    screen.fill(color=(0,0,0))
    w, h=400, 100
    r, g, b=255, 0, random.randint(0,255)
    for i in range(20):
        rect=Rect((0,0), (w, h))
        rect.center=250, 250
        screen.draw.rect(rect, (r, g, b))

        w-=25
        h+=25

        r-=10
        g+=10



    # screen.draw.filled_circle((250, 250), 100, (234, 14, 67))
pgzrun.go()