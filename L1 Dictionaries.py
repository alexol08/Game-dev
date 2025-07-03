# #Create a dictionary

# D={
#     "name":"Alex",
#     "Age": 16,
#     "Gender": "Male"
# }
# print (D)


# #Accessing values in a dictionary
# print(D["name"])
# print(D["Gender"])

# #Getting list of keys
# print(D.keys())

# #Getting list of values

# print(D.values())

# #Getting list of keys and values

# for i in D.keys():
#     print(i, ":",D[i],",",end="     ")

# #Check if the key exists in the dictionary
# a=input("Enter the key to be checked: ")
# if a in D:
#     print("Key Exist")
# else:
#     print("Key does not exist")

# #Add a key value to the dictionary

# D["Profession"]="Software Engineer"
# print(D)

# #Delete a key value from the dictionary
# del(D['Gender'])
# print(D)

# #Change a value in the dictionary
# D['Profession']='Engineer'
# print(D)

# #HOMEWORK
# dictionary={
#     'name': 'Alex',
#     'age':16,
#     'height':192,
#     'school': 'Gonzaga',
#     'job': 'student',
#     'interests': 'engineering',
#     'langauage': 'English',
#     'Birth place': 'South Africa',
#     'eye colour': 'brown',
#     'hair colour': 'brown'
# }
# print(dictionary)

# # Store a list as a value in the dictionary
# D['Marks']=[85, 90, 99, 81, 76, 51]

# print(D)
# print(D["Marks"][0])

#Dictionary with username and passowrd checking software
# users={
#     'user1':'password1',
#     'user2':'password2',
#     'user3':'password3',
#     'user4':'password4',
#     'user5':'password5',
#     'user6':'password6',
#     'user7':'password7',
#     'user8':'password8',
#     'user9':'password9',
#     'user10':'password10'
# }
# passtally=0
# usertally=0
# while True:
#     if usertally <3 or passtally < 3:
#         username=input('Enter your username:')
#         if username in users:
#             password=input('Enter your password:')
#             if users[username] == password:
#                 print ('You are now logged in')
#                 break
#             else:
#                 print ('Incorrect password - try again')
#                 passtally+=1
#                 print('You have '+str(3-passtally)+' attempts left')
#         else:
#             print('Incorrect username - try again')
#             usertally+=1
#             print('You have '+str(3-usertally)+' attempts left')
#     else:
#         print ('You have used all your attempts')

#Count the occurence of voules in the string entered by the user
# vowels= {
#     'a':0,
#     'e':0,
#     'i':0,
#     'o':0,
#     'u':0
# }
# vinput=input("Enter a word:")

# for i in vinput:
#     if i in vowels:
#         vowels[i]+=1

# print (vowels)

#Count a number digit counter
# num = {
#     '1':0,
#     '2':0,
#     '3':0,
#     '4':0,
#     '5':0,
#     '6':0,
#     '7':0,
#     '8':0,
#     '9':0,
#     '10':0
# }
# nums=input("Enter a number: ")

# for i in nums:
#     if i in num:
#         num[i]+=1

# print (num)

#### Nested dictionaries
# classroom={
#     'Alex':{'Age':16, 'Marks':[98,99,100,56,34,22,62,88]},
#     'Peter':{'Age':18, 'Marks':[45,45,46, 75,86,49,28,82,92]}
# }

# print(classroom)

###### Homework

subjects={
    'French': {'Teacher': 'Ms Weddell', 'Confidence': 'medium', 'Marks': [89, 98, 67,47,99,100]},
    'Maths': {'Teacher': 'Dr McCarthy', 'Confidence': 'high', 'Marks': [89, 99, 97, 94, 93, 100]},
    'Geography': {'Teacher': 'Mr Burn', 'Confidence': 'low', 'Marks': [34, 54, 75, 98, 56, 66]},
    'Irish': {'Teacher': 'Ms Regan', 'Confidence': 'low', 'Marks': [34, 63, 34, 64, 64, 23, 43]},
    'History': {'Teacher': 'Dr Tuite', 'Confidence': 'medium', 'Marks': [33, 30, 76, 86, 84, 45, 56]}
}
print (subjects)
