import pgzrun ## Libarry used to create simple games and graphical elements

# def draw():
#     screen.fill('dark green')

#     #line
#     screen.draw.line((50,50), (200, 50), 'red')

#     screen.draw.circle((200,150), 50, 'blue')

#     #Filled circle

#     screen.draw.filled_circle((350, 150), 50, 'light green')

#     #Rectangle

#     R=Rect((100, 250), (150,50))
#     screen.draw.filled_rect(R,'lime')

#     #Square
#     screen.draw.filled_rect(Rect((300,250), (50,50)), 'purple')
#     screen.draw.text('Drawing shapes',(200, 450), color='pink', fontsize=20)


#### Making a snowman
# def draw():
#     screen.fill('black')
#     screen.draw.filled_circle((400, 500), 100, 'white')
#     screen.draw.filled_circle((400, 350), 75, 'white')
#     screen.draw.filled_circle((400, 230), 50, 'white')

#     screen.draw.filled_circle((400, ))

# def update():
#     pass
# pgzrun.go()

#### Make a triangle Homework
import pgzrun
print("""DO NOT MAKE TWO POINTS THE SAME
DO NOT MAKE ALL POINTS ON THE SAME LINE
MAKE SURE THE POINTS MAKE THE TRIANGLE CLEAR
ENTER ONLY VALID INTEGERS FOR THE POINTS
      """)
A1=int(input('Enter the first coordinate of the first point '))
A2=int(input('Enter the second coordinate of the first point '))
B1=int(input('Enter the first coordinate of the second point '))
B2=int(input('Enter the second coordinate of the second point '))
C1=int(input('Enter the first coordinate of the third point '))
C2=int(input('Enter the second coordinate of the third point '))

def draw():
    screen.draw.line((A1, A2), (B1, B2), 'white')
    screen.draw.line((B1, B2), (C1, C2), 'white')
    screen.draw.line((C1, C2), (A1, A2), 'white')

def update():
    pass


pgzrun.go()