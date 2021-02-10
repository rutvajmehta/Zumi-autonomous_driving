#!/usr/bin/env python
# coding: utf-8

# <img src="../Data/images/ZumiHeader.png" width=700>

# # Gyroscope
# When you made your remote control, Zumi turned left or right using the number of degrees that you gave as a parameter. How does Zumi know how many degrees she is turning? Zumi is equipped with an **MPU**, or motion processing unit, and has two very important sensors that are necessary for driving straight and making accurate turns: the **gyroscope** and **accelerometer**. This lesson is about the gyroscope. You’ll learn about the accelerometer later!
# 
# 
# ## What is a gyroscope?
# A gyroscope is a device that measures rotation speed. Gyroscopes are important because we need rotation speed to calculate how many degrees Zumi has turned.
# 
# You’re probably wondering why rotation speed is necessary to figure out how much Zumi has turned. Think about how you calculate distance when you're in a car. If Zumi was going 50 miles per hour for 2.5 hours, how far did she travel?
# 
# Multiply 50 by 2.5 and you get 125 miles. So to get distance, you multiply the amount of time traveled by the speed.
# 
# Using this logic, you can find out how many angles you've "traveled" as long as you know how many angles you’ve traveled over time, which is given by the gyroscope as the rotational speed.
# 
# Don't worry about the math behind the concept! In this lesson, you’ll be learning how to use the heading function in forward, reverse, left, and right.
# 
# To access gyroscope values, you’ll need the Zumi object and the screen object for displaying values.
# 
# ### Import libraries

# In[ ]:


from zumi.zumi import Zumi
from zumi.util.screen import Screen
import time

zumi = Zumi()
screen = Screen()


# ### Axes
# There is more than one axis that you can use to measure rotational speed. The main axis is for turning left and right, but you can also measure if Zumi is tilting forward and backward or tilting left and right.
# 
# There are three codes below reading all three axes: X, Y, and Z. Run each one and check Zumi's screen to figure out which is which!
# 
# #### X angle

# In[ ]:


for i in range(0,50):
    current_angle = int(zumi.update_angles()[0])
    message = " X Angle reading        "
    message = message + str(current_angle)
    screen.draw_text(message)
    time.sleep(0.1)
    
print("Done")
screen.draw_text("  Done")


# #### Y angle

# In[ ]:


for i in range(0,50):
    current_angle = int(zumi.update_angles()[1])
    message = " Y  Angle reading        "
    message = message + str(current_angle)
    screen.draw_text(message)
    time.sleep(0.1)
    
print("Done")
screen.draw_text("  Done")


# #### Z angle

# In[ ]:


for i in range(0,50):
    current_angle = int(zumi.update_angles()[2])
    message = " Z Angle reading        "
    message = message + str(current_angle)
    screen.draw_text(message)
    time.sleep(0.1)
    
print("Done")
screen.draw_text("  Done")


# Based on the data, could you figure out which directions correspond to X, Y, and Z?
# 
# 
# * The first cell reads the Z-axis, otherwise known as **yaw**. Yaw is the left and right turning of Zumi.
# * The second cell reads the X-axis, otherwise known as **roll**. Roll is the tilt to the right or to the left.
# * The final cell reads the Y-axis, otherwise known as **pitch**. Pitch is the tilt forward or backward.
# 
# For the purposes of driving, you will care the most about the Z-axis, or yaw, of Zumi's gyroscope. It's so important that there's a function just for reading the current Z-angle. If at any time you want to know which how many degrees off you are from when you initialized the Zumi object, you can run the following code.
# 

# In[ ]:


for i in range(100):
    z_angle = int(zumi.read_z_angle())
    message = " Z Angle reading        "
    message = message + str(z_angle)
    screen.draw_text(message)
    time.sleep(0.1)


# If the angles seem like they are all over the place, you may need to do a recalibration. Sometimes you may need to manually reset the gyro angles.

# In[ ]:


zumi.mpu.calibrate_MPU()

# Reset the angles to zero them out
zumi.angle_list = [0,0,0,0,0,0,0,0,0,0]

# Try the code again
for i in range(100):
    z_angle = int(zumi.read_z_angle())
    message = " Z Angle reading        "
    message = message + str(z_angle)
    screen.draw_text(message)
    time.sleep(0.1)

