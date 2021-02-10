#!/usr/bin/env python
# coding: utf-8

# <img src="../Data/images/ZumiHeader.png" width=700>

# # Intermediate Driving Commands
# 
# In the last lesson, you learned how to use for loops to make your own shapes. The Zumi library has many of these shapes and other maneuvers programmed for you so that Zumi can operate just like a real self-driving car!
# 
# 
# ### Import libraries 

# In[ ]:


from zumi.zumi import Zumi
import time
zumi = Zumi()


# ### Drive functions
# 
# Remember when you learned about ```forward()```? Even though it set Zumi to drive at a set speed of 40 for one second in the current direction, you could also change these values. The function all listed below are all listed with their default parameters. If you call a function by name, such as ```right_u_turn()```, Zumi will do the u-turn with the defined parameters. However, just like with ```forward()```, you can change these to whatever values you would like. 
# 
# * ```right_u_turn(speed=30, step=4, delay=0.02)```
#         speed: the forward speed you want Zumi to drive at
#         step: the angle step size as it goes from (0 - 180)
#         delay: the delay between each angle step
# 
# * ```left_u_turn(speed=30, step=4, delay=0.02)```
#         speed: the forward speed you want Zumi to drive at
#         step: the angle step size as it goes from (0 - 180)
#         delay: the delay between each angle step
# 
# * ```circle(speed=30, step=2, direction=1, delay=0.02)```
#         speed: the forward speed you want Zumi to drive at
#         step: the angle step size as it goes from (0 - 360)
#         direction: -1 for clockwise , +1 for counterclockwise
#         delay: the delay between each angle step
# 
# * ```right_circle(speed=30, step=2)```
#         speed: the forward speed you want Zumi to drive at
#         step: the angle step size as it goes from (0 - 360)
# 
# * ```left_circle(speed=30, step=2)```
#         speed: the forward speed you want Zumi to drive at
#         step: the angle step size as it goes from (0 - 360)
# 
# * ```square(speed=40, seconds=1, direction=1)```
#         speed: the forward speed you want Zumi to drive at
#         seconds: the duration Zumi will drive for each side
#         direction: -1 for clockwise , +1 for counterclockwise      
# 
# * ```square_right(speed=40, seconds=1.0)```
#         speed: the forward speed you want Zumi to drive at
#         seconds: the duration Zumi will drive for each side
# 
# * ```square_left(speed=40, seconds=1.0)```
#         speed: the forward speed you want Zumi to drive at
#         seconds: the duration Zumi will drive for each side
# 
# * ```j_turn(speed=100, step=4, delay=0.005)```
#          speed: the forward speed you want Zumi to drive at
#          step: the angle step size
#          delay: the delay between each angle step
# 
# * ```figure_8(speed=30, step=3, delay=0.02)```
#          speed: the forward speed you want Zumi to drive at
#          step: the angle step size as it goes from (0 - 360)
#          delay: the delay between each angle step
# 
# * ```parallel_park(speed=15, step=1, delay=0.01)```
#         speed: the forward speed you want Zumi to drive at
#         step: the angle step size as it turns
#         delay: the delay between each angle step
# 
# * ```rectangle(speed=40, seconds=1.0, direction=1, ratio=2)```
#         speed: the forward speed you want Zumi to drive at
#         seconds: the duration Zumi will drive for the shorter side
#         direction: -1 for clockwise , +1 for counterclockwise 
#         ratio: the ratio of the longer side to the shorter side
#          
# 
# * ```triangle(speed=40, seconds=1.5, direction=1)```
#         speed: the forward speed you want Zumi to drive at
#         seconds: the duration Zumi will drive for each side
#         direction: -1 for clockwise , +1 for counterclockwise      
#          
#          
# Let's see an example of these in action!

# In[ ]:


zumi.figure_8() # Runs figure 8 at default values
time.sleep(1)
zumi.figure_8(speed = 50) # Changing one value
time.sleep(1)
zumi.figure_8(step=4, delay=0.03) # Changing two values
time.sleep(1)
zumi.figure_8(speed=40, step=4, delay=0.03) # Changing all three values


# Test out some of these drive functions in the cell below. Just know that as you change the parameters, you may need more space. We recommend that you drive Zumi on the floor and keep an eye on it while it’s driving.

# In[ ]:



# Write code here!

