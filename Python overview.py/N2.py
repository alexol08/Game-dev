'''Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.'''

a = 33
b = 200 ## an 'if statement' is written using the if keyword
if b > a:
  print("b is greater than a")

a = 33 ## The 'elif' keyword is Pythons command saying if the previous conditions were not true - try this condition
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

a = 200 ## The else keyword means that an action will happen if anything is triggered with previous conditions
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

if a > b: print("a is greater than b") ## If you only have one statement to execute - put it on the same line as the if statement

a = 2 ## If you only have one statement to execute for if and else then you can put it on the same line
b = 330
print("A") if a > b else print("B")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

a = 200
b = 33 ## And is a logical operator and is checks if both the conditions are met
c = 500
if a > b and c > a:
  print("Both conditions are True")

a = 200 ## or is a logical operator and is checks whether one of the conditions are met
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

a = 33 ## not is a logical operator and is used to mean the reverse of a conditional statement
b = 200
if not a > b:
  print("a is NOT greater than b")

x = 41 ## If statements that have if statements inside are known as as nested if statements
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

'''if statements cannot be empty, but if you for some reason have an if statement with no content, 
put in the pass statement to avoid getting an error.'''

a = 33 ## If statements cannot be empty -- use pass to avoid an error if you have no content
b = 200
if b > a:
  pass

## The match statement is used to preform different actions based on different conditions
## Instead of writing a lot of if... else statements, you can use the match statement
## The match statement selects one of many code blocks to be executed

# match expression: ## Example
#   case x:
#     code block
#   case y:
#     code block
#   case z:
#     code block

'''This is how it works:

The match expression is evaluated once.
The value of the expression is compared with the values of each case.
If there is a match, the associated block of code is executed.'''

day = 4
match day: ## This is how you can use the weekday number to print the weekday name
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")

day = 4 ## The underscore is last case value if you want a code block to execute when there are no other matches
match day: ## The value _ will always match so it is important to use it as the last case and make it behave as the default
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")

day = 4 ## The pipe character (shift + \) | is used as an or operator in the case evaluation to check for more than one value in one case
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")

month = 5 ## You can add if statements in the case evaluation as an extra condition check
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")

## Python has two primitive loops - for and while

i = 1 ## The while loop will execute statements as long as a condition is true
while i < 6:
  print(i)
  i += 1

i = 1 ## The break statement stops the loop even if the condition is true
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

i = 0 ## The continue statement stops the current iteration e.g. for/while and moves on to the next one
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

i = 1 ## The else statment can be run after the condition is no longer true
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

'''A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.'''

fruits = ["apple", "banana", "cherry"]
for x in fruits: ## prints the list
  print(x)

for x in "banana": ## Strings are iterable objects as they have a sequence of characters
  print(x) ## Looping through the letters of banana

fruits = ["apple", "banana", "cherry"]
for x in fruits: ## The break statement can stop the loop before it has finished
  print(x) ## E.g. stopping at banana insteading of going through the whole list
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"] ## The break comes before the print - stops before banana
for x in fruits:
  if x == "banana":
    break
  print(x)

fruits = ["apple", "banana", "cherry"] ## Stops the current iteration and goes on to the next iteration e.g. for, while
for x in fruits:
  if x == "banana":
    continue
  print(x)

'''To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.'''

for x in range(6):
  print(x) ## includes values 0-5; does not include last number

for x in range(2, 6): ## It defaults as 0 but you can specify the starting value
  print(x) ## Prints 2 to 6 (not including six)

for x in range(2, 30, 3): ## Defult increment in the sequence if 1 but you can specify it with a third parmater
  print(x) ## This goes in increments of 1

for x in range(6): ## else statement will be executed when loop has finished - it will not be executed if stopped by a break statement
  print(x)
else:
  print("Finally finished!")

for x in range(6):
  if x == 3: break ## Else not executed
  print(x)
else:
  print("Finally finished!")

## A nested loop is a loop inside a loop. The "inner loop" will be executed one time for each iteration of the "outer loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)

for x in [0, 1, 2]:
  pass ## for loops cannot be empty; if you have a for loop with no content; use the pass statement to avoid getting an error

'''A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.'''

def my_function(): ## A function is defined using the def keyword
  print("Hello from a function")
my_function() ## To call a function just use the function name with parenthesis

'''Information can be passed into functions as arguments.
Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
The following example has a function with one argument (fname).
 When the function is called, we pass along a first name, which is used inside the function to print the full name:'''

def my_function(fname): ## fname is the paramater - a placeholder for the argument
  print(fname + " Refsnes")
my_function("Emil") ## This is the argument in the function brackets
my_function("Tobias")
my_function("Linus")

## Arguments are often shortened to args
'''The terms parameter and argument can be used for the same thing: information that are passed into a function.
From a function's perspective:
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the value that is sent to the function when it is called.'''

#By default, a function must be called with the correct number of arguments. 
# Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

def my_function(fname, lname): ## The function excepts 2 arguments because of 2 paramaters -- it gets those args
  print(fname + " " + lname) ## You will get an error if this is not the case
my_function("Emil", "Refsnes")

def my_function(*kids): ## Use * if you do not know the number of arguments - the function will receive a tuple of args
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

##You can also send arguments with the key = value syntax.
##This way the order of the arguments does not matter.