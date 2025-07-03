import pgzrun
import random


WIDTH=800
HEIGHT=500

items=["batteryimg", "bottleimg"]
actor_items=[]
level=1


def start():
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

def draw():
    screen.blit("sky", (0,0))
    bag.draw()



pgzrun.go()

# git init
# git add .
# git commit -m "message"
# git push