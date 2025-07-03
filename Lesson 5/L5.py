# import pgzrun
# WIDTH=400
# HEIGHT=400
# def draw():
#     screen.fill(color= (0,0,0))
#     Alien.draw()
#     screen.draw.text("Hello", center=(200,50), fontsize=40)

# Alien= Actor ("alien")
# Alien.pos= (200,200)
# def on_mouse_down(pos):
#     if Alien.collidepoint(pos):
#         print("working")
    
# pgzrun.go()

import pgzrun
import random
WIDTH=1000
HEIGHT=500
yes=0
seconds=0
if yes==0:
    def update_time():
        global seconds
        seconds+=0.1
clock.schedule_interval(update_time, 0.1)

def draw():
    screen.fill(color="dark blue")
    screen.draw.text("Welcome to space", center=(200, 50), fontsize=20)
    asteroid.draw()
asteroid= Actor ("asteroid")
asteroid.pos=(random.randint(50, 950), random.randint(50,500))
def on_mouse_down(pos):
    if asteroid.collidepoint(pos):
        global yes
        print("working")
        yes +=1
        print(seconds)
pgzrun.go()



