#!/usr/bin/env python
# coding: utf-8

# <img src="../Data/images/ZumiHeader.png" width=700>

# # Lights
# 
# Like every car should have, Zumi has headlights and brake lights that you can program. On a circuit board, these lights are known as **LEDs**.
# 
# ### Import libraries

# In[ ]:


from zumi.zumi import Zumi
import time

zumi = Zumi()


# ## What is an LED?
# 
# LED stands for “light-emitting diode”. A diode is an electronic device that allows an electronic current to flow in only one direction. LEDs are replacing traditional incandescent light bulbs because they are more efficient.
# 
# ## Zumi LED Functions
# 
# In addition to turning the headlights and brake lights on and off, you can also use turn signals! 
# Here are all of the functions available for you to use:
# 
# ```
# * all_lights_on()
# 
# * all_lights_off()
# 
# * headlights_on()
# 
# * headlights_off()
#        
# * brake_lights_on()
#        
# * brake_lights_off()
#         
# * hazard_lights_on()
#         
# * hazard_lights_off()
# 
# * signal_left_on()
#        
# * signal_left_off()
#        
# * signal_right_on()
#        
# * signal_right_off()
# ```     
# 
# Now try incorporating turn signals into your remote control code or writing some new code.
# Here’s an example that you can test out:
# 

# In[ ]:


zumi.signal_right_on()
zumi.forward()
zumi.turn_right()
zumi.signal_right_off()
zumi.forward()

