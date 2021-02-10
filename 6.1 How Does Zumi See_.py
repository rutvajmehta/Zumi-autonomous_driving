#!/usr/bin/env python
# coding: utf-8

# <img src="../Data/images/ZumiHeader.png" width=700>

# # How does Zumi see?
# Self-driving cars need a lot more than just obstacle detection sensors. Human drivers have eyes and ears that help us see potential dangers up ahead that maybe a proximity detector can't detect. We can also tell the different between pedestrians, cyclists, and other cars. What else do self-driving cars need to navigate our world?
# 
# Watch [this](https://www.youtube.com/watch?v=wuhbqcMzOaw) video to see it in action.
# 
# In this lesson you are going to learn how to access the camera, take pictures, and show video. 
# 
# ## Take a Selfie
# 
# First up: use Zumi's camera to take a picture and display it on the screen!
# 
# ### Import libraries
# Import the necessary libraries and create camera objects.
# 

# In[ ]:


from zumi.util.camera import Camera
from zumi.util.screen import Screen
import cv2
import IPython.display
from PIL import Image
import time

screen = Screen()
camera = Camera()


# Just like taking an actual picture, this code has a countdown so you can be prepared.
# 
# In the code below, the camera is turned on and then the countdown begins. There is a one second delay with ```time.sleep(1)``` so that there is a one second pause between each number. The rest of the code is commented so that you can see what each line of code does.
# 
# Get ready to see yourself on the Zumi screen! For multiple pictures, run this cell multiple times.
# 

# ### Cheese! 📸 

# In[ ]:


camera.start_camera() # Turn on the camera

print("3...")
screen.draw_text("    3...")
time.sleep(1)
print("2...")
screen.draw_text("    2...")
time.sleep(1)
print("1...")

screen.draw_text("    1...")
time.sleep(1)
screen.draw_text("    Cheese!")


image = camera.capture() # Take a picture

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Convert it to gray

small = cv2.resize(gray, (128,64)) # Resize it to fit the screen
    
screen.draw_image(Image.fromarray(small).convert('1')) # show the picture! 

camera.close() # Make sure to close the camera stream


# ## Resolution
# You probably have noticed that the picture is very pixelated and hard to see. That is because the OLED screen is only 128 pixels wide and 64 pixels tall!
# 
# ### Displaying images  in Jupyter
# 
# Instead of showing your picture on the Zumi screen, display it right here in the Jupyter Notebook. As a bonus, it will appear in color!

# In[ ]:


camera.start_camera()
print("3...")
screen.draw_text("3...")
time.sleep(1)
print("2...")
screen.draw_text("2...")
time.sleep(1)
print("1...")
screen.draw_text("1...")
time.sleep(1)
screen.draw_text("Cheese!")

frame = camera.capture()
IPython.display.display(Image.fromarray(frame))
IPython.display.clear_output(wait=True) 
time.sleep(5)
        
camera.close()


# ### Video
# 
# A video is just a series of pictures one after the other. In order to display a video in Jupyter, you take pictures inside of a ```while True``` loop.

# In[ ]:


from zumi.util.camera import Camera
import cv2
import IPython.display
import PIL.Image


camera = Camera()
camera.start_camera()

try: 
    while True:
        frame = camera.capture()
        IPython.display.display(PIL.Image.fromarray(frame))
        IPython.display.clear_output(wait=True) 

finally:
    camera.close()

