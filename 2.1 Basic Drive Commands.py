#!/usr/bin/env python
# coding: utf-8

# <img src="../Data/images/ZumiHeader.png" width=700>

# <img src="../Data/images/lessonsicon.png" width=80 align="left">
# 
# # Basic Drive Commands
# 
# In the past lesson, Zumi learned how to obey traffic lights **autonomously**, which means that she was behaving without any human input or assistance. However, now Zumi needs help from you to learn how to go forward, reverse, left, and right. You will be making a custom remote control with if statements and your keyboard. First, you need to learn how to drive Zumi.
# 
# 
# ### Import libraries and create objects
# You only need to run the following cell once unless you restart the Jupyter Notebook.

# In[1]:


from zumi.zumi import Zumi
import time

zumi = Zumi()


# ## Drive Commands
# 
# In the past, you saw Zumi drive straight and stop for green and red cards. In this lesson, we will go more in-depth with what functions are, what they do, and how you can use them to create your remote control.
# 
# 
# ### What are functions?
# To make Zumi drive, we need to use some functions. These are sections of code that are already written so that you can use them to make your program more efficient. Zumi has a lot of functions that you can use! For example, the Red Light Green Light program used functions ```go_straight()``` and ```stop()```.
# 
# 
# ### Zumi functions
# Below is a list of the basic commands that you will use for your remote control program along with how they work:
# 
# * ```forward()```: Drive forward in the direction Zumi is facing at speed 40 for 1 second
# * ```reverse()```: Reverse in the direction Zumi is facing at speed 40 for 1 second
# * ```turn_left()```: Turn 10 degrees to the left
# * ```turn_left()```: Turn 10 degrees to the right 
# 
# 
# ### How to call functions
# In computer science, calling anything is basically asking it to run. Functions must be called using the object name, which in this case is zumi. The cell below has an example using the ```forward()``` function. Zumi will drive forward for one second, so make sure you have enough space in its area!
# 

# In[36]:


zumi.right_circle()


# Now try going in reverse...

# In[ ]:


# TODO Write code so Zumi reverses for 1 second
zumi.reverse(duration=5)


# Now that you have the hang of it, let's go over the next two functions. Calling ```turn_left()``` and ```turn_right()``` will cause Zumi to turn a little to the left or a little to the right.
# 
# Test this code below and then add more commands in any order to see what happens. If you want to have some time between each command, include a ```time.sleep(seconds)``` to delay the program for the specified number of seconds.
# Run the code below to see how this works, and then try adding some more commands to the code.
# 
# 

# In[29]:


zumi.forward() 
time.sleep(2)
zumi.turn_right()
zumi.forward(6)


# ### Parameters
# At this point, you may want to change the duration, direction, and speed that Zumi drives forward. Some functions will allow you to input parameters, which are extra pieces of information that allow you to further customize your function for your needs. Right now ```forward()``` has a default speed, duration, and direction, but you can alter the parameters to change how fast Zumi drives, as well as for how long in a certain direction. 
# 
# We’re going to skip changing Zumi’s direction since it requires some more understanding of Zumi's sensors, but you can change the speed and duration by defining them inside of the function call. In the cell below, the code has been modified to reduce the speed to 30 and drive for 2 seconds. Make sure you have enough space!
# 

# In[30]:


zumi.forward(speed=30, duration=2)


# You can do the same for reverse. Change the speed and duration for ```reverse()``` below:

# In[33]:


# TODO Modify reverse to go at speed 20 for 3 seconds


# ### Degrees
# The functions ```turn_left()``` and ```turn_right()``` also have parameters you can change. The default value is set to 10 degrees, but that value can be changed as well.
# 
# The code below will have Zumi turn right 90 degrees instead of 10:

# In[ ]:


zumi.turn_right(90)


# Use this diagram for reference if you need it! The angles only apply for turning right. If you are turning left, mirror the values and go counter-clockwise around the circle to find the right degree that you want.
# ![degrees](../Data/images/degrees.png)

# In[ ]:


# Test some code here


# <img src="../Data/images/lessonsicon.png" width=80 align="left">
# 
# ## Recalibrating
# If you find that Zumi isn't going straight, you may need to recalibrate. Make sure you aren't picking up Zumi and she is resting on a flat surface.

# In[ ]:


zumi.mpu.calibrate_MPU()


# Now you know the basics! Use the cell below to test out some more code. In the next lesson you will learn how to combine the drive commands with if statements to make your own remote control.

# In[ ]:


# Write some more code here!

