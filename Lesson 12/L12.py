import pgzrun

WIDTH=800
HEIGHT=500
x=50
paddle=Rect((x, 450), (150, 10))
def draw():
    screen.fill("black")
    screen.draw.filled_rect(paddle, color=("yellow"))

def update():
    global x
    if keyboard.a:
        if paddle.x<=0:
            pass
        else:
            x -= 5
    if keyboard.d:    
        if paddle.x>=650:
            pass
        else:
            x += 5
    paddle.x=x


pgzrun.go()
