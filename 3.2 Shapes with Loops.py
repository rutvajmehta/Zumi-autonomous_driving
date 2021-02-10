#!/usr/bin/env python
# coding: utf-8

# <img src="../Data/images/ZumiHeader.png" width=700>

# # Shapes with Loops
# Now that you know how to use the gyroscope, you can to use the data to drive in different shapes! Shapes are two-dimensional figures made of straight or curved lines. Usually, certain shapes have a set number of degrees that the angles add up to. For example, circles’ and squares’ angles both add up to 360°, while a triangle’s angles add up to 180°.
# 
# ![shapes](../Data/images/shapes.png)
# 

# ## Square
# Start with a square. To drive in a square, you need to make four right or left turns. If you think back to the last lesson about gyroscopes, Zumi’s gyroscope relies on a heading. Remember to import your libraries and create the objects before running the code!
# 
# 
# ### Import libraries 

# In[ ]:


from zumi.zumi import Zumi
import time

zumi = Zumi()


# ### Square code
# Since a square has four sides, you will be writing the same set of code four times. 

# In[ ]:


zumi.forward()
zumi.turn_left()
zumi.forward()
zumi.turn_left()
zumi.forward()
zumi.turn_left()
zumi.forward()
zumi.turn_left()


# If you want to make a bigger square, you can modify the duration of ```forward()```. It’s a good idea to create a variable for this value so that you can quickly change all of your code at once. Try changing the value of ```seconds``` to make bigger squares!

# In[ ]:


seconds=2

zumi.forward(duration=seconds)
zumi.turn_left()
zumi.forward(duration=seconds)
zumi.turn_left()
zumi.forward(duration=seconds)
zumi.turn_left()
zumi.forward(duration=seconds)
zumi.turn_left()


# ## Loops
# You have probably noticed that you repeat the same section of code four times. To get around this, you can use a loop, which lets you repeat parts of your code. They're a great shortcut --- without them, you might have to write the same lines over and over again. 
# In this lesson, you'll be learning about while loops and for loops. Both of them are conditional loops, so they repeat only for as long the condition that you set is true.
# 
# ### For loops
# A for loop will repeat for a specific number of times that you set. The conditional statement for a for loop follows a very specific format that looks intimidating, but we'll break it down!
# 
# ```
# for private_variable in range(minimum, maximum, increment or decrement):
#        write statements here
# ```
# 
# Private variables are variables that you only use for the loop and nothing else. In the example below, x is the private variable and is initialized to zero. The loop prints the value of x and then will increase, or increment,  x by 1 after each iteration.
# 

# In[ ]:


for x in range(0, 10, 1):
    print(x)


# Did you see that 10 wasn’t printed? That’s because it was the maximum limit. When the private variable, which is x in our example, reaches the maximum limit, it does not print it or go past it.
# 
# Python automatically starts a for loop at 0 and increments by 1 by default, so you can also leave these parameters out and achieve the same result:
# 

# In[ ]:


for x in range(10):
    print(x)


# You can also count down, or decrement, with a negative third parameter:

# In[ ]:


for j in range(9, -1, -1):
    print(j)


# ### Square with loop
# Now that you know how to use loops to repeat a section of code, rewrite the square code from the beginning of this lesson using a for loop.

# In[ ]:


for i in range(4):
    zumi.forward()
    zumi.turn_left()


# ### Square with loop and heading
# There is another way to make the same square using heading.
# 

# In[ ]:


initial_heading = zumi.read_z_angle()
for angle in range(0, 360, 90):
    zumi.forward()
    zumi.turn(initial_heading + angle)


# ### Triangle with loop
# A square is pretty simple because every turn is 90 degrees. What if you want to drive in an equilateral triangle?
# 
# You may initially try turning 60 degrees for three iterations, but if you try this out Zumi will not drive in a triangle.
# 
# Hint* In our square code, we turned a total of 360 degrees.
# 

# In[ ]:


# Write your code here for a triangle


# ### Circle with loop
# For this case, think of a circle as a shape with 360 "sides". To create a circle, first we need to 
# find the angle Zumi is facing this will be our starting point for our circle. Then we run a for loop from 0 to 361 increasing the angle by 4 every time. Decreasing the third parameter will result in a bigger circle.

# In[ ]:


init_ang_z = zumi.read_z_angle()

for i in range(0, 361, 4):
    zumi.go_straight(30, init_ang_z-i)
    time.sleep(0.02)
zumi.stop(0)


# Try to write code for a counterclockwise circle:

# In[ ]:


# Write your code for a counterclockwise circle


# There are many other shapes you can teach Zumi. Try pentagons, hexagons, or octagons. You can also attach a marker to Zumi's trunk and drive on a big piece of paper. 

# In[ ]:


# Space for more code here!

