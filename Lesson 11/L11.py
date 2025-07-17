with open("homework.txt", 'w') as file:
    file.write("Do algebra problems \nEnglish essay on clouds \nLearn 10 new words of French")

with open("homework.txt", 'a') as file:
    file.write("\nGive permission slip")

with open("homework.txt", 'r') as file:
    hw=file.read()
    print(hw)

## You can use readlines and readline in the read function

# git init
# git add .
# git commit -m "message"
# git push