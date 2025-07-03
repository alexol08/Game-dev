import pgzrun
import random

WIDTH=500
HEIGHT=500
satellites=[]
coord=[]
next_sat=1
seconds=0
def start():
    for i in range(1, 9):
        sat= Actor('satellite')
        satellites.append(sat)
        sat.pos=(random.randint(20, 480), random.randint(20, 480))
start()
def draw():
    if next_sat == 8:

        screen.fill((0, 0, 0))
        screen.draw.text("YOU HAVE WON", center=(250, 220), fontsize=60)
        screen.draw.text("Score: "+str(round(seconds, 1)), center=(250, 270))
    else:
        screen.blit('background', (0,0))
        screen.draw.text(str(round(seconds, 1)), (450, 20), fontsize=30)
        for i in range(1, 9):
            satellites[i-1].draw()
            screen.draw.text(str(i), (satellites[i-1].x+10, satellites[i-1].y-20))
        for line in coord:
            screen.draw.line(line[0], line[1], "white")
        

def on_mouse_down(pos):
    global next_sat
    if satellites[next_sat].collidepoint(pos):
        coord.append(((satellites[next_sat-1].pos), (satellites[next_sat].pos)))
        next_sat+=1
        print(coord)

def update_time():
        global seconds
        if next_sat <8:
         seconds+=0.1
clock.schedule_interval(update_time, 0.1)
    

pgzrun.go()