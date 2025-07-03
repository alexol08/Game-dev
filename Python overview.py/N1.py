# print ("Hello world")

# if 5>2:
#      print("5 is greater than two")

# x=5
# x="John"
# y=bool(5)
# print(x)
# print(y)

# x,y,z = "orange", "banana", 'cherry'
# print (x)
# print (y)
# print (z)

# fruits =['apple', 'orange', 'cherry']
# x,y,z =fruits
# print (x)
# print (y)
# print (z)

# x='Python'
# y='is'
# z='awesome'
# print (x + y + z)
# print (x, y, z)

# x=5
# y=10
# print(x+y)

# x=5
# y='John'
# print(x,y)

# x = 'awesome'
# def myfunc():
#     global x
#     x='fantastic'
# myfunc()

# print('Python is '+x)

# x='awesome'
# def myfunc2():
#      global x
#      x='fantastic'
# myfunc2()
# print('Python is '+x)

# x=y=z ='Hello world'
# print (x)
# print (y)
# print (z)

# a=True
# b=False
# print(a and b)

# x=5
# y=10
# print (x<y)
# print (x==y)

# s='hello'
# b=s.encode('utf-8')
# print (b)

# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex

# #convert from int to float:
# a = float(x)

# #convert from float to int:
# b = int(y)

# #convert from int to complex:
# c = complex(x)

# print(a)
# print(b)
# print(c)

# print(type(a))
# print(type(b))
# print(type(c))

# for x in 'banana': 
#      print (x)
# print (len('banana'))

# txt = "The best things in life are free!"
# print("free" in txt)


# txt = "The best things in life are free!"
# if "free" in txt:
#   print("Yes, 'free' is present.")


# txt = "The best things in life are free!"
# if "expensive" not in txt:
#   print("No, 'expensive' is NOT present.")

# b = "Hello, World!"
# print(b[2:5])

# b = "Hello, World!"
# print(b[:5])

# b = "Hello, World!"
# print(b[2:])

# b = "Hello, World!"
# print(b[-5:-2])

# a = "Hello, World!"
# print(a.upper())

# a = "Hello, World!"
# print(a.lower())

# a = " Hello, World! "
# print(a.strip()) # returns "Hello, World!"

# a = "Hello, World!"
# print(a.replace("H", "J"))

# a = "Hello, World!"
# print(a.split(","))

# a = "Hello"
# b = "World"
# c = a + b
# print(c)

# age = 36
# txt = f"My name is John, I am {age}"
# print(txt)

# price = 59
# txt = f"The price is {price:.2f} dollars"
# print(txt)

# txt = f"The price is {20 * 59} dollars"
# print(txt)

# txt = "We are the so-called \"Vikings\" from the north."
# print (txt)

# def myFunction() :
#   return True
# print(myFunction())
# x=5
# x |= 3

# thislist = ["apple", "banana", "cherry"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))

# mylist = ["apple", "banana", "cherry"]
# print(type(mylist))

# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)

# thislist = ['apple', 'banana', 'cherry']
# print(thislist[1])

# thislist = ["apple", "banana", "cherry"]
# print(thislist[-1])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])

# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")

# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3]=['blackcurrant', 'watermelon']
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)

# thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
# thislist.remove('banana')
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)

# ''' if you do not specify index it will just
# get rid of the last item'''

# thislist = ["apple", "banana", "cherry"]
# del thislist[0] # You can delete the whole list by just leaving the name
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)

# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])

# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   print(i)
#   i = i + 1

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist=[]
# for x in fruits: 
#   if 'a' in x: 
#     newlist.append(x)
# print (newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]
# print(newlist)

# newlist = [x for x in range(10)]
# print (newlist)

# newlist = [x for x in range(10) if x < 5]
# print(newlist)

# newlist = [x.upper() for x in fruits]
# print(newlist)

# newlist = ['hello' for x in fruits]
# print(newlist)

# newlist = [x if x != "banana" else "orange" for x in fruits]
# print(newlist)

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist)

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)

# def myfunc(n):
#   return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)

# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist[:]
# print(mylist)

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# list3=list1+list2
# print(list3)

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# list1.extend(list2)
# print(list1)

# thistuple = ("apple", "banana", "cherry")
# print(thistuple)

# thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(thistuple)

# thistuple = ("apple",)
# print(type(thistuple))

# #NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))

# thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
# print(thistuple)

# thistuple = ("apple", "banana", "cherry")
# print(thistuple[1])

# ''' You are albe to do negative indexing on a tuple like you would with a list'''

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:5])

# '''All the things with this such as ranges are the same as with lists'''

# thistuple = ("apple", "banana", "cherry")
# if "apple" in thistuple:
#   print("Yes, 'apple' is in the fruits tuple")

# x = ("apple", "banana", "cherry")
# y = list(x) ## You convert the tuple to a list change it and then convert it back
# y[1] = "kiwi"
# x = tuple(y)
# print(x)

# thistuple = ("apple", "banana", "cherry")
# y = ("orange",) ## You can make another tuple with an element and then add it to the other tuple
# thistuple += y
# print(thistuple)

# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y) ## You can remove the items the same way

# thistuple = ("apple", "banana", "cherry")
# del thistuple ##You can delete tuples entirely

# fruits = ("apple", "banana", "cherry")

# (green, yellow, red) = fruits

# print(green)
# print(yellow)
# print(red) ## They collect the values from the tuple

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (green, yellow, *red) = fruits ## With the asterix the variable will collect the remaining variables as a list
# print(green)
# print(yellow)
# print(red) 

# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
# (green, *tropic, red) = fruits
# print(green)
# print(tropic)
# print(red)
# ## If the asterisk is added to another variable name than the last, 
# ## Python will assign values to the variable until the number of values left matches the number of variables left.

# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
#   print(x)
# ''' Again you can loop through tuples as you would
# loop through lits e.g. using range and len, using a while loop'''

# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2
# print(tuple3)

# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2
# print(mytuple)

# ''' count() - returns the number of times a value occurs in a tuple
# index() - searches for a specific value and gives the position of where it was found'''

### They are the same as lists except they are immutable

# ''' sets are used to store multiple items in a single variable and it is unordered, unindexed, and items are unchangeable but you can add/remove items still
# They also do not allow duplicate values'''

# thisset = {"apple", "banana", "cherry"}
# print(thisset) ## They are written with curly brackets

# thisset = {"apple", "banana", "cherry", "apple"}
# print(thisset) ## Duplicates will be ignored

# thisset = {"apple", "banana", "cherry", True, 1, 2}
# print(thisset) ## True and 1 are considered the same value

# thisset = {"apple", "banana", "cherry", False, True, 0}
# print(thisset) ## False and 0 are considered the same value

# thisset = {"apple", "banana", "cherry"}
# print(len(thisset)) ## Use len to get number of items

# thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
# print(thisset) ## Using a set constructor to make a set

# thisset = {"apple", "banana", "cherry"}
# for x in thisset:
#   print(x)

# print("banana" in thisset)
# print("banana" not in thisset)

# thisset = {"apple", "banana", "cherry"}
# thisset.add("orange")
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}
# thisset.update(tropical)
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}
# thisset.update(tropical) ## You can add any iterable
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# thisset.remove("banana")
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# thisset.discard("banana")
# print(thisset) ## An error will not be raised when using discard() and the element does not exist however
# ## An error will happen if you are trying to remove an element that does not exist with remove()

# thisset = {"apple", "banana", "cherry"}
# x = thisset.pop() ## You can use pop() however it will just remove a random item
# print(x)
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# thisset.clear() ## The clear() function just empties the set
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# del thisset ## The delete() function deletes the set
# # print(thisset)

# ## You can loop through set items using a for loop
# thisset = {"apple", "banana", "cherry"}
# for x in thisset:
#   print(x)

# '''' union() and update() just joins all items from both sets
#      intersection() only keeps the dupicates from the sets
#      difference() keeps the items from the first set that are not in the other set
#      symmetric_difference() keeps all items except duplicates'''

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set1.union(set2)
# print(set3)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set1 | set2 ## This will still get you the same results as union()
# print(set3)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3} ## Helping you join multiple sets
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}
# myset = set1.union(set2, set3, set4)
# print(myset)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}
# myset = set1 | set2 | set3 |set4
# print(myset)

# x = {"a", "b", "c"}
# y = (1, 2, 3) ## Allows you to join a set with other data types - you cannot use |
# z = x.union(y)
# print(z)

# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3} ## The update() method inserts all items from one set to another; changing the original set and not making a new one
# set1.update(set2)
# print(set1)

# ## Both union() and update() will exclude duplicates

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.intersection(set2) ## Returns only items present in both sets
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1 & set2 ## You can use the & operator as well but intersection() allows you to do it between iterables
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.intersection_update(set2) ## Only allows duplicates and it will update the original set
# print(set1)

# set1 = {"apple", 1,  "banana", 0, "cherry"}
# set2 = {False, "google", 1, "apple", 2, True}
# set3 = set1.intersection(set2) ## True and 1 as well as False and 0 are considered duplicates
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.difference(set2) ## Difference() will return a new set that will only contain items that are present in the first set that are not present in the second set
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1 - set2 # You can use the - operator to do the same thing but again difference can be used with other data types
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.difference_update(set2)
# print(set1) ## It will also keep the items from the first set and not in the second set however it will change the original set not make a new one

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.symmetric_difference(set2) ## Will only keep items not present in both sets
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1 ^ set2 ## Same thing as symmetric_difference however only works with sets and not other data types --- ^
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.symmetric_difference_update(set2)
# print(set1) ## Updates origial set instead of making a new set

''' Dictinaries are used to stor data values in key: value pairs. It is a collection 
     which is ordered, changable, and do nto allow duplicates in keys - they are 
     written with curly brakets and have keys and values'''

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

## There is a defined order and it will not change however there is no index
## Dictionaries are chanagable - you are able to change, add, remove after the dictionary has been made
##They cannot ahve two items with the same key

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

print(len(thisdict)) ## Use len() to find how many items are in dictionaries

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(type(thisdict))
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict) ##Using a sict() constructor]

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"] ## You can acces items by using their key name in square brackets

x = thisdict.get("model") # They get() function will get you the same result

x = thisdict.keys() ## This will return a list of all the keys in the dictionary

car = {
"brand": "Ford",
"model": "Mustang", ## This is a new key value pair being added to the dictionary
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change

x = thisdict.values() ## This returns a list of all the values in the dictionary

car = {
"brand": "Ford",
"model": "Mustang", ## Change being done to the value of an existing key
"year": 1964
}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change

x = thisdict.items() ## Will return each item in a dictionary as tuples in a list
print(x)

thisdict = {
  "brand": "Ford",
  "model": "Mustang", ## Checks if a key exists within a dictionary
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

thisdict = {
  "brand": "Ford", ## This is how you change the value of a specific item by referring to its key name
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

thisdict = {
  "brand": "Ford",
  "model": "Mustang", ## update() method by updating a dictionary
  "year": 1964
}
thisdict.update({"year": 2020})

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict) ## Adding an item to a dictionary by using a new index key and assigning a value

thisdict = {
  "brand": "Ford",
  "model": "Mustang", ## The update() can be used to add iems as well if the item does not exist
  "year": 1964
}
thisdict.update({"color": "red"})

thisdict = {
  "brand": "Ford",
  "model": "Mustang", ## The pop() method removes the item with a specified key name
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang", ## The popitem() method removes the last inserted item
  "year": 1964
}
thisdict.popitem()
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang", ## This deletes the item with the specified name
  "year": 1964
}
del thisdict["model"]
print(thisdict) 

thisdict = {
  "brand": "Ford",
  "model": "Mustang", ## The del keyword can also delete the dictionary completely
  "year": 1964
}
del thisdict

thisdict = {
  "brand": "Ford",
  "model": "Mustang", ## The clear() method empties the dictionary
  "year": 1964
}
thisdict.clear()
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang", 
  "year": 1964
}
for x in thisdict: ## You can loop with a for loop - the return values are the keys of the dictionary
  print(x)

for x in thisdict: ## Gives all values of the dictionary
  print(thisdict[x])

for x in thisdict.values():## You can use the values() method to return values of a dicionary
  print(x)

for x in thisdict.keys():## You can use the keys() method to return keys of a dicionary
  print(x)

for x, y in thisdict.items(): ## Prints both keys and values using the items() method
  print(x, y)

'''You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
     There are ways to make a copy, one way is to use the built-in Dictionary method copy().'''
  
thisdict = {
  "brand": "Ford",
  "model": "Mustang", ## Making a copy with the copy() function
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang", ## Make a copy with the dict function
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

## A dictionary can contain other dictionaries called nested dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
child1 = {
  "name" : "Emil",
  "year" : 2004 ## 3 dictionaries are created and then one dictionary is made containing the others
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily["child2"]["name"]) ## this is how you access items in nested dictionaries

for x, obj in myfamily.items():
  print(x)
  for y in obj: ## This is how to loop through all the keys and values of the nested dictionaries
    print(y + ':', obj[y])

'''clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary'''