#!/usr/bin/env python
# coding: utf-8

# In[1]:


from zumi.util.camera import Camera
import cv2
import numpy as np
import time
import IPython.display
import PIL.Image


# In[ ]:


camera = Camera()
camera.start_camera()
image = camera.capture()
hsv = cv2.cvtColor(image.cv2.COLOR_BGR2HSV)
lower = np.array([160, 120, 200])
upper = np.array([180, 255, 255])
mask = cv2.inRange(hsv, lower, upper)
result = cv2.bitwise_and(image, image, mask = mask)
IPython.display.display(PIL.Image.fromarray(image))


# In[ ]:




