import pgzrun
import random


WIDTH=700
HEIGHT=500

items=["batteryimg", "bottleimg", "bagimg", "chipsimg"]
actor_items=[]
level=1
game_over=False
winning=False

def start():
    actor_items.clear()
    global bag
    for i in range(level):
        item=random.choice(items)
        actor_item=Actor(item)
        actor_items.append(actor_item)
    bag=Actor("paperimg")
    actor_items.append(bag)
    random.shuffle(actor_items)
    gap=WIDTH//(level+2)
    for i in range(level+1):
        actor_items[i].x=(i+1)*gap
        actor_items[i].y=50
start()

def draw():
    screen.blit("sky", (0,0))
    bag.draw()
    for actor in actor_items:
        actor.draw()
    if game_over:
        screen.fill("black")
        screen.draw.text("GAME OVER", center=(350, 250), fontsize=60)
    screen.draw.text("LEVEL "+str(level), center=(50, 20), fontsize=30, color="black")
    if winning: 
        screen.fill("black")
        screen.draw.text("YOU WIN!!!", center=(350, 250), fontsize=60)

def update():
    global winning
    global game_over
    for actor in actor_items:
        actor.y+=4
        if actor.y>HEIGHT:
            game_over=True
    if level>5:
        winning=True
    

def on_mouse_down(pos):
    global level
    if bag.collidepoint(pos):
        level+=1
        start()


pgzrun.go()

# git init
# git add .
# git commit -m "message"
# git push