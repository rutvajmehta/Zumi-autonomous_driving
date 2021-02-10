#!/usr/bin/env python
# coding: utf-8

# <img src="../Data/images/ZumiHeader.png" width=700>

# # IR Sensors
# 
# IR stands for **infrared**. Infrared is a form of electromagnetic radiation that is not visible with the human eye. This is a form of energy. However, not all electromagnetic radiation is dangerous. There is a small portion of it that we can see. This is visible light! The different colors that we see depend on the various wavelengths. As the wavelengths get longer and longer, we can no longer see them. However, special sensors can detect these waves. You will use the IR sensors on Zumi to detect objects that are covering the sensors.
# 
# 
# 
# 
# ![logo](../Data/images/electromagnetic_spectrum.jpg)
# 
# <center> https://imagine.gsfc.nasa.gov/science/toolbox/emspectrum1.html </center>
# 
# ## Zumi IR sensors
# 
# Zumi is equipped with 6 IR sensors: two in the front, two in the back, and two on the bottom. They all have an index so that it is easier to read their data:
#    * IR 0 = front right
#    * IR 1 = bottom right
#    * IR 2 = back right
#    * IR 3 = bottom left
#    * IR 4 = back left
#    * IR 5 = front left
# 
# 
# <img src="../Data/images/pcb.jpg" alt="pcb" width="700"/>

# ### Display IR data on the screen
# We are going to display the IR data on the screen. To get IR data we need Zumi object and to display on the screen we need to create a Screen object.

# In[ ]:


from zumi.zumi import Zumi
from zumi.util.screen import Screen
import time

zumi = Zumi()
screen = Screen()


# ### What does the data mean?
# 
# IR sensors work by emitting an infrared pulse and meausuring the infrared light that returns from bouncing off an object. This number will be between 0 and 255.
# 
# A lower number indicates that something in the vicinity is reflecting the IR light back to the sensor. You will be able to see the numbers drop as you cover the sensors. For the front and back IR sensors, try placing Zumi in front or behind of various objects to see the values of the IR sensors change.  
# 
# #### Front IR sensors

# In[ ]:


#display the ir values
for i in range(0,50):
    ir_readings = zumi.get_all_IR_data()
    front_right_ir = ir_readings[0]
    front_left_ir = ir_readings[5]
    
    message = "    IR readings        "
    message = message + str(front_right_ir) + ", " + str(front_left_ir)
    screen.draw_text(message)
    time.sleep(0.1)


# #### Back IR sensors
# 

# In[ ]:


#display the ir values
for i in range(0,50):
    ir_readings = zumi.get_all_IR_data()
    back_right_ir = ir_readings[2]
    back_left_ir = ir_readings[4]
    
    message = "    IR readings        "
    message = message + str(back_right_ir) + ", " + str(back_left_ir)
    screen.draw_text(message)
    time.sleep(0.1)


# #### Bottom IR sensors
# 
# The bottom IR sensors are a bit more precise at detecting when light is bounced off. Bottom IR sensors are great for line following or detecting if something is underneath Zumi, such as a table.

# In[ ]:


#display the ir values
for i in range(0,50):
    ir_readings = zumi.get_all_IR_data()
    bottom_right_ir = ir_readings[1]
    bottom_left_ir = ir_readings[3]
    
    message = "    IR readings        "
    message = message + str(bottom_right_ir) + ", " + str(bottom_left_ir)
    screen.draw_text(message)
    time.sleep(0.1)


# ## IR with Buzzer
# You can also combine the buzzer and the IR sensor to make music or a simple prozimity sensor.
# Run the code and place your hand in front of zumi's right IR sensor...

# In[ ]:


for i in range(0,100):
    # note can be a number between 0-60
    ir_readings = zumi.get_all_IR_data()
    zumi.play_note(int(ir_readings[0]/4),20)
    # ir_readings[0] = front right
    # Make sure to pause
    time.sleep(0.05)

