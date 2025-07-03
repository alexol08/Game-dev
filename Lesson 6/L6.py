##Mark generator + sorting hat
# import random
# register=[] ## Lists are made here to store integers
# List_A=[]
# List_B=[]
# for i in range(1, 21): ## This is the generating/sorting part
#     marks=random.randint(20,100)
#     register.append(marks)
#     if marks>60:
#         List_B.append(marks)
#     else: 
#         List_A.append(marks)

# print (register) #Printing the lists
# print (List_A)
# print(List_B)

#### Make the names of students be attached to their marks????

####################################################

## Program to generate squares of 0-50 and sorting all the numbers into even and odd lists
# General=[]
# Odd=[] ## Making lists for storing values
# Even=[]
# for i in range(0,51): ## Generating/sorting
#     value=i*i
#     General.append(value)
#     if value%2 == 0:
#         Even.append(value)
#     else:
#         Odd.append(value)

# print (General) ## Printing
# print (Odd)
# print (Even)

############################################

# To do list with different working functions
# tasks=[]
# while True:
#     print('Welcome to your daily task app')
#     print('1. View tasks')
#     print('2. Add tasks')
#     print('3. Get rid of tasks' )
#     ask=int(input("How can I help you today:"))
#     if ask == 1: 
#         print('\n')
#         if len(tasks) == 0:
#             print ("You have no tasks")
#         else:
#             number=0
#             print('Here are your tasks for today')
#             for i in tasks:
#                 number+=1
#                 print(str(number)+"."+str(i))
#         print('\n')
#     elif ask == 2:
#         print('\n')
#         amountadd=int(input("How many tasks do you want to add:"))
#         for i in range(1, amountadd+1):
#             add=input("("+str(i)+") Enter the task you want to add:")
#             tasks.append(add)
#         print('\n')
#     elif ask == 3: 
#         print('\n')
#         amountremove=int(input("How many tasks do you want to remove:"))
#         for i in range(1, amountremove+1):
#             subtract=input("("+str(i)+") Enter the task you want to add:")
#             tasks.remove(subtract)
#         print('\n')

import random
words=["apple", "banana", "cherry", "date", "elephant", "frog", "giraffe", "house", "island", "jungle",
"kite", "lemon", "monkey", "notebook", "ocean", "pencil", "queen", "river", "sun", "tree",
"umbrella", "violin", "whale", "xylophone", "yogurt", "zebra", "ant", "book", "cloud", "door",
"egg", "fish", "goat", "hat", "ice", "jam", "kangaroo", "lamp", "moon", "nest",
"orange", "pumpkin", "quilt", "robot", "star", "train", "uniform", "vase", "window", "x-ray",
"yard", "zipper", "actor", "ball", "car", "drum", "eagle", "fan", "garden", "hill",
"insect", "jacket", "key", "ladder", "mirror", "net", "owl", "piano", "quiz", "road",
"snake", "table", "uncle", "village", "water", "xenon", "yarn", "zoo", "angle", "bridge",
"castle", "desert", "engine", "feather", "glove", "hammer", "idea", "jewel", "knife", "lake",
"magnet", "needle", "orbit", "paint", "quiet", "rose", "scooter", "tower", "utensil", "valley"
]
print ("Welcome to hangman")
answer=words[random.randint(0,99)]
status=['H', 'A', 'N', 'G', 'E', 'D']
print(answer)
points=0
progress=[]
statuscheck=[]
done=False
for i in answer:
    print("-", end=" ")
    progress.append("-")
while True:
    if statuscheck == status:
        print("\n")
        print("You lose")
        done=True
    if done == True:
        break
    elif progress != list(answer):
        score=0
        print('\n')
        guess=input("Enter your guess: ")
        if len(guess)>1:
            if guess == answer:
                print("You win, the answer was "+answer)
                done=True
            else:
                points+=1
                print("STATUS: ", end="")
                statuscheck=[]
                for i in range(0, points):
                    print(status[i], end="")
                    statuscheck.append(status[i])
                print("\n")
                print(' '.join(progress))
                    
        
        else:
            if guess in answer:
                print("PROGRESS: ", end="")
                for x in answer:
                    acheck=score+len(answer)
                    bcheck=acheck-len(answer)
                    if guess == answer[bcheck]:
                        progress[bcheck]=guess
                        print(progress[bcheck], end="")
                    else:
                        print(progress[bcheck], end="")
                    score+=1
                print("\n")
            else:
                points+=1
                print("STATUS: ", end="")
                statuscheck=[]
                for i in range(0, points):
                    print(status[i], end="")
                    statuscheck.append(status[i])     
    else: 
         print("You win, the answer was "+ answer)
         break







