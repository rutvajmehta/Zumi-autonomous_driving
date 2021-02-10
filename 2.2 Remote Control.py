#!/usr/bin/env python
# coding: utf-8

# <img src="../Data/images/ZumiHeader.png" width=700>

# # Remote Control
# Now that you understand drive commands, you can write your own remote control! First, import the Zumi library and create the object before you begin.
# 
# ### Import libraries

# In[ ]:


from zumi.zumi import Zumi
import time

zumi = Zumi()


# ## User input
# To make a remote control, you need a way to register your input and translate it to motor commands. Python includes a function ```input()``` that reads the keyboard input and saves it as a variable. To see how this works, run the following code, type in your name, and hit enter. Any input that you entered will be saved in ```my_name```.
# 

# In[ ]:


my_name = input("What is your name? ")
print("Hello,",my_name)


# ## Pseudocode
# Now that you have all the tools you need, put it together in pseudocode, which is a program that’s written in plain language that a human can understand. Pseudocode is a good way to figure out how your program will work before translating it to Python. One small problem: ```input()``` can’t read arrow key controls, so your remote control code will be checking for letter inputs "w", "a", "s", and "d". 
# Look at the pseudocode below to see what we mean.
# 
# ```
# get input from user
# if input is "w", go forward
# if input is "s", reverse
# if input is "a", turn left
# if input is "d", turn right
# ```
# ![keys](../Data/images/keys_wasd.png)

# ## Translate to Python
# Translate your pseudocode to Python code. Before inputting drive commands, use print statements for testing. In the cell below, one if statement is done for you. If you want, you can change the variable names or the input statements. Make sure to test your code.
# 

# In[ ]:


#TODO Finish the rest of the missing if statements

while True:
    direction = input("Please enter a command: ")

    if direction == "w":
        print("Go forward")


# Did you notice the code is running forever? Because this is a remote control code, you want to be able to continuously tell Zumi what to do. To do this, you need to use a while loop that runs forever. Currently, the only way to stop the code is by clicking the "stop" icon in the toolbar. To safely quit from this loop, it is better to include an if statement that checks for "q" input to break from the loop.
# 
# ```
# if direction =="q":
#     break
# ```
# 
# Add this code to your code above and test that you can exit your code without errors.
# 
# ## Add drive commands
# Now that you have the logic down, add the drive commands with the correct command. The final code should look something like this:

# In[ ]:


while True:

    direction = input("Please enter a command")

    if direction == "w":
        zumi.forward()
    elif direction == "s":
        zumi.reverse()
    elif direction == "a":
        zumi.turn_left(90)
    elif direction == "d":
        zumi.turn_right(90)
    elif direction == "q":
        break


# Remember you can change the parameters for these controls or choose different keys to customize your remote control!
