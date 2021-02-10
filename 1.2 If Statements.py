#!/usr/bin/env python
# coding: utf-8

# <img src="../Data/images/ZumiHeader.png" width=700>

# <img src="../Data/images/lessonsicon.png" width=80 align="left">
# 
# # If statements
# 
# <br />
# 
# ### What are if statements?
# If statements are conditionals, which are used to help your program make decisions. You actually use conditionals every day! Some examples might include:
# 
# * If my alarm goes off, then I will wake up. Else, I will stay asleep.
# * If I am hungry, I will eat something.
# * If it's sunny out, I will wear sunscreen.
# * If my room is clean, I will get my allowance. Else, I will make no money.
# 
# If statements are written like this:
# 
# ```
# if insert condition here:
#     Insert statements here
# else:
#     Insert statements here
# 
# if alarm goes off:
#     I will wake up
# else:
#     Stay asleep
# ```
# 
# The condition is what the computer checks to know if it is true or false.
# * If the condition is true, the computer will execute, or carry out, the statements underneath it.
# * If the condition is false, the computer will NOT execute the statements underneath it.
# * "Else” has no condition! This is because “else” is the last option when using if-else statements.  When a computer reaches the “else” option after checking all the other conditions, then the else condition is automatically true and will run its statements.
# * One way to use “else” would be when something needs to happen when a condition is false. When the "if" condition is false and nothing needs to happen, don’t use an “else”.
# 
# <img src="../Data/images/codingicon.png" width=80 align="left">
# 
# ### Indentation
# 
# Indentation is very important in the Python programming language. The indentations indicate which statements belong to a particular section in the code.
# 
# You may have noticed that the statements below the if and else statements are indented 4 spaces. Suppose you want to have multiple statements execute if a condition is true. Using proper indentation, it would look like this:
# 
# 

# In[ ]:


# Try modifying x to equal a different number
x = 4

if x == 4:
    print("X equals 4!")
else:
    print("x does not equal 4.")


# Try running the code below. What happens?

# In[ ]:


zumi = 100
bugs = 55
if zumi  > bugs:
print("Squish the bugs!")
if zumi + bugs > 90:
print("Run away!")


# **Your goal**: correct the example above by indenting the lines correctly. Rerun the code to check your work. Don't forget to modify the values of ```zumi``` and ```bugs```.
# 
# ### Comparators
# 
# In the previous example, you were introduced to a new symbol. The ```>``` sign is an example of a **comparator**, but you may know it from your math class as an inequality sign. Comparators can be used inside conditions to compare values. If the statement is true, the statement below it will execute. These are comparators:
# 
# 
# * \> Greater Than
# * \< Less Than
# * \>= Greater Than or Equal To
# * <= Less Than or Equal To
# * == Equal To
# * != Not Equal To
# 
# Run the cell below and make some changes to the conditionals to see how these work!

# In[ ]:


X = 10
Y = 100
Z = 200

if (X != Y):
    print("Correct, X is not equal to Y")
    
if (Z > Y):
    print("Correct, Z is greater than Y")


# ### Nested if statements
# 
# Nested if statements are useful in situations where you have multiple conditions for the same purpose or if you have follow-up questions. For example:
# 
# ```
# if it is sunny outside:
#     if it is hot:
#         I will go swimming
#     else:                        
#         I will play baseball
# else:                              
#     I will play inside
# ```
# 
# ### Programming Challenge
# Below is an **incorrect** example. Your goal is to correct the example by indenting correctly.
# The output for the bottom example should print ```Student receives a C```.
# 

# In[ ]:


Test = 75.50
A = 90
B = 80
C = 70
D = 60
F = 50
if Test == 100:
print("Automatic pass!")
if Test > A:
print("Student receives an A")
else:
if Test > B:
print("Student receives a B")
else:
if Test > C:
print("Student receives a C")
else:
if Test > D:
print("Student receives a D, please seek tutoring")
else:
if Test > F:
print("Student has failed, please seek tutoring")


# <img src="../Data/images/lessonsicon.png" width=80 align="left">
# 
# # Else If Statements
# 
# Pretend that you have two buttons: one button opens a door and one button closes the door. You also have code that will check if the buttons are pressed. Your first thought might be to write something like this:
# 
# ```
# if button 1 is pressed:
#     Close the door
# if button 2 is pressed:
#     Open the door
# ````
# 
# What happens if you press both at the same time? Both are true and the door would try and open and close at the same time!
# 
# Else if statements, written ```elif``` in Python, solve this problem. Once a condition is met, the code will not execute any of the other ```elif``` statements, no matter if they are true or not. Just like an if-else statement, if the code runs through all of the conditions and none are met, then the else statement will execute. It is a good idea to include an else statement in case of any errors or unexpected cases, but you don't need to.
# 
# Here's an example that demonstrates why you should use else-if statements. Imagine that you want to go see a movie and you need to buy tickets. The movie theatre has different ticket prices depending on your age. Children less than 5 years old enter for free. If you are a child less than 18 years old then you pay 8 dollars. If you are younger than 55 then you pay 12 dollars. Else, you pay the senior discounted price of 10 dollars.
# 
# If you are 15 years old, how much should your ticket cost? Your ticket should cost 8 dollars. Now run the code below
# that does not use ```elif``` statements. 

# In[ ]:


age = 15

if age < 5:
    price = 0
if age < 18:
    price = 8
if age < 55:
    price = 12
else:
    price = 10
    
print("Age: " + str(age))
print("Your ticket price: $" + str(price))


# What happened? The first conditional is false because 15 is not less than 5. The second conditional is true because 15 is less than 18, so the price of the ticket is set to 8 dollars. Since we were not using ```elif``` statements, the code would not stop there! It will check the next conditional, and since 15 is less than 55, the price would be set again and updated to 12 dollars. You would be overcharged for a movie! With elif statements, the code would find the second condition to be true and ignore the rest of the conditions.
# 
# You can try this out by changing the code above! Change the second and third if statements from ```if``` to ```elif```.
# 

# In[ ]:




