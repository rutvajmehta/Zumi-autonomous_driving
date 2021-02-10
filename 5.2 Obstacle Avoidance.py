#!/usr/bin/env python
# coding: utf-8

# <img src="../Data/images/ZumiHeader.png" width=700>

# # Obstacle Avoidance
# 
# Have you ever been in a car when the emergency auto brakes went on? What happened? How was the car able to tell when to stop? Self-driving cars need to be able to avoid obstacles in an emergency. Instead of infrared, they use more advanced sensors like **LIDAR** (Light Imaging Detection and Ranging) and **RADAR**. LIDAR uses laser light to map out the environment while RADAR uses radio waves. Despite not having this technology, Zumi can still avoid obstacles!
# 
# ### Import libraries

# In[ ]:


from zumi.zumi import Zumi
import time

zumi = Zumi()


# ### Pseudocode
# 
# Before going into code, let's discuss the pseudocode for this program. How should Zumi avoid obstacles?
# First think about how humans avoid obstacles. If something is on our right, we go left. If something is our left, we go right. If something is directly in front of us, we have to either turn around or go around by turning away from the obtacle. Zumi uses the IR sensors to "see" and will make a decision based on the sensor data:
# 
# ```
# read the data from IR sensors
# if both sensors are triggered, turn 180 degrees
# if right sensor is triggered, turn left
# if left sensor is triggered, turn right
# else keep going forward
# ```
# 
# Instead of turning when the sensor is trigged, we are actually going to change the heading by +30 or -30 degrees. You are going to use the same function from Red Light Green Light which is ```go_straight()``` because it needs to be continuously driving and checking. 
# 
# Therefore the pseudocode will look something like this:
# ```
# read the data from IR sensors
# if both sensors are triggered, reverse and change heading by 180 degrees
# if right sensor is triggered, change heading by +30 degrees (for a left turn)
# if left sensor is triggered, change heading by -30 degrees (for a right turn)
# go in the direction set by heading
# ```
# 
# Here it is translated into code:

# In[ ]:


heading = 0 # Initialize heading to 0

min_ir_threshold = 100 # Variable to hold the number value that indicates something is reflecting light
turn_degrees = 30 # Variable to hold the number of degrees you will turn Zumi by

time_start = time.time() # Get the current starting time
time_elapsed = 0 # Initialize how much time has passed to 0

while time_elapsed < 20: # while the timer is below 

    time_elapsed = time.time()-time_start # update time elapsed
    ir_readings = zumi.get_all_IR_data()
    front_right_ir = ir_readings[0]
    front_left_ir = ir_readings[5]

    if front_left_ir < min_ir_threshold and front_right_ir < min_ir_threshold:
        print("something ahead")
        zumi.stop(0)
        time.sleep(0.5)
        zumi.reverse(40, 0.5, heading)
        zumi.stop(0)
        time.sleep(0.5)
        
        heading = heading - 180
           
    elif front_right_ir < min_ir_threshold:
        print("something on right")
        heading = heading + turn_degrees

    elif front_left_ir < min_ir_threshold:
        print("something on left")
        heading = heading - turn_degrees

    zumi.go_straight(30, heading, 60)
    time.sleep(0.05)
zumi.stop(0)


# ###  Variable explanation
# 
# First, ```heading``` is set to ```0``` because the very first time Zumi encounters an object it will reverse in the original direction. However, you have a variable to keep track of it because Zumi will constantly be turning around to avoid obstacles. Your heading will not be *constant*.
# 
# ```heading = 0```
# 
# Second, this code uses a timer which will automatically stop when the desired time limit is up.
# The variable ```time_elapsed``` is initialized to ```0``` and ```time_start``` to the current time, which you can grab with the ```time.time()``` function.
# 
# ```
# time_start = time.time()
# time_elapsed = 0
# ```
# Finally, the sensitivity level for triggering the obstacle avoidance and the default degrees Zumi will turn to avoid the obstacle are set. You can always change these values later and rerun the code to see how this affects your program.
# ```
# min_ir_threshold = 100
# turn_degrees = 30
# ```
# 
# As an added activity, build an obstacle course and see if Zumi can avoid obstacles from start to finish!

# In[ ]:


# You can also right your own obstacle avoidance code here!


# ### Challenge 
# Write code for Zumi that uses the bottom IR sensors to stay within a circle of black electrical tape.
