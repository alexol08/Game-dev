# import pgzrun
# import random
# WIDTH=500
# HEIGHT=500
# points=0
# game_over=False
# def draw():
#     if not game_over:
#         screen.blit("background", (0,0))
#         bee.draw()
#         flower.draw()
#     else:
#         screen.fill(color="black")
#         screen.draw.text("GAME OVER", center=(250, 250), fontsize=100)
#         screen.draw.text("HIGH SCORE: "+str(points), center=(250, 400), fontsize=40)

# bee=Actor("bee")
# bee.pos=(250, 250)
# flower=Actor("flower")
# flower.pos=(random.randint(50, 450), random.randint(50, 450))

# def update():
#     if keyboard.a:
#         bee.x-=5
#     elif keyboard.d:
#         bee.x+=5
#     elif keyboard.w:
#         bee.y-=5
#     elif keyboard.s:
#         bee.y+=5
#     if bee.colliderect(flower):
#         global points
#         points+=1
#         flower.pos=(random.randint(50, 450), random.randint(50, 450))    
# def name():
#     global game_over
#     print("Time's up")
#     game_over= True

# clock.schedule(name, 30.0)

# pgzrun.go()

import pgzrun
import random
WIDTH=700
HEIGHT=500
game_over=False
difficulty=0
# go_scene=False
location=(random.randint(1,3))
def draw():
    if not game_over:
        if difficulty>40:
            screen.fill((0,0,0))
            screen.draw.text("YOU WIN", center=(350, 250), fontsize=100)
        else:
            screen.fill((0,0,0))
            alien.draw()
            cheese.draw()
            screen.draw.text("Difficulty: " + str(difficulty), topleft=(10, 10), fontsize=30, color="white")
    else:
        screen.fill((0,0,0))
        screen.draw.text("GAME OVER", center=(350, 250), fontsize=100)

alien=Actor("alien")
alien.pos=(100, 250)
cheese=Actor("cheeze")
cheese.pos=(800, random.randint(50,450))

def update():
    global difficulty
    global game_over
    if game_over or difficulty>40:
        return
    if keyboard.w and alien.y>0:
        alien.y-=10
    if keyboard.s and alien.y<HEIGHT:
        alien.y+=10
    if difficulty > 18:
        cheese.x -= 30
    elif difficulty > 12:
        cheese.x -= 25
    elif difficulty > 9:
        cheese.x -= 20
    elif difficulty > 3:
        cheese.x -= 10
    else:
        cheese.x -= 5

    if cheese.colliderect(alien):
        game_over=True
    if cheese.x<0:
        cheese.pos=(800, random.randint(50,450))
        difficulty+=1


        
pgzrun.go()

# def scene():
#     screen.draw.text('''Aliens were living peaceful lives until
#                      suddenly their enemies started shooting a food
#                      that all aliens are allergic to: cheese 
#                      --- Make sure to avoid all the cheese''', center=(350, 250), fontsize=40)

# clock.schedule(scene, 5.0)

