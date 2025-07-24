# with open("homework.txt", 'w') as file:
#     file.write("Do algebra problems \nEnglish essay on clouds \nLearn 10 new words of French")

# with open("homework.txt", 'a') as file:
#     file.write("\nGive permission slip")

# with open("homework.txt", 'r') as file:
#     hw=file.read()
#     print(hw)
import pgzrun

WIDTH=500
HEIGHT=500

def readfile():
    QUESTIONS=[]
    with open("questions.txt", 'r') as file:
        data=file.readlines()

        for line in data:
            x=line.split(",")
            quest_dict={
                "question": x[0],
                "options": x[1:5], 
                "answer":x[-1]
            }
            print(quest_dict)
            QUESTIONS.append(quest_dict)
    print(QUESTIONS)

quest_box=Rect((50,), (200, 100))


def draw():
    screen.draw.filled_rect(quest_box, color = (255, 255, 255))



pgzrun.go()

# git init
# git add .
# git commit -m "message"
# git push